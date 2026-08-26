# pandaData 接口清单（全部 176 个，含返回字段）

> **图例**：✅ 可测试 = 已对公开 key 开放（免费试用可用，按来源 IP 限频）；— 暂未开放 = 需专属 key / 付费后使用。公共测试账号：`phone="pandastock"` / `nid="pandastock"`。

> 接口定义来源 `apis.json`（服务端 176 个接口）。其中 `get_ch_stock_ddx_data()` 已在 SDK 实现并开放，但未收录于 `apis.json`，于文末单独列出。

> 「接口返回字段详情」列出每个接口实际返回的字段（来自服务端 `returns` 定义），即调用后拿到的数据结构。


## 接口总览（176 个）

| 分类 | 接口名称 | 方法(function) | 可测试 |
|---|---|---|---|
| Levle2和大单 | 订阅Level2实时数据通道 | `subscribe_ch_l2_data_real` | — 暂未开放 |
| Levle2和大单 | 获取Level2实时数据 | `get_ch_l2_data_cur_real` | — 暂未开放 |
| Levle2和大单 | 订阅大单数据(DDE)通道 | `subscribe_ch_ddx_data_real` | — 暂未开放 |
| Levle2和大单 | 获取大单数据(DDE) | `get_ch_ddx_data_cur_real` | — 暂未开放 |
| Levle2和大单 | 获取个股历史大单历史数据 | `get_ch_stock_ddx_history` | — 暂未开放 |
| Levle2和大单 | 个股千档数据 | `get_ch_stock_thousand_level_order` | — 暂未开放 |
| Levle2和大单 | 个股实时资金流数据 | `get_ch_stock_l2_fund_flow_sa` | — 暂未开放 |
| Levle2和大单 | 获取个股最新逐笔成交 | `get_ch_stock_l2_laster_transactions_sa` | — 暂未开放 |
| Levle2和大单 | 获取个股全部逐笔成交数据 | `get_ch_stock_l2_all_transactions_sa` | — 暂未开放 |
| Levle2和大单 | 市场实时资金流数据 | `get_ch_all_market_l2_fund_flow` | — 暂未开放 |
| Levle2和大单 | 上证指数实时资金流数据 | `get_ch_sh_market_l2_fund_flow` | — 暂未开放 |
| Levle2和大单 | 深圳市场实时资金流数据 | `get_ch_sz_market_l2_fund_flow` | — 暂未开放 |
| Levle2和大单 | 创业板实时资金流数据 | `get_ch_cyb_market_l2_fund_flow` | — 暂未开放 |
| Levle2和大单 | 科创板实时资金流数据 | `get_ch_kcb_market_l2_fund_flow` | — 暂未开放 |
| Levle2和大单 | 个股实时大单成交明细 | `get_ch_stock_big_order` | — 暂未开放 |
| Levle2和大单 | 订阅Level2单只股成交明细 | `subscribe_ch_l2_transaction_single` | — 暂未开放 |
| Levle2和大单 | 订阅Level2多只股成交明细 | `subscribe_ch_l2_transaction_batch` | — 暂未开放 |
| Levle2和大单 | 订阅Level2所有股成交明细 | `subscribe_ch_l2_transaction_all` | — 暂未开放 |
| Levle2和大单 | 个股l2分价成交明细 | `get_ch_stock_price_summarize` | — 暂未开放 |
| Levle2和大单 | 订阅l2单只股十档行情通道 | `subscribe_ch_l2_deep_single` | — 暂未开放 |
| Levle2和大单 | 订阅l2多只股十档行情通道 | `subscribe_ch_l2_depth_batch` | — 暂未开放 |
| Levle2和大单 | 订阅l2所有股票十档行情通道 | `subscribe_ch_l2_depth_all` | — 暂未开放 |
| Levle2和大单 | 订阅l2单只个股买 一卖一明细 | `subscribe_ch_l2_orders_single` | — 暂未开放 |
| Levle2和大单 | 订阅l2多只个股买 一卖一明细 | `subscribe_ch_l2_orders_batch` | — 暂未开放 |
| Levle2和大单 | 订阅l2所有股票买 一卖一明细 | `subscribe_ch_l2_orders_all` | — 暂未开放 |
| Levle2和大单 | 日内实时暗盘资金 | `get_ch_stock_dark_rank` | — 暂未开放 |
| Levle2和大单 | 历史暗盘资金 | `get_ch_stock_dark_rank_history` | — 暂未开放 |
| Levle2和大单 | 个股DDE实时数据 | `get_ch_stock_ea_dde` | — 暂未开放 |
| 新闻资讯 | 重点资讯新闻 | `get_core_new` | ✅ 可测试 |
| 新闻资讯 | 国内主要新闻 | `get_domestic_financial_news` | ✅ 可测试 |
| 新闻资讯 | 国际主要新闻 | `get_global_financial_news` | ✅ 可测试 |
| 新闻资讯 | 时评类新闻 | `get_options_news` | ✅ 可测试 |
| 新闻资讯 | 个股新闻 | `get_ch_stock_month_news` | — 暂未开放 |
| 新闻资讯 | 财经快讯(数据源sn) | `get_ch_sn_kx` | — 暂未开放 |
| 新闻资讯 | 财经快讯(数据源SA) | `get_ch_sa_kx` | — 暂未开放 |
| 新闻资讯 | 个股公告 | `get_ch_stock_announce` | — 暂未开放 |
| 新闻资讯 | 个股研报 | `get_ch_stock_research_report` | — 暂未开放 |
| 特色数据 | 每日ST股信息 | `get_ch_stock_st_history` | — 暂未开放 |
| 特色数据 | 沪深300成分股权重 | `get_ch_hs300_constituent_weight_history` | — 暂未开放 |
| 特色数据 | 上证50成分股权重 | `get_ch_sz50_constituent_weight_history` | — 暂未开放 |
| 特色数据 | 中证500成分股权重 | `get_ch_zz500_constituent_weight_history` | — 暂未开放 |
| 特色数据 | 中证1000成分股权重 | `get_ch_zz1000_constituent_weight_history` | — 暂未开放 |
| 特色数据 | 个股除权除息历史 | `get_ch_stock_dividend_history` | — 暂未开放 |
| 特色数据 | 年度高送转/分红 | `get_ch_year_high_stock_dividend` | — 暂未开放 |
| 特色数据 | 个股股本变化历史 | `get_ch_stock_share_capital` | — 暂未开放 |
| 特色数据 | 个股资金流明细历史 | `get_ch_stock_fund_flow_detail_history` | — 暂未开放 |
| 特色数据 | 年度解禁数据 | `get_ch_year_stock_lock_up` | — 暂未开放 |
| 特色数据 | 1日融资买入排行 | `get_ch_rz_buy_1_day` | — 暂未开放 |
| 特色数据 | 5日融资买入排行 | `get_ch_rz_buy_5_day` | — 暂未开放 |
| 特色数据 | 20日融资买入排行 | `get_ch_rz_buy_20_day` | — 暂未开放 |
| 特色数据 | 个股一致行动人信息 | `get_ch_stock_pacs` | — 暂未开放 |
| 特色数据 | 市场每个交易日涨跌平数量 | `get_ch_day_zd_count_history` | — 暂未开放 |
| 特色数据 | 上证A股每个交易日涨跌平数量 | `get_ch_sh_day_zd_count_history` | — 暂未开放 |
| 特色数据 | 深圳A股每个交易日涨跌平数量 | `get_ch_sz_day_zd_count_history` | — 暂未开放 |
| 特色数据 | 创业板每个交易日涨跌平数量 | `get_ch_cyb_day_zd_count_history` | — 暂未开放 |
| 特色数据 | 科创板每个交易日涨跌平数量 | `get_ch_kcb_day_zd_count_history` | — 暂未开放 |
| 特色数据 | 北证每个交易日涨跌平数量 | `get_ch_bj_day_zd_count_history` | — 暂未开放 |
| 特色数据 | 市场每个交易周涨跌平数量 | `get_ch_week_zd_count_history` | — 暂未开放 |
| 特色数据 | 上证A股每个交易周涨跌平数量 | `get_ch_sh_week_zd_count_history` | — 暂未开放 |
| 特色数据 | 深圳A股每个交易周涨跌平数量 | `get_ch_sz_week_zd_count_history` | — 暂未开放 |
| 特色数据 | 创业板每个交易周涨跌平数量 | `get_ch_cyb_week_zd_count_history` | — 暂未开放 |
| 特色数据 | 科创板每个交易周涨跌平数量 | `get_ch_kcb_week_zd_count_history` | — 暂未开放 |
| 特色数据 | 北证每个交易周涨跌平数量 | `get_ch_bj_week_zd_count_history` | — 暂未开放 |
| 特色数据 | 市场每个交易月涨跌平数量 | `get_ch_month_zd_count_history` | — 暂未开放 |
| 特色数据 | 上证A股每个交易月涨跌平数量 | `get_ch_sh_month_zd_count_history` | — 暂未开放 |
| 特色数据 | 深圳A股每个交易月涨跌平数量 | `get_ch_sz_month_zd_count_history` | — 暂未开放 |
| 特色数据 | 创业板每个交易月涨跌平数量 | `get_ch_cyb_month_zd_count_history` | — 暂未开放 |
| 特色数据 | 科创板每个交易月涨跌平数量 | `get_ch_kcb_month_zd_count_history` | — 暂未开放 |
| 特色数据 | 北证每个交易月涨跌平数量 | `get_ch_bj_month_zd_count_history` | — 暂未开放 |
| 特色数据 | 中国全社会用电量同比 | `get_ch_electricity_use_history` | — 暂未开放 |
| 特色数据 | 全市场PE/PB 月数据历史 | `get_ch_market_pe_pb_month_history` | — 暂未开放 |
| 特色数据 | 全市场PE/PB 日数据历史 | `get_ch_market_pe_pb_day_history` | — 暂未开放 |
| 特色数据 | 中国年度GDP同比增长率 | `get_ch_gdp_yearly_growth` | — 暂未开放 |
| 特色数据 | 中国季度GDP同比增长率 | `get_ch_gdp_quarter_rate` | — 暂未开放 |
| 特色数据 | 中国季度GDP环比增长率 | `get_ch_gdp_qoq_rate` | — 暂未开放 |
| 特色数据 | 个股l2分价成交明细历史 | `get_ch_stock_price_summarize_history` | — 暂未开放 |
| 特色数据 | 交易日涨跌停时序数据 | `get_ch_limit_up_down_history` | — 暂未开放 |
| 特色数据 | 交易日涨跌分布时序数据 | `get_ch_zd_map_history` | — 暂未开放 |
| 特色数据 | 交易日涨停股信息 | `get_ch_lb_stock_history_history` | — 暂未开放 |
| 特色数据 | 交易日全天成交额数据 | `get_ch_market_amount_curve_history` | — 暂未开放 |
| 特色数据 | 中国GDP 季度数据 | `get_ch_gdp_quarter_value` | — 暂未开放 |
| 港股行情 | 订阅港股实时行情通道 | `subscribe_hk_stock_real` | — 暂未开放 |
| 港股行情 | 获取港股实时行情 | `get_hk_stock_real` | — 暂未开放 |
| 港股行情 | 订阅港股指数实时行情通道 | `subscribe_hk_market_real` | — 暂未开放 |
| 港股行情 | 获取港股指数实时行情 | `get_hk_market_real` | — 暂未开放 |
| 港股行情 | 港股股票列表 | `get_hk_stock` | — 暂未开放 |
| 港股行情 | 港股个股历史日线 | `get_hk_stock_day_history` | — 暂未开放 |
| 港股行情 | 港股个股历史周线 | `get_hk_stock_week_history` | — 暂未开放 |
| 港股行情 | 港股个股历史月线 | `get_hk_stock_month_history` | — 暂未开放 |
| 港股行情 | 港股指数历史日线 | `get_hk_market_history` | — 暂未开放 |
| 港股行情 | 港股指数历史周线 | `get_hk_market_week_history` | — 暂未开放 |
| 港股行情 | 港股指数历史月线 | `get_hk_market_month_history` | — 暂未开放 |
| 港股行情 | 港股主要财务指标 | `get_hk_stock_main_fin_data` | — 暂未开放 |
| 港股行情 | 港股资产负债表 | `get_hk_stock_balance_sheet` | — 暂未开放 |
| 港股行情 | 港股利润表 | `get_hk_stock_profit_statement` | — 暂未开放 |
| 港股行情 | 港股现金流表 | `get_hk_stock_cash_flow` | — 暂未开放 |
| 个股数据 | 获取股票列表 | `get_ch_stock` | ✅ 可测试 |
| 个股数据 | 订阅实时行情通道 | `subscribe_ch_stock_real` | — 暂未开放 |
| 个股数据 | 获取所有个股实时行情 | `get_ch_stock_real` | ✅ 可测试 |
| 个股数据 | 获取单只个股实时行情 | `get_ch_one_stock_real` | ✅ 可测试 |
| 个股数据 | 个股实时分钟K线 | `get_ch_stock_minute_real` | — 暂未开放 |
| 个股数据 | 个股实时逐笔成交 | `get_ch_stock_transaction_real` | — 暂未开放 |
| 个股数据 | 前复权日线 | `get_ch_stock_front_day_history` | ✅ 可测试 |
| 个股数据 | 前复权周线 | `get_ch_stock_front_week_history` | — 暂未开放 |
| 个股数据 | 前复权月线 | `get_ch_stock_front_month_history` | — 暂未开放 |
| 个股数据 | 后复权日线 | `get_ch_stock_back_day_history` | — 暂未开放 |
| 个股数据 | 后复权周线 | `get_ch_stock_back_week_history` | — 暂未开放 |
| 个股数据 | 后复权月线 | `get_ch_stock_back_month_history` | — 暂未开放 |
| 个股数据 | 历史分笔 | `get_ch_stock_transaction_history` | — 暂未开放 |
| 个股数据 | 主力评分数据 | `get_ch_stock_primer_info` | — 暂未开放 |
| 个股数据 | 个股资金流 | `get_ch_stock_fund_flow` | — 暂未开放 |
| 个股数据 | 人气排名数据 | `get_ch_stock_attention_tank` | — 暂未开放 |
| 个股数据 | 股东人数历史 | `get_ch_stock_share_holder` | — 暂未开放 |
| 个股数据 | 大宗交易历史 | `get_ch_stock_block_trading` | — 暂未开放 |
| 个股数据 | 增减持历史 | `get_ch_stock_inc_or_dec` | — 暂未开放 |
| 个股数据 | 等比前复权日线 | `get_ch_stock_front_ratio_history` | — 暂未开放 |
| 个股数据 | 等比前复权周线 | `get_ch_stock_front_ratio_week_history` | — 暂未开放 |
| 个股数据 | 等比前复权月线 | `get_ch_stock_front_ratio_month_history` | — 暂未开放 |
| 个股数据 | 等比后复权日线 | `get_ch_stock_back_ratio_history` | — 暂未开放 |
| 个股数据 | 历史分钟数据 | `get_ch_stock_minute_history` | ✅ 可测试 |
| 个股数据 | 个股分时图 | `get_ch_stock_time_line` | — 暂未开放 |
| 个股数据 | 个股昨日分时图 | `get_ch_stock_time_line_yes` | — 暂未开放 |
| 个股数据 | 个股五日分时 | `get_ch_stock_five_days_time_line` | — 暂未开放 |
| 个股数据 | 个股竞价分时数据 | `get_ch_stock_auction_time_line` | — 暂未开放 |
| 板块数据 | 获取概念板块列表 | `get_ch_concept` | ✅ 可测试 |
| 板块数据 | 获取行业板块列表 | `get_ch_industry` | ✅ 可测试 |
| 板块数据 | 订阅概念板块实时行情通道 | `subscribe_ch_concept_real` | — 暂未开放 |
| 板块数据 | 获取概念板块实时行情 | `get_ch_concept_real` | ✅ 可测试 |
| 板块数据 | 订阅行业板块实时行情通道 | `subscribe_ch_industry_real` | — 暂未开放 |
| 板块数据 | 获取行业板块实时行情 | `get_ch_industry_real` | ✅ 可测试 |
| 板块数据 | 概念板块日线 | `get_ch_concept_day_history` | ✅ 可测试 |
| 板块数据 | 概念板块周线 | `get_ch_concept_week_history` | — 暂未开放 |
| 板块数据 | 概念板块月线 | `get_ch_concept_month_history` | — 暂未开放 |
| 板块数据 | 行业板块日线 | `get_ch_industry_day_history` | ✅ 可测试 |
| 板块数据 | 行业板块周线 | `get_ch_industry_week_history` | — 暂未开放 |
| 板块数据 | 行业板块月线 | `get_ch_industry_month_history` | — 暂未开放 |
| 市场数据 | 获取融资融券余额 | `get_rzrq_balance` | — 暂未开放 |
| 市场数据 | 上交所每日统计信息 | `get_sh_market_daily_info` | — 暂未开放 |
| 市场数据 | 上交所每周统计信息 | `get_sh_market_week_info` | — 暂未开放 |
| 市场数据 | 上交所每月统计信息 | `get_sh_market_month_info` | — 暂未开放 |
| 市场数据 | 订阅指数实时行情通道 | `subscribe_ch_market_real` | — 暂未开放 |
| 市场数据 | 获取指数实时行情 | `get_ch_market_real` | ✅ 可测试 |
| 市场数据 | 涨跌停数量历史 | `get_ch_limit_up_down` | ✅ 可测试 |
| 市场数据 | 指数日线 | `get_ch_market_day_history` | ✅ 可测试 |
| 市场数据 | 指数周线 | `get_ch_market_week_history` | — 暂未开放 |
| 市场数据 | 指数月线 | `get_ch_market_month_history` | — 暂未开放 |
| 市场数据 | 龙虎榜数据 | `get_lhb_data` | ✅ 可测试 |
| 市场数据 | 市场资金流历史 | `get_ch_market_fund_flow` | ✅ 可测试 |
| 市场数据 | 全市场买卖对比 | `get_ch_all_market_bear_compare` | ✅ 可测试 |
| 市场数据 | 上证买卖对比 | `get_ch_sh_market_bear_compare` | — 暂未开放 |
| 市场数据 | 深证买卖对比 | `get_ch_sz_market_bear_compare` | — 暂未开放 |
| 市场数据 | 创业板买卖对比 | `get_ch_cyb_market_bear_compare` | — 暂未开放 |
| 市场数据 | 科创板买卖对比 | `get_ch_kcb_market_bear_compare` | — 暂未开放 |
| 市场数据 | 北证买卖对比 | `get_ch_bj_market_bear_compare` | — 暂未开放 |
| 市场数据 | 市场实时涨跌分布时序数据 | `get_ch_market_zd_map` | — 暂未开放 |
| 市场数据 | 市场实时涨跌停数量 | `get_ch_today_limit_up_down` | — 暂未开放 |
| 市场数据 | 市场实时涨停股列表 | `get_ch_today_lb_stock` | — 暂未开放 |
| 市场数据 | 市场全天实时成交额 | `get_ch_market_amount_curve` | — 暂未开放 |
| 财务数据 | 利润表 | `get_ch_stock_income_statement` | — 暂未开放 |
| 财务数据 | 现金流表 | `get_ch_stock_cash_flow_statement` | — 暂未开放 |
| 财务数据 | 财务主表 | `get_ch_stock_financial_indicators` | — 暂未开放 |
| 财务数据 | 资产负债表 | `get_ch_stock_balance_sheet` | — 暂未开放 |
| 财务数据 | 财务辅助表 | `get_ch_stock_auxiliary_data` | — 暂未开放 |
| 财务数据 | 股东表 | `get_ch_stock_share_capital_and_shareholders` | — 暂未开放 |
| 财务数据 | 业绩预告 | `get_ch_stock_net_profit` | — 暂未开放 |
| 财务数据 | 财务核心指标(数据源SI) | `get_ch_si_stock_fin_key_indicators` | — 暂未开放 |
| 财务数据 | 利润表(数据源SI) | `get_ch_si_stock_fin_income_statements` | — 暂未开放 |
| 财务数据 | 资产负债表(数据源SI) | `get_ch_si_stock_fin_balance_sheet` | — 暂未开放 |
| 财务数据 | 现金流表(数据源SI) | `get_ch_si_stock_fin_cash_flow` | — 暂未开放 |
| 财务数据 | 个股财务核心指标(数据源Ea) | `get_ch_ea_stock_fin_key_indicators` | — 暂未开放 |
| 财务数据 | 个股资产负债表(数据源Ea) | `get_ch_ea_stock_fin_balance_sheet` | — 暂未开放 |
| 财务数据 | 个股利润表(数据源Ea) | `get_ch_ea_stock_fin_income_statements` | — 暂未开放 |
| 财务数据 | 个股现金流量表(数据源Ea) | `get_ch_ea_stock_fin_cash_flow` | — 暂未开放 |
| 可转债 | 订阅可转债实时行情通道 | `subscribe_ch_kzz_stock_real` | — 暂未开放 |
| 可转债 | 获取可转债实时行情 | `get_ch_kzz_cur_real` | — 暂未开放 |
| 可转债 | 获取可转债列表 | `get_ch_kzz_stock` | — 暂未开放 |

