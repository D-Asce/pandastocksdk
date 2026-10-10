# 行情数据用推送还是轮询？我把两种架构的实测脚本开源了

> 写给做行情接入、监控告警、实时看板的工程师。
> 这篇文章只讨论架构和数据本身，不推荐任何产品。

---

## 一、一个很常见的直觉错误

很多人接行情数据，第一反应是写个循环：

```python
while True:
    data = requests.get("https://api.example.com/quotes?codes=600519,000001")
    process(data)
    time.sleep(3)
```

这个写法能跑通，能出数据，在 demo 里看不出问题。

但它有一个**结构性的缺陷**，和你的服务器性能、网络质量、标的数量都无关。

---

## 二、轮询的真正代价：延迟下限被你自己锁死了

先算一笔账。

假设你的 SLA 是「行情延迟不超过 1 秒」，你轮询间隔设 3 秒。

请求本身的耗时是多少？从你的客户端到数据源，通常是 20~200ms。

于是每一次取数的实际时间线是：

```
t=0.0s  发起请求
t=0.1s  收到响应        <- 数据此刻已经"旧"了 100ms
t=3.0s  发起下一次      <- 这 2.9s 里，数据完全没更新
t=3.1s  收到响应
...
```

**最坏情况下，数据年龄 = 轮询间隔 + 请求耗时 = 3.1 秒。**
平均情况下也有约 1.5 秒。

关键结论：**无论你的代码多快、网络多快，你能拿到的数据永远比真实行情落后「一个轮询间隔」。**

想把延迟压到 500ms？那就 `sleep(0.5)`，请求数翻 6 倍。

这不是调优问题，这是**架构天花板**。轮询的延迟下限由轮询间隔决定，而间隔由你的成本和被限流的风险决定。

---

## 三、还有一个容易忽略的问题：无效请求的比例

轮询的第二个代价是**绝大多数请求拿到的都是你不需要的数据**。

假设你轮询 100 只股票，每 3 秒一次：

- 停牌股：价格全天不变，28800 次请求返回同一个值
- 低流动性小盘股：几秒内可能真的没变化
- 收盘后：所有数据都不再更新，但你的循环还在跑

粗略估算，**全天真正产生新数据的时刻，可能只占 5%~15%**。

也就是说，你 85% 以上的请求在做三件事：占用连接、消耗配额、触发限流。

而一旦触发限流，你的轮询间隔就被迫拉长 —— **延迟进一步恶化**。这是个正反馈陷阱：请求越多，被限流越狠，延迟越高，只能降频率，数据越不实时。

---

## 四、推送架构怎么解决这两件事

推送（Pub/Sub）的模型完全不同。

数据源作为发布者，在数据产生的那一刻就推给所有订阅者：

```
数据源 ──(NATS/WS/MQ)──> 订阅者A
                    ├──> 订阅者B
                    └──> 订阅者C
```

关键差异：

| | 轮询 | 推送 |
|---|---|---|
| 延迟 | 间隔 + 请求耗时 | 传输耗时（通常 < 100ms） |
| 拉长间隔的影响 | 延迟线性变差 | 无影响（改订阅即可） |
| 无效请求 | 85%+ | 无（数据不变就不推） |
| 限流风险 | 高，且恶性循环 | 低 |
| 扩标的成本 | 线性增加请求数 | 线性增加订阅数 |

### 4.1 代码对比

轮询版本（你需要自己处理重连、去重、限流）：

```python
import time, requests

while True:
    try:
        r = requests.get(BASE_URL, params={"symbols": ALL_SYMBOLS}, timeout=2)
        for tick in r.json()["data"]:
            handle(tick)
    except Exception:
        pass  # 吞掉，然后继续打
    time.sleep(POLL_INTERVAL)
```

推送版本（数据到达即处理，与上游解耦）：

```python
import asyncio, nats

async def main():
    nc = await nats.connect(NATS_URL)
    await nc.subscribe("market.quote.>", cb=handle)

    # 连接建立后只需要保持活着
    await asyncio.Future()

async def handle(msg):
    tick = json.loads(msg.data)
    await process(tick)
```

差别不只是代码行数。

