"""本地 MCP Server（stdio），暴露 pandaData 全部 22 个请求接口。"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP
from panda_stock import PandaStock

mcp = FastMCP("pandaData")

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
    """获取 A股 实时行情快照（ChStockCurReal）。"""
    return _json(_ps.get_ch_stock_real())


@mcp.tool()
def ChMarketCurReal() -> str:
    """获取 A股 指数实时快照（ChMarketCurReal）。"""
    return _json(_ps.get_ch_market_real())


@mcp.tool()
def ChConceptCurReal() -> str:
    """获取概念板块实时快照（ChConceptCurReal）。"""
    return _json(_ps.get_ch_concept_real())


@mcp.tool()
def ChIndustryCurReal() -> str:
    """获取行业板块实时快照（ChIndustryCurReal）。"""
    return _json(_ps.get_ch_industry_real())


# ========== 列表 ==========
@mcp.tool()
def chStockList() -> str:
    """获取 A股 股票列表。"""
    return _json(_ps.get_ch_stock())


@mcp.tool()
def chConceptList() -> str:
    """获取概念板块列表。"""
    return _json(_ps.get_ch_concept())


@mcp.tool()
def chIndustryList() -> str:
    """获取行业板块列表。"""
    return _json(_ps.get_ch_industry())


# ========== 单只实时 ==========
@mcp.tool()
def ChOneStockReal(code: str) -> str:
    """获取单只股票实时行情。code: 如 600519"""
    return _json(_ps.get_ch_one_stock_real(code))


# ========== 历史 ==========
@mcp.tool()
def chStockFrontDayHistory(code: str) -> str:
    """获取个股前复权日线历史。code: 如 600519"""
    return _json(_ps.get_ch_stock_front_day_history(code))


@mcp.tool()
def chConceptDayHistory(code: str) -> str:
    """获取概念板块日线历史。code: 如 300502"""
    return _json(_ps.get_ch_concept_day_history(code))


@mcp.tool()
def chIndustryDayHistory(code: str) -> str:
    """获取行业板块日线历史。code: 如 300502"""
    return _json(_ps.get_ch_industry_day_history(code))


@mcp.tool()
def chStockMinuteHistory(code: str, minute: int, date: str) -> str:
    """获取个股分钟历史。code: 如 600519；minute: 分钟周期(1/5/15/30/60)；date: 如 20260818"""
    return _json(_ps.get_ch_stock_minute_history(code, minute, date))


@mcp.tool()
def ChMarketDayHistory(code: str) -> str:
    """获取指数日线历史。code: 如 000001"""
    return _json(_ps.get_ch_market_day_history(code))


# ========== 资讯 ==========
@mcp.tool()
def ChCoreNews(date: str) -> str:
    """获取核心资讯。date: 如 20260818"""
    return _json(_ps.get_core_new(date))


@mcp.tool()
def ChDomesticNews(date: str) -> str:
    """获取国内财经要闻。date: 如 20260818"""
    return _json(_ps.get_domestic_financial_news(date))


@mcp.tool()
def ChGlobalNews(date: str) -> str:
    """获取全球财经要闻。date: 如 20260818"""
    return _json(_ps.get_global_financial_news(date))


@mcp.tool()
def ChOptionNews(date: str) -> str:
    """获取期权资讯。date: 如 20260818"""
    return _json(_ps.get_options_news(date))


# ========== 市场 ==========
@mcp.tool()
def ChLimitUpDown() -> str:
    """获取今日涨跌停统计。"""
    return _json(_ps.get_ch_limit_up_down())


@mcp.tool()
def ChLhbData(date: str) -> str:
    """获取龙虎榜数据。date: 如 20260818"""
    return _json(_ps.get_lhb_data(date))


@mcp.tool()
def ChMarketFundFlow() -> str:
    """获取市场资金流向。"""
    return _json(_ps.get_ch_market_fund_flow())


@mcp.tool()
def chAllMarketBearCompare() -> str:
    """获取全市场多空对比。"""
    return _json(_ps.get_ch_all_market_bear_compare())


# ========== DDX ==========
@mcp.tool()
def chDdxStockData(code: str) -> str:
    """获取个股 DDX 数据。code: 如 600519"""
    return _json(_ps.get_ch_stock_ddx_data(code))


if __name__ == "__main__":
    mcp.run()