## 汇总
- 接口总数（apis.json）：**176**
- 已开放可测试：**21**（含文末补充 1 个，合计 22 个已开放）
- 暂未开放：**155**

## 已开放接口（22 个，公开 key 可用）
- `get_ch_all_market_bear_compare`
- `get_ch_concept`
- `get_ch_concept_day_history`
- `get_ch_concept_real`
- `get_ch_industry`
- `get_ch_industry_day_history`
- `get_ch_industry_real`
- `get_ch_limit_up_down`
- `get_ch_market_day_history`
- `get_ch_market_fund_flow`
- `get_ch_market_real`
- `get_ch_one_stock_real`
- `get_ch_stock`
- `get_ch_stock_ddx_data`
- `get_ch_stock_front_day_history`
- `get_ch_stock_minute_history`
- `get_ch_stock_real`
- `get_core_new`
- `get_domestic_financial_news`
- `get_global_financial_news`
- `get_lhb_data`
- `get_options_news`

> 说明：`get_ch_stock_ddx_data()` 对应主题 `chDdxStockData`，已在 `panda_stock.py` 实现且纳入开放范围，但未出现在 `apis.json` 接口目录中，故上表未计其行，此处单列。


## 接口返回字段详情

### 订阅Level2实时数据通道 — `subscribe_ch_l2_data_real`
分类：Levle2和大单 ｜ 可测试：—

  - `action_amount` (number)：当日竞价成交金额（万元）
  - `pre_action_amount` (number)：昨日竞价成交金额（万元）
  - `l2_vol_rise_speed` (number)：成交量涨速
  - `l2_total_buy_vol` (number)：买入委托总量
  - `l2_total_sell_vol` (number)：卖出委托总量
  - `l2_buy_cancel` (number)：撤销的买入委托总量
  - `l2_sell_cancel` (number)：撤销的卖出委托总量
  - `l2_deal_tick_num` (integer)：成交笔数
  - `l2_order_tick_num` (integer)：委托笔数
  - `inst_aggressive_buy_amount` (number)：主力主动净买额（万元）
  - `inst_net_amount` (number)：主力净流入金额（万元）

### 获取Level2实时数据 — `get_ch_l2_data_cur_real`
分类：Levle2和大单 ｜ 可测试：—

  - `action_amount` (number)：当日竞价成交金额（万元）
  - `pre_action_amount` (number)：昨日竞价成交金额（万元）
  - `l2_vol_rise_speed` (number)：成交量涨速
  - `l2_total_buy_vol` (number)：买入委托总量
  - `l2_total_sell_vol` (number)：卖出委托总量
  - `l2_buy_cancel` (number)：撤销的买入委托总量
  - `l2_sell_cancel` (number)：撤销的卖出委托总量
  - `l2_deal_tick_num` (integer)：成交笔数
  - `l2_order_tick_num` (integer)：委托笔数
  - `inst_aggressive_buy_amount` (number)：主力主动净买额（万元）
  - `inst_net_amount` (number)：主力净流入金额（万元）

### 订阅大单数据(DDE)通道 — `subscribe_ch_ddx_data_real`
分类：Levle2和大单 ｜ 可测试：—

  - `ddx` (number)：当日DDX（大单动向）
  - `ddy` (number)：当日DDY（涨跌动因）
  - `ddz` (number)：当日DDZ（大单差分）
  - `ddx_positive_in_five` (number)：5日内DDX为正的天数
  - `ddx_positive_in_ten` (number)：10日内DDX为正的天数
  - `ddx_inc_days` (number)：DDX连续递增天数
  - `ddx_positive_continue_days` (number)：DDX连续为正的天数
  - `bbd_amount` (number)：大单净额（万元）
  - `sell_odd` (integer)：卖出单数
  - `buy_odd` (integer)：买入单数
  - `odd_ratio` (number)：单数比（卖出单数/买入单数）
  - `big_odd_ratio` (number)：大单单差（大单买入占比 - 大单卖出占比）
  - `big_odd_buy_ratio` (number)：大单买入金额占总成交额比例
  - `big_odd_sell_ratio` (number)：大单卖出金额占总成交额比例
  - `medium_odd_ratio` (number)：中单单差（中单买入占比 - 中单卖出占比）
  - `small_odd_ratio` (number)：小单单差（小单买入占比 - 小单卖出占比）
  - `small_odd_buy_ratio` (number)：小单买入金额占总成交额比例
  - `small_odd_sell_ratio` (number)：小单卖出金额占总成交额比例
  - `xl_odd_ratio` (number)：超大单单差（超大单买入占比 - 超大单卖出占比）
  - `xl_odd_buy_ratio` (number)：超大单买入金额占总成交额比例
  - `xl_odd_sell_ratio` (number)：超大单卖出金额占总成交额比例

### 获取大单数据(DDE) — `get_ch_ddx_data_cur_real`
分类：Levle2和大单 ｜ 可测试：—

  - `ddx` (number)：当日DDX（大单动向）
  - `ddy` (number)：当日DDY（涨跌动因）
  - `ddz` (number)：当日DDZ（大单差分）
  - `ddx_positive_in_five` (number)：5日内DDX为正的天数
  - `ddx_positive_in_ten` (number)：10日内DDX为正的天数
  - `ddx_inc_days` (number)：DDX连续递增天数
  - `ddx_positive_continue_days` (number)：DDX连续为正的天数
  - `bbd_amount` (number)：大单净额（万元）
  - `sell_odd` (integer)：卖出单数
  - `buy_odd` (integer)：买入单数
  - `odd_ratio` (number)：单数比（卖出单数/买入单数）
  - `big_odd_ratio` (number)：大单单差（大单买入占比 - 大单卖出占比）
  - `big_odd_buy_ratio` (number)：大单买入金额占总成交额比例
  - `big_odd_sell_ratio` (number)：大单卖出金额占总成交额比例
  - `medium_odd_ratio` (number)：中单单差（中单买入占比 - 中单卖出占比）
  - `small_odd_ratio` (number)：小单单差（小单买入占比 - 小单卖出占比）
  - `small_odd_buy_ratio` (number)：小单买入金额占总成交额比例
  - `small_odd_sell_ratio` (number)：小单卖出金额占总成交额比例
  - `xl_odd_ratio` (number)：超大单单差（超大单买入占比 - 超大单卖出占比）
  - `xl_odd_buy_ratio` (number)：超大单买入金额占总成交额比例
  - `xl_odd_sell_ratio` (number)：超大单卖出金额占总成交额比例

### 获取个股历史大单历史数据 — `get_ch_stock_ddx_history`
分类：Levle2和大单 ｜ 可测试：—

  - `ddx` (number)：当天ddx
  - `ddy` (number)：当天ddy
  - `ddz` (number)：当天ddz
  - `ddx_positive_in_five` (number)：5日内 DDX 为正的天数
  - `ddx_positive_in_ten` (number)：10日内 DDX 为正的天数
  - `ddx_positive_continue_days` (number)：ddx 连续为正的天数
  - `ddx_inc_days` (number)：ddx 连续递增天数
  - `bbd_amount` (number)：大单净额(万元)
  - `sell_odd` (integer)：卖出单数
  - `buy_odd` (integer)：买入单数
  - `odd_ratio` (number)：单数比  卖出单数/买入单数
  - `xl_odd_ratio` (number)：超大单单差   超大单买入占比 - 超大单卖出占比
  - `xl_odd_buy_ratio` (number)：超大单买入金额占总成交额比例
  - `xl_odd_sell_ratio` (number)：超大单卖出金额占总成交额比例
  - `big_odd_ratio` (number)：大单单差   大单买入占比 - 大单卖出占比
  - `big_odd_buy_ratio` (number)：大单买入金额占总成交额比例
  - `big_odd_sell_ratio` (number)：大单卖出金额占总成交额比例
  - `medium_odd_ratio` (number)：中单单差   中单买入占比 - 中单卖出占比
  - `small_odd_ratio` (number)：小单单差   小单买入占比 - 小单卖出占比
  - `small_odd_buy_ratio` (number)：小单买入金额占总成交额比例
  - `small_odd_sell_ratio` (number)：小单卖出金额占总成交额比例

### 个股千档数据 — `get_ch_stock_thousand_level_order`
分类：Levle2和大单 ｜ 可测试：—

  - `buy` (dict)：买方数据
  - `sell` (dict)：卖方数据

### 个股实时资金流数据 — `get_ch_stock_l2_fund_flow_sa`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `super_big_net_amt` (number)：超大单净额
  - `big_net_amt` (number)：大单净额
  - `medium_net_amt` (number)：中单净额
  - `small_net_amt` (number)：小单净额

### 获取个股最新逐笔成交 — `get_ch_stock_l2_laster_transactions_sa`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `price` (number)：成交量
  - `direction` (string)：买卖方向，buy-买，sell-卖，其他-中性

### 获取个股全部逐笔成交数据 — `get_ch_stock_l2_all_transactions_sa`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `price` (number)：成交价格
  - `volume` (number)：成交量
  - `direction` (string)：买卖方向，buy-买，sell-卖，其他-中性

### 市场实时资金流数据 — `get_ch_all_market_l2_fund_flow`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `date` (string)：日期
  - `super_big_net_amt` (number)：超大单净流入金额
  - `big_net_amt` (number)：大单净流入金额
  - `medium_net_amt` (number)：中单净流入金额
  - `small_net_amt` (number)：小单净流入金额
  - `super_big_in` (number)：超大单买入金额
  - `super_big_out` (number)：超大单卖出金额
  - `big_in` (number)：大单买入金额
  - `big_out` (number)：大单卖出金额
  - `medium_in` (number)：中单买入金额
  - `medium_out` (number)：中单卖出金额
  - `small_in` (number)：小单买入金额
  - `small_out` (number)：小单卖出金额

### 上证指数实时资金流数据 — `get_ch_sh_market_l2_fund_flow`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `date` (string)：日期
  - `super_big_net_amt` (number)：超大单净流入金额
  - `big_net_amt` (number)：大单净流入金额
  - `medium_net_amt` (number)：中单净流入金额
  - `small_net_amt` (number)：小单净流入金额
  - `super_big_in` (number)：超大单买入金额
  - `super_big_out` (number)：超大单卖出金额
  - `big_in` (number)：大单买入金额
  - `big_out` (number)：大单卖出金额
  - `medium_in` (number)：中单买入金额
  - `medium_out` (number)：中单卖出金额
  - `small_in` (number)：小单买入金额
  - `small_out` (number)：小单卖出金额

### 深圳市场实时资金流数据 — `get_ch_sz_market_l2_fund_flow`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `date` (string)：日期
  - `super_big_net_amt` (number)：超大单净流入金额
  - `big_net_amt` (number)：大单净流入金额
  - `medium_net_amt` (number)：中单净流入金额
  - `small_net_amt` (number)：小单净流入金额
  - `super_big_in` (number)：超大单买入金额
  - `super_big_out` (number)：超大单卖出金额
  - `big_in` (number)：大单买入金额
  - `big_out` (number)：大单卖出金额
  - `medium_in` (number)：中单买入金额
  - `medium_out` (number)：中单卖出金额
  - `small_in` (number)：小单买入金额
  - `small_out` (number)：小单卖出金额

### 创业板实时资金流数据 — `get_ch_cyb_market_l2_fund_flow`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `date` (string)：日期
  - `super_big_net_amt` (number)：超大单净流入金额
  - `big_net_amt` (number)：大单净流入金额
  - `medium_net_amt` (number)：中单净流入金额
  - `small_net_amt` (number)：小单净流入金额
  - `super_big_in` (number)：超大单买入金额
  - `super_big_out` (number)：超大单卖出金额
  - `big_in` (number)：大单买入金额
  - `big_out` (number)：大单卖出金额
  - `medium_in` (number)：中单买入金额
  - `medium_out` (number)：中单卖出金额
  - `small_in` (number)：小单买入金额
  - `small_out` (number)：小单卖出金额

### 科创板实时资金流数据 — `get_ch_kcb_market_l2_fund_flow`
分类：Levle2和大单 ｜ 可测试：—

  - `time` (string)：时间
  - `date` (string)：日期
  - `super_big_net_amt` (number)：超大单净流入金额
  - `big_net_amt` (number)：大单净流入金额
  - `medium_net_amt` (number)：中单净流入金额
  - `small_net_amt` (number)：小单净流入金额
  - `super_big_in` (number)：超大单买入金额
  - `super_big_out` (number)：超大单卖出金额
  - `big_in` (number)：大单买入金额
  - `big_out` (number)：大单卖出金额
  - `medium_in` (number)：中单买入金额
  - `medium_out` (number)：中单卖出金额
  - `small_in` (number)：小单买入金额
  - `small_out` (number)：小单卖出金额

### 个股实时大单成交明细 — `get_ch_stock_big_order`
分类：Levle2和大单 ｜ 可测试：—

  - `ticktime` (string)：时间
  - `price` (number)：成交价
  - `volume` (number)：成交量
  - `amount` (number)：成交额
  - `kind` (string)：成交类型。U 主动买入，D 主动卖出，E 中性

### 订阅Level2单只股成交明细 — `subscribe_ch_l2_transaction_single`
分类：Levle2和大单 ｜ 可测试：—

  - `id` (string)：成交ID
  - `time` (string)：时间
  - `price` (number)：成交价
  - `vol` (number)：成交量
  - `side` (string)：成交方向。B 主动买，S 主动卖，M 中性

### 订阅Level2多只股成交明细 — `subscribe_ch_l2_transaction_batch`
分类：Levle2和大单 ｜ 可测试：—

  - `id` (string)：成交ID
  - `time` (string)：时间
  - `price` (number)：成交价
  - `vol` (number)：成交量
  - `side` (string)：成交方向。B 主动买，S 主动卖，M 中性

### 订阅Level2所有股成交明细 — `subscribe_ch_l2_transaction_all`
分类：Levle2和大单 ｜ 可测试：—

  - `id` (string)：成交ID
  - `time` (string)：时间
  - `price` (number)：成交价
  - `vol` (number)：成交量
  - `side` (string)：成交方向。B 主动买，S 主动卖，M 中性

### 个股l2分价成交明细 — `get_ch_stock_price_summarize`
分类：Levle2和大单 ｜ 可测试：—

  - `price` (number)：成交价格
  - `vol` (number)：成交量(股)
  - `zb` (number)：该价位成交量占总成交量比例
  - `jml` (number)：主动买入占比
  - `b_vol` (number)：主动买量(股)
  - `s_vol` (number)：主动卖量(股)

### 订阅l2单只股十档行情通道 — `subscribe_ch_l2_deep_single`
分类：Levle2和大单 ｜ 可测试：—

  - `code` (string)：个股代码
  - `name` (string)：个股名称
  - `time` (string)：时间
  - `date` (string)：日期
  - `prev_close` (number)：昨收价
  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `price` (number)：当前价
  - `volume` (number)：成交量
  - `amount` (number)：成交额
  - `bids` (list)：买十档信息
  - `asks` (list)：卖十档信息

### 订阅l2多只股十档行情通道 — `subscribe_ch_l2_depth_batch`
分类：Levle2和大单 ｜ 可测试：—

  - `code` (string)：个股代码
  - `name` (string)：个股名称
  - `time` (string)：时间
  - `date` (string)：日期
  - `prev_close` (number)：昨收价
  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `price` (number)：当前价
  - `volume` (number)：成交量
  - `amount` (number)：成交额
  - `bids` (list)：买十档信息
  - `asks` (list)：卖十档信息

### 订阅l2所有股票十档行情通道 — `subscribe_ch_l2_depth_all`
分类：Levle2和大单 ｜ 可测试：—

  - `code` (string)：个股代码
  - `name` (string)：个股名称
  - `time` (string)：时间
  - `date` (string)：日期
  - `prev_close` (number)：昨收价
  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `price` (number)：当前价
  - `volume` (number)：成交量
  - `amount` (number)：成交额
  - `bids` (list)：买十档信息
  - `asks` (list)：卖十档信息

### 订阅l2单只个股买 一卖一明细 — `subscribe_ch_l2_orders_single`
分类：Levle2和大单 ｜ 可测试：—

  - `code` (string)：个股代码
  - `time` (string)：时间
  - `buy_price` (number)：买一价
  - `sell_price` (number)：卖一价
  - `buy_vol` (number)：买一总量(股)
  - `buy_count` (number)：买单笔数
  - `sell_vol` (number)：卖一总量（股）
  - `sell_count` (number)：卖单笔数
  - `buy_queue` (list)：买队列逐笔明细，最多返回50笔
  - `sell_queue` (list)：卖队列逐笔明细，最多返回50笔

### 订阅l2多只个股买 一卖一明细 — `subscribe_ch_l2_orders_batch`
分类：Levle2和大单 ｜ 可测试：—

  - `code` (string)：个股代码
  - `time` (string)：时间
  - `buy_price` (number)：买一价
  - `sell_price` (number)：卖一价
  - `buy_vol` (number)：买一总量(股)
  - `buy_count` (number)：买单笔数
  - `sell_vol` (number)：卖一总量（股）
  - `sell_count` (number)：卖单笔数
  - `buy_queue` (list)：买队列逐笔明细，最多返回50笔
  - `sell_queue` (list)：卖队列逐笔明细，最多返回50笔

### 订阅l2所有股票买 一卖一明细 — `subscribe_ch_l2_orders_all`
分类：Levle2和大单 ｜ 可测试：—

  - `code` (string)：个股代码
  - `time` (string)：时间
  - `buy_price` (number)：买一价
  - `sell_price` (number)：卖一价
  - `buy_vol` (number)：买一总量(股)
  - `buy_count` (number)：买单笔数
  - `sell_vol` (number)：卖一总量（股）
  - `sell_count` (number)：卖单笔数
  - `buy_queue` (list)：买队列逐笔明细，最多返回50笔
  - `sell_queue` (list)：卖队列逐笔明细，最多返回50笔

### 日内实时暗盘资金 — `get_ch_stock_dark_rank`
分类：Levle2和大单 ｜ 可测试：—

  - `date` (string)：日期
  - `value` (list)：个股列表

### 历史暗盘资金 — `get_ch_stock_dark_rank_history`
分类：Levle2和大单 ｜ 可测试：—

  - `date` (string)：日期
  - `value` (list)：个股列表

### 个股DDE实时数据 — `get_ch_stock_ea_dde`
分类：Levle2和大单 ｜ 可测试：—

  - `code` (string)：个股代码
  - `name` (string)：个股名称
  - `today_ddx` (number)：当天ddx 数值
  - `today_ddy` (number)：当天ddy 数值
  - `today_ddz` (number)：当天ddz 数据
  - `five_ddx` (number)：近五日ddx
  - `five_ddy` (number)：近五日ddy
  - `ten_ddx` (number)：近十日ddx
  - `ten_ddy` (number)：近十日ddy
  - `red_in_five` (number)：近五日ddx 为正的天数
  - `red_in_ten` (number)：近十日ddx 为正的天数
  - `red_continue` (number)：近期ddx 连续为正的天数

### 重点资讯新闻 — `get_core_new`
分类：新闻资讯 ｜ 可测试：✅

  - `date` (string)：发布日期时间
  - `content` (string)：正文
  - `title` (string)：标题

### 国内主要新闻 — `get_domestic_financial_news`
分类：新闻资讯 ｜ 可测试：✅

  - `date` (string)：发布日期
  - `content` (string)：正文
  - `title` (string)：标题

### 国际主要新闻 — `get_global_financial_news`
分类：新闻资讯 ｜ 可测试：✅

  - `date` (string)：发布日期
  - `content` (string)：正文
  - `title` (string)：标题

### 时评类新闻 — `get_options_news`
分类：新闻资讯 ｜ 可测试：✅

  - `date` (string)：发布日期
  - `content` (string)：正文
  - `title` (string)：标题

### 个股新闻 — `get_ch_stock_month_news`
分类：新闻资讯 ｜ 可测试：—

  - `date` (string)：发布日期
  - `content` (string)：新闻内容
  - `title` (string)：新闻标题

