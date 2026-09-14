"""pandaData MCP Server（stdio）

基于 mcp 2.x（MCPServer）重写的本地 MCP Server，暴露 pandaData 全部 22 个
请求/响应接口。兼容 Python 3.9+，与 mcp>=2.0、nats-py==2.14.0 搭配使用。

English: local stdio MCP server exposing 22 pandaData A-share market data
request/response interfaces (quotes, klines, news, fund flow, DDX...).
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.mcpserver import MCPServer
from panda_stock import PandaStock

# 服务端程序集标识（name 会出现在 tools/list 的 serverInfo 中）
mcp = MCPServer(
    "pandaData",
    version="1.5.4",
    description="pandaData: A-share (Chinese stock market) realtime quotes, "
    "K-line history, sector data, financial news, fund flow and DDX via "
    "NATS request/response.",
)

_ps = PandaStock(
    phone=os.getenv("PANDA_PHONE", ""),
    nid=os.getenv("PANDA_NID", ""),
)
if _ps.phone and _ps.nid:
    _ps.connect_server()


def _json(data) -> str:
    return json.dumps(data, ensure_ascii=False, default=str)


# ========== 实时快照（CurReal）==========
@mcp.tool()
def ChStockCurReal() -> str:
    """获取A股实时行情快照。Get realtime snapshot of ALL A-share stocks. No arguments."""
    return _json(_ps.get_ch_stock_real())


@mcp.tool()
def ChMarketCurReal() -> str:
    """获取A股指数实时快照。Get realtime snapshot of A-share market indices (SH/SZ/BJ). No arguments."""
    return _json(_ps.get_ch_market_real())


@mcp.tool()
def ChConceptCurReal() -> str:
    """获取概念板块实时快照。Get realtime snapshot of concept sectors. No arguments."""
    return _json(_ps.get_ch_concept_real())


@mcp.tool()
def ChIndustryCurReal() -> str:
    """获取行业板块实时快照。Get realtime snapshot of industry sectors. No arguments."""
    return _json(_ps.get_ch_industry_real())


# ========== 列表 ==========
@mcp.tool()
def chStockList() -> str:
    """获取A股股票列表。Get the list of all A-share stocks (code/name). No arguments."""
    return _json(_ps.get_ch_stock())


@mcp.tool()
def chConceptList() -> str:
    """获取概念板块列表。Get list of concept sectors. No arguments."""
    return _json(_ps.get_ch_concept())


@mcp.tool()
def chIndustryList() -> str:
    """获取行业板块列表。Get list of industry sectors. No arguments."""
    return _json(_ps.get_ch_industry())


# ========== 单只实时 ==========
@mcp.tool()
def ChOneStockReal(code: str) -> str:
    """获取单只股票实时行情。Get realtime quote for ONE stock. Args: code (str): 6-digit ticker, e.g. "600519" (贵州茅台 / Kweichow Moutai)."""
    return _json(_ps.get_ch_one_stock_real(code))


# ========== 历史 ==========
@mcp.tool()
def chStockFrontDayHistory(code: str) -> str:
    """获取个股前复权日线历史。Get forward-adjusted daily K-line history for one stock. Args: code (str): ticker like "600519"."""
    return _json(_ps.get_ch_stock_front_day_history(code))


@mcp.tool()
def chConceptDayHistory(code: str) -> str:
    """获取概念板块日线历史。Get daily K-line history for a concept sector. Args: code (str): sector code like "300502"."""
    return _json(_ps.get_ch_concept_day_history(code))


@mcp.tool()
def chIndustryDayHistory(code: str) -> str:
    """获取行业板块日线历史。Get daily K-line history for an industry sector. Args: code (str): sector code like "300502"."""
    return _json(_ps.get_ch_industry_day_history(code))


@mcp.tool()
def chStockMinuteHistory(code: str, minute: int, date: str) -> str:
    """获取个股分钟历史。Get minute-level K-line history for one stock. Args: code (str): ticker like "600519"; minute (int): 1/5/15/30/60; date (str): YYYYMMDD like "20260818"."""
    return _json(_ps.get_ch_stock_minute_history(code, minute, date))


@mcp.tool()
def ChMarketDayHistory(code: str) -> str:
    """获取指数日线历史。Get daily K-line history for an index. Args: code (str): index code like "000001" (上证指数)."""
    return _json(_ps.get_ch_market_day_history(code))


# ========== 资讯 ==========
@mcp.tool()
def ChCoreNews(date: str) -> str:
    """获取核心资讯。Get core market news. Args: date (str): YYYYMMDD like "20260818"."""
    return _json(_ps.get_core_new(date))


@mcp.tool()
def ChDomesticNews(date: str) -> str:
    """获取国内财经要闻。Get domestic (China) financial news. Args: date (str): YYYYMMDD."""
    return _json(_ps.get_domestic_financial_news(date))


@mcp.tool()
def ChGlobalNews(date: str) -> str:
    """获取全球财经要闻。Get global financial news. Args: date (str): YYYYMMDD."""
    return _json(_ps.get_global_financial_news(date))


@mcp.tool()
def ChOptionNews(date: str) -> str:
    """获取期权资讯。Get options-related news. Args: date (str): YYYYMMDD."""
    return _json(_ps.get_options_news(date))


# ========== 市场 ==========
@mcp.tool()
def ChLimitUpDown() -> str:
    """获取今日涨跌停统计。Get today's limit-up/limit-down statistics. No arguments."""
    return _json(_ps.get_ch_limit_up_down())


@mcp.tool()
def ChLhbData(date: str) -> str:
    """获取龙虎榜数据。Get Dragon-Tiger list (top traded stocks) data. Args: date (str): YYYYMMDD."""
    return _json(_ps.get_lhb_data(date))


@mcp.tool()
def ChMarketFundFlow() -> str:
    """获取市场资金流向。Get whole-market capital flow. No arguments."""
    return _json(_ps.get_ch_market_fund_flow())


@mcp.tool()
def chAllMarketBearCompare() -> str:
    """获取全市场多空对比。Get bull/bear (long/short) comparison of the whole market. No arguments."""
    return _json(_ps.get_ch_all_market_bear_compare())


# ========== DDX ==========
@mcp.tool()
def chDdxStockData(code: str) -> str:
    """获取个股DDX数据。Get DDX (large order tracking) data for one stock. Args: code (str): ticker like "600519"."""
    return _json(_ps.get_ch_stock_ddx_data(code))


def main() -> None:
    """Console entry point: run the stdio MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()