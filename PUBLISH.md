# 上架与推广清单（P0）

> 诊断结论：产品层已完备（MCP server / PyPI / Pages / SKILL.md），但**发现层为空** —— 官方 MCP 注册表、Smithery、mcp.so 均未收录，GitHub topics 为空。
> 本文件是可直接执行的上架步骤。所有命令在仓库根目录执行。

**核查时间：2026-09-26**，当时状态：

| 渠道 | 状态 | 证据 |
|---|---|---|
| 官方 MCP Registry | ❌ 未收录 | `GET /v0/servers?search=D-Asce` → `count:0` |
| Smithery | ❌ 未收录 | `GET /registry.smithery.ai/servers/D-Asce/pandastocksdk` → 404 |
| mcp.so | ❌ 未收录 | `/server/pandastock-mcp` → 404 |
| GitHub topics | ❌ 空 | `topics: []` |
| PyPI project_urls | ❌ 占位符 | 三条全指 `github.com/example/pandastock-mcp` |
| PyPI 描述 | ❌ 陈旧 | 1547 字符，写「166」，仓库写「176」 |

---

## 0. 前置：提交本次修复

```powershell
cd D:\code\net\pandastocksdk
git add README.md pyproject.toml mcp/server.py
git commit -m "fix: repair PyPI project_urls, align versions, rebuild README first screen"
git push origin main
```

---

## 1. GitHub topics（2 分钟，杠杆最高）

`gh` 未安装，用 API + PAT 即可：

```powershell
$env:GH_TOKEN = "<你的 PAT，需 repo 权限>"
$headers = @{ Authorization = "token $env:GH_TOKEN"; Accept = "application/vnd.github+json" }
$body = @{
  names = @(
    "mcp","model-context-protocol","mcp-server",
    "a-share","china-stock","stock-data","market-data",
    "quantitative-finance","algorithmic-trading","trading",
    "nats","python","llm","ai-trading","realtime-data"
  )
} | ConvertTo-Json
Invoke-RestMethod -Method Put -Uri "https://api.github.com/repos/D-Asce/pandastocksdk/topics" `
  -Headers $headers -Body $body -ContentType "application/json"
```

验证：`https://api.github.com/repos/D-Asce/pandastocksdk/topics` 应返回非空 `names`。

---

## 2. 官方 MCP Registry（最重要）

`server.json` 已就绪（schema `2025-12-11`，name `io.github.D-Asce/pandastocksdk`）。
官方 CLI 为 `mcp-publisher`，支持 GitHub OIDC 免 token 发布。

### 2a. 本地手动发布

```powershell
# 安装 mcp-publisher（Rust 二进制，或从 https://github.com/modelcontextprotocol/registry/releases 下载）
mcp-publisher login github
mcp-publisher publish server.json
```

### 2b. CI 自动发布（推荐，随版本自动更新）

`.github/workflows/mcp-registry.yml`：

```yaml
name: Publish to MCP Registry
on:
  release:
    types: [published]
  push:
    branches: [main]
    paths: [server.json]

permissions:
  id-token: write
  contents: read

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install mcp-publisher
        run: |
          curl -sSL https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher-linux-x64 \
            -o mcp-publisher && chmod +x mcp-publisher && sudo mv mcp-publisher /usr/local/bin/
      - name: Publish
        run: mcp-publisher publish server.json
```

> 注：`id-token: write` 是 GitHub OIDC 关键，**不需要 PAT**。
> 若 CI 失败提示需先 `login github --experimental`，改用本地 2a 手动发布一次即可。

验证：
```powershell
Invoke-RestMethod "https://registry.modelcontextprotocol.io/v0/servers?search=D-Asce"
# 期望返回 servers 数组非空
```

---

## 3. Smithery

Smithery 支持从 GitHub 仓库自动索引：

1. 打开 https://smithery.ai/account
2. **Add Server** → 选 GitHub → 授权 → 选 `D-Asce/pandastocksdk`
3. 它会读取 `server.json` / `pyproject.toml` 自动生成配置

或直接访问（部分情况下自动抓取）：
`https://smithery.ai/server/D-Asce/pandastocksdk`

验证：`https://registry.smithery.ai/servers/D-Asce/pandastocksdk` 返回 200。

---

## 4. mcp.so / Glama / 中文 MCP 广场

| 渠道 | 提交入口 | 需要内容 |
|---|---|---|
| mcp.so | https://mcp.so/add | repo URL + `pip install pandastock-mcp` + 工具列表 |
| Glama | https://glama.ai/mcp 中的 Submit | 仓库已有 `glama.json`，填 repo URL 即可 |
| SeekTool.ai | 已收录（README 原有链接） | 更新描述为「176 个接口，22 个免注册可试」 |
| ToolPilot.ai | 已收录 | 同上 |
| 中文广场：DataWhale MCP 列表 / 魔搭 ModelScope MCP / 阿里云百炼 | 各自 GitHub issue 或表单 | 中文描述 + 免注册测试账号是加分项 |

提交描述统一口径（**不要再出现 166**）：

> pandaData：A 股实时数据 MCP Server。NATS 推送行情 / Level2 / DDX 大单 / 资金流 / AI 选股。服务端 176 个接口，22 个开放接口，**提供免注册公共测试账号**，`pip install pandastock-mcp` 即用。

---

## 5. PyPI 重新发布（修死链 + 陈旧描述）

`project.urls` 已修复，但**必须重新发版**才会生效（PyPI 元数据不可原地改）。

```powershell
cd D:\code\net\pandastocksdk
py -m pip install --upgrade build twine
py -m build
py -m twine upload dist/*
```

发版前检查：
- [ ] `pyproject.toml` version 与 `server.json` version 一致（当前均为 `1.5.5`）
- [ ] `mcp/server.py` 内 `version="1.5.5"`（当前已改）
- [ ] `py -m build` 成功，`twine check dist/*` 通过
- [ ] README 用的是新首屏（`readme = "README.md"` 会直接带上去）

验证：
```powershell
(Invoke-RestMethod "https://pypi.org/pypi/pandastock-mcp/json").info.project_urls
# 期望 Homepage/Repository/Documentation 指向 github.com/D-Asce/pandastocksdk
```

---

## 6. 遗留问题（未在 P0 处理）

- **依赖声明冲突**：PyPI 现网 1.5.4 声明 `mcp<2,>=1.0.0`，仓库已改为 `mcp>=2.0`。1.5.5 发版后自动覆盖，但**升级用户会装上 mcp 2.x**，需确认 `mcp.server.mcpserver.MCPServer` 在目标环境可用。
- **LICENSE 检测**：文件内容是标准 MIT，但 GitHub API license 字段返回 `Other/NOASSERTION`（可能因版权行 `Copyright (c) 2026 pandaData` 与常规格式差异）。目录收录时会显示 "Other"，建议确认。
- **无 tests / CI**：仓库有 dev extra 却无 `tests/` 目录，仅 `mirror.yml` 一个 workflow。P1 处理。
- **远程 HTTP MCP endpoint**：当前仅 stdio，用户必须本地装 Python。P2 最大架构机会。

---

## 7. 完成判据

全部达成即 P0 结束：

- [ ] `GET registry.modelcontextprotocol.io/v0/servers?search=D-Asce` → 非空
- [ ] `registry.smithery.ai/servers/D-Asce/pandastocksdk` → 200
- [ ] `api.github.com/repos/D-Asce/pandastocksdk/topics` → 非空
- [ ] PyPI `project_urls` 无 `github.com/example`
- [ ] PyPI description 无 `166`，README 首屏第一行是产品 + badge，无第三方广告