### 财经快讯(数据源sn) — `get_ch_sn_kx`
分类：新闻资讯 ｜ 可测试：—

  - `date` (string)：日期 YYYY-MM-DD
  - `id` (string)：快讯唯一ID
  - `title` (string)：标题
  - `content` (string)：正文全文
  - `time_ms` (number)：发布时间(毫秒时间戳)
  - `tags_json` (string)：标签JSON，包含话题标签和关联股票信息

### 财经快讯(数据源SA) — `get_ch_sa_kx`
分类：新闻资讯 ｜ 可测试：—

  - `content` (string)：快讯内容
  - `time_ms` (string)：时间戳字符串
  - `tags_json` (string)：关联的标签列表
  - `title` (string)：标题
  - `date` (string)：日期

### 个股公告 — `get_ch_stock_announce`
分类：新闻资讯 ｜ 可测试：—

  - `date` (string)：日期
  - `data` (list)：日内发布的公告列表数据
  - `ann_id` (string)：公告ID
  - `title` (string)：公告标题
  - `content` (string)：公告内容

### 个股研报 — `get_ch_stock_research_report`
分类：新闻资讯 ｜ 可测试：—

  - `date` (string)：日期
  - `reports` (list)：当天发布的研报数据表
  - `title` (string)：研报名称
  - `org` (string)：研报发布机构名称
  - `analyst` (string)：研报分析员
  - `content` (string)：研报内容

### 每日ST股信息 — `get_ch_stock_st_history`
分类：特色数据 ｜ 可测试：—

  - `reason` (string)：加ST/加*ST
  - `change_date` (string)：变更为ST股时间
  - `code` (string)：个股代码

### 沪深300成分股权重 — `get_ch_hs300_constituent_weight_history`
分类：特色数据 ｜ 可测试：—

  - `weight` (number)：权重数值
  - `code` (string)：个股代码
  - `date` (string)：日期

### 上证50成分股权重 — `get_ch_sz50_constituent_weight_history`
分类：特色数据 ｜ 可测试：—

  - `weight` (number)：权重数值
  - `code` (string)：个股代码
  - `date` (string)：日期

### 中证500成分股权重 — `get_ch_zz500_constituent_weight_history`
分类：特色数据 ｜ 可测试：—

  - `weight` (number)：权重数值
  - `code` (string)：个股代码
  - `date` (string)：日期

### 中证1000成分股权重 — `get_ch_zz1000_constituent_weight_history`
分类：特色数据 ｜ 可测试：—

  - `weight` (number)：权重数值
  - `code` (string)：个股代码
  - `date` (string)：日期

### 个股除权除息历史 — `get_ch_stock_dividend_history`
分类：特色数据 ｜ 可测试：—

  - `type` (string)：类型 1 除权除息 2 扩/缩股 3 配股调整
  - `bonus` (number)：红利 (元)
  - `share_bonus` (number)：送股数量
  - `allotment` (number)：配股数量
  - `allo_price` (number)：配股价格
  - `date` (string)：日期

### 年度高送转/分红 — `get_ch_year_high_stock_dividend`
分类：特色数据 ｜ 可测试：—

  - `name` (string)：股票名称
  - `capitalization_issue` (number)：转增(每10股)
  - `stock_dividend` (number)：送股(每10股)
  - `cash_dividend` (number)：派现(每10股 元)
  - `recorde_date` (number)：股权登记日
  - `dps` (number)：每股收益(元)
  - `reps` (number)：每股未分配利润(元)
  - `crps` (number)：每股资本公积金(元)
  - `tag_date` (string)：公告日期
  - `report_type` (string)：公告类型
  - `code` (string)：股票代码

### 个股股本变化历史 — `get_ch_stock_share_capital`
分类：特色数据 ｜ 可测试：—

  - `total_shares` (string)：总股本(股)
  - `circulating_shares` (number)：流通股本(股)
  - `date` (number)：日期

### 个股资金流明细历史 — `get_ch_stock_fund_flow_detail_history`
分类：特色数据 ｜ 可测试：—

  - `change_percent` (string)：涨跌幅(%)
  - `turnover_amount` (number)：成交额(万元)
  - `main_net_inflow` (number)：主力净流入金额(万元)
  - `main_net_inflow_ratio` (number)：主力资金净流入比率(%)
  - `super_large_buy_amount` (number)：超大单买入金额(万元)
  - `super_large_buy_volume` (number)：超大单买入量(万股)
  - `super_large_buy_avg_price` (number)：超大单买入均价(元)
  - `super_large_sell_amount` (number)：超大单卖出金额(万元)
  - `super_large_sell_volume` (number)：超大单卖出量(万股)
  - `super_large_sell_avg_price` (number)：超大单卖出均价(元)
  - `super_large_net_buy_amount` (number)：超大单净买入金额(万元)
  - `large_buy_amount` (number)：大单买入金额(万元)
  - `large_buy_volume` (number)：大单买入量(万股)
  - `large_buy_avg_price` (number)：大单买入均价(元)
  - `large_sell_amount` (number)：大单卖出金额(万元)
  - `large_sell_volume` (number)：大单卖出量(万股)
  - `large_sell_avg_price` (number)：大单卖出均价(元)
  - `large_net_buy_amount` (number)：大单净买入金额(万元)
  - `medium_buy_amount` (number)：中单买入金额(万元)
  - `medium_buy_volume` (number)：中单买入量(万股)
  - `medium_buy_avg_price` (number)：中单买入均价(元)
  - `medium_sell_amount` (number)：中单卖出金额(万元)
  - `medium_sell_volume` (number)：中单卖出量(万股)
  - `medium_sell_avg_price` (number)：中单卖出均价(元)
  - `medium_net_buy_amount` (number)：中单净买入金额(万元)
  - `small_buy_amount` (number)：小单买入金额(万元)
  - `small_buy_volume` (number)：小单买入量(万股)
  - `small_buy_avg_price` (number)：小单买入均价(元)
  - `small_sell_amount` (number)：小单卖出金额(万元)
  - `small_sell_volume` (number)：小单卖出量(万股)
  - `small_sell_avg_price` (number)：小单卖出均价(元)
  - `small_net_buy_amount` (number)：小单净买入金额(万元)

### 年度解禁数据 — `get_ch_year_stock_lock_up`
分类：特色数据 ｜ 可测试：—

  - `name` (string)：股票名称
  - `expiration_date` (string)：解禁日期
  - `expiration_count` (number)：解禁数量(万股)
  - `expiration_float_rate` (number)：解禁占已流通A股比例(%)
  - `expiration_total_rate` (number)：解禁占总股本比例(%)
  - `expiration_amount` (number)：解禁市值(万元)
  - `expiration_type` (string)：解禁类型
  - `code` (string)：

### 1日融资买入排行 — `get_ch_rz_buy_1_day`
分类：特色数据 ｜ 可测试：—

  - `name` (string)：股票名称
  - `buy_amount` (number)：融资净买入(万元)
  - `rz_balance` (number)：融资余额(万元)
  - `increase` (number)：增幅(%)
  - `float_cap_percent` (number)：占流通市值比例(%)
  - `margin_balance` (number)：两融余额(万元)
  - `date` (string)：日期
  - `code` (string)：股票代码

### 5日融资买入排行 — `get_ch_rz_buy_5_day`
分类：特色数据 ｜ 可测试：—

  - `name` (string)：股票名称
  - `buy_amount` (number)：融资净买入(万元)
  - `rz_balance` (number)：融资余额(万元)
  - `increase` (number)：增幅(%)
  - `float_cap_percent` (number)：占流通市值比例(%)
  - `margin_balance` (number)：两融余额(万元)
  - `date` (string)：日期
  - `code` (string)：股票代码

### 20日融资买入排行 — `get_ch_rz_buy_20_day`
分类：特色数据 ｜ 可测试：—

  - `name` (string)：股票名称
  - `buy_amount` (number)：融资净买入(万元)
  - `rz_balance` (number)：融资余额(万元)
  - `increase` (number)：增幅(%)
  - `float_cap_percent` (number)：占流通市值比例(%)
  - `margin_balance` (number)：两融余额(万元)
  - `code` (string)：股票代码
  - `date` (string)：日期

### 个股一致行动人信息 — `get_ch_stock_pacs`
分类：特色数据 ｜ 可测试：—

  - `stock_code` (string)：股票代码
  - `col_cutoff_date` (string)：截止日期
  - `col_shareholder` (string)：股东名称
  - `col_type` (string)：股东性质
  - `col_group_qty` (number)：一致行动组持股数量(股)
  - `col_group_pct` (number)：一致行动组占总股本比例(%)
  - `col_group_mv` (number)：一致行动组期末参考市值(元)
  - `col_sh_qty` (number)：股东持股数量(股)
  - `col_sh_pct` (number)：股东持股占总股本比例(%)
  - `col_sh_mv` (number)：股东持股期末参考市值(元)
  - `col_sh_nature` (number)：股东股本性质
  - `col_sh_rank` (number)：股东股东排名
  - `col_sh_t_qty` (number)：股东持流通股数量(股)
  - `col_sh_t_pct` (number)：股东持流通股占总股本比例(%)
  - `col_sh_t_mv` (number)：股东持流通股期末参考市值(元)
  - `col_sh_t_nature` (string)：股东持流通股股本性质
  - `col_sh_t_rank` (number)：股东持流通股股东排名
  - `col_group_t_qty` (number)：一致行动组持流通股(股)
  - `col_group_t_pct` (number)：一致行动组持流通股占总股本比例(%)
  - `col_group_t_mv` (number)：一致行动组持流通股期末参考市值(元)

### 市场每个交易日涨跌平数量 — `get_ch_day_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 上证A股每个交易日涨跌平数量 — `get_ch_sh_day_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 深圳A股每个交易日涨跌平数量 — `get_ch_sz_day_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 创业板每个交易日涨跌平数量 — `get_ch_cyb_day_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 科创板每个交易日涨跌平数量 — `get_ch_kcb_day_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 北证每个交易日涨跌平数量 — `get_ch_bj_day_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 市场每个交易周涨跌平数量 — `get_ch_week_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (string)：上涨数量
  - `xd` (string)：下跌数量
  - `pp` (string)：平盘数量

### 上证A股每个交易周涨跌平数量 — `get_ch_sh_week_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨
  - `xd` (number)：下跌
  - `pp` (number)：平盘

### 深圳A股每个交易周涨跌平数量 — `get_ch_sz_week_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 创业板每个交易周涨跌平数量 — `get_ch_cyb_week_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 科创板每个交易周涨跌平数量 — `get_ch_kcb_week_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 北证每个交易周涨跌平数量 — `get_ch_bj_week_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 市场每个交易月涨跌平数量 — `get_ch_month_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 上证A股每个交易月涨跌平数量 — `get_ch_sh_month_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 深圳A股每个交易月涨跌平数量 — `get_ch_sz_month_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 创业板每个交易月涨跌平数量 — `get_ch_cyb_month_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 科创板每个交易月涨跌平数量 — `get_ch_kcb_month_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 北证每个交易月涨跌平数量 — `get_ch_bj_month_zd_count_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `sz` (number)：上涨数量
  - `xd` (number)：下跌数量
  - `pp` (number)：平盘数量

### 中国全社会用电量同比 — `get_ch_electricity_use_history`
分类：特色数据 ｜ 可测试：—

  - `tag_date` (string)：发布日期
  - `attache_date` (string)：数据所属月份
  - `val` (string)：数值
  - `pre_val` (string)：前值
  - `except_val` (string)：预期值

### 全市场PE/PB 月数据历史 — `get_ch_market_pe_pb_month_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `pe` (number)：市场市盈率(不包含亏损股)
  - `pe_loss` (number)：市场市盈率(包含亏损股)
  - `pb` (number)：市场市净率

### 全市场PE/PB 日数据历史 — `get_ch_market_pe_pb_day_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `pe` (number)：市场市盈率(不包含亏损股)
  - `pe_loss` (number)：市场市盈率(包含亏损股)
  - `pb` (number)：市场市净率

### 中国年度GDP同比增长率 — `get_ch_gdp_yearly_growth`
分类：特色数据 ｜ 可测试：—

  - `previous` (string)：上一次公布的年度GDP增速
  - `consensus` (string)：市场预测的年度GDP增速（通常无预期）
  - `actual` (string)：当期实际公布的年度GDP增速（如"5"表示5%）
  - `pub_time` (string)：数据发布时间
  - `revised` (string)：对前值的修正值（通常无修正）
  - `date` (string)：数据对应的统计周期

### 中国季度GDP同比增长率 — `get_ch_gdp_quarter_rate`
分类：特色数据 ｜ 可测试：—

  - `previous` (string)：上一次公布的季度GDP同比增速
  - `consensus` (string)：市场预测的季度GDP同比增速（空表示无预期）
  - `actual` (string)：当期实际公布的季度GDP同比增速（如"5"表示5%）
  - `pub_time` (string)：数据发布时间
  - `revised` (string)：对前值的修正值（通常无修正）
  - `date` (string)：数据对应的统计周期

### 中国季度GDP环比增长率 — `get_ch_gdp_qoq_rate`
分类：特色数据 ｜ 可测试：—

  - `previous` (string)：上一次公布的季度GDP环比增速
  - `consensus` (string)：市场预测的季度GDP环比增速（通常无预期）
  - `actual` (string)：当期实际公布的季度GDP环比增速（如"1.3"表示1.3%）
  - `pub_time` (string)：数据发布时间
  - `revised` (string)：对前值的修正值（通常无修正）
  - `date` (string)：数据对应的统计周期

### 个股l2分价成交明细历史 — `get_ch_stock_price_summarize_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `val` (list)：分家数据列表

### 交易日涨跌停时序数据 — `get_ch_limit_up_down_history`
分类：特色数据 ｜ 可测试：—

  - `date` (string)：日期
  - `rise` (number)：涨停数量
  - `fall` (number)：跌停数量
  - `zhaban` (number)：炸板数量
  - `nonword` (number)：非一字涨停数量
  - `tradetime` (string)：时间

### 交易日涨跌分布时序数据 — `get_ch_zd_map_history`
分类：特色数据 ｜ 可测试：—

  - `time` (string)：时间
  - `up_over_10` (number)：涨幅>10%
  - `up_7_10` (number)：涨幅7%~10%
  - `up_5_7` (number)：涨幅5%~7%
  - `up_2_5` (number)：涨幅2%~5%
  - `up_0_2` (number)：涨幅0%~2%
  - `flat` (number)：平盘
  - `down_0_2` (number)：跌幅0%~2%
  - `down_2_5` (number)：跌幅2%~5%
  - `down_5_7` (number)：跌幅5%~7%
  - `down_7_10` (number)：跌幅7%~10%
  - `down_over_10` (string)：跌幅>10%

### 交易日涨停股信息 — `get_ch_lb_stock_history_history`
分类：特色数据 ｜ 可测试：—

  - `today_lb_ratio` (string)：当日连板晋级率
  - `stocks` (list)：涨停个股列表

### 交易日全天成交额数据 — `get_ch_market_amount_curve_history`
分类：特色数据 ｜ 可测试：—

  - `time` (string)：时间
  - `amount` (number)：成交额

### 中国GDP 季度数据 — `get_ch_gdp_quarter_value`
分类：特色数据 ｜ 可测试：—

  - `previous` (string)：上一季度GDP总量，单位：亿
  - `date` (string)：数据对应的统计周期
  - `consensus` (string)：市场预测的季度GDP总量（空值表示无预期）
  - `actual` (string)：当期实际公布的季度GDP总量（如"334193"表示334193亿元）
  - `pub_time` (string)：数据发布时间
  - `revised` (string)：对前值的修正值（通常无修正）

### 订阅港股实时行情通道 — `subscribe_hk_stock_real`
分类：港股行情 ｜ 可测试：—

  - `name` (string)：个股名称
  - `last_close` (string)：昨日收盘价
  - `open` (string)：今日开盘价
  - `high` (string)：今日最高价
  - `low` (string)：今日最低价
  - `close` (string)：现价
  - `amount` (string)：成交额（万元）
  - `change` (string)：涨跌幅
  - `volume` (string)：成交量(手)
  - `time` (string)：时间

### 获取港股实时行情 — `get_hk_stock_real`
分类：港股行情 ｜ 可测试：—

  - `name` (string)：个股名称
  - `last_close` (string)：昨日收盘价
  - `open` (string)：今日开盘价
  - `high` (string)：今日最高价
  - `low` (string)：今日最低价
  - `close` (string)：现价
  - `amount` (string)：成交额（万元）
  - `change` (string)：涨跌幅
  - `volume` (string)：成交量(手)
  - `time` (string)：时间

### 订阅港股指数实时行情通道 — `subscribe_hk_market_real`
分类：港股行情 ｜ 可测试：—

  - `name` (string)：指数名称
  - `last_close` (string)：昨日收盘价
  - `open` (string)：今日开盘价
  - `high` (string)：今日最高价
  - `low` (string)：今日最低价
  - `close` (string)：现价
  - `amount` (string)：成交额（万元）
  - `change` (string)：涨跌幅
  - `date` (string)：日期
  - `time` (string)：时间

### 获取港股指数实时行情 — `get_hk_market_real`
分类：港股行情 ｜ 可测试：—

  - `name` (string)：指数名称
  - `last_close` (string)：昨日收盘价
  - `open` (string)：今日开盘价
  - `high` (string)：今日最高价
  - `low` (string)：今日最低价
  - `close` (string)：现价
  - `amount` (string)：成交额（万元）
  - `change` (string)：涨跌幅
  - `date` (string)：日期
  - `time` (string)：时间

### 港股股票列表 — `get_hk_stock`
分类：港股行情 ｜ 可测试：—

  - `code` (string)：个股代码
  - `total_shares` (string)：总股本(股)
  - `time_to_market` (string)：上市日期

### 港股个股历史日线 — `get_hk_stock_day_history`
分类：港股行情 ｜ 可测试：—

  - `open` (string)：开盘价
  - `high` (string)：最高价
  - `low` (string)：最低价
  - `last_close` (string)：昨收价
  - `volume` (string)：成交量(股)
  - `amount` (string)：成交额(万元)
  - `date` (string)：日期

### 港股个股历史周线 — `get_hk_stock_week_history`
分类：港股行情 ｜ 可测试：—

  - `open` (string)：开盘价
  - `high` (string)：最高价
  - `low` (string)：最低价
  - `last_close` (string)：昨收价
  - `volume` (string)：成交量(股)
  - `amount` (string)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (string)：周内交易天数

### 港股个股历史月线 — `get_hk_stock_month_history`
分类：港股行情 ｜ 可测试：—

  - `open` (string)：开盘价
  - `high` (string)：最高价
  - `low` (string)：最低价
  - `last_close` (string)：昨收价
  - `volume` (string)：成交量(股)
  - `amount` (string)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (string)：周内交易天数

### 港股指数历史日线 — `get_hk_market_history`
分类：港股行情 ｜ 可测试：—

  - `open` (string)：开盘价
  - `high` (string)：最高价
  - `low` (string)：最低价
  - `last_close` (string)：昨收价
  - `volume` (string)：成交量(股)
  - `amount` (string)：成交额(万元)
  - `date` (string)：日期

### 港股指数历史周线 — `get_hk_market_week_history`
分类：港股行情 ｜ 可测试：—

  - `open` (string)：开盘价
  - `high` (string)：最高价
  - `low` (string)：最低价
  - `last_close` (string)：昨收价
  - `volume` (string)：成交量(股)
  - `amount` (string)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (string)：周内交易天数

### 港股指数历史月线 — `get_hk_market_month_history`
分类：港股行情 ｜ 可测试：—

  - `open` (string)：开盘价
  - `high` (string)：最高价
  - `low` (string)：最低价
  - `last_close` (string)：昨收价
  - `volume` (string)：成交量(股)
  - `amount` (string)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (string)：周内交易天数

### 港股主要财务指标 — `get_hk_stock_main_fin_data`
分类：港股行情 ｜ 可测试：—

  - `diluted_eps` (string)：稀释每股收益(元)
  - `ttm_eps` (string)：TTM每股收益(元)
  - `bvps` (string)：每股净资产(元)
  - `ops_cash_per_share` (string)：每股经营现金流(元)
  - `ops_rev_per_share` (string)：每股营业收入(元)
  - `total_revenue` (string)：营业总收入(元)
  - `revenue_yoy` (string)：营业总收入同比增长(%)
  - `revenue_qoq` (string)：营业总收入滚动环比增长(%)
  - `gross_profit` (string)：毛利润(元)
  - `gp_yoy` (string)：毛利润同比增长(%)

