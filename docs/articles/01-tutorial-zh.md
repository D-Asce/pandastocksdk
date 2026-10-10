# 用 MCP 把 A 股实时行情接进 Claude / Cursor

> 写给做量化研究、策略开发的朋友 —— 那些每次都要手写 Tushare / Akshare
> 调用、反复记字段名的人。

---

## 一、我们以前是怎么查 A 股数据的

做 A 股量化，第一步永远是「怎么把数据取出来」。

```python
import tushare as ts
pro = ts.pro_api('你的token')
df = pro.daily(ts_code='600519.SH', start_date='20260101', end_date='20261010')
```

然后你会发现：

- **字段名记不住** —— `total_share` 还是 `shares_outstanding`？`turnover_rate` 还是 `turn`？
- **每个工具都要写一遍** —— 策略回测写一次，因子计算写一次，日报推送写一次
- **实时数据是空白** —— Tushare 是 T+1 的，盘中实时要另找数据源
- **AI 工具帮不上忙** —— Claude / Cursor 能帮你写代码，但查数据这一步还是得你自己来

最后这一点，就是 MCP 要解决的问题。

---

## 二、什么是 MCP

MCP（Model Context Protocol）让 AI 工具**直接调用外部数据接口**，而不是靠你把数据喂给它。

配置一次之后，你只需要说：

> 「帮我查一下贵州茅台最近 20 个交易日的走势，标注出放量上涨的日子」

AI 自己就会：
1. 识别要查的标的（600519）
2. 调用数据接口拉日线
3. 计算成交量均值
4. 找出放量上涨的交易日
5. 把结果整理给你

**你不需要写一行取数代码。**

---

## 三、PandaStock MCP：A 股数据的 MCP 服务

[PandaStock](https://github.com/D-Asce/pandastocksdk) 是一个把 A 股数据
包装成 MCP 服务的项目。它背后是 NATS 推送的实时数据通道，对外暴露
**22 个开放接口**（服务端共 176 个接口），覆盖：

| 能力 | 工具 | 说明 |
|---|---|---|
| 实时行情 | `ChOneStockReal` | 单只股票实时报价 |
| 实时快照 | `ChStockCurReal` | 全市场实时行情快照 |
| 日 K 线 | `chStockFrontDayHistory` | 前复权日线 |
| 分钟 K 线 | `chStockMinuteHistory` | 1/5/15/30/60 分钟线 |
| 资讯 | `ChCoreNews` | 核心市场资讯 |
| 资金流 | `ChMarketFundFlow` | 市场资金流向 |
| 龙虎榜 | `ChLhbData` | 龙虎榜数据 |
| DDX | `chDdxStockData` | DDX 大单跟踪 |

**和 Tushare / Akshare 的区别**：

| | Tushare / Akshare | PandaStock MCP |
|---|---|---|
| 接入方式 | Python SDK / HTTP | MCP，AI 工具原生调用 |
| 实时数据 | Tushare 无实时 | NATS 推送实时行情 |
| Level-2 / DDX | 需另找数据源 | 内置 |
| 使用门槛 | 要写代码、记字段 | 自然语言即可 |
| 免注册测试账号 | 无 | ✅ `pandastock` / `pandastock` |

---

## 四、5 分钟上手

### 1. 安装

```bash
pip install pandastock-mcp
```

### 2. 配置（用公共测试账号，免注册）

```json
{
  "mcpServers": {
    "panda-stock": {
      "command": "pandastock-mcp",
      "env": {
        "PANDA_PHONE": "pandastock",
        "PANDA_NID": "pandastock"
      }
    }
  }
}
```

### 3. 在 Cursor / Claude 里用

重启之后，你就可以直接问：

- 「查一下 600519 最近一根 K 线」
- 「拉一下 000001 本周的分钟数据」
- 「今天有哪些股票涨停」
- 「最近市场资金流向怎么样」

AI 会自动调用对应的 MCP 工具，返回结构化数据。

---

## 五、一个完整的例子

**你的需求**：找出最近 5 个交易日全市场资金流入最多的 5 只股票。

**传统方式**：写一个 Tushare 脚本 → 拉 daily_basic → 按资金流排序 → 导出表格 → 再复制到分析环境。10 行代码起。

**用 MCP**：

> 「帮我找最近 5 个交易日资金流入最多的 5 只 A 股，列出代码、名称、净流入金额」

AI 自动完成：调 `ChMarketFundFlow` → 排序 → 输出表格。**零代码。**

---

## 六、为什么这件事值得分享

1. **A 股 MCP 还很少** —— 大部分量化工具还是 REST API 思维，MCP 化的 A 股数据服务屈指可数
2. **免费 + 免注册** —— 测试账号开箱即用，不需要申请 token、不需要积分
3. **实时性是刚需** —— Tushare 做不了盘中，这是 MCP 差异化最明显的地方
4. **AI 工具链正在迁移** —— Cursor、Claude Code、Cline、Trae 都在支持 MCP，现在接入正当时

---

## 七、动手试试

- 仓库：https://github.com/D-Asce/pandastocksdk
- 安装：`pip install pandastock-mcp`
- 测试账号：`phone=pandastock` / `nid=pandastock`
- 接口清单：仓库 `INTERFACES.md`（176 个接口）

**如果你觉得有用，欢迎在仓库点个 star，或者把你的使用场景告诉我 —— 22 个开放接口远没用满，你的需求就是下一步开发的方向。**

---

*PandaStock 是 pandaData 的开源实现。NATS 推送行情 / Level-2 / DDX 大单 / 资金流 / AI 选股。*