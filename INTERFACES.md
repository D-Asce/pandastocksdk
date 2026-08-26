# pandaData 接口清单（全部 176 个）

> **图例**：✅ 可测试 = 已对公开 key 开放（免费试用可用，按来源 IP 限频）；— 暂未开放 = 需专属 key / 付费后使用。

> 接口定义来源 `apis.json`（服务端 176 个接口）。其中 `get_ch_stock_ddx_data()` 已在 SDK 实现并开放，但未收录于 `apis.json`，于文末单独列出。


| 分类 | 接口名称 | 方法(function) | 说明 | 可测试 |
|---|---|---|---|---|
| Levle2和大单 | 订阅Level2实时数据通道 | `subscribe_ch_l2_data_real` | 订阅全量个股Level2数据通道，从竞价开始实时推送。数据包含竞价金额、成交量涨… | — 暂未开放 |
| Levle2和大单 | 获取Level2实时数据 | `get_ch_l2_data_cur_real` | 随时获取全量个股Level2高级行情数据，包括竞价金额、成交量涨速、委托/撤单/… | — 暂未开放 |
| Levle2和大单 | 订阅大单数据(DDE)通道 | `subscribe_ch_ddx_data_real` | 订阅全量个股DDE大单数据通道，交易日9:31左右开始实时推送。包含DDX、DD… | — 暂未开放 |
| Levle2和大单 | 获取大单数据(DDE) | `get_ch_ddx_data_cur_real` | 实时获取全量个股DDE大单数据，包含DDX/DDY/DDZ三大核心指标、各类资金… | — 暂未开放 |
| Levle2和大单 | 获取个股历史大单历史数据 | `get_ch_stock_ddx_history` | 获取个股DDE历史数据 | — 暂未开放 |
| Levle2和大单 | 个股千档数据 | `get_ch_stock_thousand_level_order` | 获取指定个股的千档盘口数据，包含每档详细挂单数据。注意每个档位挂单明细中，最多返… | — 暂未开放 |
| Levle2和大单 | 个股实时资金流数据 | `get_ch_stock_l2_fund_flow_sa` | 获取个股level2实时超大单，大单，中单，小单净流入金额。超大单：单笔≥50万… | — 暂未开放 |
| Levle2和大单 | 获取个股最新逐笔成交 | `get_ch_stock_l2_laster_transactions_sa` | 获取个股最新 100 条逐笔成交（约最近 1-2 分钟内数据） | — 暂未开放 |
| Levle2和大单 | 获取个股全部逐笔成交数据 | `get_ch_stock_l2_all_transactions_sa` | 获取获取当日全部逐笔成交数据明细。数据量较大，单只个股获取时间较长 | — 暂未开放 |
| Levle2和大单 | 市场实时资金流数据 | `get_ch_all_market_l2_fund_flow` | 实时获取市场总体资金流数据 | — 暂未开放 |
| Levle2和大单 | 上证指数实时资金流数据 | `get_ch_sh_market_l2_fund_flow` | 上证指数实时资金流数据 | — 暂未开放 |
| Levle2和大单 | 深圳市场实时资金流数据 | `get_ch_sz_market_l2_fund_flow` | 深圳市场实时资金流数据 | — 暂未开放 |
| Levle2和大单 | 创业板实时资金流数据 | `get_ch_cyb_market_l2_fund_flow` | 创业板实时资金流数据 | — 暂未开放 |
| Levle2和大单 | 科创板实时资金流数据 | `get_ch_kcb_market_l2_fund_flow` | 科创板实时资金流数据 | — 暂未开放 |
| Levle2和大单 | 个股实时大单成交明细 | `get_ch_stock_big_order` | 返回个股交易日当天实时成交大单明细 | — 暂未开放 |
| Levle2和大单 | 订阅Level2单只股成交明细 | `subscribe_ch_l2_transaction_single` | 订阅单只个股Level2个股成交明细通道，实时推送变化个股。数据可能存在重复，本… | — 暂未开放 |
| Levle2和大单 | 订阅Level2多只股成交明细 | `subscribe_ch_l2_transaction_batch` | 批量订阅多只股Level2个股成交明细通道，实时推送变化个股。数据可能存在重复，… | — 暂未开放 |
| Levle2和大单 | 订阅Level2所有股成交明细 | `subscribe_ch_l2_transaction_all` | 批量所有个股Level2个股成交明细通道，实时推送变化个股。数据可能存在重复，本… | — 暂未开放 |
| Levle2和大单 | 个股l2分价成交明细 | `get_ch_stock_price_summarize` | 盘中实时返回个股l2 分价成交明细 | — 暂未开放 |
| Levle2和大单 | 订阅l2单只股十档行情通道 | `subscribe_ch_l2_deep_single` | 订阅单只个股Level2个股十档行情数据，实时推送 | — 暂未开放 |
| Levle2和大单 | 订阅l2多只股十档行情通道 | `subscribe_ch_l2_depth_batch` | 订阅多只个股Level2个股十档行情数据，实时推送 | — 暂未开放 |
| Levle2和大单 | 订阅l2所有股票十档行情通道 | `subscribe_ch_l2_depth_all` | 订阅多所有股票Level2个股十档行情数据，实时推送 | — 暂未开放 |
| Levle2和大单 | 订阅l2单只个股买 一卖一明细 | `subscribe_ch_l2_orders_single` | 实时推送订阅个股，买一，卖一总体挂单总量，挂单笔数。同时返回详细的挂单信息。要注… | — 暂未开放 |
| Levle2和大单 | 订阅l2多只个股买 一卖一明细 | `subscribe_ch_l2_orders_batch` | 实时推送订阅个股，买一，卖一总体挂单总量，挂单笔数。同时返回详细的挂单信息。要注… | — 暂未开放 |
| Levle2和大单 | 订阅l2所有股票买 一卖一明细 | `subscribe_ch_l2_orders_all` | 实时推送订阅个股，买一，卖一总体挂单总量，挂单笔数。同时返回详细的挂单信息。要注… | — 暂未开放 |
| Levle2和大单 | 日内实时暗盘资金 | `get_ch_stock_dark_rank` | 获取交易日内所有个股实时暗盘资金数据 | — 暂未开放 |
| Levle2和大单 | 历史暗盘资金 | `get_ch_stock_dark_rank_history` | 获取某个交易日所有个股暗盘资金数据 | — 暂未开放 |
| Levle2和大单 | 个股DDE实时数据 | `get_ch_stock_ea_dde` | 获取所有个股DDE决策数据 | — 暂未开放 |
| 新闻资讯 | 重点资讯新闻 | `get_core_new` | 获取指定日期重点资讯新闻 | ✅ 可测试 |
| 新闻资讯 | 国内主要新闻 | `get_domestic_financial_news` | 获取指定日期国内资讯新闻 | ✅ 可测试 |
| 新闻资讯 | 国际主要新闻 | `get_global_financial_news` | 获取指定日期国际主要新闻 | ✅ 可测试 |
| 新闻资讯 | 时评类新闻 | `get_options_news` | 获取指定日期时评类新闻 | ✅ 可测试 |
| 新闻资讯 | 个股新闻 | `get_ch_stock_month_news` | 获取个股指定年-月的新闻数据 | — 暂未开放 |
| 新闻资讯 | 财经快讯(数据源sn) | `get_ch_sn_kx` | 获取指定日期快讯数据，包含正文全文、来源、标签、关联股票等信息。返回数据格式为D… | — 暂未开放 |
| 新闻资讯 | 财经快讯(数据源SA) | `get_ch_sa_kx` | 获取市场财经快讯(数据源SA) | — 暂未开放 |
| 新闻资讯 | 个股公告 | `get_ch_stock_announce` | 获取个股指定日期公告信息，如果返回数据为空，表示当天无公告。 | — 暂未开放 |
| 新闻资讯 | 个股研报 | `get_ch_stock_research_report` | 获取个股指定日期研报信息。如果对应日期返回为空，则表示当日无研报数据 | — 暂未开放 |
| 特色数据 | 每日ST股信息 | `get_ch_stock_st_history` | 获取指定交易日ST个股列表 | — 暂未开放 |
| 特色数据 | 沪深300成分股权重 | `get_ch_hs300_constituent_weight_history` | 获取沪深300指数成分股，每月权重信息。数据从2015年1月到目前， | — 暂未开放 |
| 特色数据 | 上证50成分股权重 | `get_ch_sz50_constituent_weight_history` | 获取上证50指数成分股，每月权重信息。数据从2015年1月到目前， | — 暂未开放 |
| 特色数据 | 中证500成分股权重 | `get_ch_zz500_constituent_weight_history` | 获取中证500指数成分股，每月权重信息。数据从2015年1月到目前， | — 暂未开放 |
| 特色数据 | 中证1000成分股权重 | `get_ch_zz1000_constituent_weight_history` | 获取中证1000指数成分股，每月权重信息。数据从2015年1月到目前， | — 暂未开放 |
| 特色数据 | 个股除权除息历史 | `get_ch_stock_dividend_history` | 获取指定个股除权除息历史 | — 暂未开放 |
| 特色数据 | 年度高送转/分红 | `get_ch_year_high_stock_dividend` | 获取自然年内所有高送转，分红派息个股数据。数据从1992年至今，每日更新数据 | — 暂未开放 |
| 特色数据 | 个股股本变化历史 | `get_ch_stock_share_capital` | 获取指定个股每个交易日股本情况。从个股上市到今日。每日更新 | — 暂未开放 |
| 特色数据 | 个股资金流明细历史 | `get_ch_stock_fund_flow_detail_history` | 获取指定个股历史资金流详细数据。目前数据从2010年到现在，该数据会定期更新 | — 暂未开放 |
| 特色数据 | 年度解禁数据 | `get_ch_year_stock_lock_up` | 获取自然年内所有限售解禁个股信息，数据从2006年到2035年。定时更新 | — 暂未开放 |
| 特色数据 | 1日融资买入排行 | `get_ch_rz_buy_1_day` | 获取近1日融资买入信息 | — 暂未开放 |
| 特色数据 | 5日融资买入排行 | `get_ch_rz_buy_5_day` | 获取近5日融资买入信息 | — 暂未开放 |
| 特色数据 | 20日融资买入排行 | `get_ch_rz_buy_20_day` | 获取近20日融资买入信息 | — 暂未开放 |
| 特色数据 | 个股一致行动人信息 | `get_ch_stock_pacs` | 获取A股个股一致行动人信息。一致行动人指通过协议、合作等途径扩大对上市公司表决权… | — 暂未开放 |
| 特色数据 | 市场每个交易日涨跌平数量 | `get_ch_day_zd_count_history` | 返回市场历史上每个交易日上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 上证A股每个交易日涨跌平数量 | `get_ch_sh_day_zd_count_history` | 获取上证A股每个交易日，上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 深圳A股每个交易日涨跌平数量 | `get_ch_sz_day_zd_count_history` | 获取深圳A股每个交易日，上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 创业板每个交易日涨跌平数量 | `get_ch_cyb_day_zd_count_history` | 获取创业板每个交易日，上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 科创板每个交易日涨跌平数量 | `get_ch_kcb_day_zd_count_history` | 获取科创板每个交易日，上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 北证每个交易日涨跌平数量 | `get_ch_bj_day_zd_count_history` | 获取北证每个交易日，上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 市场每个交易周涨跌平数量 | `get_ch_week_zd_count_history` | 返回市场历史上每个交易周上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 上证A股每个交易周涨跌平数量 | `get_ch_sh_week_zd_count_history` | 返回上证A股历史上每个交易周上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 深圳A股每个交易周涨跌平数量 | `get_ch_sz_week_zd_count_history` | 返回深圳A股历史上每个交易周上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 创业板每个交易周涨跌平数量 | `get_ch_cyb_week_zd_count_history` | 返回创业板历史上每个交易周上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 科创板每个交易周涨跌平数量 | `get_ch_kcb_week_zd_count_history` | 返回科创板历史上每个交易周上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 北证每个交易周涨跌平数量 | `get_ch_bj_week_zd_count_history` | 返回北证历史上每个交易周上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 市场每个交易月涨跌平数量 | `get_ch_month_zd_count_history` | 返回市场历史上每个交易月上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 上证A股每个交易月涨跌平数量 | `get_ch_sh_month_zd_count_history` | 返回上证A股历史上每个交易月上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 深圳A股每个交易月涨跌平数量 | `get_ch_sz_month_zd_count_history` | 返回深圳A股历史上每个交易月上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 创业板每个交易月涨跌平数量 | `get_ch_cyb_month_zd_count_history` | 返回创业板历史上每个交易月上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 科创板每个交易月涨跌平数量 | `get_ch_kcb_month_zd_count_history` | 返回科创板历史上每个交易月上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 北证每个交易月涨跌平数量 | `get_ch_bj_month_zd_count_history` | 返回北证历史上每个交易月上涨，下跌，平盘数量 | — 暂未开放 |
| 特色数据 | 中国全社会用电量同比 | `get_ch_electricity_use_history` | 返回中国全社会用电量同比历史数据 | — 暂未开放 |
| 特色数据 | 全市场PE/PB 月数据历史 | `get_ch_market_pe_pb_month_history` | 返回全市体市场PE，PB 历史数据，按月统计 | — 暂未开放 |
| 特色数据 | 全市场PE/PB 日数据历史 | `get_ch_market_pe_pb_day_history` | 返回全市体市场PE，PB 历史数据，按日统计。在增量存储中 | — 暂未开放 |
| 特色数据 | 中国年度GDP同比增长率 | `get_ch_gdp_yearly_growth` | 获取中国年度GDP同比增长率，数据从2000年到现在 | — 暂未开放 |
| 特色数据 | 中国季度GDP同比增长率 | `get_ch_gdp_quarter_rate` | 数据从2014年到现在 | — 暂未开放 |
| 特色数据 | 中国季度GDP环比增长率 | `get_ch_gdp_qoq_rate` | 数据从2014年到现在 | — 暂未开放 |
| 特色数据 | 个股l2分价成交明细历史 | `get_ch_stock_price_summarize_history` | 查询个股某个交易日l2 分价成交明细。数据从2026年7月13日开始存储 | — 暂未开放 |
| 特色数据 | 交易日涨跌停时序数据 | `get_ch_limit_up_down_history` | 返回指定交易日涨跌停数量变化曲线数据，数据从2026年7月17日开始 | — 暂未开放 |
| 特色数据 | 交易日涨跌分布时序数据 | `get_ch_zd_map_history` | 返回指定交易日涨跌分布变化曲线数据，数据从2026年7月17日开始 | — 暂未开放 |
| 特色数据 | 交易日涨停股信息 | `get_ch_lb_stock_history_history` | 获取指定交易日涨停股信息，包括连板晋级率等信息。数据从2024年4月开始 | — 暂未开放 |
| 特色数据 | 交易日全天成交额数据 | `get_ch_market_amount_curve_history` | 获取指定交易全天成交额数据 | — 暂未开放 |
| 特色数据 | 中国GDP 季度数据 | `get_ch_gdp_quarter_value` | 获取中国GDP 季度数据值 | — 暂未开放 |
| 港股行情 | 订阅港股实时行情通道 | `subscribe_hk_stock_real` | 订阅个股实时行情通道，通道采用全量数据推送 | — 暂未开放 |
| 港股行情 | 获取港股实时行情 | `get_hk_stock_real` | 获取全量港股个股实时行情数据 | — 暂未开放 |
| 港股行情 | 订阅港股指数实时行情通道 | `subscribe_hk_market_real` | 订阅指数实时行情通道，通道采用全量数据推送。包括恒生指数，恒生中企指数，恒生科技… | — 暂未开放 |
| 港股行情 | 获取港股指数实时行情 | `get_hk_market_real` | 获取所有指数实时行情数据。包括恒生指数，恒生中企指数，恒生科技指数，恒生红筹指数 | — 暂未开放 |
| 港股行情 | 港股股票列表 | `get_hk_stock` | 获取所有个股基础信息 | — 暂未开放 |
| 港股行情 | 港股个股历史日线 | `get_hk_stock_day_history` | 获取指定个股日线数据 | — 暂未开放 |
| 港股行情 | 港股个股历史周线 | `get_hk_stock_week_history` | 获取指定个股周线数据 | — 暂未开放 |
| 港股行情 | 港股个股历史月线 | `get_hk_stock_month_history` | 获取指定个股月线数据 | — 暂未开放 |
| 港股行情 | 港股指数历史日线 | `get_hk_market_history` | 获取指数日线数据，目前支持获取恒生指数，恒生中企指数，恒生科技指数，恒生红筹指数 | — 暂未开放 |
| 港股行情 | 港股指数历史周线 | `get_hk_market_week_history` | 获取指数周线数据，目前支持获取恒生指数，恒生中企指数，恒生科技指数，恒生红筹指数 | — 暂未开放 |
| 港股行情 | 港股指数历史月线 | `get_hk_market_month_history` | 获取指数月线数据，目前支持获取恒生指数，恒生中企指数，恒生科技指数，恒生红筹指数 | — 暂未开放 |
| 港股行情 | 港股主要财务指标 | `get_hk_stock_main_fin_data` | 获取指定个股历史主要财务指标数据 | — 暂未开放 |
| 港股行情 | 港股资产负债表 | `get_hk_stock_balance_sheet` | 获取指定个股资产负债表历史 | — 暂未开放 |
| 港股行情 | 港股利润表 | `get_hk_stock_profit_statement` | 获取指定个股利润表历史 | — 暂未开放 |
| 港股行情 | 港股现金流表 | `get_hk_stock_cash_flow` | 获取指定个股现金流表历史 | — 暂未开放 |
| 个股数据 | 获取股票列表 | `get_ch_stock` | 获取所有A股个股信息列表 | ✅ 可测试 |
| 个股数据 | 订阅实时行情通道 | `subscribe_ch_stock_real` | 订阅个股实时行情通道，采用增量发送模式，数据在交易时段实时推送。返回五档盘口、成… | — 暂未开放 |
| 个股数据 | 获取所有个股实时行情 | `get_ch_stock_real` | 随时获取全量A股实时行情数据，返回所有个股的最新价、涨跌幅、成交量、盘口、市值等… | ✅ 可测试 |
| 个股数据 | 获取单只个股实时行情 | `get_ch_one_stock_real` | 查询单只个股实时行情，返回数据中包含该股的Level2大单数据、竞价金额、成交量… | ✅ 可测试 |
| 个股数据 | 个股实时分钟K线 | `get_ch_stock_minute_real` | 获取个股当日实时分钟成交数据，支持1分钟、5分钟、15分钟、30分钟、60分钟周… | — 暂未开放 |
| 个股数据 | 个股实时逐笔成交 | `get_ch_stock_transaction_real` | 获取个股交易当天实时逐笔成交明细数据，包含时间、价格、成交量及买卖方向。该接口仅… | — 暂未开放 |
| 个股数据 | 前复权日线 | `get_ch_stock_front_day_history` | 获取指定个股前复权日线数据 | ✅ 可测试 |
| 个股数据 | 前复权周线 | `get_ch_stock_front_week_history` | 获取指定个股前复权周线数据 | — 暂未开放 |
| 个股数据 | 前复权月线 | `get_ch_stock_front_month_history` | 获取指定个股前复权月线数据 | — 暂未开放 |
| 个股数据 | 后复权日线 | `get_ch_stock_back_day_history` | 获取指定个股后复权日线数据 | — 暂未开放 |
| 个股数据 | 后复权周线 | `get_ch_stock_back_week_history` | 获取指定个股后复权周线数据 | — 暂未开放 |
| 个股数据 | 后复权月线 | `get_ch_stock_back_month_history` | 获取指定个股后复权月线数据 | — 暂未开放 |
| 个股数据 | 历史分笔 | `get_ch_stock_transaction_history` | 获取指定个股历史分笔个数。按照年份加月份进行查询 | — 暂未开放 |
| 个股数据 | 主力评分数据 | `get_ch_stock_primer_info` | 获取指定个股主力成本及相关评分数据 | — 暂未开放 |
| 个股数据 | 个股资金流 | `get_ch_stock_fund_flow` | 获取指定个股历史资金流，该数据每日盘后更新 | — 暂未开放 |
| 个股数据 | 人气排名数据 | `get_ch_stock_attention_tank` | 获取个股历史交易日内，在市场以及行业内人气排名数据 | — 暂未开放 |
| 个股数据 | 股东人数历史 | `get_ch_stock_share_holder` | 获取个股历史股东人数变化数据 | — 暂未开放 |
| 个股数据 | 大宗交易历史 | `get_ch_stock_block_trading` | 获取个股历史大宗交易数据 | — 暂未开放 |
| 个股数据 | 增减持历史 | `get_ch_stock_inc_or_dec` | 获取个股增减持历史数据 | — 暂未开放 |
| 个股数据 | 等比前复权日线 | `get_ch_stock_front_ratio_history` | 获取指定个股等比前复权日线数据 | — 暂未开放 |
| 个股数据 | 等比前复权周线 | `get_ch_stock_front_ratio_week_history` | 获取指定个股前复权周线数据 | — 暂未开放 |
| 个股数据 | 等比前复权月线 | `get_ch_stock_front_ratio_month_history` | 获取指定个股等比前复权月线数据 | — 暂未开放 |
| 个股数据 | 等比后复权日线 | `get_ch_stock_back_ratio_history` | 获取指定个股等比后复权日线数据 | — 暂未开放 |
| 个股数据 | 历史分钟数据 | `get_ch_stock_minute_history` | 获取指定个股历史分钟数据。按照年份加月份进行查询 | ✅ 可测试 |
| 个股数据 | 个股分时图 | `get_ch_stock_time_line` |  | — 暂未开放 |
| 个股数据 | 个股昨日分时图 | `get_ch_stock_time_line_yes` | 获取指定个股昨天的分时图数据 | — 暂未开放 |
| 个股数据 | 个股五日分时 | `get_ch_stock_five_days_time_line` | 获取指定个股五日分时数据 | — 暂未开放 |
| 个股数据 | 个股竞价分时数据 | `get_ch_stock_auction_time_line` | 获取指定个股当日竞价分时数据 | — 暂未开放 |
| 板块数据 | 获取概念板块列表 | `get_ch_concept` | 获取A股概念板块列表 | ✅ 可测试 |
| 板块数据 | 获取行业板块列表 | `get_ch_industry` | 获取A股概念板块列表 | ✅ 可测试 |
| 板块数据 | 订阅概念板块实时行情通道 | `subscribe_ch_concept_real` | 订阅概念板块实时行情通道，全量推送所有概念板块的实时数据，包括涨跌幅、成交量、成… | — 暂未开放 |
| 板块数据 | 获取概念板块实时行情 | `get_ch_concept_real` | 随时获取所有概念板块实时行情数据，包括板块涨跌幅、成交量、成分股涨跌统计等关键指… | ✅ 可测试 |
| 板块数据 | 订阅行业板块实时行情通道 | `subscribe_ch_industry_real` | 订阅行业板块实时行情通道，全量推送所有行业板块的实时数据，包括涨跌幅、成交量、成… | — 暂未开放 |
| 板块数据 | 获取行业板块实时行情 | `get_ch_industry_real` | 随时获取所有行业板块实时行情数据，包括板块涨跌幅、成交量、成分股涨跌统计等关键指… | ✅ 可测试 |
| 板块数据 | 概念板块日线 | `get_ch_concept_day_history` | 获取概念版块日线数据 | ✅ 可测试 |
| 板块数据 | 概念板块周线 | `get_ch_concept_week_history` | 获取概念板块周线数据 | — 暂未开放 |
| 板块数据 | 概念板块月线 | `get_ch_concept_month_history` | 获取概念板块月线数据 | — 暂未开放 |
| 板块数据 | 行业板块日线 | `get_ch_industry_day_history` | 获取行业版块日线数据 | ✅ 可测试 |
| 板块数据 | 行业板块周线 | `get_ch_industry_week_history` | 获取行业板块周线数据 | — 暂未开放 |
| 板块数据 | 行业板块月线 | `get_ch_industry_month_history` | 获取行业板块月线数据 | — 暂未开放 |
| 市场数据 | 获取融资融券余额 | `get_rzrq_balance` | 获取融资融券余额历史数据 | — 暂未开放 |
| 市场数据 | 上交所每日统计信息 | `get_sh_market_daily_info` | 获取上海证券交易所每日统计信息，包括上证A股，上证B股，科创板等。包含总成交量，… | — 暂未开放 |
| 市场数据 | 上交所每周统计信息 | `get_sh_market_week_info` | 获取上海证券交易所每周统计信息，包括上证A股，上证B股，科创板等。包含总成交量，… | — 暂未开放 |
| 市场数据 | 上交所每月统计信息 | `get_sh_market_month_info` | 获取上海证券交易所每月统计信息，包括上证A股，上证B股，科创板等。包含总成交量，… | — 暂未开放 |
| 市场数据 | 订阅指数实时行情通道 | `subscribe_ch_market_real` | 订阅指数实时行情通道，全量推送上证指数、深证成指、创业板指、科创综指、科创50、… | — 暂未开放 |
| 市场数据 | 获取指数实时行情 | `get_ch_market_real` | 随时获取六大指数（上证指数、深证成指、创业板指、科创综指、科创50、北证50）的… | ✅ 可测试 |
| 市场数据 | 涨跌停数量历史 | `get_ch_limit_up_down` | 获取交易日涨跌停数量历史数据 | ✅ 可测试 |
| 市场数据 | 指数日线 | `get_ch_market_day_history` | 获取指数日线数据，目前支持获取上证指数， 深证成指，创业板指，科创综指，科创50… | ✅ 可测试 |
| 市场数据 | 指数周线 | `get_ch_market_week_history` | 获取指定指数周线数据，目前支持获取上证指数， 深证成指，创业板指，科创综指，科创… | — 暂未开放 |
| 市场数据 | 指数月线 | `get_ch_market_month_history` | 获取指定指数月线数据，目前支持获取上证指数， 深证成指，创业板指，科创综指，科创… | — 暂未开放 |
| 市场数据 | 龙虎榜数据 | `get_lhb_data` | 获取指定日期龙虎榜数据 | ✅ 可测试 |
| 市场数据 | 市场资金流历史 | `get_ch_market_fund_flow` | 获取市场总体资金流历史数据 | ✅ 可测试 |
| 市场数据 | 全市场买卖对比 | `get_ch_all_market_bear_compare` | 全市场全天买一，卖一金额对比 | ✅ 可测试 |
| 市场数据 | 上证买卖对比 | `get_ch_sh_market_bear_compare` | 上海市场全天买一，卖一金额对比 | — 暂未开放 |
| 市场数据 | 深证买卖对比 | `get_ch_sz_market_bear_compare` | 深圳市场全天买一，卖一金额对比 | — 暂未开放 |
| 市场数据 | 创业板买卖对比 | `get_ch_cyb_market_bear_compare` | 创业板全天买一，卖一金额对比 | — 暂未开放 |
| 市场数据 | 科创板买卖对比 | `get_ch_kcb_market_bear_compare` | 科创板全天买一，卖一金额对比 | — 暂未开放 |
| 市场数据 | 北证买卖对比 | `get_ch_bj_market_bear_compare` | 北证全天买一，卖一金额对比 | — 暂未开放 |
| 市场数据 | 市场实时涨跌分布时序数据 | `get_ch_market_zd_map` | 获取市场实时涨跌分布时序数据 | — 暂未开放 |
| 市场数据 | 市场实时涨跌停数量 | `get_ch_today_limit_up_down` | 获取实时个股涨跌停数量时序数据，包含涨停，跌停，非一字板涨停，炸板数量 | — 暂未开放 |
| 市场数据 | 市场实时涨停股列表 | `get_ch_today_lb_stock` | 获取实时涨停股列表，包含连板高度，连板晋级率等信息 | — 暂未开放 |
| 市场数据 | 市场全天实时成交额 | `get_ch_market_amount_curve` | 实时获取市场全天成交额实时数据，包含当天，昨天全天成交额数据 | — 暂未开放 |
| 财务数据 | 利润表 | `get_ch_stock_income_statement` | 获取指定个股利润表历史数据 | — 暂未开放 |
| 财务数据 | 现金流表 | `get_ch_stock_cash_flow_statement` | 获取指定个股现金流表历史数据 | — 暂未开放 |
| 财务数据 | 财务主表 | `get_ch_stock_financial_indicators` | 获取指定个股财务主表历史数据 | — 暂未开放 |
| 财务数据 | 资产负债表 | `get_ch_stock_balance_sheet` | 获取指定个股资产负债表历史数据 | — 暂未开放 |
| 财务数据 | 财务辅助表 | `get_ch_stock_auxiliary_data` | 获取指定个股资历史财务信息辅助表 | — 暂未开放 |
| 财务数据 | 股东表 | `get_ch_stock_share_capital_and_shareholders` | 获取指定个股历史股本股东表 | — 暂未开放 |
| 财务数据 | 业绩预告 | `get_ch_stock_net_profit` | 获取全市场个股预告，预盈预亏信息 | — 暂未开放 |
| 财务数据 | 财务核心指标(数据源SI) | `get_ch_si_stock_fin_key_indicators` | 从SI数据源获取个股财务核心指标（含盈利能力、成长能力、财务风险、营运能力等88… | — 暂未开放 |
| 财务数据 | 利润表(数据源SI) | `get_ch_si_stock_fin_income_statements` | 从SI数据源获取个股利润表全量历史数据，含营业总收入、营业总成本、各项费用、利润… | — 暂未开放 |
| 财务数据 | 资产负债表(数据源SI) | `get_ch_si_stock_fin_balance_sheet` | 从SI数据源获取个股资产负债表全量历史数据，含流动资产、非流动资产、流动负债、非… | — 暂未开放 |
| 财务数据 | 现金流表(数据源SI) | `get_ch_si_stock_fin_cash_flow` | 从SI数据源获取个股现金流量表全量历史数据，含经营活动、投资活动、筹资活动三大现… | — 暂未开放 |
| 财务数据 | 个股财务核心指标(数据源Ea) | `get_ch_ea_stock_fin_key_indicators` | 获取指定个股财务核心指标数据（数据源Ea），包含每股指标、盈利能力、增长能力、偿… | — 暂未开放 |
| 财务数据 | 个股资产负债表(数据源Ea) | `get_ch_ea_stock_fin_balance_sheet` | 获取指定个股资产负债表数据（数据源Ea），包含总资产、固定资产、货币资金、应收账… | — 暂未开放 |
| 财务数据 | 个股利润表(数据源Ea) | `get_ch_ea_stock_fin_income_statements` | 获取指定个股利润表数据（数据源Ea），包含营业总收入、营业总成本、销售费用、管理… | — 暂未开放 |
| 财务数据 | 个股现金流量表(数据源Ea) | `get_ch_ea_stock_fin_cash_flow` | 获取指定个股现金流量表数据（数据源Ea），包含经营活动、投资活动、筹资活动现金流… | — 暂未开放 |
| 可转债 | 订阅可转债实时行情通道 | `subscribe_ch_kzz_stock_real` | 订阅可转债实时行情通道，采用增量发送模式，数据包含五档盘口、Level2成交数据… | — 暂未开放 |
| 可转债 | 获取可转债实时行情 | `get_ch_kzz_cur_real` | 随时获取可转债全量实时行情数据，包括五档盘口、Level2资金流向、主力净买额、… | — 暂未开放 |
| 可转债 | 获取可转债列表 | `get_ch_kzz_stock` | 获取所有可转债的基本信息列表，包括代码、名称、正股、转股价、溢价率、到期日等核心… | — 暂未开放 |

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