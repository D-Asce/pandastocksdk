# 上架与推广清单（P0）

> 诊断结论：产品层已完备（MCP server / PyPI / Pages / SKILL.md），但**发现层为空** —— 官方 MCP 注册表、Smithery、mcp.so 均未收录，GitHub topics 为空。
> 本文件是可直接执行的上架步骤。所有命令在仓库根目录执行。

**核查时间：2026-09-26**，当时状态：

| 渠道 | 状态 | 证据 |
|---|---|---|
| 官方 MCP Registry | ❌ 未收录 | `GET /v0/servers?search=D-Asce` → `count:0` |
| Smithery | ❌ 未收录 | `GET /registry.smithery.ai/servers/D-Asce/pandastocksdk` → 404 |
| mcp.so | ❌ 未收录 | `/server/pandastock-mcp` → 404 |
| GitHub topics | ❌ 空 | `topics: []`（PUT → 403，PAT 权限不足） |
| CI workflow | ❌ 未入库 | `publish-mcp.yml` 本地就绪，push 被拒：PAT 缺 `workflow` scope |
| PyPI project_urls | ❌ 占位符 | 三条全指 `github.com/example/pandastock-mcp` |
| PyPI 描述 | ❌ 陈旧 | 1547 字符，写「166」，仓库写「176」 |

---

## 0. 前置：提交本次修复 ✅ 已完成

已推送：`1fe9a44`（project_urls/版本）→ `c780574`（README 首屏）→ `92ad425` + `015eab0`（本文件）。
以下命令仅供追溯：

```powershell
cd D:\code\net\pandastocksdk
git add README.md pyproject.toml mcp/server.py
git commit -m "fix: repair PyPI project_urls, align versions, rebuild README first screen"
git push origin main
```

---

## 1. GitHub topics（2 分钟，杠杆最高）

> **2026-09-26 实测**：仓库已存的 git 凭据是 fine-grained PAT，PUT topics 返回
> `403 Resource not accessible by personal access token`（缺 Administration: write）。
> 两条路选一：
>
> a) 网页最快：https://github.com/D-Asce/pandastocksdk/edit → 填 topics
> b) 换一个带 **Administration → Contents/Administration write** 的 PAT 再跑下面的命令

```powershell
$env:GH_TOKEN = "<你的 PAT，需 repository Administration: write>"
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

> **2026-09-26 实测**：`mcp-publisher validate` 对线上注册表 schema 已通过（`✅ server.json is valid`）。
> 注册表对 PyPI 包的**所有权校验 = 读 PyPI README 里的 `mcp-name: io.github.D-Asce/pandastocksdk` 标记**。
> 现网 1.5.4 的 PyPI description **没有这个标记**（旧 README），1.5.5 分发包已确认带标记。
> ⇒ **必须先完成第 5 节 PyPI 发版，Registry 才能发布成功。**

### 2a. 本地手动发布

```powershell
# 下载 CLI（Windows amd64，v1.8.1 实测可用）
$url = "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_windows_amd64.tar.gz"
Invoke-WebRequest -Uri $url -OutFile mcp-publisher.tar.gz
tar xf mcp-publisher.tar.gz mcp-publisher.exe