### 港股资产负债表 — `get_hk_stock_balance_sheet`
分类：港股行情 ｜ 可测试：—

  - `investment_property` (string)：投资物业
  - `intangible_assets` (string)：无形资产
  - `land_use_rights` (string)：土地使用权
  - `construction_in_progress` (string)：在建工程
  - `deferred_tax_assets` (string)：递延所得税资产
  - `prepayments_other_assets` (string)：预付款项、按金及其他资产
  - `investment_in_associates` (string)：于联营公司的投资
  - `investment_in_joint_ventures` (string)：于合营公司的投资
  - `fvtpl_financial_assets` (string)：指定以公允价值记账之金融资产
  - `time_deposits` (string)：定期存款

### 港股利润表 — `get_hk_stock_profit_statement`
分类：港股行情 ｜ 可测试：—

  - `report_type` (string)：报告类型
  - `turnover` (string)：营业额
  - `other_revenue` (string)：其他收入
  - `total_revenue` (string)：总收入
  - `cost_of_revenue` (string)：收入成本
  - `gross_profit` (string)：毛利
  - `other_income_loss_net` (string)：其他收益/(亏损)净额
  - `sales_marketing_expenses` (string)：销售及市场推广开支
  - `general_admin_expenses` (string)：一般及行政开支
  - `operating_profit` (string)：经营盈利

### 港股现金流表 — `get_hk_stock_cash_flow`
分类：港股行情 ｜ 可测试：—

  - `report_type` (string)：报告类型
  - `profit_before_tax_subtotal` (string)：除税前溢利小计
  - `interest_income` (string)：利息收入
  - `interest_and_related_expenses` (string)：利息及相关开支
  - `dividend_income` (string)：股息收入
  - `share_of_associates_jv_profit_loss` (string)：分占联营公司及合营公司的(盈利)/亏损净额
  - `impairment_loss` (string)：无形资产、土地使用权、使用权资产、投资物业以及物业、设备及器材的减值净额
  - `fv_gain_loss` (string)：以公允价值计量且其变动计入损益的金融资产及其他金融工具的公允价值收益净额
  - `gain_on_disposal_of_assets` (string)：减:出售资产之溢利
  - `depreciation_amortization` (string)：加:折旧及摊销

### 获取股票列表 — `get_ch_stock`
分类：个股数据 ｜ 可测试：✅

  - `name` (string)：股票名称
  - `total_shares` (number)：总股本(股)
  - `circulating_shares` (number)：流通股本(股)
  - `time_to_market` (string)：上市日期
  - `belong_hs300` (number)：是否属于沪深300 1 属于  0  不属于
  - `belong_rzrq` (number)：是否属于融资融券标的 1 属于  0  不属于
  - `belong_hsgt` (number)：是否属于沪深股通 1 属于  0  不属于
  - `is_st` (number)：是否是ST股票 1 属于  0  不属于
  - `code` (string)：股票代码

### 订阅实时行情通道 — `subscribe_ch_stock_real`
分类：个股数据 ｜ 可测试：—

  - `time` (string)：数据时间，格式 yyyy-MM-dd HH:mm:ss
  - `close` (number)：当前价（元）
  - `open` (number)：开盘价（元）
  - `high` (number)：最高价（元）
  - `low` (number)：最低价（元）
  - `last_close` (number)：上个交易日收盘价（元）
  - `amount` (number)：成交额（元）
  - `volume` (number)：成交量（手）
  - `pre_volume` (number)：前成交量（手）
  - `buy_five` (list)：买五档价格
  - `buy_five_vol` (list)：买五档量
  - `sell_five` (list)：卖五档价格
  - `sell_five_vol` (list)：卖五档量
  - `turnover` (number)：换手率（%）
  - `volume_ratio` (number)：量比
  - `bid_ask_ratio` (number)：委比（%）
  - `market_cap` (number)：总市值（元）
  - `float_cap` (number)：流通市值（元）
  - `dynamic_pe` (number)：动态市盈率
  - `static_pe` (number)：静态市盈率
  - `pb` (number)：市净率

### 获取所有个股实时行情 — `get_ch_stock_real`
分类：个股数据 ｜ 可测试：✅

  - `time` (string)：数据时间，格式 yyyy-MM-dd HH:mm:ss
  - `close` (number)：当前价（元）
  - `open` (number)：开盘价（元）
  - `high` (number)：最高价（元）
  - `low` (number)：最低价（元）
  - `last_close` (number)：上个交易日收盘价（元）
  - `amount` (number)：成交额（元）
  - `volume` (number)：成交量（手）
  - `pre_volume` (number)：前成交量（手）
  - `buy_five` (list)：买五档价格
  - `buy_five_vol` (list)：买五档量
  - `sell_five` (list)：卖五档价格
  - `sell_five_vol` (list)：卖五档量
  - `turnover` (number)：换手率（%）
  - `volume_ratio` (number)：量比
  - `bid_ask_ratio` (number)：委比（%）
  - `market_cap` (number)：总市值（元）
  - `float_cap` (number)：流通市值（元）
  - `dynamic_pe` (number)：动态市盈率
  - `static_pe` (number)：静态市盈率
  - `pb` (number)：市净率

### 获取单只个股实时行情 — `get_ch_one_stock_real`
分类：个股数据 ｜ 可测试：✅

  - `time` (string)：数据时间
  - `close` (number)：当前价（元）
  - `open` (number)：开盘价（元）
  - `high` (number)：最高价（元）
  - `low` (number)：最低价（元）
  - `last_close` (number)：上个交易日收盘价（元）
  - `amount` (number)：成交额（元）
  - `volume` (number)：成交量（手）
  - `pre_volume` (number)：前成交量（手）
  - `buy_five` (list)：买五档价格
  - `buy_five_vol` (list)：买五档量
  - `sell_five` (list)：卖五档价格
  - `sell_five_vol` (list)：卖五档量
  - `turnover` (number)：换手率（%）
  - `volume_ratio` (number)：量比
  - `bid_ask_ratio` (number)：委比（%）
  - `market_cap` (number)：总市值（元）
  - `float_cap` (number)：流通市值（元）
  - `dynamic_pe` (number)：动态市盈率
  - `static_pe` (number)：静态市盈率
  - `pb` (number)：市净率
  - `action_amount` (number)：当日竞价成交金额（万元）
  - `pre_action_amount` (number)：昨日竞价成交金额（万元）
  - `l2_vol_rise_speed` (number)：成交量涨速
  - `l2_total_buy_vol` (number)：买入委托总量
  - `l2_total_sell_vol` (number)：卖出委托总量
  - `l2_buy_cancel` (number)：撤销的买入委托总量
  - `l2_sell_cancel` (number)：撤销的卖出委托总量
  - `l2_deal_tick_num` (integer)：成交笔数
  - `l2_order_tick_num` (integer)：委托笔数

### 个股实时分钟K线 — `get_ch_stock_minute_real`
分类：个股数据 ｜ 可测试：—

  - `date_time` (string)：日期时间
  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `close` (number)：收盘价
  - `amount` (number)：成交额（元）
  - `volume` (number)：成交量（手）

### 个股实时逐笔成交 — `get_ch_stock_transaction_real`
分类：个股数据 ｜ 可测试：—

  - `time` (string)：成交时间
  - `price` (number)：成交价格
  - `volume` (number)：成交量（手）
  - `buy_or_sell` (integer)：买卖方向：0=买盘，1=卖盘

### 前复权日线 — `get_ch_stock_front_day_history`
分类：个股数据 ｜ 可测试：✅

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `close` (number)：收盘价

### 前复权周线 — `get_ch_stock_front_week_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：周内交易天数
  - `close` (number)：收盘价

### 前复权月线 — `get_ch_stock_front_month_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：月内交易天数
  - `close` (number)：收盘价

### 后复权日线 — `get_ch_stock_back_day_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `close` (number)：收盘价

### 后复权周线 — `get_ch_stock_back_week_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：周内交易天数
  - `close` (number)：收盘价

### 后复权月线 — `get_ch_stock_back_month_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：月内交易天数
  - `close` (number)：收盘价

### 历史分笔 — `get_ch_stock_transaction_history`
分类：个股数据 ｜ 可测试：—

  - `price` (number)：价格
  - `volume` (number)：成交量
  - `buy_or_sell` (number)：买卖方向  0 买盘  1 卖盘
  - `time` (string)：时间

### 主力评分数据 — `get_ch_stock_primer_info`
分类：个股数据 ｜ 可测试：—

  - `score_change` (number)：评分较上一日变动
  - `stock_rank` (number)：评分打败股票比例
  - `score_msg` (string)：评分总结文字
  - `tomorrow_up_percent` (number)：次日上涨概率
  - `tomorrow_avg_zf` (number)：次日平均涨幅
  - `tomorrow_cal_count` (number)：次日信息计算样本数量
  - `next_five_up_percent` (number)：后5日上涨概率
  - `next_five_avg_zf` (number)：后5日均涨幅
  - `next_five_cal_count` (number)：后5日信息计算样本数量
  - `score_history` (list)：评分历史数据

### 个股资金流 — `get_ch_stock_fund_flow`
分类：个股数据 ｜ 可测试：—

  - `primer_amount_ratio` (number)：主力净流入占比
  - `xl_order_net_amount` (number)：超大单净额(元)
  - `xl_order_amount_ratio` (number)：超大单净额占比
  - `big_order_net_amount` (number)：大单净额(元)
  - `big_order_amount_ratio` (number)：大单净额占比
  - `medium_order_net_amount` (number)：中单净额(元)
  - `medium_order_amount_ratio` (number)：中单净额占比
  - `small_order_net_amount` (number)：小单净额(元)
  - `small_order_amount_ratio` (number)：小单净额占比
  - `primer_net_amount` (number)：主力净流入(元)

### 人气排名数据 — `get_ch_stock_attention_tank`
分类：个股数据 ｜ 可测试：—

  - `market_rank` (number)：全市场人气排名
  - `classified_rank` (number)：行业内人气排名
  - `date` (string)：日期

### 股东人数历史 — `get_ch_stock_share_holder`
分类：个股数据 ｜ 可测试：—

  - `holder_count` (string)：股东人数(户)
  - `date` (string)：日期

### 大宗交易历史 — `get_ch_stock_block_trading`
分类：个股数据 ｜ 可测试：—

  - `price` (number)：成交价
  - `amount` (number)：成交金额(万元)
  - `date` (string)：日期

### 增减持历史 — `get_ch_stock_inc_or_dec`
分类：个股数据 ｜ 可测试：—

  - `price` (number)：成交均价，如未披露价格，该值为0
  - `count` (number)：增减持数量(股)，负数表示减持
  - `date` (string)：日期

### 等比前复权日线 — `get_ch_stock_front_ratio_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `close` (number)：收盘价

### 等比前复权周线 — `get_ch_stock_front_ratio_week_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (number)：日期
  - `trading_days` (string)：周内交易天数
  - `close` (number)：收盘价

### 等比前复权月线 — `get_ch_stock_front_ratio_month_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：月内交易天数
  - `close` (number)：收盘价

### 等比后复权日线 — `get_ch_stock_back_ratio_history`
分类：个股数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `close` (number)：收盘价

### 历史分钟数据 — `get_ch_stock_minute_history`
分类：个股数据 ｜ 可测试：✅

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `close` (number)：收盘价
  - `amount` (number)：成交额
  - `volume` (number)：成交量
  - `date_time` (string)：日期时间

### 个股分时图 — `get_ch_stock_time_line`
分类：个股数据 ｜ 可测试：—

  - `time` (string)：时间
  - `price` (number)：价格
  - `avg_price` (number)：均价
  - `volume` (number)：成交量。单位：股

### 个股昨日分时图 — `get_ch_stock_time_line_yes`
分类：个股数据 ｜ 可测试：—

  - `time` (string)：时间
  - `price` (number)：价格
  - `avg_price` (number)：成交均价
  - `volume` (number)：成交量。单位：股

### 个股五日分时 — `get_ch_stock_five_days_time_line`
分类：个股数据 ｜ 可测试：—

  - `time` (string)：时间
  - `price` (number)：价格
  - `avg_price` (number)：均价
  - `volume` (number)：成交量。单位：股

### 个股竞价分时数据 — `get_ch_stock_auction_time_line`
分类：个股数据 ｜ 可测试：—

  - `time` (string)：时间
  - `price` (number)：集合竞价撮合价
  - `mat` (number)：已匹配数量。单位：股
  - `unmat` (number)：未匹配数量。数值为正，有买单成交不了，买盘剩余。数值为负，有卖单成交不了，卖盘有剩余。单位：股

### 获取概念板块列表 — `get_ch_concept`
分类：板块数据 ｜ 可测试：✅

  - `name` (string)：板块名称
  - `stocks` (list)：成分股股票代码列表
  - `code` (string)：概念板块对应的代码

### 获取行业板块列表 — `get_ch_industry`
分类：板块数据 ｜ 可测试：✅

  - `name` (string)：板块名称
  - `stocks` (list)：成分股股票代码列表
  - `code` (string)：行业板块代码

### 订阅概念板块实时行情通道 — `subscribe_ch_concept_real`
分类：板块数据 ｜ 可测试：—

  - `code` (string)：板块代码
  - `name` (string)：板块名称
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `close` (number)：现价
  - `low` (number)：最低价
  - `volume` (number)：成交量（手）
  - `amount` (number)：成交额（万元）
  - `change` (number)：涨跌幅（%）
  - `date` (string)：日期
  - `time` (string)：时间
  - `up_count` (integer)：上涨数量
  - `down_count` (integer)：下跌数量
  - `limit_up_count` (integer)：涨停数量
  - `limit_down_count` (integer)：跌停数量

### 获取概念板块实时行情 — `get_ch_concept_real`
分类：板块数据 ｜ 可测试：✅

  - `code` (string)：板块代码
  - `name` (string)：板块名称
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `close` (number)：现价
  - `low` (number)：最低价
  - `volume` (number)：成交量（手）
  - `amount` (number)：成交额（万元）
  - `change` (number)：涨跌幅（%）
  - `date` (string)：日期
  - `time` (string)：时间
  - `up_count` (integer)：上涨数量
  - `down_count` (integer)：下跌数量
  - `limit_up_count` (integer)：涨停数量
  - `limit_down_count` (integer)：跌停数量

### 订阅行业板块实时行情通道 — `subscribe_ch_industry_real`
分类：板块数据 ｜ 可测试：—

  - `code` (string)：板块代码
  - `name` (string)：板块名称
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `close` (number)：现价
  - `low` (number)：最低价
  - `volume` (number)：成交量（手）
  - `amount` (number)：成交额（万元）
  - `change` (number)：涨跌幅（%）
  - `date` (string)：日期
  - `time` (string)：时间
  - `up_count` (integer)：上涨数量
  - `down_count` (integer)：下跌数量
  - `limit_up_count` (integer)：涨停数量
  - `limit_down_count` (integer)：跌停数量

### 获取行业板块实时行情 — `get_ch_industry_real`
分类：板块数据 ｜ 可测试：✅

  - `code` (string)：板块代码
  - `name` (string)：板块名称
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `close` (number)：现价
  - `low` (number)：最低价
  - `volume` (number)：成交量（手）
  - `amount` (number)：成交额（万元）
  - `change` (number)：涨跌幅（%）
  - `date` (string)：日期
  - `time` (string)：时间
  - `up_count` (integer)：上涨数量
  - `down_count` (integer)：下跌数量
  - `limit_up_count` (integer)：涨停数量
  - `limit_down_count` (integer)：跌停数量

### 概念板块日线 — `get_ch_concept_day_history`
分类：板块数据 ｜ 可测试：✅

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `close` (number)：收盘价

### 概念板块周线 — `get_ch_concept_week_history`
分类：板块数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：周内交易天数
  - `close` (number)：收盘价

### 概念板块月线 — `get_ch_concept_month_history`
分类：板块数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：周内交易天数
  - `close` (number)：收盘价

### 行业板块日线 — `get_ch_industry_day_history`
分类：板块数据 ｜ 可测试：✅

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `close` (number)：收盘价

### 行业板块周线 — `get_ch_industry_week_history`
分类：板块数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：周内交易天数
  - `close` (number)：收盘价

### 行业板块月线 — `get_ch_industry_month_history`
分类：板块数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `trading_days` (number)：周内交易天数
  - `close` (number)：收盘价

### 获取融资融券余额 — `get_rzrq_balance`
分类：市场数据 ｜ 可测试：—

  - `rz_balance` (number)：融资余额(万元)
  - `rq_balance` (number)：融券余额(万元)
  - `dae` (string)：日期

### 上交所每日统计信息 — `get_sh_market_daily_info`
分类：市场数据 ｜ 可测试：—

  - `a_stock` (dict)：上证A股
  - `b_stock` (dict)：上证B股
  - `kcb_stock` (dict)：科创板
  - `market` (dict)：上交所总体
  - `date` (string)：日期
  - `total_value` (number)：总市值(亿元)
  - `trade_vol` (number)：成交量(亿股)
  - `avg_pe` (number)：平均市盈率(倍)
  - `total_to_rate` (number)：换手率(%)
  - `nego_to_rate` (number)：流通换手率(%)
  - `trade_amt` (number)：成交金额(亿元)
  - `nego_value` (number)：流通市值(亿元)
  - `list_num` (number)：股票数

### 上交所每周统计信息 — `get_sh_market_week_info`
分类：市场数据 ｜ 可测试：—

  - `a_stock` (dict)：上证A股
  - `b_stock` (dict)：上证B股
  - `kcb_stock` (dict)：科创板
  - `market` (dict)：上交所总体
  - `begin_date` (string)：周起始日期
  - `end_date` (string)：周结束日期
  - `low_vol` (number)：最低成交量(亿股)
  - `low_vol_date` (string)：最低成交量日期
  - `low_amt` (number)：最低成交金额(亿元)
  - `low_amt_date` (number)：最低成交金额日期
  - `avg_pe_rate` (number)：平均市盈率(倍)
  - `trade_amt` (number)：成交金额(亿元)
  - `list_num` (number)：股票数量
  - `high_amt` (number)：最高成交金额(亿元)
  - `high_amt_date` (string)：最高成交金额日期
  - `high_vol` (number)：最高成交量(亿股)
  - `high_vol_date` (string)：最高成交量日期
  - `total_value` (number)：市价总值(亿元)
  - `trade_vol` (number)：成交量(亿股)
  - `total_to_rate` (number)：换手率(%)
  - `nego_value` (number)：流通市值(亿元)
  - `trade_days` (number)：交易天数
  - `to_rate` (number)：流通换手率(%)

### 上交所每月统计信息 — `get_sh_market_month_info`
分类：市场数据 ｜ 可测试：—

  - `a_stock` (dict)：上证A股
  - `b_stock` (dict)：上证B股
  - `kcb_stock` (dict)：科创板
  - `market` (dict)：上交所总体
  - `query_date` (string)：查询日期
  - `low_vol` (number)：最低成交量(亿股)
  - `low_vol_date` (string)：最低成交量日期
  - `low_amt` (number)：最低成交金额(亿元)
  - `low_amt_date` (string)：最低成交金额日期
  - `avg_pe_rate` (number)：平均市盈率(倍)
  - `trade_amt` (number)：成交金额(亿元)
  - `list_num` (number)：股票数量
  - `high_amt` (number)：最高成交金额(亿元)
  - `high_amt_date` (number)：最高成交金额日期
  - `high_vol` (number)：最高成交量(亿股)
  - `high_vol_date` (string)：最高成交量日期
  - `total_value` (number)：市价总值(亿元)
  - `trade_vol` (number)：成交量(亿股)
  - `total_to_rate` (number)：换手率(%)
  - `nego_value` (number)：流通市值(亿元)
  - `trade_days` (number)：交易天数
  - `to_rate` (number)：流通换手率(%)

### 订阅指数实时行情通道 — `subscribe_ch_market_real`
分类：市场数据 ｜ 可测试：—

  - `code` (string)：指数代码
  - `name` (string)：指数名称
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `close` (number)：现价
  - `low` (number)：最低价
  - `volume` (number)：成交量（手）
  - `amount` (number)：成交额（万元）
  - `change` (number)：涨跌幅（%）
  - `date` (string)：日期
  - `time` (string)：时间
  - `up_count` (number)：上涨数量
  - `down_count` (number)：下跌数量

### 获取指数实时行情 — `get_ch_market_real`
分类：市场数据 ｜ 可测试：✅

  - `code` (string)：指数代码
  - `name` (string)：指数名称
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `close` (number)：现价
  - `low` (number)：最低价
  - `volume` (number)：成交量（手）
  - `amount` (number)：成交额（万元）
  - `change` (number)：涨跌幅（%）
  - `date` (string)：日期
  - `time` (string)：时间
  - `up_count` (integer)：上涨数量
  - `down_count` (integer)：下跌数量

