# pandaData — A 股实时数据 SDK + MCP Server

<!-- mcp-name: io.github.D-Asce/pandastocksdk -->

[![PyPI version](https://img.shields.io/pypi/v/pandastock-mcp.svg)](https://pypi.org/project/pandastock-mcp/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **A 股数据 API + AI 选股 · 开源客户端**
>
> 基于 **NATS** 的 A 股实时数据通道 —— 行情、Level2、DDX 大单、资金流、选股信号**主动推给你**，不是让你轮询 REST。

## ⚡ 30 秒上手

**免注册**：内置公共测试账号，装完直接跑，无需申请。

```bash
pip install pandastock-mcp
```

```python
from panda_stock import PandaStock

# 公共测试账号（配额说明见下方「公共测试账号」）
ps = PandaStock(phone="pandastock", nid="pandastock")
ps.connect_server()

print(ps.get_ch_stock())                  # 全市场股票列表
print(ps.get_ch_one_stock_real("600519")) # 单只实时行情
print(ps.get_ch_select_stock())           # AI 选股
```

## 🤖 MCP 接入（Claude / Cursor / OpenClaw）

```bash
pip install pandastock-mcp
```

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

升级：`pip install --upgrade pandastock-mcp` · 详见 `mcp/config_example.json`

> 📞 **接口咨询 / 专属 key 申请**：加微信 `onestock188` 或 `pandastock888`
> 📅 最后更新：2026-11-23
>
> 🇨🇳 **国内直连（无需梯子）**：https://gitee.com/nutou123/pandastocksdk

## ✨ 特性

- **免注册试用**：公共测试账号装完即可调用，先验证再申请专属 key
- **实时快照（请求/响应）**：4 个 CurReal 主题通过请求获取 A 股实时行情 / 指数 / 概念 / 行业，无需订阅
- **AI 选股**：`get_ch_select_stock()` 等 AI 选股接口
- **22 个开放接口**：全部为请求/响应接口；服务端共 **210 个接口**覆盖全量数据（完整清单见 [INTERFACES.md](INTERFACES.md)）
- **MCP ready**：本地 stdio MCP Server 暴露 22 个工具，Claude / Cursor / OpenClaw 直接调用

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

## 🎁 公共测试账号

> 开放一个**公共测试账号**，无需申请即可直接试玩：

| 字段 | 值 |
|---|---|
| phone | `pandastock` |
| nid | `pandastock` |

> 公共账号**按来源 IP 限频、限接口、含全局日上限**，仅供评估试玩。
> 正式 / 高频 / 全量接口，请申请**专属 phone/nid**：加微信 onestock188 或 pandastock888

- 初始化示例：`PandaStock(phone="pandastock", nid="pandastock")`（与专属账号同一套服务端鉴权，仅配额不同）

## 🔑 测试账号可调用的 22 个接口（服务端共 210 个，完整清单 + 返回字段见 INTERFACES.md）

接口按成本/价值分档，客户端不含限制逻辑，鉴权/配额/频率/分级全部在服务端（NATS 网关）执行。

**22 个请求/响应接口：**

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

> 服务端共 **210 个接口**，完整清单（含「是否可测试」+ **每个接口返回的字段明细**）见 [`INTERFACES.md`](INTERFACES.md)（「接口返回字段详情」一节）。上表 22 个为已对公开 key 开放的请求接口。

## 全部 210 个接口一览（测试账号可调用标记）

> 完整返回字段见 [`INTERFACES.md`](INTERFACES.md) 的「接口返回字段详情」。标 ✅ 可调用 的即上方 22 个公开测试账号可调用接口；其余需专属 key 后使用。

| 分类 | 接口名称 | 方法(function) | 测试账号 |
|---|---|---|---|
| 个股数据 | 获取股票列表 | `get_ch_stock` | ✅ 可调用 |
| 个股数据 | 每日ST股信息 | `get_ch_stock_st_history` | — |
| 个股数据 | 订阅实时行情通道 | `subscribe_ch_stock_real` | — |
| 个股数据 | 订阅北证个股实时行情 | `subscribe_ch_bj_stock_real` | — |
| 个股数据 | 获取所有个股实时行情 | `get_ch_stock_real` | ✅ 可调用 |
| 个股数据 | 获取单只个股实时行情 | `get_ch_one_stock_real` | ✅ 可调用 |
| 个股数据 | 个股实时分钟K线 | `get_ch_stock_minute_real` | — |
| 个股数据 | 历史分钟数据 | `get_ch_stock_minute_history` | ✅ 可调用 |
| 个股数据 | 个股分时图 | `get_ch_stock_time_line` | — |
| 个股数据 | 个股昨日分时图 | `get_ch_stock_time_line_yes` | — |
| 个股数据 | 个股五日分时 | `get_ch_stock_five_days_time_line` | — |
| 个股数据 | 个股竞价分时数据 | `get_ch_stock_auction_time_line` | — |
| 个股数据 | 前复权日线 | `get_ch_stock_front_day_history` | ✅ 可调用 |
| 个股数据 | 前复权周线 | `get_ch_stock_front_week_history` | — |
| 个股数据 | 前复权月线 | `get_ch_stock_front_month_history` | — |
| 个股数据 | 后复权日线 | `get_ch_stock_back_day_history` | — |
| 个股数据 | 后复权周线 | `get_ch_stock_back_week_history` | — |
| 个股数据 | 后复权月线 | `get_ch_stock_back_month_history` | — |
| 个股数据 | 个股实时逐笔成交 | `get_ch_stock_transaction_real` | — |
| 个股数据 | 历史分笔 | `get_ch_stock_transaction_history` | — |
| 个股数据 | 十大股东 | `get_ch_stock_ten_holders` | — |
| 个股数据 | 十大流通股东 | `get_ch_stock_ten_circulating_holders` | — |
| 个股数据 | 股东人数历史 | `get_ch_stock_share_holder` | — |
| 个股数据 | 个股除权除息历史 | `get_ch_stock_dividend_history` | — |
| 个股数据 | 年度高送转/分红 | `get_ch_year_high_stock_dividend` | — |
| 个股数据 | 年度解禁数据 | `get_ch_year_stock_lock_up` | — |
| 个股数据 | 大宗交易历史 | `get_ch_stock_block_trading` | — |
| 个股数据 | 增减持历史 | `get_ch_stock_inc_or_dec` | — |
| 个股数据 | 个股股本变化历史 | `get_ch_stock_share_capital` | — |
| 个股数据 | 个股一致行动人信息 | `get_ch_stock_pacs` | — |
| 个股数据 | 个股公告 | `get_ch_stock_announce` | — |
| 个股数据 | 个股研报 | `get_ch_stock_research_report` | — |
| 个股数据 | 历史暗盘资金 | `get_ch_stock_dark_rank_history` | — |
| 个股数据 | 个股资金流明细历史 | `get_ch_stock_fund_flow_detail_history` | — |
| 个股数据 | 1日融资买入排行 | `get_ch_rz_buy_1_day` | — |
| 个股数据 | 5日融资买入排行 | `get_ch_rz_buy_5_day` | — |
| 个股数据 | 20日融资买入排行 | `get_ch_rz_buy_20_day` | — |
| 个股数据 | 获取个股实时筹码峰数据 | `get_ch_stock_chip_data` | — |
| 个股数据 | 日内实时暗盘资金 | `get_ch_stock_dark_rank` | — |
| 个股数据 | 主力评分数据 | `get_ch_stock_primer_info` | — |
| 个股数据 | 人气排名数据 | `get_ch_stock_attention_tank` | — |
| 个股数据 | 个股资金流 | `get_ch_stock_fund_flow` | — |
| 个股数据 | 不复权日线 | `get_ch_stock_none_day_history` | — |
| 板块数据 | 获取概念板块列表 | `get_ch_concept` | ✅ 可调用 |
| 板块数据 | 获取行业板块列表 | `get_ch_industry` | ✅ 可调用 |
| 板块数据 | 订阅概念板块实时行情通道 | `subscribe_ch_concept_real` | — |
| 板块数据 | 获取概念板块实时行情 | `get_ch_concept_real` | ✅ 可调用 |
| 板块数据 | 订阅行业板块实时行情通道 | `subscribe_ch_industry_real` | — |
| 板块数据 | 获取行业板块实时行情 | `get_ch_industry_real` | ✅ 可调用 |
| 板块数据 | 概念板块日线 | `get_ch_concept_day_history` | ✅ 可调用 |
| 板块数据 | 概念板块周线 | `get_ch_concept_week_history` | — |
| 板块数据 | 概念板块月线 | `get_ch_concept_month_history` | — |
| 板块数据 | 行业板块日线 | `get_ch_industry_day_history` | ✅ 可调用 |
| 板块数据 | 行业板块周线 | `get_ch_industry_week_history` | — |
| 板块数据 | 行业板块月线 | `get_ch_industry_month_history` | — |
| 板块数据 | 获取A数据源概念板块列表 | `get_ch_sa_concept_list` | — |
| 板块数据 | 获取A数据源概念板块实时行情 | `get_ch_sa_concept_real` | — |
| 板块数据 | 获取A数据源概念板块日K线 | `get_ch_sa_concept_day_k` | — |
| 板块数据 | 订阅A概念板块实时行情 | `subscribe_ch_sa_concept_real` | — |
| 板块数据 | 获取A数据源行业板块列表 | `get_ch_sa_industry_list` | — |
| 板块数据 | 获取A数据源行业板块实时行情 | `get_ch_sa_industry_real` | — |
| 板块数据 | 获取A数据源行业板块日K线 | `get_ch_sa_industry_day_k` | — |
| 板块数据 | 订阅A行业板块实时行情 | `subscribe_ch_sa_industry_real` | — |
| 板块数据 | 订阅A概念板块实时资金流 | `subscribe_ch_sa_concept_money_flow` | — |
| 板块数据 | 订阅A行业板块实时资金流 | `subscribe_ch_sa_industry_money_flow` | — |
| 指数数据 | 指数日线 | `get_ch_market_day_history` | ✅ 可调用 |
| 指数数据 | 指数周线 | `get_ch_market_week_history` | — |
| 指数数据 | 指数月线 | `get_ch_market_month_history` | — |
| 指数数据 | 沪深300成分股权重 | `get_ch_hs300_constituent_weight_history` | — |
| 指数数据 | 上证50成分股权重 | `get_ch_sz50_constituent_weight_history` | — |
| 指数数据 | 中证500成分股权重 | `get_ch_zz500_constituent_weight_history` | — |
| 指数数据 | 中证1000成分股权重 | `get_ch_zz1000_constituent_weight_history` | — |
| 指数数据 | 涨跌停数量历史 | `get_ch_limit_up_down` | ✅ 可调用 |
| 指数数据 | 交易日涨跌分布时序数据 | `get_ch_zd_map_history` | — |
| 指数数据 | 涨停股历史数据 | `get_ch_zt_stock_history` | — |
| 指数数据 | 交易日涨停股信息 | `get_ch_lb_stock_history_history` | — |
| 指数数据 | 龙虎榜数据 | `get_lhb_data` | ✅ 可调用 |
| 指数数据 | 交易日涨跌停时序数据 | `get_ch_limit_up_down_history` | — |
| 指数数据 | 上交所每日统计信息 | `get_sh_market_daily_info` | — |
| 指数数据 | 上交所每周统计信息 | `get_sh_market_week_info` | — |
| 指数数据 | 上交所每月统计信息 | `get_sh_market_month_info` | — |
| 指数数据 | 交易日全天成交额数据 | `get_ch_market_amount_curve_history` | — |
| 指数数据 | 全市场PE/PB 日数据历史 | `get_ch_market_pe_pb_day_history` | — |
| 指数数据 | 全市场PE/PB 月数据历史 | `get_ch_market_pe_pb_month_history` | — |
| 指数数据 | 市场每个交易日涨跌平数量 | `get_ch_day_zd_count_history` | — |
| 指数数据 | 上证A股每个交易日涨跌平数量 | `get_ch_sh_day_zd_count_history` | — |
| 指数数据 | 深圳A股每个交易日涨跌平数量 | `get_ch_sz_day_zd_count_history` | — |
| 指数数据 | 创业板每个交易日涨跌平数量 | `get_ch_cyb_day_zd_count_history` | — |
| 指数数据 | 科创板每个交易日涨跌平数量 | `get_ch_kcb_day_zd_count_history` | — |
| 指数数据 | 北证每个交易日涨跌平数量 | `get_ch_bj_day_zd_count_history` | — |
| 指数数据 | 市场每个交易周涨跌平数量 | `get_ch_week_zd_count_history` | — |
| 指数数据 | 上证A股每个交易周涨跌平数量 | `get_ch_sh_week_zd_count_history` | — |
| 指数数据 | 深圳A股每个交易周涨跌平数量 | `get_ch_sz_week_zd_count_history` | — |
| 指数数据 | 创业板每个交易周涨跌平数量 | `get_ch_cyb_week_zd_count_history` | — |
| 指数数据 | 科创板每个交易周涨跌平数量 | `get_ch_kcb_week_zd_count_history` | — |
| 指数数据 | 北证每个交易周涨跌平数量 | `get_ch_bj_week_zd_count_history` | — |
| 指数数据 | 市场每个交易月涨跌平数量 | `get_ch_month_zd_count_history` | — |
| 指数数据 | 上证A股每个交易月涨跌平数量 | `get_ch_sh_month_zd_count_history` | — |
| 指数数据 | 深圳A股每个交易月涨跌平数量 | `get_ch_sz_month_zd_count_history` | — |
| 指数数据 | 创业板每个交易月涨跌平数量 | `get_ch_cyb_month_zd_count_history` | — |
| 指数数据 | 科创板每个交易月涨跌平数量 | `get_ch_kcb_month_zd_count_history` | — |
| 指数数据 | 北证每个交易月涨跌平数量 | `get_ch_bj_month_zd_count_history` | — |
| 指数数据 | 订阅指数实时行情通道 | `subscribe_ch_market_real` | — |
| 指数数据 | 获取指数实时行情 | `get_ch_market_real` | ✅ 可调用 |
| 指数数据 | 市场实时涨跌停数量 | `get_ch_today_limit_up_down` | — |
| 指数数据 | 市场实时涨跌分布时序数据 | `get_ch_market_zd_map` | — |
| 指数数据 | 涨停股实时信息 | `get_ch_today_zt_stock` | — |
| 指数数据 | 市场实时涨停股列表 | `get_ch_today_lb_stock` | — |
| 指数数据 | 市场全天实时成交额 | `get_ch_market_amount_curve` | — |
| 指数数据 | 获取融资融券余额 | `get_rzrq_balance` | — |
| 指数数据 | 全市场买卖对比 | `get_ch_all_market_bear_compare` | ✅ 可调用 |
| 指数数据 | 上证买卖对比 | `get_ch_sh_market_bear_compare` | — |
| 指数数据 | 深证买卖对比 | `get_ch_sz_market_bear_compare` | — |
| 指数数据 | 创业板买卖对比 | `get_ch_cyb_market_bear_compare` | — |
| 指数数据 | 科创板买卖对比 | `get_ch_kcb_market_bear_compare` | — |
| 指数数据 | 北证买卖对比 | `get_ch_bj_market_bear_compare` | — |
| 指数数据 | 市场资金流历史 | `get_ch_market_fund_flow` | ✅ 可调用 |
| 指数数据 | A股交易日历 | `get_ch_calendar` | — |
| 指数数据 | 南向资金（港股通） | `get_south_bound` | — |
| Level2数据 | 订阅Level2实时数据通道 | `subscribe_ch_l2_data_real` | — |
| Level2数据 | 获取Level2实时数据 | `get_ch_l2_data_cur_real` | — |
| Level2数据 | 订阅大单数据(DDE)通道 | `subscribe_ch_ddx_data_real` | — |
| Level2数据 | 获取大单数据(DDE) | `get_ch_ddx_data_cur_real` | — |
| Level2数据 | 获取个股历史大单历史数据 | `get_ch_stock_ddx_history` | — |
| Level2数据 | 个股DDE实时数据 | `get_ch_stock_ea_dde` | — |
| Level2数据 | 全量逐笔成交明细 | `subscribe_ch_l2_transaction_all` | — |
| Level2数据 | 全量十档行情 | `subscribe_ch_l2_depth_all` | — |
| Level2数据 | 个股千档数据 | `get_ch_stock_thousand_level_order` | — |
| Level2数据 | 订阅个股千档行情 | `subscribe_ch_stock_thousand_level` | — |
| Level2数据 | 个股实时大单成交明细 | `get_ch_stock_big_order` | — |
| Level2数据 | 个股l2分价成交明细 | `get_ch_stock_price_summarize` | — |
| Level2数据 | 个股l2分价成交明细历史 | `get_ch_stock_price_summarize_history` | — |
| Level2数据 | 个股实时资金流数据 | `get_ch_stock_l2_fund_flow_sa` | — |
| Level2数据 | 个股实时资金流通道 | `subscribe_ch_l2_stock_money_flow_all` | — |
| Level2数据 | 获取所有个股实时资金流列表 | `get_ch_all_stock_fund_flow` | — |
| Level2数据 | 市场实时资金流数据 | `get_ch_all_market_l2_fund_flow` | — |
| Level2数据 | 上证指数实时资金流数据 | `get_ch_sh_market_l2_fund_flow` | — |
| Level2数据 | 深圳市场实时资金流数据 | `get_ch_sz_market_l2_fund_flow` | — |
| Level2数据 | 创业板实时资金流数据 | `get_ch_cyb_market_l2_fund_flow` | — |
| Level2数据 | 科创板实时资金流数据 | `get_ch_kcb_market_l2_fund_flow` | — |
| Level2数据 | 逐笔还原通道 | `subscribe_ch_stock_l2_trans` | — |
| Level2数据 | 逐笔还原回放通道 | `subscribe_ch_stock_l2_replay_trans` | — |
| Level2数据 | 逐笔委托通道 | `subscribe_ch_stock_l2_order_ex` | — |
| Level2数据 | 逐笔委托回放通道 | `subscribe_ch_stock_l2_replay_order` | — |
| Level2数据 | 竞价匹配通道 | `subscribe_ch_stock_l2_auction` | — |
| Level2数据 | 竞价匹配回放通道 | `subscribe_ch_stock_l2_replay_auction` | — |
| Level2数据 | 订阅个股逐笔还原（按代码） | `ch_sub_trans_ex` | — |
| Level2数据 | 订阅个股逐笔委托（按代码） | `ch_sub_order_ex` | — |
| Level2数据 | 订阅个股竞价匹配（按代码） | `ch_sub_auction_ex` | — |
| Level2数据 | 订阅个股千档（按代码） | `ch_stock_sub_thousand_level` | — |
| Level2数据 | 回放个股逐笔还原（按代码） | `replay_ch_stock_tran` | — |
| Level2数据 | 回放个股逐笔委托（按代码） | `replay_ch_stock_order` | — |
| Level2数据 | 回放个股竞价匹配（按代码） | `replay_ch_stock_auction` | — |
| 财务数据 | 利润表 | `get_ch_stock_income_statement` | — |
| 财务数据 | 现金流表 | `get_ch_stock_cash_flow_statement` | — |
| 财务数据 | 财务主表 | `get_ch_stock_financial_indicators` | — |
| 财务数据 | 资产负债表 | `get_ch_stock_balance_sheet` | — |
| 财务数据 | 财务辅助表 | `get_ch_stock_auxiliary_data` | — |
| 财务数据 | 股东表 | `get_ch_stock_share_capital_and_shareholders` | — |
| 财务数据 | 业绩预告 | `get_ch_stock_net_profit` | — |
| 财务数据 | 财务核心指标(数据源C) | `get_ch_si_stock_fin_key_indicators` | — |
| 财务数据 | 利润表(数据源C) | `get_ch_si_stock_fin_income_statements` | — |
| 财务数据 | 资产负债表(数据源C) | `get_ch_si_stock_fin_balance_sheet` | — |
| 财务数据 | 现金流表(数据源C) | `get_ch_si_stock_fin_cash_flow` | — |
| 财务数据 | 个股财务核心指标(数据源B) | `get_ch_ea_stock_fin_key_indicators` | — |
| 财务数据 | 个股资产负债表(数据源B) | `get_ch_ea_stock_fin_balance_sheet` | — |
| 财务数据 | 个股利润表(数据源B) | `get_ch_ea_stock_fin_income_statements` | — |
| 财务数据 | 个股现金流量表(数据源B) | `get_ch_ea_stock_fin_cash_flow` | — |
| 新闻资讯 | 重点资讯新闻 | `get_core_new` | ✅ 可调用 |
| 新闻资讯 | 国内主要新闻 | `get_domestic_financial_news` | ✅ 可调用 |
| 新闻资讯 | 国际主要新闻 | `get_global_financial_news` | ✅ 可调用 |
| 新闻资讯 | 时评类新闻 | `get_options_news` | ✅ 可调用 |
| 新闻资讯 | 个股新闻 | `get_ch_stock_month_news` | — |
| 新闻资讯 | 财经快讯(数据源sn) | `get_ch_sn_kx` | — |
| 新闻资讯 | 财经快讯(数据源A) | `get_ch_sa_kx` | — |
| 可转债 | 订阅可转债实时行情通道 | `subscribe_ch_kzz_stock_real` | — |
| 可转债 | 获取可转债实时行情 | `get_ch_kzz_cur_real` | — |
| 可转债 | 获取可转债列表 | `get_ch_kzz_stock` | — |
| ETF | 获取ETF基金列表 | `get_ch_etf_stock_list` | — |
| ETF | 获取ETF实时行情 | `get_ch_etf_real` | — |
| ETF | 获取ETF日K线 | `get_ch_etf_day_k` | — |
| ETF | 订阅ETF实时行情 | `subscribe_ch_etf_real` | — |
| 宏观数据 | 中国年度GDP同比增长率 | `get_ch_gdp_yearly_growth` | — |
| 宏观数据 | 中国季度GDP同比增长率 | `get_ch_gdp_quarter_rate` | — |
| 宏观数据 | 中国季度GDP环比增长率 | `get_ch_gdp_qoq_rate` | — |
| 宏观数据 | 中国GDP 季度数据 | `get_ch_gdp_quarter_value` | — |
| 宏观数据 | 中国GDP年度值 | `get_ch_gdp_year_value` | — |
| 宏观数据 | 汇丰制造业PMI终值  | `get_hsbc_pmi_final` | — |
| 宏观数据 | 汇丰制造业PMI初值 | `get_hsbc_pmi_preliminary` | — |
| 宏观数据 | 中国全社会用电量同比 | `get_ch_electricity_use_history` | — |
| 特色数据 | A股个股1分钟历史数据 | `a_stock_minute1_history` | — |
| 港股行情 | 订阅港股实时行情通道 | `subscribe_hk_stock_real` | — |
| 港股行情 | 获取港股实时行情 | `get_hk_stock_real` | — |
| 港股行情 | 订阅港股指数实时行情通道 | `subscribe_hk_market_real` | — |
| 港股行情 | 获取港股指数实时行情 | `get_hk_market_real` | — |
| 港股行情 | 港股股票列表 | `get_hk_stock` | — |
| 港股行情 | 港股个股历史日线 | `get_hk_stock_day_history` | — |
| 港股行情 | 港股个股历史周线 | `get_hk_stock_week_history` | — |
| 港股行情 | 港股个股历史月线 | `get_hk_stock_month_history` | — |
| 港股行情 | 港股指数历史日线 | `get_hk_market_history` | — |
| 港股行情 | 港股指数历史周线 | `get_hk_market_week_history` | — |
| 港股行情 | 港股指数历史月线 | `get_hk_market_month_history` | — |
| 港股行情 | 港股主要财务指标 | `get_hk_stock_main_fin_data` | — |
| 港股行情 | 港股资产负债表 | `get_hk_stock_balance_sheet` | — |
| 港股行情 | 港股利润表 | `get_hk_stock_profit_statement` | — |
| 港股行情 | 港股现金流表 | `get_hk_stock_cash_flow` | — |
| 美股行情 | 获取美股指数实时行情 | `get_us_market_real` | — |
| 美股行情 | 获取美股个股实时行情 | `get_us_stock_real` | — |
| 美股行情 | 订阅美股指数实时行情通道 | `subscribe_us_market_real` | — |
| 美股行情 | 订阅美股个股实时行情通道 | `subscribe_us_stock_real` | — |


## Tools

本地 MCP Server（`mcp/server.py`）暴露 22 个请求/响应工具，与公开测试账号的 22 个开放接口一一对应。

| Tool | Description |
|---|---|
| `ChStockCurReal` | A股实时行情快照 / Realtime snapshot of ALL A-share stocks |
| `ChMarketCurReal` | 指数实时快照 / Realtime snapshot of market indices |
| `ChConceptCurReal` | 概念板块实时快照 / Realtime snapshot of concept sectors |
| `ChIndustryCurReal` | 行业板块实时快照 / Realtime snapshot of industry sectors |
| `chStockList` | 股票列表 / List of all A-share stocks |
| `chConceptList` | 概念板块列表 / List of concept sectors |
| `chIndustryList` | 行业板块列表 / List of industry sectors |
| `ChOneStockReal` | 单只股票实时行情 / Realtime quote for ONE stock (e.g. "600519") |
| `chStockFrontDayHistory` | 个股前复权日线 / Forward-adjusted daily K-line for one stock |
| `chConceptDayHistory` | 概念板块日线 / Concept sector daily K-line |
| `chIndustryDayHistory` | 行业板块日线 / Industry sector daily K-line |
| `chStockMinuteHistory` | 个股分钟历史 / Minute-level K-line (1/5/15/30/60) |
| `ChMarketDayHistory` | 指数日线 / Index daily K-line |
| `ChCoreNews` | 核心资讯 / Core market news |
| `ChDomesticNews` | 国内财经要闻 / Domestic financial news |
| `ChGlobalNews` | 全球财经要闻 / Global financial news |
| `ChOptionNews` | 期权资讯 / Options-related news |
| `ChLimitUpDown` | 涨跌停统计 / Limit-up & limit-down statistics |
| `ChLhbData` | 龙虎榜数据 / Dragon-Tiger list data |
| `ChMarketFundFlow` | 市场资金流向 / Whole-market capital flow |
| `chAllMarketBearCompare` | 全市场多空对比 / Bull/bear comparison of the whole market |
| `chDdxStockData` | 个股DDX / DDX large-order tracking for one stock |

## 🤖 SKILL.md

仓库根目录 `SKILL.md` 供 Claude Code / OpenClaw 直接激活。

## 📝 深度文章

| 文章 | 内容 |
|---|---|
| [用 MCP 把 A 股实时行情接进 Claude / Cursor](docs/articles/01-tutorial-zh.md) | 5 分钟上手教程 · 安装 / 配置 / 实战示例 |
| [为什么 A 股数据用 NATS 推送而不是 REST 轮询](docs/articles/02-why-nats-zh.md) | 架构差异化 · Level-2 / DDX / 实时推送的技术原因 |
| [Building an MCP Server for A-share Realtime Data](docs/articles/03-architecture-en.md) | English · NATS push vs REST polling for market data |
| [行情数据用推送还是轮询？附可运行压测脚本](docs/articles/04-推送vs轮询-zh.md) | 纯技术 · 延迟量化方法 + 可复现 benchmark 脚本（可独立阅读） |
| [数据平台全景：Python · MCP · NATS 三种接入方式](docs/articles/05-数据平台全景-zh.md) | 全景指南 · 接口能力 · 三种接入方式对比 · 完整代码示例 |

## ☁️ 托管 MCP 端点

不想装 Python？直接用 Hugging Face 上的托管 Space（免安装、免注册，公开测试账号）：

**`D-Asce/pandastock-mcp-space`** → https://github.com/D-Asce/pandastock-mcp-space

MCP 客户端配置（注意 URL 尾斜杠不能省）：

```json
{ "mcpServers": { "panda-stock": { "url": "https://asce-pandastock-mcp.hf.space/gradio_api/mcp/" } } }
```

或在 https://huggingface.co/settings/mcp 点 Space 卡片上的 MCP 徽章一键添加。

## ⚖️ 许可证

MIT（见 `LICENSE`）。客户端开源，**调用后端需有效 phone/nid，按量计费**。

## 📰 已收录渠道

[SeekTool.ai Tools Directory](https://seektool.ai/)

<a href="https://www.toolpilot.ai" target="_blank"><img src="https://www.toolpilot.ai/cdn/shop/files/f-w_690x151_crop_center.png" alt="Featured on ToolPilot"></a>
