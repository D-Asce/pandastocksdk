"""pandaData 可用接口示例（22 个请求/响应接口）。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from panda_stock import PandaStock

# 替换为你申请到的 phone / nid（见 README"免费试用"）
PHONE = "your_phone"
NID = "your_nid"

ps = PandaStock(phone=PHONE, nid=NID)
ps.connect_server()

# ========== 实时快照（CurReal）==========
print("=== ChStockCurReal ===")
print(ps.get_ch_stock_real())

print("=== ChMarketCurReal ===")
print(ps.get_ch_market_real())

print("=== ChConceptCurReal ===")
print(ps.get_ch_concept_real())

print("=== ChIndustryCurReal ===")
print(ps.get_ch_industry_real())

# ========== 列表 ==========
print("=== chStockList ===")
print(ps.get_ch_stock())

print("=== chConceptList ===")
print(ps.get_ch_concept())

print("=== chIndustryList ===")
print(ps.get_ch_industry())

# ========== 单只实时 ==========
print("=== ChOneStockReal (600519) ===")
print(ps.get_ch_one_stock_real("600519"))

# ========== 历史 ==========
print("=== chStockFrontDayHistory (600519) ===")
print(ps.get_ch_stock_front_day_history("600519"))

print("=== chConceptDayHistory (300502) ===")
print(ps.get_ch_concept_day_history("300502"))

print("=== chIndustryDayHistory (300502) ===")
print(ps.get_ch_industry_day_history("300502"))

print("=== chStockMinuteHistory (600519, 5, 20260818) ===")
print(ps.get_ch_stock_minute_history("600519", 5, "20260818"))

print("=== ChMarketDayHistory (000001) ===")
print(ps.get_ch_market_day_history("000001"))

# ========== 资讯 ==========
print("=== ChCoreNews ===")
print(ps.get_core_new("20260818"))

print("=== ChDomesticNews ===")
print(ps.get_domestic_financial_news("20260818"))

print("=== ChGlobalNews ===")
print(ps.get_global_financial_news("20260818"))

print("=== ChOptionNews ===")
print(ps.get_options_news("20260818"))

# ========== 市场 ==========
print("=== ChLimitUpDown ===")
print(ps.get_ch_limit_up_down())

print("=== ChLhbData ===")
print(ps.get_lhb_data("20260818"))

print("=== ChMarketFundFlow ===")
print(ps.get_ch_market_fund_flow())

print("=== chAllMarketBearCompare ===")
print(ps.get_ch_all_market_bear_compare())

# ========== DDX ==========
print("=== chDdxStockData (600519) ===")
print(ps.get_ch_stock_ddx_data("600519"))