### 涨跌停数量历史 — `get_ch_limit_up_down`
分类：市场数据 ｜ 可测试：✅

  - `limit_up` (number)：涨停数量
  - `limit_down` (number)：跌停数量
  - `touch_limit_up` (number)：触及涨停数量
  - `touch_limit_down` (number)：触及跌停数量
  - `limit_up_percent` (number)：涨停封板率
  - `limit_down_percent` (number)：跌停封板率
  - `date` (string)：日期

### 指数日线 — `get_ch_market_day_history`
分类：市场数据 ｜ 可测试：✅

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (string)：日期
  - `close` (number)：收盘价

### 指数周线 — `get_ch_market_week_history`
分类：市场数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (number)：日期
  - `trading_days` (string)：周内交易天数
  - `close` (number)：收盘价

### 指数月线 — `get_ch_market_month_history`
分类：市场数据 ｜ 可测试：—

  - `open` (number)：开盘价
  - `high` (number)：最高价
  - `low` (number)：最低价
  - `last_close` (number)：昨收价
  - `volume` (number)：成交量(股)
  - `amount` (number)：成交额(万元)
  - `date` (number)：日期
  - `trading_days` (string)：周内交易天数
  - `close` (number)：收盘价

### 龙虎榜数据 — `get_lhb_data`
分类：市场数据 ｜ 可测试：✅

  - `name` (string)：个股名称
  - `code` (string)：个股代码
  - `lhb_net_amount` (number)：龙虎榜净买额(元)
  - `lhb_buy_amount` (number)：龙虎榜买入额(元)
  - `lhb_sell_amount` (number)：龙虎榜卖出额(元)
  - `lhb_deal_amount` (number)：龙虎榜成交额(元)
  - `amount` (number)：今日总成交额
  - `net_amount_ratio` (number)：净买额占成交额比例
  - `deal_amount_ratio` (number)：龙虎榜成交金额占总成交额比例
  - `reason` (string)：上榜原因
  - `buy_seat` (list)：买入席位信息
  - `sell_seat` (list)：卖出席位信息

### 市场资金流历史 — `get_ch_market_fund_flow`
分类：市场数据 ｜ 可测试：✅

  - `xl_order_net_amount` (number)：超大单净额(元)
  - `big_order_net_amount` (number)：大单净额(元)
  - `medium_order_net_amount` (number)：中单净额(元)
  - `small_order_net_amount` (number)：小单净额(元)
  - `primer_amount_ratio` (number)：主力净流入占比
  - `xl_order_amount_ratio` (number)：超大单净额占比
  - `big_order_amount_ratio` (number)：大单净额占比
  - `medium_order_amount_ratio` (number)：中单净额占比
  - `small_order_amount_ratio` (number)：小单净额占比
  - `primer_net_amount` (number)：主机净额

### 全市场买卖对比 — `get_ch_all_market_bear_compare`
分类：市场数据 ｜ 可测试：✅

  - `tradetime` (string)：时间
  - `bid` (number)：买一金额
  - `ask` (number)：卖一金额

### 上证买卖对比 — `get_ch_sh_market_bear_compare`
分类：市场数据 ｜ 可测试：—

  - `tradetime` (string)：时间
  - `bid` (number)：买一金额
  - `ask` (number)：卖一金额

### 深证买卖对比 — `get_ch_sz_market_bear_compare`
分类：市场数据 ｜ 可测试：—

  - `tradetime` (string)：时间
  - `bid` (number)：买一金额
  - `ask` (number)：卖一金额

### 创业板买卖对比 — `get_ch_cyb_market_bear_compare`
分类：市场数据 ｜ 可测试：—

  - `tradetime` (string)：时间
  - `bid` (number)：买一金额
  - `ask` (number)：卖一金额

### 科创板买卖对比 — `get_ch_kcb_market_bear_compare`
分类：市场数据 ｜ 可测试：—

  - `tradetime` (string)：时间
  - `bid` (number)：买一金额
  - `ask` (number)：卖一金额

### 北证买卖对比 — `get_ch_bj_market_bear_compare`
分类：市场数据 ｜ 可测试：—

  - `tradetime` (string)：时间
  - `bid` (number)：买一金额
  - `ask` (number)：卖一金额

### 市场实时涨跌分布时序数据 — `get_ch_market_zd_map`
分类：市场数据 ｜ 可测试：—

  - `time` (string)：时间
  - `up_over_10` (number)：涨幅>10%
  - `up_7_10` (number)：涨幅7%~10%
  - `up_5_7` (number)：涨幅5%~7%
  - `up_2_5` (number)：涨幅2%~5%
  - `up_0_2` (number)：涨幅0%~2%
  - `flat` (number)：平盘
  - `down_0_2` (number)：跌幅0%~2%
  - `down_2_5` (number)：跌幅2%~5%
  - `down_5_7` (number)：跌幅5%~7%
  - `down_7_10` (number)：跌幅7%~10%
  - `down_over_10` (number)：跌幅>10%

### 市场实时涨跌停数量 — `get_ch_today_limit_up_down`
分类：市场数据 ｜ 可测试：—

  - `date` (string)：日期 (YYYY-MM-DD)
  - `rise` (number)：涨停家数
  - `fall` (number)：跌停家数
  - `zhaban` (number)：炸板数
  - `nonword` (number)：非一字板涨停数
  - `tradetime` (string)：时间点

### 市场实时涨停股列表 — `get_ch_today_lb_stock`
分类：市场数据 ｜ 可测试：—

  - `update_time` (string)：时间
  - `yes_lb_ratio` (number)：昨日连板晋级率
  - `today_lb_ratio` (number)：今日连板晋级率
  - `stocks` (list)：涨停股列表

### 市场全天实时成交额 — `get_ch_market_amount_curve`
分类：市场数据 ｜ 可测试：—

  - `today` (string)：当日成交额数据
  - `yesterday` (string)：昨日全天成交额数据

### 利润表 — `get_ch_stock_income_statement`
分类：财务数据 ｜ 可测试：—

  - `net_profit_adjusted` (number)：扣除非经常性损益后的净利润
  - `tag_time` (number)：报告期
  - `net_profit_minority` (number)：少数股东损益
  - `basic_eps` (number)：基本每股收益
  - `me` (number)：综合收益总额
  - `adjusted_eps` (number)：扣除非经常性损益每股收益
  - `operating_revenue` (number)：营业收入
  - `comprehensive_income` (number)：归属于母公司综合收益
  - `operating_costs` (number)：营业成本
  - `announce_time` (number)：营业税金及附加
  - `sales_expenses` (number)：sales_expenses
  - `management_expenses` (number)：管理费用
  - `financial_expenses` (number)：财务费用
  - `rd_expenses` (number)：研发费用
  - `other_gains` (number)：其他收益
  - `investment_income` (number)：投资收益
  - `fair_value_gain_loss` (number)：公允价值变动损益
  - `asset_impairment_loss` (number)：资产减值损失
  - `credit_impairment_loss` (number)：信用减值损失
  - `asset_disposal_gain_loss` (number)：资产处置收益
  - `operating_profit` (number)：营业利润
  - `non_operating_income` (number)：营业外收入
  - `total_profit` (number)：利润总额
  - `income_tax_expense` (number)：所得税费用
  - `net_profit` (number)：净利润
  - `net_profit_attributable_parent` (number)：归属于母公司所有者的净利润
  - `other_comprehensive_income` (number)：其他综合收益
  - `total_comprehensive_income` (number)：综合收益总额
  - `comprehensive_income_parent` (number)：归属于母公司综合收益
  - `comprehensive_income_minority` (number)：归属于少数股东综合收益
  - `diluted_eps` (number)：稀释每股收益
  - `operating_revenue_ttm` (number)：营业总收入TTM
  - `operating_revenue_single_quarter` (number)：营业总收入(单季度)
  - `net_profit_single_quarter` (number)：净利润（单季度）
  - `operating_costs_single_quarter` (number)：营业成本（单季度）
  - `interest_income` (number)：利息收入
  - `premium_earned` (number)：已赚保费
  - `commission_income` (number)：手续费及佣金收入
  - `interest_expense` (number)：利息支出
  - `commission_expense` (number)：手续费及佣金支出
  - `surrender_value` (number)：退保金
  - `net_claims_expense` (number)：赔付支出净额
  - `net_insurance_contract_reserve` (number)：提取保险合同准备金净额
  - `policy_dividend_expense` (number)：保单红利支出
  - `reinsurance_expense` (number)：分保费用
  - `exchange_gain_loss` (number)：汇兑收益
  - `net_fair_value_hedge_gain` (number)：净敞口套期收益
  - `other_business_income` (number)：其他业务收入
  - `business_management_expenses` (number)：业务及管理费
  - `other_business_costs` (number)：其他业务成本

### 现金流表 — `get_ch_stock_cash_flow_statement`
分类：财务数据 ｜ 可测试：—

  - `announce_time` (string)：公告日期
  - `tag_time` (string)：报告期
  - `cash_from_sales` (number)：销售商品、提供劳务收到的现金
  - `tax_refunds_received` (number)：收到的税费返还
  - `other_operating_cash_in` (number)：收到其他与经营活动有关的现金
  - `total_operating_cash_in` (number)：经营活动现金流入小计
  - `cash_for_goods` (number)：购买商品、接受劳务支付的现金
  - `cash_to_employees` (number)：支付给职工以及为职工支付的现金
  - `tax_payments` (number)：支付的各项税费
  - `other_operating_cash_out` (number)：支付其他与经营活动有关的现金
  - `total_operating_cash_out` (number)：经营活动现金流出小计
  - `net_operating_cash_flow` (number)：经营活动产生的现金流量净额
  - `net_operating_cash_flow2` (number)：经营活动产生的现金流量净额2
  - `cash_from_investment_recovery` (number)：收回投资收到的现金
  - `cash_from_investment_income` (number)：取得投资收益收到的现金
  - `cash_from_asset_disposal` (number)：处置固定资产、无形资产和其他长期资产收回的现金净额
  - `cash_from_subsidiary_disposal` (number)：处置子公司及其他营业单位收到的现金净额
  - `other_investing_cash_in` (number)：收到其他与投资活动有关的现金
  - `total_investing_cash_in` (number)：投资活动现金流入小计
  - `cash_for_asset_purchase` (number)：购建固定资产、无形资产和其他长期资产支付的现金
  - `cash_for_investment` (number)：投资支付的现金
  - `cash_for_subsidiary_acquisition` (number)：取得子公司及其他营业单位支付的现金净额
  - `other_investing_cash_out` (number)：支付其他与投资活动有关的现金
  - `total_investing_cash_out` (number)：投资活动现金流出小计
  - `net_investing_cash_flow` (number)：投资活动产生的现金流量净额
  - `cash_from_capital_absorption` (number)：吸收投资收到的现金
  - `cash_from_borrowing` (number)：取得借款收到的现金
  - `other_financing_cash_in` (number)：收到其他与筹资活动有关的现金
  - `total_financing_cash_in` (number)：筹资活动现金流入小计
  - `cash_for_debt_repayment` (number)：偿还债务支付的现金
  - `cash_for_dividends` (number)：分配股利、利润或偿付利息支付的现金
  - `other_financing_cash_out` (number)：支付其他与筹资活动有关的现金
  - `total_financing_cash_out` (number)：筹资活动现金流出小计
  - `net_financing_cash_flow` (number)：筹资活动产生的现金流量净额
  - `exchange_rate_effect` (number)：汇率变动对现金的影响
  - `other_cash_effects` (number)：其他原因对现金的影响
  - `net_cash_increase` (number)：现金及现金等价物净增加额
  - `beginning_cash_balance` (number)：期初现金及现金等价物余额
  - `ending_cash_balance` (number)：期末现金及现金等价物余额
  - `asset_impairment_provision` (number)：资产减值准备
  - `depreciation_amortization` (number)：固定资产折旧、油气资产折耗、生产性生物资产折旧
  - `intangible_assets_amortization` (number)：无形资产摊销
  - `long_term_prepaid_expenses_amortization` (number)：长期待摊费用摊销
  - `loss_on_asset_disposal` (number)：处置固定资产、无形资产和其他长期资产的损失
  - `loss_on_fixed_assets_retirement` (number)：固定资产报废损失
  - `fair_value_change_loss` (number)：公允价值变动损失
  - `financial_expenses_cf` (number)：财务费用
  - `investment_loss` (number)：投资损失
  - `deferred_tax_assets_decrease` (number)：递延所得税资产减少
  - `deferred_tax_liabilities_increase` (number)：递延所得税负债增加
  - `inventory_decrease` (number)：存货的减少
  - `operating_receivables_decrease` (number)：经营性应收项目的减少
  - `operating_payables_increase` (number)：经营性应付项目的增加
  - `other_adjustments` (number)：其他
  - `net_increase_customer_deposits` (number)：客户存款和同业存放款项净增加额
  - `net_increase_central_bank_borrowing` (number)：向中央银行借款净增加额
  - `net_increase_other_financial_institutions` (number)：向其他金融机构拆入资金净增加额
  - `cash_from_insurance_premiums` (number)：收到原保险合同保费取得的现金
  - `net_cash_from_reinsurance` (number)：收到再保险业务现金净额
  - `net_increase_policy_holder_deposits` (number)：保户储金及投资款净增加额
  - `net_increase_trading_assets` (number)：处置以公允价值计量且其变动计入当期损益的金融资产净增加额
  - `cash_from_interest_commission` (number)：收取利息、手续费及佣金的现金
  - `net_increase_borrowed_funds` (number)：拆入资金净增加额
  - `net_increase_repurchase` (number)：回购业务资金净增加额
  - `net_increase_customer_loans` (number)：客户贷款及垫款净增加额
  - `net_increase_deposits_central_bank` (number)：存放中央银行和同业款项净增加额
  - `cash_for_insurance_claims` (number)：支付原保险合同赔付款项的现金
  - `cash_for_interest_commission` (number)：支付利息、手续费及佣金的现金
  - `cash_for_policy_dividends` (number)：支付保单红利的现金
  - `investment_property_depreciation` (number)：投资性房地产的折旧及摊销
  - `right_of_use_assets_depreciation` (number)：使用权资产折旧
  - `net_increase_interest_fees` (number)：收取利息和手续费净增加额(金融类)
  - `cash_for_fees` (number)：支付手续费的现金(金融类)
  - `cash_for_bond_issuance` (number)：发行债券支付的现金(金融类)

### 财务主表 — `get_ch_stock_financial_indicators`
分类：财务数据 ｜ 可测试：—

  - `announce_time` (string)：公告日期
  - `tag_time` (string)：报告期
  - `eps` (number)：基本每股收益
  - `adjusted_eps` (number)：扣除非经常性损益每股收益
  - `undistributed_profit_per_share` (number)：每股未分配利润
  - `net_assets_per_share` (number)：每股净资产
  - `capital_reserve_per_share` (number)：每股资本公积金
  - `operating_cash_flow_per_share` (number)：每股经营现金流量
  - `free_cash_flow_per_share` (number)：每股企业自由现金流
  - `shareholder_free_cash_flow_per_share` (number)：每股股东自由现金流
  - `roe` (number)：净资产收益率
  - `weighted_roe` (number)：加权净资产收益率
  - `roic` (number)：投入资本回报率(ROIC)
  - `return_on_investment` (number)：投资收益率
  - `net_profit_margin` (number)：销售净利率
  - `total_assets_profit_margin` (number)：总资产净利率
  - `profit_margin` (number)：净利润率
  - `gross_margin` (number)：销售毛利率
  - `cost_profit_margin` (number)：成本费用利润率
  - `operating_profit_margin` (number)：营业利润率
  - `tax_rate` (number)：营业税金率
  - `cost_rate` (number)：营业成本率
  - `three_expense_ratio` (number)：三费比重
  - `management_expense_ratio` (number)：管理费用率
  - `financial_expense_ratio` (number)：财务费用率
  - `ebit` (number)：息税前利润(EBIT)
  - `ebitda` (number)：息税折旧摊销前利润(EBITDA)
  - `ebitda_to_revenue` (number)：EBITDA/营业总收入
  - `accounts_receivable_turnover` (number)：应收帐款周转率
  - `inventory_turnover` (number)：存货周转率
  - `working_capital_turnover` (number)：运营资金周转率
  - `total_assets_turnover` (number)：总资产周转率
  - `fixed_assets_turnover` (number)：固定资产周转率
  - `accounts_receivable_turnover_days` (number)：应收帐款周转天数
  - `inventory_turnover_days` (number)：存货周转天数
  - `current_assets_turnover` (number)：流动资产周转率
  - `current_assets_turnover_days` (number)：流动资产周转天数
  - `total_assets_turnover_days` (number)：总资产周转天数
  - `equity_turnover` (number)：股东权益周转率
  - `current_ratio` (number)：流动比率
  - `quick_ratio` (number)：速动比率
  - `cash_ratio` (number)：现金比率
  - `interest_coverage_ratio` (number)：利息保障倍数
  - `non_current_liabilities_ratio` (number)：非流动负债比率
  - `current_liabilities_ratio` (number)：流动负债比率
  - `tangible_assets_debt_ratio` (number)：有形资产净值债务率
  - `equity_multiplier` (number)：权益乘数
  - `equity_to_liabilities` (number)：股东的权益/负债合计
  - `tangible_assets_to_liabilities` (number)：有形资产/负债合计
  - `operating_cash_flow_to_liabilities` (number)：经营活动产生的现金流量净额/负债合计
  - `ebitda_to_liabilities` (number)：EBITDA/负债合计
  - `asset_liability_ratio` (number)：资产负债率
  - `current_assets_ratio` (number)：流动资产比率
  - `cash_ratio_to_assets` (number)：货币资金比率
  - `inventory_ratio` (number)：存货比率
  - `fixed_assets_ratio` (number)：固定资产比率
  - `liability_structure_ratio` (number)：负债结构比
  - `parent_equity_to_invested_capital` (number)：归属于母公司股东权益/全部投入资本
  - `equity_to_interest_bearing_debt` (number)：股东的权益/带息债务
  - `tangible_assets_to_net_debt` (number)：有形资产/净债务
  - `interest_bearing_debt_ratio` (number)：有息负债率
  - `revenue_growth` (number)：营业收入增长率
  - `net_profit_growth` (number)：净利润增长率
  - `net_assets_growth` (number)：净资产增长率
  - `fixed_assets_growth` (number)：固定资产增长率
  - `total_assets_growth` (number)：总资产增长率
  - `investment_income_growth` (number)：投资收益增长率
  - `operating_profit_growth` (number)：营业利润增长率
  - `adjusted_eps_growth` (number)：扣非每股收益同比
  - `adjusted_net_profit_growth` (number)：扣非净利润同比
  - `operating_cash_flow_to_revenue` (number)：经营活动产生的现金流量净额/营业收入
  - `sales_cash_to_revenue` (number)：销售商品提供劳务收到的现金/营业收入
  - `revenue_cash_content` (number)：营业收入现金含量
  - `operating_cash_flow_to_profit` (number)：经营活动产生的现金流量净额/经营活动净收益
  - `capital_expenditure_to_depreciation` (number)：资本支出/折旧和摊销
  - `net_cash_flow_per_share` (number)：每股现金流量净额
  - `operating_cash_flow_to_short_term_debt` (number)：经营净现金比率（短期债务）
  - `operating_cash_flow_to_total_debt` (number)：经营净现金比率（全部债务）
  - `operating_cash_flow_to_net_profit` (number)：经营活动现金净流量与净利润比率
  - `total_assets_cash_recovery` (number)：全部资产现金回收率
  - `audit_opinion` (integer)：审计意见 0-未审计,1-无保留意见,2-带强调事项段的无保留意见,3-保留意见,4-无法表示意见,5-否定意见及其他
  - `dividend_payout_ratio` (number)：股利支付率
  - `financial_total_score` (number)：财务总评分

