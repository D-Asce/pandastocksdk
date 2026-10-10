# Building an MCP Server for A-share Realtime Data: NATS Push vs REST Polling

*Written for the MCP and quantitative-finance communities.*

---

## The problem

If you've ever tried to build an AI agent that answers questions about Chinese
A-share stocks, you've hit the same wall:

- "What's Kweichow Moutai's price today?"
- "Show me the last 20 trading days of 000001"
- "Which stocks had the biggest net inflow this week?"

The data exists — Tushare, Akshare, Baostock all provide it. But getting it
into an agent means writing a tool for every query, remembering field names,
and wiring each one up by hand. That's maintenance burden, not engineering.

**MCP (Model Context Protocol) changes the equation**: the agent discovers
tools, infers arguments from natural language, and calls them itself. Your
job stops being "write data-access code" and starts being "define what data
exists."

---

## Why A-share data is a bad fit for REST polling

Most stock-data APIs are REST: you ask, you get an answer, you hang up. That
works fine for end-of-day batch jobs. It breaks down for anything that needs
to be *now*:

| Need | REST reality |
|---|---|
| Realtime quote | Poll every N seconds; you're always slightly behind |
| Level-2 order book | 10 levels × 4000 symbols — polling is wasteful and slow |
| DDX big-order tracking | You miss the burst between polls |
| Intraday momentum | Latency accumulates across the chain |

The A-share market has a real-time push infrastructure. PandaStock exposes it
over **NATS request/response + publish/subscribe** instead of REST polling:

- **Request/response** for point queries (one stock, one answer) — 176 server-side endpoints, 22 open
- **Publish/subscribe** for streaming snapshots (whole-market realtime, Level-2, DDX) — pushed to subscribers, not pulled

The practical difference: a REST client asks "what's the price now?" and gets a
slightly stale number. A NATS subscriber *is told* when the price changes.

---

## What the server exposes

PandaStock MCP ships 22 open tools across five groups:

| Group | Tools | Covers |
|---|---|---|
| Realtime | `ChOneStockReal`, `ChStockCurReal`, `ChMarketCurReal`, `ChConceptCurReal`, `ChIndustryCurReal` | single stock, whole market, sectors |
| Lists | `chStockList`, `chConceptList`, `chIndustryList` | code/name directories |
| History | `chStockFrontDayHistory`, `chStockMinuteHistory`, `ChMarketDayHistory` | daily + minute K-lines |
| News | `ChCoreNews`, `ChDomesticNews`, `ChGlobalNews`, `ChOptionNews` | market news |
| Market | `ChLimitUpDown`, `ChLhbData`, `ChMarketFundFlow`, `chAllMarketBearCompare`, `chDdxStockData` | limit-ups, dragon-tiger list, fund flow, DDX |

---

## A realistic agent workflow

> *"Compare Kweichow Moutai's 20-day performance against the CSI 300, and
> flag any days with unusual volume."*

A REST-based agent needs: 3 hand-written tools (Moutai bars, index bars,
volume statistics) + orchestration logic. With MCP:

1. Agent calls `chStockFrontDayHistory("600519")` → daily bars
2. Agent calls `ChMarketDayHistory("000300")` → index bars
3. Agent computes relative performance + volume z-score locally
4. Returns the comparison

The data-access layer is declarative. The agent handles the analysis. That's
the whole point of the protocol.

---

## Free, no registration

A common friction point for demos is credentials. PandaStock ships with a
public test account (`phone=pandastock`, `nid=pandastock`) — no signup, no
token, no quota application. Rate-limited by source IP, which is fine for
demos and tutorials.

```bash
pip install pandastock-mcp
```

Configure in any MCP client (Cursor, Claude Desktop, Cline, Trae, Zed):

```json
{
  "mcpServers": {
    "panda-stock": {
      "command": "pandastock-mcp",
      "env": { "PANDA_PHONE": "pandastock", "PANDA_NID": "pandastock" }
    }
  }
}
```

---

## Where it fits in the ecosystem

PandaStock isn't trying to replace Tushare or Akshare — those are excellent
data-collection layers. The distinction:

- **Tushare / Akshare** = the data source (historical, fundamentals, T+1)
- **PandaStock MCP** = the tool layer (realtime, agent-discoverable, L2/DDX)

A practical stack for A-share agent work: Akshare for offline research,
PandaStock MCP for realtime + agent interaction.

---

## Try it

- Repo: <https://github.com/D-Asce/pandastocksdk>
- Install: `pip install pandastock-mcp`
- Interface catalog: `INTERFACES.md` (176 server-side endpoints, 22 open)
- Test account: `phone=pandastock` / `nid=pandastock`

The 22 open endpoints don't cover everything yet — your use case is the
best signal for what to expose next.

---

*PandaStock is a pandaData open-source implementation. NATS-pushed quotes,
Level-2, DDX big orders, money flow and AI stock screening for A-share data.*