推送版本里，**上游抖动不会传导成你的故障**：断线由客户端库自动重连、重订阅，业务代码完全无感。而轮询版本里每一次失败都要你自己兜。

### 4.2 为什么行情数据特别适合推送

这是行情类数据的特性，也是它和普通业务数据的区别：

**数据是「状态广播」而不是「请求响应」。**

- 一次 K 线变动，需要推给 100 个订阅者和推给 1 个订阅者，成本几乎一样
- 数据源不需要知道谁在听（发布订阅解耦）
- 每个订阅者独立判断自己关心哪些标的（用 subject 通配符订阅）

这个特征在订单、传感器、集群监控、日志流里同样成立。**凡是「一个变化要通知 N 个消费者」的场景，都该用推送。**

---

## 五、但推送不是银弹，有三个真实的坑

前人踩过的，不重复一遍。

### 5.1 必须处理断线重连和消息补发

网络一定会断。断开后到重连之间的数据，是**永久丢失**的。

所以一个可用的推送客户端必须做到：

```
连接断开 ──> 自动重连（指数退避）
         ──> 重连后重新订阅
         ──> 主动拉取断线期间的全量快照（补齐空洞）
         ──> 之后转为增量推送
```

**只重连不补数据是不完整的** —— 断线 30 秒，你的数据就永远缺了 30 秒。

### 5.2 必须处理乱序和重复

网络不保证顺序，同一条消息可能重发。

实务做法是每个 tick 带单调递增的序号（或时间戳 + 序号）：

```python
last_seq = 0

async def handle(msg):
    global last_seq
    tick = json.loads(msg.data)
    if tick["seq"] <= last_seq:
        return          # 重复或过期，丢弃
    last_seq = tick["seq"]
    await process(tick)
```

这个 `if` 看着简单，但缺了它，指标统计会出现你查不出原因的数据漂移。

### 5.3 NATS 这类协议需要心跳

空闲连接会被中间设备（NAT、防火墙、负载均衡）悄悄回收。你以为连着，其实已经死了，直到下一次写入才发现。

必须开启心跳，让连接保持活跃：

```
nats.connect(url, ping_interval=20, max_outstanding_pings=5)
```

**症状识别**：如果你的数据「停了一阵又突然来了一大波」，八成是心跳没配，连接被静默回收了。

---

## 六、怎么自己测出延迟差异

架构不能靠说服，要靠数据。下面是完整的压测脚本，你可以直接拿去跑自己的数据源。

它做三件事：

1. **测轮询**：`N` 个并发 worker，每 `P` 秒拉一次，记录每条数据的到达时刻
2. **测推送**：订阅同一数据源，记录到达时刻
3. **对比**：输出两组数据的年龄分布