### 资产负债表 — `get_ch_stock_balance_sheet`
分类：财务数据 ｜ 可测试：—

  - `announce_time` (string)：公告日期
  - `tag_time` (string)：报告期
  - `cash` (number)：货币资金
  - `trading_financial_assets` (number)：交易性金融资产
  - `notes_receivable` (number)：应收票据
  - `accounts_receivable` (number)：应收账款
  - `prepayments` (number)：预付款项
  - `other_receivables` (number)：其他应收款
  - `intercompany_receivables` (number)：应收关联公司款
  - `interest_receivable` (number)：应收利息
  - `dividends_receivable` (number)：应收股利
  - `inventory` (number)：存货
  - `consumable_biological_assets` (number)：消耗性生物资产
  - `non_current_assets_due_within_one_year` (number)：一年内到期的非流动资产
  - `other_current_assets` (number)：其他流动资产
  - `total_current_assets` (number)：流动资产合计
  - `available_for_sale_financial_assets` (number)：可供出售金融资产
  - `held_to_maturity_investments` (number)：持有至到期投资
  - `long_term_receivables` (number)：长期应收款
  - `long_term_equity_investment` (number)：长期股权投资
  - `investment_property` (number)：投资性房地产
  - `fixed_assets` (number)：固定资产
  - `construction_in_progress` (number)：在建工程
  - `construction_materials` (number)：工程物资
  - `fixed_assets_for_disposal` (number)：固定资产清理
  - `productive_biological_assets` (number)：生产性生物资产
  - `oil_gas_assets` (number)：油气资产
  - `intangible_assets` (number)：无形资产
  - `development_expenditure` (number)：开发支出
  - `goodwill` (number)：商誉
  - `long_term_prepaid_expenses` (number)：长期待摊费用
  - `deferred_tax_assets` (number)：递延所得税资产
  - `other_non_current_assets` (number)：其他非流动资产
  - `total_non_current_assets` (number)：非流动资产合计
  - `total_assets` (number)：资产总计
  - `short_term_loans` (number)：短期借款
  - `trading_financial_liabilities` (number)：交易性金融负债
  - `notes_payable` (number)：应付票据
  - `accounts_payable` (number)：应付账款
  - `advance_receipts` (number)：预收款项
  - `employee_compensation_payable` (number)：应付职工薪酬
  - `taxes_payable` (number)：应交税费
  - `interest_payable` (number)：应付利息
  - `dividends_payable` (number)：应付股利
  - `other_payables` (number)：其他应付款
  - `intercompany_payables` (number)：应付关联公司款
  - `non_current_liabilities_due_within_one_year` (number)：一年内到期的非流动负债
  - `other_current_liabilities` (number)：其他流动负债
  - `total_current_liabilities` (number)：流动负债合计
  - `long_term_loans` (number)：长期借款
  - `bonds_payable` (number)：应付债券
  - `long_term_payables` (number)：长期应付款
  - `special_payables` (number)：专项应付款
  - `provisions` (number)：预计负债(非流动负债)
  - `deferred_tax_liabilities` (number)：递延所得税负债
  - `other_non_current_liabilities` (number)：其他非流动负债
  - `total_non_current_liabilities` (number)：非流动负债合计
  - `total_liabilities` (number)：负债合计
  - `share_capital` (number)：实收资本（或股本）
  - `capital_reserve` (number)：资本公积
  - `surplus_reserve` (number)：盈余公积
  - `treasury_shares` (number)：减：库存股
  - `undistributed_profit` (number)：未分配利润
  - `minority_interest` (number)：少数股东权益
  - `foreign_currency_translation_difference` (number)：外币报表折算价差
  - `abnormal_operation_adjustment` (number)：非正常经营项目收益调整
  - `total_owners_equity` (number)：所有者权益（或股东权益）合计
  - `total_liabilities_and_equity` (number)：负债和所有者（或股东权益）合计
  - `notes_and_accounts_payable` (number)：应付票据及应付账款
  - `notes_and_accounts_receivable` (number)：应收票据及应收账款
  - `deferred_income_non_current` (number)：递延收益(资产负债表-非流动负债)
  - `other_comprehensive_income_bs` (number)：其他综合收益(资产负债表)
  - `other_equity_instruments` (number)：其他权益工具(资产负债表)
  - `special_reserve` (number)：专项储备
  - `right_of_use_assets` (number)：使用权资产
  - `lease_liabilities` (number)：租赁负债
  - `contract_liabilities` (number)：合同负债
  - `contract_assets` (number)：合同资产
  - `other_assets` (number)：其他资产
  - `financing_receivables` (number)：应收款项融资

### 财务辅助表 — `get_ch_stock_auxiliary_data`
分类：财务数据 ｜ 可测试：—

  - `announce_time` (string)：公告日期
  - `tag_time` (string)：报告期
  - `net_profit_last_year` (number)：近一年净利润(元)
  - `revenue_last_year` (number)：最近一年营业收入(万元)
  - `net_profit_parent_last_year` (number)：近一年归母净利润(万元)
  - `adjusted_net_profit_last_year` (number)：近一年扣非净利润(万元)
  - `operating_profit_last_year` (number)：近一年营业利润(万元)
  - `operating_cash_flow_last_year` (number)：近一年经营活动现金流净额
  - `investing_cash_flow_last_year` (number)：近一年投资活动现金流净额(万元)
  - `net_cash_flow_last_year` (number)：近一年现金净流量(万元)
  - `revenue_ttm` (number)：营业总收入TTM(万元)
  - `operating_costs_non_financial_last_year` (number)：近一年营业成本-非金融类(万元)
  - `operating_costs_financial_last_year` (number)：近一年营业成本-金融类(万元)
  - `eps_single_quarter` (number)：基本每股收益（单季度）
  - `adjusted_eps_single_quarter` (number)：扣非每股收益(单季度)
  - `revenue_single_quarter` (number)：营业总收入(单季度)(万元)
  - `net_profit_single_quarter` (number)：净利润（单季度）(万元)
  - `operating_costs_single_quarter` (number)：营业成本（单季度）(万元)
  - `domestic_sales_revenue` (number)：主营业务收入(内销)(万元)
  - `export_sales_revenue` (number)：主营业务收入(外销)(万元)
  - `preferred_shares_liabilities` (number)：其中:优先股(非流动负债科目)
  - `perpetual_bonds_liabilities` (number)：永续债(非流动负债科目)
  - `long_term_employee_payables` (number)：长期应付职工薪酬
  - `preferred_shares_equity` (number)：其中:优先股(所有者权益科目)
  - `perpetual_bonds_equity` (number)：永续债(所有者权益科目)
  - `interest_expense_detail` (number)：其中:利息费用
  - `interest_income_detail` (number)：其中:利息收入
  - `general_risk_reserve` (number)：一般风险准备(金融类)
  - `other_causes_cash_effect` (number)：加:其他原因对现金的影响2(万元)
  - `debt_to_equity` (number)：债务转为资本
  - `convertible_bonds_due` (number)：一年内到期的可转换公司债券
  - `finance_lease_assets` (number)：融资租入固定资产
  - `continuing_operations_profit` (number)：持续经营净利润
  - `discontinued_operations_profit` (number)：终止经营净利润

### 股东表 — `get_ch_stock_share_capital_and_shareholders`
分类：财务数据 ｜ 可测试：—

  - `announce_time` (string)：公告日期
  - `tag_time` (string)：报告期
  - `total_shares` (number)：总股本
  - `circulating_a_shares` (number)：已上市流通A股
  - `circulating_b_shares` (number)：已上市流通B股
  - `circulating_h_shares` (number)：已上市流通H股
  - `free_float_shares` (number)：自由流通股
  - `restricted_a_shares` (number)：受限流通A股
  - `shareholder_count` (integer)：股东人数(户)
  - `largest_shareholder_holding` (number)：第一大股东的持股数量
  - `top_10_circulating_shareholders` (number)：十大流通股东持股数量合计
  - `top_10_shareholders` (number)：十大股东持股数量合计
  - `largest_circulating_shareholder` (number)：第一大流通股东持股量
  - `top_10_circulating_a_shares` (number)：十大流通股东持有的流通A股合计
  - `total_institutions` (integer)：机构总量（家）
  - `total_institution_holdings` (number)：机构持股总量(股)
  - `qfii_institutions` (integer)：QFII机构数
  - `qfii_holdings` (number)：QFII持股量
  - `broker_institutions` (integer)：券商机构数
  - `broker_holdings` (number)：券商持股量
  - `insurance_institutions` (integer)：保险机构数
  - `insurance_holdings` (number)：保险持股量
  - `fund_institutions` (integer)：基金机构数
  - `fund_holdings` (number)：基金持股量
  - `social_security_institutions` (integer)：社保机构数
  - `social_security_holdings` (number)：社保持股量
  - `private_equity_institutions` (integer)：私募机构数
  - `private_equity_holdings` (number)：私募持股量
  - `finance_company_institutions` (integer)：财务公司机构数
  - `finance_company_holdings` (number)：财务公司持股量
  - `annuity_institutions` (integer)：年金机构数
  - `annuity_holdings` (number)：年金持股量
  - `bank_institutions` (integer)：银行机构数
  - `bank_holdings` (number)：银行持股量
  - `general_corporate_institutions` (integer)：一般法人机构数
  - `general_corporate_holdings` (number)：一般法人持股量
  - `trust_institutions` (integer)：信托机构数
  - `trust_holdings` (number)：信托持股量
  - `special_corporate_institutions` (integer)：特殊法人机构数
  - `special_corporate_holdings` (number)：特殊法人持股量
  - `asset_management_institutions` (integer)：资管计划机构数
  - `asset_management_holdings` (number)：资管计划持股量
  - `northbound_institutions` (integer)：北上资金数（家）
  - `northbound_holdings` (number)：北上资金持股量
  - `national_team_holdings` (number)：国家队持股数量（万股）
  - `employee_count` (integer)：员工总数(人)

### 业绩预告 — `get_ch_stock_net_profit`
分类：财务数据 ｜ 可测试：—

  - `name` (string)：股票名称
  - `tag_date` (string)：公告日期
  - `report_type` (string)：预告类型
  - `report_name` (string)：预告名称
  - `report_msg` (string)：预告摘要
  - `net_profit` (number)：净利润预告值(万元)
  - `net_profit_inc_per` (number)：净利润增长率
  - `pre_net_profit` (number)：上年同期净利润(万元)
  - `code` (string)：个股代码

### 财务核心指标(数据源SI) — `get_ch_si_stock_fin_key_indicators`
分类：财务数据 ｜ 可测试：—

  - `report_period` (string)：报告期, YYYY-MM-DD
  - `report_name` (string)：报告名称
  - `announcement_date` (string)：公告日期, YYYY-MM-DD
  - `currency` (string)：货币
  - `report_type` (string)：报表类型
  - `data_source` (string)：数据来源
  - `is_audit` (string)：是否审计
  - `accpayrt` (number)：应付账款周转率
  - `accpaytdays` (number)：应付账款周转天数
  - `accrecgturndays` (number)：应收账款周转天数
  - `accrecgturnrt` (number)：应收账款周转率
  - `assliabrt` (number)：资产负债率
  - `biztotcost` (number)：营业成本
  - `biztotinco` (number)：营业总收入
  - `cashrt` (number)：现金比率
  - `consvatquickrt` (number)：保守速动比率
  - `crps` (number)：每股资本公积金
  - `curassturndays` (number)：流动资产周转天数
  - `curassturnrt` (number)：流动资产周转率
  - `currentrt` (number)：流动比率
  - `ebitmargin` (number)：息税前利润率
  - `ebitps` (number)：每股息税前利润
  - `em` (number)：权益乘数
  - `emconms` (number)：权益乘数(含少数股权的净资产)
  - `epsbasic` (number)：基本每股收益
  - `epsdilutednewp` (number)：摊薄每股收益_最新股数
  - `epsfulldiluted` (number)：稀释每股收益
  - `equrt` (number)：产权比率
  - `fcfeps` (number)：每股股东自由现金流量
  - `fcffps` (number)：每股企业自由现金流量
  - `goodwill` (number)：商誉
  - `incotaxtotp` (number)：所得税/利润总额
  - `invturndays` (number)：存货周转天数
  - `invturnrt` (number)：存货周转率
  - `mananetr` (number)：经营现金流量净额
  - `naps` (number)：每股净资产
  - `napsadj` (number)：调整每股净资产_期末股数
  - `napsnewp` (number)：每股净资产_最新股数
  - `ncfps` (number)：每股现金流量净额
  - `netprofit` (number)：净利润
  - `npconmstoavgta` (number)：总资产净利率_平均(含少数股东损益)
  - `npcut` (number)：扣非净利润
  - `npgrt` (number)：归属母公司净利润增长率
  - `nptoavgta` (number)：总资产净利率_平均
  - `opncfps` (number)：每股现金流
  - `opncftonp` (number)：经营活动净现金/归属母公司的净利润
  - `opncftoopti` (number)：经营性现金净流量/营业总收入
  - `opncftosi` (number)：经营活动净现金/销售收入
  - `opprort` (number)：营业利润率
  - `oprevps` (number)：每股营业收入
  - `parenetp` (number)：归母净利润
  - `prototcrt` (number)：成本费用利润率
  - `quickrt` (number)：速动比率
  - `reps` (number)：每股留存收益
  - `righaggr` (number)：股东权益合计(净资产)
  - `roa` (number)：总资产报酬率(ROA)
  - `roanopatconms` (number)：息前税后总资产报酬率_平均
  - `roeavg` (number)：净资产收益率_平均
  - `roeavgcut` (number)：净资产收益率_平均_扣除非经常损益
  - `roediluted` (number)：摊薄净资产收益率
  - `roedilutedcut` (number)：摊薄净资产收益率_扣除非经常损益
  - `roeweighted` (number)：净资产收益率(ROE)
  - `roic` (number)：投入资本回报率
  - `rota` (number)：总资本回报率
  - `scostrt` (number)：销售成本率
  - `sgpmargin` (number)：毛利率
  - `snpmarginconms` (number)：销售净利率
  - `srps` (number)：每股盈余公积金
  - `tagrt` (number)：营业总收入增长率
  - `taturndays` (number)：总资产周转天数
  - `taturnrt` (number)：总资产周转率
  - `tcexprt` (number)：成本费用率
  - `toprevps` (number)：每股营业总收入
  - `triexprt` (number)：期间费用率
  - `upps` (number)：每股未分配利润
  - `accpayrt_tongbi` (number)：accpayrt 同比
  - `accpaytdays_tongbi` (number)：accpaytdays 同比
  - `accrecgturndays_tongbi` (number)：accrecgturndays 同比
  - `accrecgturnrt_tongbi` (number)：accrecgturnrt 同比
  - `assliabrt_tongbi` (number)：assliabrt 同比
  - `biztotcost_tongbi` (number)：biztotcost 同比
  - `biztotinco_tongbi` (number)：biztotinco 同比
  - `cashrt_tongbi` (number)：cashrt 同比
  - `consvatquickrt_tongbi` (number)：consvatquickrt 同比
  - `crps_tongbi` (number)：crps 同比
  - `curassturndays_tongbi` (number)：curassturndays 同比
  - `curassturnrt_tongbi` (number)：curassturnrt 同比
  - `currentrt_tongbi` (number)：currentrt 同比
  - `ebitmargin_tongbi` (number)：ebitmargin 同比
  - `ebitps_tongbi` (number)：ebitps 同比
  - `em_tongbi` (number)：em 同比
  - `emconms_tongbi` (number)：emconms 同比
  - `epsbasic_tongbi` (number)：epsbasic 同比
  - `epsdilutednewp_tongbi` (number)：epsdilutednewp 同比
  - `epsfulldiluted_tongbi` (number)：epsfulldiluted 同比
  - `equrt_tongbi` (number)：equrt 同比
  - `fcfeps_tongbi` (number)：fcfeps 同比
  - `fcffps_tongbi` (number)：fcffps 同比
  - `goodwill_tongbi` (number)：goodwill 同比
  - `incotaxtotp_tongbi` (number)：incotaxtotp 同比
  - `invturndays_tongbi` (number)：invturndays 同比
  - `invturnrt_tongbi` (number)：invturnrt 同比
  - `mananetr_tongbi` (number)：mananetr 同比
  - `naps_tongbi` (number)：naps 同比
  - `napsadj_tongbi` (number)：napsadj 同比
  - `napsnewp_tongbi` (number)：napsnewp 同比
  - `ncfps_tongbi` (number)：ncfps 同比
  - `netprofit_tongbi` (number)：netprofit 同比
  - `npconmstoavgta_tongbi` (number)：npconmstoavgta 同比
  - `npcut_tongbi` (number)：npcut 同比
  - `npgrt_tongbi` (number)：npgrt 同比
  - `nptoavgta_tongbi` (number)：nptoavgta 同比
  - `opncfps_tongbi` (number)：opncfps 同比
  - `opncftonp_tongbi` (number)：opncftonp 同比
  - `opncftoopti_tongbi` (number)：opncftoopti 同比
  - `opncftosi_tongbi` (number)：opncftosi 同比
  - `opprort_tongbi` (number)：opprort 同比
  - `oprevps_tongbi` (number)：oprevps 同比
  - `parenetp_tongbi` (number)：parenetp 同比
  - `prototcrt_tongbi` (number)：prototcrt 同比
  - `quickrt_tongbi` (number)：quickrt 同比
  - `reps_tongbi` (number)：reps 同比
  - `righaggr_tongbi` (number)：righaggr 同比
  - `roa_tongbi` (number)：roa 同比
  - `roanopatconms_tongbi` (number)：roanopatconms 同比
  - `roeavg_tongbi` (number)：roeavg 同比
  - `roeavgcut_tongbi` (number)：roeavgcut 同比
  - `roediluted_tongbi` (number)：roediluted 同比
  - `roedilutedcut_tongbi` (number)：roedilutedcut 同比
  - `roeweighted_tongbi` (number)：roeweighted 同比
  - `roic_tongbi` (number)：roic 同比
  - `rota_tongbi` (number)：rota 同比
  - `scostrt_tongbi` (number)：scostrt 同比
  - `sgpmargin_tongbi` (number)：sgpmargin 同比
  - `snpmarginconms_tongbi` (number)：snpmarginconms 同比
  - `srps_tongbi` (number)：srps 同比
  - `tagrt_tongbi` (number)：tagrt 同比
  - `taturndays_tongbi` (number)：taturndays 同比
  - `taturnrt_tongbi` (number)：taturnrt 同比
  - `tcexprt_tongbi` (number)：tcexprt 同比
  - `toprevps_tongbi` (number)：toprevps 同比
  - `triexprt_tongbi` (number)：triexprt 同比
  - `upps_tongbi` (number)：upps 同比

