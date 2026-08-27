# pandaData SDK

> A 股数据 API + AI 选股 · 开源客户端

基于 **NATS** 的 A股 实时数据通道——行情、Level2、DDX 大单、资金流、选股信号**主动推给你**，不是让你轮询 REST。

> 📞 **接口咨询 / 专属 key 申请**：加微信 `onestock188` 或 `pandastock888`

## ✨ 特性

- **实时快照（请求/响应）**：4 个 CurReal 主题通过请求获取 A股 实时行情 / 指数 / 概念 / 行业，无需订阅
- **AI 选股**：`get_ch_select_stock()` 等 AI 选股接口
- **22 个开放接口**：全部为请求/响应接口（底层 176 个接口覆盖全量数据）
- **MCP ready**：提供本地 MCP Server（22 个工具），Claude / Cursor / OpenClaw 直接调用

## 安装

```bash
pip install nats-py==2.14.0
```

## 🚀 快速开始

```python
from panda_stock import PandaStock

# 公共测试账号（见下方"测试账号"），可直接试玩
ps = PandaStock(phone="pandastock", nid="pandastock")
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

## 🎁 公共测试账号

> 开放一个**公共测试账号**，无需申请即可直接试玩：

| 字段 | 值 |
|---|---|
| phone | `pandastock` |
| nid | `pandastock` |

> 公共账号**按来源 IP 限频、限接口、含全局日上限**，仅供评估试玩。
> 正式 / 高频 / 全量接口，请申请**专属 phone/nid**：加微信 onestock188 或 pandastock888

- 初始化示例：`PandaStock(phone="pandastock", nid="pandastock")`（与专属账号同一套服务端鉴权，仅配额不同）

## 🔑 测试账号可调用的 22 个接口（服务端共 176 个，完整清单 + 返回字段见 INTERFACES.md）

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

> 服务端共 **176 个接口**，完整清单（含「是否可测试」+ **每个接口返回的字段明细**）见 [`INTERFACES.md`](INTERFACES.md)（「接口返回字段详情」一节）。上表 22 个为已对公开 key 开放的请求接口。

## 全部 176 个接口一览（测试账号可调用标记）

> 完整返回字段见 [`INTERFACES.md`](INTERFACES.md) 的「接口返回字段详情」。标 ✅ 可调用 的即上方 22 个公开测试账号可调用接口；其余需专属 key 后使用。

| 分类 | 接口名称 | 方法(function) | 测试账号 |
|---|---|---|---|
| Levle2和大单 | 订阅Level2实时数据通道 | `subscribe_ch_l2_data_real` | — |
| Levle2和大单 | 获取Level2实时数据 | `get_ch_l2_data_cur_real` | — |
| Levle2和大单 | 订阅大单数据(DDE)通道 | `subscribe_ch_ddx_data_real` | — |
| Levle2和大单 | 获取大单数据(DDE) | `get_ch_ddx_data_cur_real` | — |
| Levle2和大单 | 获取个股历史大单历史数据 | `get_ch_stock_ddx_history` | — |
| Levle2和大单 | 个股千档数据 | `get_ch_stock_thousand_level_order` | — |
| Levle2和大单 | 个股实时资金流数据 | `get_ch_stock_l2_fund_flow_sa` | — |
| Levle2和大单 | 获取个股最新逐笔成交 | `get_ch_stock_l2_laster_transactions_sa` | — |
| Levle2和大单 | 获取个股全部逐笔成交数据 | `get_ch_stock_l2_all_transactions_sa` | — |
| Levle2和大单 | 市场实时资金流数据 | `get_ch_all_market_l2_fund_flow` | — |
| Levle2和大单 | 上证指数实时资金流数据 | `get_ch_sh_market_l2_fund_flow` | — |
| Levle2和大单 | 深圳市场实时资金流数据 | `get_ch_sz_market_l2_fund_flow` | — |
| Levle2和大单 | 创业板实时资金流数据 | `get_ch_cyb_market_l2_fund_flow` | — |
| Levle2和大单 | 科创板实时资金流数据 | `get_ch_kcb_market_l2_fund_flow` | — |
| Levle2和大单 | 个股实时大单成交明细 | `get_ch_stock_big_order` | — |
| Levle2和大单 | 订阅Level2单只股成交明细 | `subscribe_ch_l2_transaction_single` | — |
| Levle2和大单 | 订阅Level2多只股成交明细 | `subscribe_ch_l2_transaction_batch` | — |
| Levle2和大单 | 订阅Level2所有股成交明细 | `subscribe_ch_l2_transaction_all` | — |
| Levle2和大单 | 个股l2分价成交明细 | `get_ch_stock_price_summarize` | — |
| Levle2和大单 | 订阅l2单只股十档行情通道 | `subscribe_ch_l2_deep_single` | — |
| Levle2和大单 | 订阅l2多只股十档行情通道 | `subscribe_ch_l2_depth_batch` | — |
| Levle2和大单 | 订阅l2所有股票十档行情通道 | `subscribe_ch_l2_depth_all` | — |
| Levle2和大单 | 订阅l2单只个股买 一卖一明细 | `subscribe_ch_l2_orders_single` | — |
| Levle2和大单 | 订阅l2多只个股买 一卖一明细 | `subscribe_ch_l2_orders_batch` | — |
| Levle2和大单 | 订阅l2所有股票买 一卖一明细 | `subscribe_ch_l2_orders_all` | — |
| Levle2和大单 | 日内实时暗盘资金 | `get_ch_stock_dark_rank` | — |
| Levle2和大单 | 历史暗盘资金 | `get_ch_stock_dark_rank_history` | — |
| Levle2和大单 | 个股DDE实时数据 | `get_ch_stock_ea_dde` | — |
| 新闻资讯 | 重点资讯新闻 | `get_core_new` | ✅ 可调用 |
| 新闻资讯 | 国内主要新闻 | `get_domestic_financial_news` | ✅ 可调用 |
| 新闻资讯 | 国际主要新闻 | `get_global_financial_news` | ✅ 可调用 |
| 新闻资讯 | 时评类新闻 | `get_options_news` | ✅ 可调用 |
| 新闻资讯 | 个股新闻 | `get_ch_stock_month_news` | — |
| 新闻资讯 | 财经快讯(数据源sn) | `get_ch_sn_kx` | — |
| 新闻资讯 | 财经快讯(数据源SA) | `get_ch_sa_kx` | — |
| 新闻资讯 | 个股公告 | `get_ch_stock_announce` | — |
| 新闻资讯 | 个股研报 | `get_ch_stock_research_report` | — |
| 特色数据 | 每日ST股信息 | `get_ch_stock_st_history` | — |
| 特色数据 | 沪深300成分股权重 | `get_ch_hs300_constituent_weight_history` | — |
| 特色数据 | 上证50成分股权重 | `get_ch_sz50_constituent_weight_history` | — |
| 特色数据 | 中证500成分股权重 | `get_ch_zz500_constituent_weight_history` | — |
| 特色数据 | 中证1000成分股权重 | `get_ch_zz1000_constituent_weight_history` | — |
| 特色数据 | 个股除权除息历史 | `get_ch_stock_dividend_history` | — |
| 特色数据 | 年度高送转/分红 | `get_ch_year_high_stock_dividend` | — |
| 特色数据 | 个股股本变化历史 | `get_ch_stock_share_capital` | — |
| 特色数据 | 个股资金流明细历史 | `get_ch_stock_fund_flow_detail_history` | — |
| 特色数据 | 年度解禁数据 | `get_ch_year_stock_lock_up` | — |
| 特色数据 | 1日融资买入排行 | `get_ch_rz_buy_1_day` | — |
| 特色数据 | 5日融资买入排行 | `get_ch_rz_buy_5_day` | — |
| 特色数据 | 20日融资买入排行 | `get_ch_rz_buy_20_day` | — |
| 特色数据 | 个股一致行动人信息 | `get_ch_stock_pacs` | — |
| 特色数据 | 市场每个交易日涨跌平数量 | `get_ch_day_zd_count_history` | — |
| 特色数据 | 上证A股每个交易日涨跌平数量 | `get_ch_sh_day_zd_count_history` | — |
| 特色数据 | 深圳A股每个交易日涨跌平数量 | `get_ch_sz_day_zd_count_history` | — |
| 特色数据 | 创业板每个交易日涨跌平数量 | `get_ch_cyb_day_zd_count_history` | — |
| 特色数据 | 科创板每个交易日涨跌平数量 | `get_ch_kcb_day_zd_count_history` | — |
| 特色数据 | 北证每个交易日涨跌平数量 | `get_ch_bj_day_zd_count_history` | — |
| 特色数据 | 市场每个交易周涨跌平数量 | `get_ch_week_zd_count_history` | — |
| 特色数据 | 上证A股每个交易周涨跌平数量 | `get_ch_sh_week_zd_count_history` | — |
| 特色数据 | 深圳A股每个交易周涨跌平数量 | `get_ch_sz_week_zd_count_history` | — |
| 特色数据 | 创业板每个交易周涨跌平数量 | `get_ch_cyb_week_zd_count_history` | — |
| 特色数据 | 科创板每个交易周涨跌平数量 | `get_ch_kcb_week_zd_count_history` | — |
| 特色数据 | 北证每个交易周涨跌平数量 | `get_ch_bj_week_zd_count_history` | — |
| 特色数据 | 市场每个交易月涨跌平数量 | `get_ch_month_zd_count_history` | — |
| 特色数据 | 上证A股每个交易月涨跌平数量 | `get_ch_sh_month_zd_count_history` | — |
| 特色数据 | 深圳A股每个交易月涨跌平数量 | `get_ch_sz_month_zd_count_history` | — |
| 特色数据 | 创业板每个交易月涨跌平数量 | `get_ch_cyb_month_zd_count_history` | — |
| 特色数据 | 科创板每个交易月涨跌平数量 | `get_ch_kcb_month_zd_count_history` | — |
| 特色数据 | 北证每个交易月涨跌平数量 | `get_ch_bj_month_zd_count_history` | — |
| 特色数据 | 中国全社会用电量同比 | `get_ch_electricity_use_history` | — |
| 特色数据 | 全市场PE/PB 月数据历史 | `get_ch_market_pe_pb_month_history` | — |
| 特色数据 | 全市场PE/PB 日数据历史 | `get_ch_market_pe_pb_day_history` | — |
| 特色数据 | 中国年度GDP同比增长率 | `get_ch_gdp_yearly_growth` | — |
| 特色数据 | 中国季度GDP同比增长率 | `get_ch_gdp_quarter_rate` | — |
| 特色数据 | 中国季度GDP环比增长率 | `get_ch_gdp_qoq_rate` | — |
| 特色数据 | 个股l2分价成交明细历史 | `get_ch_stock_price_summarize_history` | — |
| 特色数据 | 交易日涨跌停时序数据 | `get_ch_limit_up_down_history` | — |
| 特色数据 | 交易日涨跌分布时序数据 | `get_ch_zd_map_history` | — |
| 特色数据 | 交易日涨停股信息 | `get_ch_lb_stock_history_history` | — |
| 特色数据 | 交易日全天成交额数据 | `get_ch_market_amount_curve_history` | — |
| 特色数据 | 中国GDP 季度数据 | `get_ch_gdp_quarter_value` | — |
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
| 个股数据 | 获取股票列表 | `get_ch_stock` | ✅ 可调用 |
| 个股数据 | 订阅实时行情通道 | `subscribe_ch_stock_real` | — |
| 个股数据 | 获取所有个股实时行情 | `get_ch_stock_real` | ✅ 可调用 |
| 个股数据 | 获取单只个股实时行情 | `get_ch_one_stock_real` | ✅ 可调用 |
| 个股数据 | 个股实时分钟K线 | `get_ch_stock_minute_real` | — |
| 个股数据 | 个股实时逐笔成交 | `get_ch_stock_transaction_real` | — |
| 个股数据 | 前复权日线 | `get_ch_stock_front_day_history` | ✅ 可调用 |
| 个股数据 | 前复权周线 | `get_ch_stock_front_week_history` | — |
| 个股数据 | 前复权月线 | `get_ch_stock_front_month_history` | — |
| 个股数据 | 后复权日线 | `get_ch_stock_back_day_history` | — |
| 个股数据 | 后复权周线 | `get_ch_stock_back_week_history` | — |
| 个股数据 | 后复权月线 | `get_ch_stock_back_month_history` | — |
| 个股数据 | 历史分笔 | `get_ch_stock_transaction_history` | — |
| 个股数据 | 主力评分数据 | `get_ch_stock_primer_info` | — |
| 个股数据 | 个股资金流 | `get_ch_stock_fund_flow` | — |
| 个股数据 | 人气排名数据 | `get_ch_stock_attention_tank` | — |
| 个股数据 | 股东人数历史 | `get_ch_stock_share_holder` | — |
| 个股数据 | 大宗交易历史 | `get_ch_stock_block_trading` | — |
| 个股数据 | 增减持历史 | `get_ch_stock_inc_or_dec` | — |
| 个股数据 | 等比前复权日线 | `get_ch_stock_front_ratio_history` | — |
| 个股数据 | 等比前复权周线 | `get_ch_stock_front_ratio_week_history` | — |
| 个股数据 | 等比前复权月线 | `get_ch_stock_front_ratio_month_history` | — |
| 个股数据 | 等比后复权日线 | `get_ch_stock_back_ratio_history` | — |
| 个股数据 | 历史分钟数据 | `get_ch_stock_minute_history` | ✅ 可调用 |
| 个股数据 | 个股分时图 | `get_ch_stock_time_line` | — |
| 个股数据 | 个股昨日分时图 | `get_ch_stock_time_line_yes` | — |
| 个股数据 | 个股五日分时 | `get_ch_stock_five_days_time_line` | — |
| 个股数据 | 个股竞价分时数据 | `get_ch_stock_auction_time_line` | — |
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
| 市场数据 | 获取融资融券余额 | `get_rzrq_balance` | — |
| 市场数据 | 上交所每日统计信息 | `get_sh_market_daily_info` | — |
| 市场数据 | 上交所每周统计信息 | `get_sh_market_week_info` | — |
| 市场数据 | 上交所每月统计信息 | `get_sh_market_month_info` | — |
| 市场数据 | 订阅指数实时行情通道 | `subscribe_ch_market_real` | — |
| 市场数据 | 获取指数实时行情 | `get_ch_market_real` | ✅ 可调用 |
| 市场数据 | 涨跌停数量历史 | `get_ch_limit_up_down` | ✅ 可调用 |
| 市场数据 | 指数日线 | `get_ch_market_day_history` | ✅ 可调用 |
| 市场数据 | 指数周线 | `get_ch_market_week_history` | — |
| 市场数据 | 指数月线 | `get_ch_market_month_history` | — |
| 市场数据 | 龙虎榜数据 | `get_lhb_data` | ✅ 可调用 |
| 市场数据 | 市场资金流历史 | `get_ch_market_fund_flow` | ✅ 可调用 |
| 市场数据 | 全市场买卖对比 | `get_ch_all_market_bear_compare` | ✅ 可调用 |
| 市场数据 | 上证买卖对比 | `get_ch_sh_market_bear_compare` | — |
| 市场数据 | 深证买卖对比 | `get_ch_sz_market_bear_compare` | — |
| 市场数据 | 创业板买卖对比 | `get_ch_cyb_market_bear_compare` | — |
| 市场数据 | 科创板买卖对比 | `get_ch_kcb_market_bear_compare` | — |
| 市场数据 | 北证买卖对比 | `get_ch_bj_market_bear_compare` | — |
| 市场数据 | 市场实时涨跌分布时序数据 | `get_ch_market_zd_map` | — |
| 市场数据 | 市场实时涨跌停数量 | `get_ch_today_limit_up_down` | — |
| 市场数据 | 市场实时涨停股列表 | `get_ch_today_lb_stock` | — |
| 市场数据 | 市场全天实时成交额 | `get_ch_market_amount_curve` | — |
| 财务数据 | 利润表 | `get_ch_stock_income_statement` | — |
| 财务数据 | 现金流表 | `get_ch_stock_cash_flow_statement` | — |
| 财务数据 | 财务主表 | `get_ch_stock_financial_indicators` | — |
| 财务数据 | 资产负债表 | `get_ch_stock_balance_sheet` | — |
| 财务数据 | 财务辅助表 | `get_ch_stock_auxiliary_data` | — |
| 财务数据 | 股东表 | `get_ch_stock_share_capital_and_shareholders` | — |
| 财务数据 | 业绩预告 | `get_ch_stock_net_profit` | — |
| 财务数据 | 财务核心指标(数据源SI) | `get_ch_si_stock_fin_key_indicators` | — |
| 财务数据 | 利润表(数据源SI) | `get_ch_si_stock_fin_income_statements` | — |
| 财务数据 | 资产负债表(数据源SI) | `get_ch_si_stock_fin_balance_sheet` | — |
| 财务数据 | 现金流表(数据源SI) | `get_ch_si_stock_fin_cash_flow` | — |
| 财务数据 | 个股财务核心指标(数据源Ea) | `get_ch_ea_stock_fin_key_indicators` | — |
| 财务数据 | 个股资产负债表(数据源Ea) | `get_ch_ea_stock_fin_balance_sheet` | — |
| 财务数据 | 个股利润表(数据源Ea) | `get_ch_ea_stock_fin_income_statements` | — |
| 财务数据 | 个股现金流量表(数据源Ea) | `get_ch_ea_stock_fin_cash_flow` | — |
| 可转债 | 订阅可转债实时行情通道 | `subscribe_ch_kzz_stock_real` | — |
| 可转债 | 获取可转债实时行情 | `get_ch_kzz_cur_real` | — |
| 可转债 | 获取可转债列表 | `get_ch_kzz_stock` | — |

## 🧩 MCP 接入（本地 stdio）

安装
```bash
pip install pandastock-mcp
```

更新
```bash
pip install --upgrade pandastock-mcp
```

Agent 配置
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

详见 `mcp/config_example.json`。

## 🤖 SKILL.md

仓库根目录 `SKILL.md` 供 Claude Code / OpenClaw 直接激活。

## ⚖️ 许可证

MIT（见 `LICENSE`）。客户端开源，**调用后端需有效 phone/nid，按量计费**。