```python
"""
measure_feed_latency.py —— 量化「轮询 vs 推送」的延迟差异

用法:
    python measure_feed_latency.py --mode poll  --url URL --symbols 600519,000001 --interval 3
    python measure_feed_latency.py --mode push  --nats nats://host:4222 --subject market.quote.>

注意: 脚本假设数据源返回/推送的 tick 里带有数据生成时间戳字段 ts,
      若没有, 需要先校准本机时钟或改为对比"两次数据变化的时间差".
"""
import argparse, asyncio, json, statistics, time
from collections import defaultdict


def summarize(name, ages_ms):
    if not ages_ms:
        print(f"{name}: 无样本")
        return
    ages_ms.sort()
    n = len(ages_ms)
    p = lambda q: ages_ms[min(n - 1, int(n * q))]
    print(f"\n{name}  (样本 {n})")
    print(f"  min    {ages_ms[0]:>8.0f} ms")
    print(f"  p50    {p(.50):>8.0f} ms")
    print(f"  p90    {p(.90):>8.0f} ms")
    print(f"  p99    {p(.99):>8.0f} ms")
    print(f"  max    {ages_ms[-1]:>8.0f} ms")
    print(f"  mean   {statistics.mean(ages_ms):>8.0f} ms")
    return p(.50), p(.99)


async def run_poll(args):
    import aiohttp
    """轮询模式: 每个 worker 独立按固定间隔拉取。"""
    symbols = args.symbols.split(",")
    ages = defaultdict(list)

    async def worker(wid):
        async with aiohttp.ClientSession() as s:
            while True:
                try:
                    async with s.get(args.url,
                                     params={"symbols": ",".join(symbols)}) as r:
                        now = time.time()
                        for tick in await r.json():
                            # 数据年龄 = 收到时刻 - 数据生成时刻
                            age = (now - tick["ts"]) * 1000
                            ages[tick["symbol"]].append(age)
                except asyncio.CancelledError:
                    raise
                except Exception as e:
                    print(f"  worker{wid} 错误: {e}")
                await asyncio.sleep(args.interval)

    print(f"轮询模式: {args.workers} worker, 间隔 {args.interval}s, "
          f"运行 {args.duration}s")
    # 必须显式调度: 仅定义协程不会执行
    tasks = [asyncio.create_task(worker(i)) for i in range(args.workers)]
    await asyncio.sleep(args.duration)
    for t in tasks:
        t.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    all_ages = [a for v in ages.values() for a in v]
    return summarize("轮询数据年龄", all_ages)


async def run_push(args):
    """推送模式: 订阅后被动接收。"""
    import nats
    ages = []

    async def cb(msg):
        now = time.time()
        tick = json.loads(msg.data)
        ages.append((now - tick["ts"]) * 1000)

    print(f"推送模式: 订阅 {args.subject}, 运行 {args.duration}s")
    nc = await nats.connect(args.nats, ping_interval=20)
    await nc.subscribe(args.subject, cb=cb)
    await asyncio.sleep(args.duration)
    await nc.drain()
    return summarize("推送数据年龄", ages)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["poll", "push"], required=True)
    ap.add_argument("--url")
    ap.add_argument("--nats")
    ap.add_argument("--subject")
    ap.add_argument("--symbols", default="600519,000001")
    ap.add_argument("--interval", type=float, default=3.0)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--duration", type=int, default=120)
    args = ap.parse_args()

    print("=" * 60)
    print("行情数据延迟测量 —— 压测期间请勿关闭网络")
    print("=" * 60)
    if args.mode == "poll":
        asyncio.run(run_poll(args))
    else:
        asyncio.run(run_push(args))
    print("\n提示: 轮询的 p50 接近 interval/2，p99 接近 interval —— "
          "这正是架构天花板，与你的代码质量无关。")


if __name__ == "__main__":
    main()
```

**怎么读结果**：

- 轮询的 `p99` 会非常接近你的 `--interval`（因为最坏情况就是刚好错过一次）
- 推送的 `p99` 取决于网络 RTT，通常在几十毫秒量级
- **把 interval 从 3s 改成 1s，轮询的 p99 跟着变成 1s，推送的 p99 不变**

最后这一点，是整篇文章的结论。

---

## 七、什么时候该用哪种

不是所有场景都值得上推送。

**用推送：**
- 延迟有明确 SLA（交易、告警、看板）
- 标的数量多（轮询请求数会失控）
- 上游有明确的限流策略
- 存在多个下游消费者

**用轮询就够了：**
- 分钟级 / 日终数据（收盘价、K 线）
- 单个或极少数标的
- 延迟不敏感（日报、批量回测取数）
- 数据源**不提供**推送通道 —— 这时候再优化架构也没用，先看有没有 `websocket` 或订阅接口

最后一条最实际：**先确认你的数据源到底提供什么。** 很多数据源根本不提供推送通道，那么「该用推送」就只是个无法执行的建议。

---

## 八、小结

1. 轮询的延迟下限 = 轮询间隔，这是架构天花板，调优改不了
2. 轮询有 85%+ 的无效请求，且容易触发「越限流越降频」的恶性循环
3. 推送把延迟降到网络 RTT 量级，且标的多时成本增长平缓
4. 推送的三个必做项：重连补发、乱序去重、心跳保活
5. **先确认数据源提供什么通道，再谈架构**

---

如果需要可运行的参考实现，本文提到的采集与分发部分可以看
[这个仓库](https://github.com/D-Asce/pandastocksdk)（A 股数据方向，Go + NATS 实现）。

欢迎在评论区交流你遇到的实际延迟问题 —— 不同的上游差异很大，
实测数据比理论更有参考价值。