### 利润表(数据源SI) — `get_ch_si_stock_fin_income_statements`
分类：财务数据 ｜ 可测试：—

  - `report_period` (string)：报告期, YYYY-MM-DD
  - `report_name` (string)：报告名称
  - `announcement_date` (string)：公告日期, YYYY-MM-DD
  - `currency` (string)：货币
  - `report_type` (string)：报表类型
  - `data_source` (string)：数据来源
  - `is_audit` (string)：是否审计
  - `amortizcostassetssapi` (number)：以摊余成本计量的金融资产终止确认产生的收益
  - `asseimpalossprofit` (number)：资产减值损失
  - `assetsdislinco` (number)：资产处置收益
  - `assoinveprof` (number)：对联营企业和合营企业的投资收益
  - `basiceps` (number)：基本每股收益
  - `bizcost` (number)：营业成本
  - `bizinco` (number)：营业收入
  - `biztax` (number)：营业税金及附加
  - `biztotcost` (number)：营业总成本
  - `biztotinco` (number)：营业总收入
  - `cinaforsfv` (number)：可供出售金融资产公允价值变动损益
  - `cinalibofrbp` (number)：重新计量设定受益计划变动额
  - `compcreditfaval` (number)：企业自身信用风险公允价值变动
  - `compincoamt` (number)：综合收益总额
  - `compnetexpe` (number)：赔付支出净额
  - `conopernprofit` (number)：持续经营净利润
  - `contress` (number)：提取保险合同准备金净额
  - `cpltohinco` (number)：（二）以后将重分类进损益的其他综合收益
  - `creditimplosseprofit` (number)：信用减值损失
  - `custinco` (number)：托管收益
  - `deveexpe` (number)：研发费用
  - `dilutedeps` (number)：稀释每股收益
  - `earnprem` (number)：已赚保费
  - `epocfhgl` (number)：现金流量套期损益的有效部分
  - `equmcpothinco` (number)：权益法下不能转损益的其他综合收益
  - `euqmicolothinco` (number)：权益法下可转损益的其他综合收益
  - `exchggain` (number)：汇兑收益
  - `finassintoothinco` (number)：金融资产重分类计入其他综合收益的金额
  - `finexpe` (number)：财务费用
  - `futuloss` (number)：期货损益
  - `hedcashflow` (number)：现金流量套期储备
  - `htmccinaforsfv` (number)：持有至到期投资重分类为可供出售金融资产损益
  - `incotaxexpe` (number)：所得税费用
  - `inteexpe` (number)：利息支出
  - `inteinco` (number)：利息收入
  - `inteincoopcost` (number)：利息收入
  - `interestexpense` (number)：利息费用
  - `inveinco` (number)：投资收益
  - `manaexpe` (number)：管理费用
  - `mergeformnetprof` (number)：被合并方在合并前实现净利润
  - `minysharinco` (number)：归属于少数股东的其他综合收益
  - `minysharincoamt` (number)：归属于少数股东的综合收益总额
  - `minysharrigh` (number)：少数股东损益
  - `ncpothinco` (number)：（一）以后不能重分类进损益的其他综合收益
  - `netexpohedinc` (number)：净敞口套期收益
  - `netprofit` (number)：净利润
  - `noncassetsdisi` (number)：非流动资产处置利得
  - `noncassetsdisl` (number)：非流动资产处置损失
  - `nonoexpe` (number)：营业外支出
  - `nonoreve` (number)：营业外收入
  - `othdebtinvcredimpr` (number)：其他债权投资信用减值准备
  - `othdebtinvfaval` (number)：其他债权投资公允价值变动
  - `othequinfaval` (number)：其他权益工具投资公允价值变动
  - `otherbizcost` (number)：其他业务成本
  - `otherbizinco` (number)：其他业务收入
  - `otherbizprof` (number)：其他业务利润
  - `othercompinco` (number)：其他综合收益
  - `othercpltohinco` (number)：其他
  - `otherinco` (number)：其他收益
  - `parecompinco` (number)：归属于母公司所有者的其他综合收益
  - `parecompincoamt` (number)：归属于母公司所有者的综合收益总额
  - `parenetp` (number)：归属于母公司所有者的净利润
  - `perprofit` (number)：营业利润
  - `polidiviexpe` (number)：保单红利支出
  - `pounexpe` (number)：手续费及佣金支出
  - `pouninco` (number)：手续费及佣金收入
  - `realsale` (number)：房地产销售收入
  - `realsalecost` (number)：房地产销售成本
  - `reinexpe` (number)：分保费用
  - `salesexpe` (number)：销售费用
  - `subsidyincome` (number)：补贴收入
  - `surrgold` (number)：退保金
  - `tdiffforcur` (number)：外币财务报表折算差额
  - `teropernprofit` (number)：终止经营净利润
  - `totprofit` (number)：利润总额
  - `unreinveloss` (number)：未确认投资损失
  - `valuechgloss` (number)：公允价值变动收益
  - `amortizcostassetssapi_tongbi` (number)：amortizcostassetssapi 同比
  - `asseimpalossprofit_tongbi` (number)：asseimpalossprofit 同比
  - `assetsdislinco_tongbi` (number)：assetsdislinco 同比
  - `assoinveprof_tongbi` (number)：assoinveprof 同比
  - `basiceps_tongbi` (number)：basiceps 同比
  - `bizcost_tongbi` (number)：bizcost 同比
  - `bizinco_tongbi` (number)：bizinco 同比
  - `biztax_tongbi` (number)：biztax 同比
  - `biztotcost_tongbi` (number)：biztotcost 同比
  - `biztotinco_tongbi` (number)：biztotinco 同比
  - `cinaforsfv_tongbi` (number)：cinaforsfv 同比
  - `cinalibofrbp_tongbi` (number)：cinalibofrbp 同比
  - `compcreditfaval_tongbi` (number)：compcreditfaval 同比
  - `compincoamt_tongbi` (number)：compincoamt 同比
  - `compnetexpe_tongbi` (number)：compnetexpe 同比
  - `conopernprofit_tongbi` (number)：conopernprofit 同比
  - `contress_tongbi` (number)：contress 同比
  - `cpltohinco_tongbi` (number)：cpltohinco 同比
  - `creditimplosseprofit_tongbi` (number)：creditimplosseprofit 同比
  - `custinco_tongbi` (number)：custinco 同比
  - `deveexpe_tongbi` (number)：deveexpe 同比
  - `dilutedeps_tongbi` (number)：dilutedeps 同比
  - `earnprem_tongbi` (number)：earnprem 同比
  - `epocfhgl_tongbi` (number)：epocfhgl 同比
  - `equmcpothinco_tongbi` (number)：equmcpothinco 同比
  - `euqmicolothinco_tongbi` (number)：euqmicolothinco 同比
  - `exchggain_tongbi` (number)：exchggain 同比
  - `finassintoothinco_tongbi` (number)：finassintoothinco 同比
  - `finexpe_tongbi` (number)：finexpe 同比
  - `futuloss_tongbi` (number)：futuloss 同比
  - `hedcashflow_tongbi` (number)：hedcashflow 同比
  - `htmccinaforsfv_tongbi` (number)：htmccinaforsfv 同比
  - `incotaxexpe_tongbi` (number)：incotaxexpe 同比
  - `inteexpe_tongbi` (number)：inteexpe 同比
  - `inteinco_tongbi` (number)：inteinco 同比
  - `inteincoopcost_tongbi` (number)：inteincoopcost 同比
  - `interestexpense_tongbi` (number)：interestexpense 同比
  - `inveinco_tongbi` (number)：inveinco 同比
  - `manaexpe_tongbi` (number)：manaexpe 同比
  - `mergeformnetprof_tongbi` (number)：mergeformnetprof 同比
  - `minysharinco_tongbi` (number)：minysharinco 同比
  - `minysharincoamt_tongbi` (number)：minysharincoamt 同比
  - `minysharrigh_tongbi` (number)：minysharrigh 同比
  - `ncpothinco_tongbi` (number)：ncpothinco 同比
  - `netexpohedinc_tongbi` (number)：netexpohedinc 同比
  - `netprofit_tongbi` (number)：netprofit 同比
  - `noncassetsdisi_tongbi` (number)：noncassetsdisi 同比
  - `noncassetsdisl_tongbi` (number)：noncassetsdisl 同比
  - `nonoexpe_tongbi` (number)：nonoexpe 同比
  - `nonoreve_tongbi` (number)：nonoreve 同比
  - `othdebtinvcredimpr_tongbi` (number)：othdebtinvcredimpr 同比
  - `othdebtinvfaval_tongbi` (number)：othdebtinvfaval 同比
  - `othequinfaval_tongbi` (number)：othequinfaval 同比
  - `otherbizcost_tongbi` (number)：otherbizcost 同比
  - `otherbizinco_tongbi` (number)：otherbizinco 同比
  - `otherbizprof_tongbi` (number)：otherbizprof 同比
  - `othercompinco_tongbi` (number)：othercompinco 同比
  - `othercpltohinco_tongbi` (number)：othercpltohinco 同比
  - `otherinco_tongbi` (number)：otherinco 同比
  - `parecompinco_tongbi` (number)：parecompinco 同比
  - `parecompincoamt_tongbi` (number)：parecompincoamt 同比
  - `parenetp_tongbi` (number)：parenetp 同比
  - `perprofit_tongbi` (number)：perprofit 同比
  - `polidiviexpe_tongbi` (number)：polidiviexpe 同比
  - `pounexpe_tongbi` (number)：pounexpe 同比
  - `pouninco_tongbi` (number)：pouninco 同比
  - `realsale_tongbi` (number)：realsale 同比
  - `realsalecost_tongbi` (number)：realsalecost 同比
  - `reinexpe_tongbi` (number)：reinexpe 同比
  - `salesexpe_tongbi` (number)：salesexpe 同比
  - `subsidyincome_tongbi` (number)：subsidyincome 同比
  - `surrgold_tongbi` (number)：surrgold 同比
  - `tdiffforcur_tongbi` (number)：tdiffforcur 同比
  - `teropernprofit_tongbi` (number)：teropernprofit 同比
  - `totprofit_tongbi` (number)：totprofit 同比
  - `unreinveloss_tongbi` (number)：unreinveloss 同比
  - `valuechgloss_tongbi` (number)：valuechgloss 同比

### 资产负债表(数据源SI) — `get_ch_si_stock_fin_balance_sheet`
分类：财务数据 ｜ 可测试：—

  - `report_period` (string)：报告期, YYYY-MM-DD
  - `report_name` (string)：报告名称
  - `announcement_date` (string)：公告日期, YYYY-MM-DD
  - `currency` (string)：货币
  - `report_type` (string)：报表类型
  - `data_source` (string)：数据来源
  - `is_audit` (string)：是否审计
  - `accheldfors` (number)：划分为持有待售的资产
  - `accopaya` (number)：应付账款
  - `accorece` (number)：应收账款
  - `accrexpe` (number)：预提费用
  - `accudepr` (number)：累计折旧
  - `actitradsecu` (number)：代理买卖证券款
  - `actiundesecu` (number)：代理承销证券款
  - `advapaym` (number)：预收款项
  - `amortizcostassets` (number)：以摊余成本计量的金融资产
  - `avaisellasse` (number)：可供出售金融资产
  - `bdspaya` (number)：应付债券
  - `bdspayaperbond` (number)：应付债券：永续债
  - `bdspayaprest` (number)：应付债券：优先股
  - `capisurp` (number)：资本公积
  - `cenbankborr` (number)：向中央银行借款
  - `comasse` (number)：公益性生物资产
  - `consprog` (number)：在建工程
  - `consprogtot` (number)：在建工程合计
  - `contractasset` (number)：合同资产
  - `contractliab` (number)：合同负债
  - `copepoun` (number)：应付手续费及佣金
  - `copewithreinrece` (number)：应付分保账款
  - `copeworkersal` (number)：应付职工薪酬
  - `curfds` (number)：货币资金
  - `curtrandiff` (number)：外币报表折算差额
  - `defeincotaxliab` (number)：递延所得税负债
  - `defereve` (number)：一年内的递延收益
  - `defetaxasset` (number)：递延所得税资产
  - `deposit` (number)：吸收存款及同业存放
  - `derifinaasset` (number)：衍生金融资产
  - `deriliab` (number)：衍生金融负债
  - `deveexpe` (number)：开发支出
  - `dividrece` (number)：应收股利
  - `divipaya` (number)：应付股利
  - `dometicksett` (number)：国内票证结算
  - `duenoncliab` (number)：一年内到期的非流动负债
  - `engimate` (number)：工程物资
  - `equiinve` (number)：长期股权投资
  - `expecurrliab` (number)：预计流动负债
  - `expenoncliab` (number)：预计非流动负债
  - `expinoncurrasset` (number)：一年内到期的非流动资产
  - `expotaxrebarece` (number)：应收出口退税
  - `fairvalueassets` (number)：以公允价值计量且其变动计入其他综合收益的金融资产
  - `fdsborr` (number)：拆入资金
  - `fixedasseclea` (number)：固定资产清理
  - `fixedassecleatot` (number)：固定资产及清理合计
  - `fixedasseimmo` (number)：固定资产原值
  - `fixedasseimpa` (number)：固定资产减值准备
  - `fixedassenet` (number)：固定资产净额
  - `fixedassenetw` (number)：固定资产净值
  - `generiskrese` (number)：一般风险准备
  - `goodwill` (number)：商誉
  - `holdinvedue` (number)：债权投资
  - `hydrasset` (number)：油气资产
  - `insucontrese` (number)：保险合同准备金
  - `intaasset` (number)：无形资产
  - `intelpay` (number)：内部应付款
  - `intelrece` (number)：内部应收款
  - `intepaya` (number)：应付利息
  - `interece` (number)：应收利息
  - `inteticksett` (number)：国际票证结算
  - `inve` (number)：存货
  - `inveprop` (number)：投资性房地产
  - `lcopeworkersal` (number)：长期应付职工薪酬
  - `leaseliab` (number)：租赁负债
  - `lendandloan` (number)：发放贷款及垫款
  - `liabheldfors` (number)：划分为持有待售的负债
  - `logprepexpe` (number)：长期待摊费用
  - `longborr` (number)：长期借款
  - `longdefeinco` (number)：长期递延收益
  - `longpaya` (number)：长期应付款
  - `longpayatot` (number)：长期应付款合计
  - `longrece` (number)：长期应收款
  - `margrece` (number)：应收保证金
  - `margrequ` (number)：应付保证金
  - `minysharrigh` (number)：少数股东权益
  - `notesaccopaya` (number)：应付票据及应付账款
  - `notesaccorece` (number)：应收票据及应收账款
  - `notespaya` (number)：应付票据
  - `notesrece` (number)：应收票据
  - `ocl` (number)：其他综合收益
  - `othdebtinvest` (number)：其他债权投资
  - `othequin` (number)：其他权益工具
  - `othequininvest` (number)：其他权益工具投资
  - `othercurrasse` (number)：其他流动资产
  - `othercurreliabi` (number)：其他流动负债
  - `otherfeepaya` (number)：其他应交款
  - `otherlonginve` (number)：其他长期投资
  - `othernoncasse` (number)：其他非流动资产
  - `othernoncfinasse` (number)：其他非流动金融资产
  - `othernoncliabi` (number)：其他非流动负债
  - `otherpay` (number)：其他应付款
  - `otherpaytot` (number)：其他应付款合计
  - `otherrece` (number)：其他应收款
  - `otherrecetot` (number)：其他应收款(合计)
  - `paidincapi` (number)：实收资本(或股本)
  - `paresharrigh` (number)：归属于母公司股东权益合计
  - `perbond` (number)：永续债
  - `plac` (number)：拆出资金
  - `premrece` (number)：应收保费
  - `prep` (number)：预付款项
  - `prepexpe` (number)：待摊费用
  - `prest` (number)：优先股
  - `prodasse` (number)：生产性生物资产
  - `purcresaasset` (number)：买入返售金融资产
  - `recfinanc` (number)：应收款项融资
  - `reincontrese` (number)：应收分保合同准备金
  - `reinrece` (number)：应收分保账款
  - `rese` (number)：盈余公积
  - `righaggr` (number)：所有者权益(或股东权益)合计
  - `ruseassets` (number)：使用权资产
  - `sellrepasse` (number)：卖出回购金融资产款
  - `settresedepo` (number)：结算备付金
  - `shorttermbdspaya` (number)：应付短期债券
  - `shorttermborr` (number)：短期借款
  - `specpaya` (number)：专项应付款
  - `specrese` (number)：专项储备
  - `subsrece` (number)：应收补贴款
  - `taxespaya` (number)：应交税费
  - `topaycashdivi` (number)：拟分配现金股利
  - `totalcurrliab` (number)：流动负债合计
  - `totalnoncassets` (number)：非流动资产合计
  - `totalnoncliab` (number)：非流动负债合计
  - `totasset` (number)：资产总计
  - `totcurrasset` (number)：流动资产合计
  - `totliab` (number)：负债合计
  - `totliabsharequi` (number)：负债和所有者权益(或股东权益)总计
  - `tradfinasset` (number)：交易性金融资产
  - `tradfinliab` (number)：交易性金融负债
  - `tradshartrad` (number)：股权分置流通权
  - `treastk` (number)：减:库存股
  - `undiprof` (number)：未分配利润
  - `unreinveloss` (number)：未确定的投资损失
  - `unseg` (number)：待处理流动资产损益
  - `warliabrese` (number)：担保责任赔偿准备金
  - `accheldfors_tongbi` (number)：accheldfors 同比
  - `accopaya_tongbi` (number)：accopaya 同比
  - `accorece_tongbi` (number)：accorece 同比
  - `accrexpe_tongbi` (number)：accrexpe 同比
  - `accudepr_tongbi` (number)：accudepr 同比
  - `actitradsecu_tongbi` (number)：actitradsecu 同比
  - `actiundesecu_tongbi` (number)：actiundesecu 同比
  - `advapaym_tongbi` (number)：advapaym 同比
  - `amortizcostassets_tongbi` (number)：amortizcostassets 同比
  - `avaisellasse_tongbi` (number)：avaisellasse 同比
  - `bdspaya_tongbi` (number)：bdspaya 同比
  - `bdspayaperbond_tongbi` (number)：bdspayaperbond 同比
  - `bdspayaprest_tongbi` (number)：bdspayaprest 同比
  - `capisurp_tongbi` (number)：capisurp 同比
  - `cenbankborr_tongbi` (number)：cenbankborr 同比
  - `comasse_tongbi` (number)：comasse 同比
  - `consprog_tongbi` (number)：consprog 同比
  - `consprogtot_tongbi` (number)：consprogtot 同比
  - `contractasset_tongbi` (number)：contractasset 同比
  - `contractliab_tongbi` (number)：contractliab 同比
  - `copepoun_tongbi` (number)：copepoun 同比
  - `copewithreinrece_tongbi` (number)：copewithreinrece 同比
  - `copeworkersal_tongbi` (number)：copeworkersal 同比
  - `curfds_tongbi` (number)：curfds 同比
  - `curtrandiff_tongbi` (number)：curtrandiff 同比
  - `defeincotaxliab_tongbi` (number)：defeincotaxliab 同比
  - `defereve_tongbi` (number)：defereve 同比
  - `defetaxasset_tongbi` (number)：defetaxasset 同比
  - `deposit_tongbi` (number)：deposit 同比
  - `derifinaasset_tongbi` (number)：derifinaasset 同比
  - `deriliab_tongbi` (number)：deriliab 同比
  - `deveexpe_tongbi` (number)：deveexpe 同比
  - `dividrece_tongbi` (number)：dividrece 同比
  - `divipaya_tongbi` (number)：divipaya 同比
  - `dometicksett_tongbi` (number)：dometicksett 同比
  - `duenoncliab_tongbi` (number)：duenoncliab 同比
  - `engimate_tongbi` (number)：engimate 同比
  - `equiinve_tongbi` (number)：equiinve 同比
  - `expecurrliab_tongbi` (number)：expecurrliab 同比
  - `expenoncliab_tongbi` (number)：expenoncliab 同比
  - `expinoncurrasset_tongbi` (number)：expinoncurrasset 同比
  - `expotaxrebarece_tongbi` (number)：expotaxrebarece 同比
  - `fairvalueassets_tongbi` (number)：fairvalueassets 同比
  - `fdsborr_tongbi` (number)：fdsborr 同比
  - `fixedasseclea_tongbi` (number)：fixedasseclea 同比
  - `fixedassecleatot_tongbi` (number)：fixedassecleatot 同比
  - `fixedasseimmo_tongbi` (number)：fixedasseimmo 同比
  - `fixedasseimpa_tongbi` (number)：fixedasseimpa 同比
  - `fixedassenet_tongbi` (number)：fixedassenet 同比
  - `fixedassenetw_tongbi` (number)：fixedassenetw 同比
  - `generiskrese_tongbi` (number)：generiskrese 同比
  - `goodwill_tongbi` (number)：goodwill 同比
  - `holdinvedue_tongbi` (number)：holdinvedue 同比
  - `hydrasset_tongbi` (number)：hydrasset 同比
  - `insucontrese_tongbi` (number)：insucontrese 同比
  - `intaasset_tongbi` (number)：intaasset 同比
  - `intelpay_tongbi` (number)：intelpay 同比
  - `intelrece_tongbi` (number)：intelrece 同比
  - `intepaya_tongbi` (number)：intepaya 同比
  - `interece_tongbi` (number)：interece 同比
  - `inteticksett_tongbi` (number)：inteticksett 同比
  - `inve_tongbi` (number)：inve 同比
  - `inveprop_tongbi` (number)：inveprop 同比
  - `lcopeworkersal_tongbi` (number)：lcopeworkersal 同比
  - `leaseliab_tongbi` (number)：leaseliab 同比
  - `lendandloan_tongbi` (number)：lendandloan 同比
  - `liabheldfors_tongbi` (number)：liabheldfors 同比
  - `logprepexpe_tongbi` (number)：logprepexpe 同比
  - `longborr_tongbi` (number)：longborr 同比
  - `longdefeinco_tongbi` (number)：longdefeinco 同比
  - `longpaya_tongbi` (number)：longpaya 同比
  - `longpayatot_tongbi` (number)：longpayatot 同比
  - `longrece_tongbi` (number)：longrece 同比
  - `margrece_tongbi` (number)：margrece 同比
  - `margrequ_tongbi` (number)：margrequ 同比
  - `minysharrigh_tongbi` (number)：minysharrigh 同比
  - `notesaccopaya_tongbi` (number)：notesaccopaya 同比
  - `notesaccorece_tongbi` (number)：notesaccorece 同比
  - `notespaya_tongbi` (number)：notespaya 同比
  - `notesrece_tongbi` (number)：notesrece 同比
  - `ocl_tongbi` (number)：ocl 同比
  - `othdebtinvest_tongbi` (number)：othdebtinvest 同比
  - `othequin_tongbi` (number)：othequin 同比
  - `othequininvest_tongbi` (number)：othequininvest 同比
  - `othercurrasse_tongbi` (number)：othercurrasse 同比
  - `othercurreliabi_tongbi` (number)：othercurreliabi 同比
  - `otherfeepaya_tongbi` (number)：otherfeepaya 同比
  - `otherlonginve_tongbi` (number)：otherlonginve 同比
  - `othernoncasse_tongbi` (number)：othernoncasse 同比
  - `othernoncfinasse_tongbi` (number)：othernoncfinasse 同比
  - `othernoncliabi_tongbi` (number)：othernoncliabi 同比
  - `otherpay_tongbi` (number)：otherpay 同比
  - `otherpaytot_tongbi` (number)：otherpaytot 同比
  - `otherrece_tongbi` (number)：otherrece 同比
  - `otherrecetot_tongbi` (number)：otherrecetot 同比
  - `paidincapi_tongbi` (number)：paidincapi 同比
  - `paresharrigh_tongbi` (number)：paresharrigh 同比
  - `perbond_tongbi` (number)：perbond 同比
  - `plac_tongbi` (number)：plac 同比
  - `premrece_tongbi` (number)：premrece 同比
  - `prep_tongbi` (number)：prep 同比
  - `prepexpe_tongbi` (number)：prepexpe 同比
  - `prest_tongbi` (number)：prest 同比
  - `prodasse_tongbi` (number)：prodasse 同比
  - `purcresaasset_tongbi` (number)：purcresaasset 同比
  - `recfinanc_tongbi` (number)：recfinanc 同比
  - `reincontrese_tongbi` (number)：reincontrese 同比
  - `reinrece_tongbi` (number)：reinrece 同比
  - `rese_tongbi` (number)：rese 同比
  - `righaggr_tongbi` (number)：righaggr 同比
  - `ruseassets_tongbi` (number)：ruseassets 同比
  - `sellrepasse_tongbi` (number)：sellrepasse 同比
  - `settresedepo_tongbi` (number)：settresedepo 同比
  - `shorttermbdspaya_tongbi` (number)：shorttermbdspaya 同比
  - `shorttermborr_tongbi` (number)：shorttermborr 同比
  - `specpaya_tongbi` (number)：specpaya 同比
  - `specrese_tongbi` (number)：specrese 同比
  - `subsrece_tongbi` (number)：subsrece 同比
  - `taxespaya_tongbi` (number)：taxespaya 同比
  - `topaycashdivi_tongbi` (number)：topaycashdivi 同比
  - `totalcurrliab_tongbi` (number)：totalcurrliab 同比
  - `totalnoncassets_tongbi` (number)：totalnoncassets 同比
  - `totalnoncliab_tongbi` (number)：totalnoncliab 同比
  - `totasset_tongbi` (number)：totasset 同比
  - `totcurrasset_tongbi` (number)：totcurrasset 同比
  - `totliab_tongbi` (number)：totliab 同比
  - `totliabsharequi_tongbi` (number)：totliabsharequi 同比
  - `tradfinasset_tongbi` (number)：tradfinasset 同比
  - `tradfinliab_tongbi` (number)：tradfinliab 同比
  - `tradshartrad_tongbi` (number)：tradshartrad 同比
  - `treastk_tongbi` (number)：treastk 同比
  - `undiprof_tongbi` (number)：undiprof 同比
  - `unreinveloss_tongbi` (number)：unreinveloss 同比
  - `unseg_tongbi` (number)：unseg 同比
  - `warliabrese_tongbi` (number)：warliabrese 同比