# 设备码登录：终端会打印 https://github.com/login/device + 一次性 code，需你浏览器授权
.\mcp-publisher.exe login github
.\mcp-publisher.exe validate
.\mcp-publisher.exe publish
```

### 2b. CI 自动发布（推荐；workflow 文件**尚未入库**）

**本地已就绪：`.github/workflows/publish-mcp.yml`（75 行，YAML 已校验），但 push 被拒**：

> **2026-09-26 实测**：`git push` 返回
> `refusing to allow a Personal Access Token to create or update workflow .github/workflows/publish-mcp.yml without workflow scope`；
> Contents API PUT 同样 `403 Resource not accessible by personal access token`。
> 仓库现有凭据是 fine-grained PAT 且未授予 **Workflows: Write**。二选一：
>
> a) **网页最快**：https://github.com/D-Asce/pandastocksdk/new/main → 文件名粘贴
>    `.github/workflows/publish-mcp.yml` → 把本地同名文件内容粘进去 → Commit
> b) **改 PAT**：Settings → Developer settings → Fine-grained tokens → 该 token →
>    Repository permissions → **Workflows: Read and write** → 保存后在仓库根目录：
>    `git add .github/workflows/publish-mcp.yml && git commit -m "ci: add MCP Registry publish workflow (OIDC auth + PyPI preflight)" && git push origin main`

要点：

- 触发：`push` tag `v*` + `workflow_dispatch` 手动
- 认证：`mcp-publisher login github-oidc`，`permissions: id-token: write` —— **不需要任何 secret**
- **preflight 步骤**：发布前自动检查 PyPI 上该版本存在且 README 含 `mcp-name` 标记，
  不满足则带明确报错失败（防止出现「发了但没生效」的静默错误）
- `validate` 步骤再对线上 schema 校验一次才 publish

⚠️ 曾经的草稿有两处错，已修正：
1. 下载 URL 写成 `mcp-publisher-linux-x64` —— **该文件不存在**，实际是 `mcp-publisher_linux_amd64.tar.gz`
2. 漏了认证步骤 —— 必须先 `login github-oidc` 再 `publish`

使用（PyPI 发版之后）：

```powershell
git tag v1.5.5
git push origin v1.5.5
# 或 GitHub 页 → Actions → Publish to MCP Registry → Run workflow
```

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
| SeekTool.ai | 已收录（README 反链已移除，待定是否恢复） | 更新描述为「176 个接口，22 个免注册可试」 |
| ToolPilot.ai | 同上 | 同上 |
| 中文广场：DataWhale MCP 列表 / 魔搭 ModelScope MCP / 阿里云百炼 | 各自 GitHub issue 或表单 | 中文描述 + 免注册测试账号是加分项 |

提交描述统一口径（**不要再出现 166**）：

> pandaData：A 股实时数据 MCP Server。NATS 推送行情 / Level2 / DDX 大单 / 资金流 / AI 选股。服务端 176 个接口，22 个开放接口，**提供免注册公共测试账号**，`pip install pandastock-mcp` 即用。

---

## 5. PyPI 重新发布（修死链 + 陈旧描述）—— 当前唯一硬阻塞

`project.urls` 已修复，但**必须重新发版**才会生效（PyPI 元数据不可原地改）。
且第 2 节 Registry 发布依赖本次发版产出的 `mcp-name` 标记 ⇒ **先做本节，再做第 2 节**。

> **2026-09-26 已完成的验证**（产物在 `D:\code\net\pandastocksdk\dist\`）：
> - `python -m build` ✅ → `pandastock_mcp-1.5.5.tar.gz` + `pandastock_mcp-1.5.5-py3-none-any.whl`
> - `twine check dist/*` ✅ 两包均 PASSED
> - wheel METADATA ✅ 4 条 `Project-URL` 全指真实仓库，无 `github.com/example`，
>   `Requires-Dist: mcp>=2.0` + `nats-py==2.14.0`
> - sdist README ✅ 含 `<!-- mcp-name: io.github.D-Asce/pandastocksdk -->`
>
> **本机无 PyPI 凭证**：无 `.pypirc`、WinVault keyring 无 twine/pypi 条目、无 `PYPI_*` 环境变量
> （1.5.4 应是在别的环境/交互输入上传的）。所以**上传这一步必须你来**：

```powershell
cd D:\code\net\pandastocksdk
# 用 PyPI API token（pypi.org → Account settings → API tokens），用户名固定 __token__
py -m twine upload dist/*
# 提示 Username: __token__   Password: pypi-AgEIcHlwaS5vcmc...
```

发版前检查（全部 ✅ 已完成）：
- [x] `pyproject.toml` version 与 `server.json` version 一致（均为 `1.5.5`）
- [x] `mcp/server.py` 内 `version="1.5.5"`
- [x] `py -m build` 成功，`twine check dist/*` 通过
- [x] README 新首屏（`readme = "README.md"` 直接带上）
- [x] `mcp-name` 标记进分发包
- [ ] **`twine upload dist/*`（需要你的 token，本机无法代做）**

验证：
```powershell
(Invoke-RestMethod "https://pypi.org/pypi/pandastock-mcp/json").info.project_urls
# 期望 Homepage/Repository/Documentation 指向 github.com/D-Asce/pandastocksdk
```

---

## 6. 遗留问题（未在 P0 处理）

- **依赖声明冲突**：PyPI 现网 1.5.4 声明 `mcp<2,>=1.0.0`，仓库已改为 `mcp>=2.0`。1.5.5 发版后自动覆盖，但**升级用户会装上 mcp 2.x**，需确认 `mcp.server.mcpserver.MCPServer` 在目标环境可用。
- **LICENSE 检测**：文件内容是标准 MIT，但 GitHub API license 字段返回 `Other/NOASSERTION`（可能因版权行 `Copyright (c) 2026 pandaData` 与常规格式差异）。目录收录时会显示 "Other"，建议确认。
- **无 tests / CI**：仓库有 dev extra 却无 `tests/` 目录；远端现有 1 个 workflow（`mirror.yml` 镜像），`publish-mcp.yml` 本地就绪但未入库（见 2b），另缺测试与 PyPI 发布流水线。P1 处理。
- **远程 HTTP MCP endpoint**：当前仅 stdio，用户必须本地装 Python。P2 最大架构机会。

---

## 7. 完成判据

全部达成即 P0 结束：

- [ ] `GET registry.modelcontextprotocol.io/v0/servers?search=D-Asce` → 非空
- [ ] `registry.smithery.ai/servers/D-Asce/pandastocksdk` → 200
- [ ] `api.github.com/repos/D-Asce/pandastocksdk/topics` → 非空
- [ ] PyPI `project_urls` 无 `github.com/example`
- [ ] PyPI description 无 `166`，README 首屏第一行是产品 + badge，无第三方广告
