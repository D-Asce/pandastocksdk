# pandaData SDK

> A 股数据 API + AI 选股 · 开源客户端

基于 **NATS** 的 A股 实时数据通道——行情、Level2、DDX 大单、资金流、选股信号**主动推给你**，不是让你轮询 REST。

## ✨ 特性

- **实时推送 / 订阅**：NATS pub/sub，4 个实时通道主动下发行情 / 指数 / 概念 / 行业
- **AI 选股**：`get_ch_select_stock()` 等 AI 选股接口
- **22 个开放接口**：18 个请求/响应 + 4 个实时订阅（底层 176 个接口覆盖全量数据）
- **MCP ready**：提供本地 MCP Server（22 个工具），Claude / Cursor / OpenClaw 直接调用

## 安装

```bash
pip install nats-py==2.14.0
```

## 🚀 快速开始

```python
from panda_stock import PandaStock

# 用你申请到的 phone / nid 初始化（见下方"免费试用"）
ps = PandaStock(phone="your_phone", nid="your_nid")
ps.connect_server()

# 获取股票列表
print(ps.get_ch_stock())

# AI 选股
print(ps.get_ch_select_stock())

# 单只股票实时行情
print(ps.get_ch_one_stock_real("600519"))
```

## 📡 实时快照（请求/响应）

4 个 CurReal 主题通过请求方式获取实时快照，无需订阅：

```python
# A股实时行情
print(ps.get_ch_stock_real())

# 指数实时
print(ps.get_ch_market_real())

# 概念板块实时
print(ps.get_ch_concept_real())

# 行业板块实时
print(ps.get_ch_industry_real())
```

## 🎁 免费试用（申请方式待定）

> 公共测试账号的**每日额度 / 调用频率 / 开放接口范围**由服务端统一配置。
> 申请入口：[待补充——申请链接或加微信/邮件]

- 公共 phone/nid 仅供试玩，限频、限接口
- 正式 / 高频 / 实时数据，请申请**专属 phone/nid**

## 🔑 当前开放的 22 个接口

接口按成本/价值分档，客户端不含限制逻辑，鉴权/配额/频率/分级全部在服务端（NATS 网关）执行。

**18 个请求/响应接口：**

| 主题 | 方法 | 说明 |
|---|---|---|
| chStockList | `get_ch_stock()` | 股票列表 |
| chConceptList | `get_ch_concept()` | 概念板块列表 |
| chIndustryList | `get_ch_industry()` | 行业板块列表 |
| ChStockCurReal | `get_ch_stock_real()` | A股实时快照 |
| ChMarketCurReal | `get_ch_market_real()` | 指数实时快照 |
| ChConceptCurReal | `get_ch_concept_real()` | 概念板块实时快照 |
| ChIndustryCurReal | `get_ch_industry_real()` | 行业板块实时快照 |
| ChOneStockReal | `get_ch_one_stock_real(code)` | 单只股票实时 |
| chStockFrontDayHistory | `get_ch_stock_front_day_history(code)` | 个股前复权日线 |
| chConceptDayHistory | `get_ch_concept_day_history(code)` | 概念日线 |
| chIndustryDayHistory | `get_ch_industry_day_history(code)` | 行业日线 |
| chStockMinuteHistory | `get_ch_stock_minute_history(code, minute, date)` | 分钟历史 |
| ChMarketDayHistory | `get_ch_market_day_history(code)` | 指数日线 |
| ChCoreNews | `get_core_new(date)` | 核心资讯 |
| ChDomesticNews | `get_domestic_financial_news(date)` | 国内要闻 |
| ChGlobalNews | `get_global_financial_news(date)` | 全球要闻 |
| ChOptionNews | `get_options_news(date)` | 期权资讯 |
| ChLimitUpDown | `get_ch_limit_up_down()` | 涨跌停统计 |
| ChLhbData | `get_lhb_data(date)` | 龙虎榜 |
| ChMarketFundFlow | `get_ch_market_fund_flow()` | 市场资金流 |
| chAllMarketBearCompare | `get_ch_all_market_bear_compare()` | 全市场多空对比 |
| chDdxStockData | `get_ch_stock_ddx_data(code)` | 个股 DDX |

> 服务端共 **176 个接口**，完整清单（含每个接口「是否可测试」标注）见 [`INTERFACES.md`](INTERFACES.md)。上表 22 个为已对公开 key 开放的请求接口。

## 🧩 MCP 接入（本地 stdio）

```json
{
  "mcpServers": {
    "pandaData": {
      "command": "python",
      "args": ["mcp/server.py"],
      "env": { "PANDA_PHONE": "your_phone", "PANDA_NID": "your_nid" }
    }
  }
}
```

详见 `mcp/config_example.json`。

## 🤖 SKILL.md

仓库根目录 `SKILL.md` 供 Claude Code / OpenClaw 直接激活。

## ⚖️ 许可证

MIT（见 `LICENSE`）。客户端开源，**调用后端需有效 phone/nid，按量计费**。