### 现金流表(数据源SI) — `get_ch_si_stock_fin_cash_flow`
分类：财务数据 ｜ 可测试：—

  - `report_period` (string)：报告期, YYYY-MM-DD
  - `report_name` (string)：报告名称
  - `announcement_date` (string)：公告日期, YYYY-MM-DD
  - `currency` (string)：货币
  - `report_type` (string)：报表类型
  - `data_source` (string)：数据来源
  - `is_audit` (string)：是否审计
  - `acquassetcash` (number)：购建固定资产、无形资产和其他长期资产所支付的现金
  - `bankloannetincr` (number)：向中央银行借款净增加额
  - `bizcashinfl` (number)：经营活动现金流入小计
  - `bizcashoutf` (number)：经营活动现金流出小计
  - `cashfinalbala` (number)：现金的期末余额
  - `cashnetr` (number)：现金及现金等价物净增加额
  - `cashopenbala` (number)：现金的期初余额
  - `charintecash` (number)：收取利息、手续费及佣金的现金
  - `chgexchgchgs` (number)：汇率变动对现金及现金等价物的影响
  - `debtpaycash` (number)：偿还债务支付的现金
  - `deponetr` (number)：客户存款和同业存放款项净增加额
  - `dispfinanetincrinve` (number)：处置可供出售金融资产净增加额
  - `disptradnetincr` (number)：处置交易性金融资产净增加额
  - `diviprofpaycash` (number)：分配股利、利润或偿付利息所支付的现金
  - `equfinalbala` (number)：现金等价物的期末余额
  - `equopenbala` (number)：现金等价物的期初余额
  - `fdsborrnetr` (number)：拆入资金净增加额
  - `finalcashbala` (number)：期末现金及现金等价物余额
  - `fincashinfl` (number)：筹资活动现金流入小计
  - `fincashoutf` (number)：筹资活动现金流出小计
  - `fininstnetr` (number)：向其他金融机构拆入资金净增加额
  - `finnetcflow` (number)：筹资活动产生的现金流量净额
  - `finrelacash` (number)：支付其他与筹资活动有关的现金
  - `fixedassetnetc` (number)：处置固定资产、无形资产和其他长期资产所收回的现金净额
  - `incrcashpled` (number)：增加质押和定期存款所支付的现金
  - `inicashbala` (number)：期初现金及现金等价物余额
  - `insnetc` (number)：收到再保险业务现金净额
  - `inspremcash` (number)：收到原保险合同保费取得的现金
  - `invcashinfl` (number)：投资活动现金流入小计
  - `invcashoutf` (number)：投资活动现金流出小计
  - `inveretugetcash` (number)：取得投资收益收到的现金
  - `invnetcashflow` (number)：投资活动产生的现金流量净额
  - `invpayc` (number)：投资所支付的现金
  - `invrececash` (number)：吸收投资收到的现金
  - `issbdrececash` (number)：发行债券收到的现金
  - `labopayc` (number)：购买商品、接受劳务支付的现金
  - `laborgetcash` (number)：销售商品、提供劳务收到的现金
  - `loannetr` (number)：质押贷款净增加额
  - `loansnetr` (number)：客户贷款及垫款净增加额
  - `mananetr` (number)：经营活动产生的现金流量净额
  - `payacticash` (number)：支付的其他与经营活动有关的现金
  - `paycompgold` (number)：支付原保险合同赔付款项的现金
  - `paydivicash` (number)：支付保单红利的现金
  - `payintecash` (number)：支付利息、手续费及佣金的现金
  - `payinvecash` (number)：支付的其他与投资活动有关的现金
  - `paytax` (number)：支付的各项税费
  - `payworkcash` (number)：支付给职工以及为职工支付的现金
  - `recefincash` (number)：收到其他与筹资活动有关的现金
  - `recefromloan` (number)：取得借款收到的现金
  - `receinvcash` (number)：收到的其他与投资活动有关的现金
  - `receotherbizcash` (number)：收到的其他与经营活动有关的现金
  - `reducashpled` (number)：减少质押和定期存款所收到的现金
  - `repnetincr` (number)：回购业务资金净增加额
  - `savinetr` (number)：保户储金及投资款净增加额
  - `subsnetc` (number)：处置子公司及其他营业单位收到的现金净额
  - `subspaydivid` (number)：子公司支付给少数股东的股利、利润
  - `subspaynetcash` (number)：取得子公司及其他营业单位支付的现金净额
  - `subsrececash` (number)：子公司吸收少数股东投资收到的现金
  - `taxrefd` (number)：收到的税费返还
  - `tradepaymnetr` (number)：存放中央银行和同业款项净增加额
  - `withinvgetcash` (number)：收回投资所收到的现金
  - `acquassetcash_tongbi` (number)：acquassetcash 同比
  - `bankloannetincr_tongbi` (number)：bankloannetincr 同比
  - `bizcashinfl_tongbi` (number)：bizcashinfl 同比
  - `bizcashoutf_tongbi` (number)：bizcashoutf 同比
  - `cashfinalbala_tongbi` (number)：cashfinalbala 同比
  - `cashnetr_tongbi` (number)：cashnetr 同比
  - `cashopenbala_tongbi` (number)：cashopenbala 同比
  - `charintecash_tongbi` (number)：charintecash 同比
  - `chgexchgchgs_tongbi` (number)：chgexchgchgs 同比
  - `debtpaycash_tongbi` (number)：debtpaycash 同比
  - `deponetr_tongbi` (number)：deponetr 同比
  - `dispfinanetincrinve_tongbi` (number)：dispfinanetincrinve 同比
  - `disptradnetincr_tongbi` (number)：disptradnetincr 同比
  - `diviprofpaycash_tongbi` (number)：diviprofpaycash 同比
  - `equfinalbala_tongbi` (number)：equfinalbala 同比
  - `equopenbala_tongbi` (number)：equopenbala 同比
  - `fdsborrnetr_tongbi` (number)：fdsborrnetr 同比
  - `finalcashbala_tongbi` (number)：finalcashbala 同比
  - `fincashinfl_tongbi` (number)：fincashinfl 同比
  - `fincashoutf_tongbi` (number)：fincashoutf 同比
  - `fininstnetr_tongbi` (number)：fininstnetr 同比
  - `finnetcflow_tongbi` (number)：finnetcflow 同比
  - `finrelacash_tongbi` (number)：finrelacash 同比
  - `fixedassetnetc_tongbi` (number)：fixedassetnetc 同比
  - `incrcashpled_tongbi` (number)：incrcashpled 同比
  - `inicashbala_tongbi` (number)：inicashbala 同比
  - `insnetc_tongbi` (number)：insnetc 同比
  - `inspremcash_tongbi` (number)：inspremcash 同比
  - `invcashinfl_tongbi` (number)：invcashinfl 同比
  - `invcashoutf_tongbi` (number)：invcashoutf 同比
  - `inveretugetcash_tongbi` (number)：inveretugetcash 同比
  - `invnetcashflow_tongbi` (number)：invnetcashflow 同比
  - `invpayc_tongbi` (number)：invpayc 同比
  - `invrececash_tongbi` (number)：invrececash 同比
  - `issbdrececash_tongbi` (number)：issbdrececash 同比
  - `labopayc_tongbi` (number)：labopayc 同比
  - `laborgetcash_tongbi` (number)：laborgetcash 同比
  - `loannetr_tongbi` (number)：loannetr 同比
  - `loansnetr_tongbi` (number)：loansnetr 同比
  - `mananetr_tongbi` (number)：mananetr 同比
  - `payacticash_tongbi` (number)：payacticash 同比
  - `paycompgold_tongbi` (number)：paycompgold 同比
  - `paydivicash_tongbi` (number)：paydivicash 同比
  - `payintecash_tongbi` (number)：payintecash 同比
  - `payinvecash_tongbi` (number)：payinvecash 同比
  - `paytax_tongbi` (number)：paytax 同比
  - `payworkcash_tongbi` (number)：payworkcash 同比
  - `recefincash_tongbi` (number)：recefincash 同比
  - `recefromloan_tongbi` (number)：recefromloan 同比
  - `receinvcash_tongbi` (number)：receinvcash 同比
  - `receotherbizcash_tongbi` (number)：receotherbizcash 同比
  - `reducashpled_tongbi` (number)：reducashpled 同比
  - `repnetincr_tongbi` (number)：repnetincr 同比
  - `savinetr_tongbi` (number)：savinetr 同比
  - `subsnetc_tongbi` (number)：subsnetc 同比
  - `subspaydivid_tongbi` (number)：subspaydivid 同比
  - `subspaynetcash_tongbi` (number)：subspaynetcash 同比
  - `subsrececash_tongbi` (number)：subsrececash 同比
  - `taxrefd_tongbi` (number)：taxrefd 同比
  - `tradepaymnetr_tongbi` (number)：tradepaymnetr 同比
  - `withinvgetcash_tongbi` (number)：withinvgetcash 同比

### 个股财务核心指标(数据源Ea) — `get_ch_ea_stock_fin_key_indicators`
分类：财务数据 ｜ 可测试：—

  - `basic_eps` (number)：基本每股收益(元) BASIC_EPS
  - `diluted_eps` (number)：稀释每股收益(元) DILUTED_EPS
  - `ttm_eps` (number)：TTM每股收益(元) EPS_TTM
  - `bvps` (number)：每股净资产(元) BPS
  - `ops_cash_per_share` (number)：每股经营现金流(元) PER_NETCASH_OPERATE
  - `ops_rev_per_share` (number)：每股营业收入(元) PER_OI
  - `total_revenue` (number)：营业总收入(元) OPERATE_INCOME
  - `revenue_yoy` (number)：营业总收入同比增长(%) OPERATE_INCOME_YOY
  - `revenue_qoq` (number)：营业总收入滚动环比增长(%) OPERATE_INCOME_QOQ
  - `gross_profit` (number)：毛利润(元) GROSS_PROFIT
  - `gp_yoy` (number)：毛利润同比增长(%) GROSS_PROFIT_YOY
  - `gp_qoq` (number)：毛利润滚动环比增长(%) GROSS_PROFIT_QOQ
  - `net_profit` (number)：归母净利润(元) HOLDER_PROFIT
  - `np_yoy` (number)：归母净利润同比增长(%) HOLDER_PROFIT_YOY
  - `np_qoq` (number)：归母净利润滚动环比增长(%) HOLDER_PROFIT_QOQ
  - `tax_to_profit` (number)：所得税/利润总额(%) TAX_EBT
  - `ops_cf_to_rev` (number)：经营现金流/营业收入(%) OCF_SALES
  - `avg_roe` (number)：平均净资产收益率(%) ROE_AVG
  - `ann_roe` (number)：年化净资产收益率(%) ROE_YEARLY
  - `roa` (number)：总资产净利率(%) ROA
  - `gross_margin` (number)：毛利率(%) GROSS_PROFIT_RATIO
  - `net_margin` (number)：净利率(%) NET_PROFIT_RATIO
  - `ann_roi` (number)：年化投资回报率(%) ROIC_YEARLY
  - `ar_turnover` (number)：应收账款周转率(次) 注意：原始数据中是周转天数
  - `inv_turnover` (number)：存货周转率(次) 注意：原始数据中是周转天数
  - `ca_turnover` (number)：流动资产周转率(次) 注意：原始数据中是周转天数
  - `ta_turnover` (number)：总资产周转率(次) 注意：原始数据中是周转天数
  - `current_ratio` (number)：流动比率(倍) CURRENT_RATIO
  - `curr_liab_ratio` (number)：流动负债/总负债(%) CURRENTDEBT_DEBT
  - `debt_ratio` (number)：资产负债率(%) DEBT_ASSET_RATIO
  - `equity_multi` (number)：权益乘数 EQUITY_MULTIPLIER
  - `equity_ratio` (number)：产权比率 EQUITY_RATIO
  - `tag_date` (string)：报告日期
  - `report_type` (string)：报告类型

### 个股资产负债表(数据源Ea) — `get_ch_ea_stock_fin_balance_sheet`
分类：财务数据 ｜ 可测试：—

  - `secucode` (string)：股票代码(带市场)
  - `report_date` (string)：报告日期
  - `report_type` (string)：报告类型
  - `total_assets` (number)：总资产(元)
  - `fixed_asset` (number)：固定资产(元)
  - `monetaryfunds` (number)：货币资金(元)
  - `accounts_rece` (number)：应收账款(元)
  - `inventory` (number)：存货(元)
  - `total_liabilities` (number)：总负债(元)
  - `accounts_payable` (number)：应付账款(元)
  - `total_equity` (number)：股东权益合计(元)
  - `current_ratio` (number)：流动比率(%)
  - `debt_asset_ratio` (number)：资产负债率(%)

### 个股利润表(数据源Ea) — `get_ch_ea_stock_fin_income_statements`
分类：财务数据 ｜ 可测试：—

  - `secucode` (string)：股票代码(带市场)
  - `report_date` (string)：报告日期
  - `report_type` (string)：报告类型
  - `total_operate_income` (number)：营业总收入(元)
  - `total_operate_cost` (number)：营业总成本(元)
  - `operate_cost` (number)：营业成本(元)
  - `sale_expense` (number)：销售费用(元)
  - `manage_expense` (number)：管理费用(元)
  - `finance_expense` (number)：财务费用(元)
  - `operate_profit` (number)：营业利润(元)
  - `total_profit` (number)：利润总额(元)
  - `income_tax` (number)：所得税(元)
  - `parent_netprofit` (number)：归母净利润(元)
  - `deduct_parent_netprofit` (number)：扣非归母净利润(元)

### 个股现金流量表(数据源Ea) — `get_ch_ea_stock_fin_cash_flow`
分类：财务数据 ｜ 可测试：—

  - `secucode` (string)：股票代码(带市场)
  - `report_date` (string)：报告日期
  - `report_type` (string)：报告类型
  - `netcash_operate` (number)：经营活动现金流净额(元)
  - `sales_services` (number)：销售商品收到现金(元)
  - `netcash_invest` (number)：投资活动现金流净额(元)
  - `construct_long_asset` (number)：购建固定资产支付(元)
  - `netcash_finance` (number)：筹资活动现金流净额(元)
  - `cce_add` (number)：现金净增加额(元)

### 订阅可转债实时行情通道 — `subscribe_ch_kzz_stock_real`
分类：可转债 ｜ 可测试：—

  - `time` (string)：数据时间
  - `close` (number)：当前价
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `low` (number)：今日最低价
  - `pre_volume` (number)：前成交量
  - `volume` (number)：成交量
  - `amount` (number)：成交额（元）
  - `buy_five` (list)：买五档价
  - `buy_five_vol` (list)：买五档量
  - `sell_five` (list)：卖五档价
  - `sell_five_vol` (list)：卖五档量
  - `turnover` (number)：换手率（%）
  - `volume_ratio` (number)：量比
  - `bid_ask_ratio` (number)：委比（%）
  - `inst_aggressive_buy_amount` (number)：主力主动净买额（万元）
  - `inst_net_amount` (number)：主力净流入（万元）
  - `l2_total_buy_vol` (number)：总买量
  - `l2_total_sell_vol` (number)：总卖量
  - `l2_deal_tick_num` (integer)：L2逐笔成交数
  - `l2_order_tick_num` (integer)：L2逐笔委托数

### 获取可转债实时行情 — `get_ch_kzz_cur_real`
分类：可转债 ｜ 可测试：—

  - `time` (string)：数据时间
  - `close` (number)：当前价
  - `last_close` (number)：昨日收盘价
  - `open` (number)：今日开盘价
  - `high` (number)：今日最高价
  - `low` (number)：今日最低价
  - `pre_volume` (number)：前成交量
  - `volume` (number)：成交量
  - `amount` (number)：成交额（元）
  - `buy_five` (list)：买五档价
  - `buy_five_vol` (list)：买五档量
  - `sell_five` (list)：卖五档价
  - `sell_five_vol` (list)：卖五档量
  - `turnover` (number)：换手率（%）
  - `volume_ratio` (number)：量比
  - `bid_ask_ratio` (number)：委比（%）
  - `inst_aggressive_buy_amount` (number)：主力主动净买额（万元）
  - `inst_net_amount` (number)：主力净流入（万元）
  - `l2_total_buy_vol` (number)：总买量
  - `l2_total_sell_vol` (number)：总卖量
  - `l2_deal_tick_num` (integer)：L2逐笔成交数
  - `l2_order_tick_num` (integer)：L2逐笔委托数

### 获取可转债列表 — `get_ch_kzz_stock`
分类：可转债 ｜ 可测试：—

  - `code` (string)：可转债代码
  - `name` (string)：可转债名称
  - `underlying_stock` (string)：正股代码
  - `price` (number)：可转债现价（元）
  - `underlying_stock_price` (number)：正股价（元）
  - `convert_price` (number)：最新转股价（元）
  - `convert_value` (number)：转股价值（元）
  - `conversion_premium` (number)：转股溢价率（%）
  - `convert_rate` (number)：转股价值
  - `outstanding_volume` (number)：未转股余额（万元）
  - `cur_rate` (number)：当期利率（%）
  - `time_to_market` (string)：上市日期
  - `end_date` (string)：到期日期
  - `end_price` (number)：到期赎回价（元）
  - `convert_date` (string)：转股起始日
  - `put_back_price` (number)：回售价（元）
  - `redeem_date` (string)：赎回日期
  - `redeem_price` (number)：赎回价格（元）
  - `force_redeem_price` (number)：强赎触发价（元）
  - `score` (number)：评分
  - `main_score` (number)：主力评分
  - `convert_code` (string)：转股代码
