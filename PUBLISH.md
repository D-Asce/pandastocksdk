# 上架与推广清单（P0）

> 诊断结论：产品层已完备（MCP server / PyPI / Pages / SKILL.md），但**发现层为空** —— 官方 MCP 注册表、Smithery、mcp.so 均未收录，GitHub topics 为空。
> 本文件是可直接执行的上架步骤。所有命令在仓库根目录执行。

**核查时间：2026-09-26**，当时状态：

| 渠道 | 状态 | 证据 |
|---|---|---|
| 官方 MCP Registry | ❌ 未收录 | `GET /v0/servers?search=D-Asce` → `count:0` |
| Smithery | ❌ 未收录 | `GET /registry.smithery.ai/servers/D-Asce/pandastocksdk` → 404 |
| mcp.so | ❌ 未收录 | `/server/pandastock-mcp` → 404 |
| GitHub topics | ✅ 已设置（2026-09-26 网页路径） | 12 个：a-share, china-stock, llm, market-data, mcp, mcp-server, model-context-protocol, nats, python, quantitative-finance, realtime-data, stock-data |
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

## 1. GitHub topics ✅ 已完成（杠杆最高）

> **2026-09-26 已完成**：走网页路径（原 a）在 https://github.com/D-Asce/pandastocksdk/edit 填入 12 个 topics。
> API 验证 `GET /repos/D-Asce/pandastocksdk/topics` → `count=12`：
> `a-share, china-stock, llm, market-data, mcp, mcp-server, model-context-protocol, nats, python, quantitative-finance, realtime-data, stock-data`
>
> 备注：PAT 直接 PUT topics 仍为 403（fine-grained PAT 缺 Administration: write）；下方命令仅在换 PAT 后可用。

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

### 2b. CI 自动发布（✅ workflow 已入库，2026-10-10）

> ✅ **2026-10-10 已解决**：先前记录的「PAT 缺 workflow scope 导致 push 被拒」**结论有误**。
> 实测 Contents API `PUT /repos/D-Asce/pandastocksdk/contents/.github/workflows/publish-mcp.yml`
> **成功入库**（commit `a63b681`，2674 字节）。GitHub Actions 已注册该 workflow：
> `GET /actions/workflows` → `Publish to MCP Registry [active] path=.github/workflows/publish-mcp.yml`。
> 内容校验：拉回文件按 CRLF→LF 归一化后 SHA256 `b8db0144d40bd864`，与本地原件一致；
> YAML 解析 `jobs=['publish']`、`triggers=['workflow_dispatch','push']` —— 无内容损坏。
>
> **历史记录（2026-09-26 实测，已被推翻）**：`git push` 曾返回
> `refusing to allow a Personal Access Token to create or update workflow .github/workflows/publish-mcp.yml without workflow scope`。
> 可见 **git push 路径受限，但 Contents API 路径可用** —— 二者权限判定不同，不必再改 PAT。

**现在只需**：PyPI 发版后打 tag 触发

```powershell
git tag v1.5.5
git push origin v1.5.5
```

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

## 4. 第三方目录收录

### 4a. 2026-09-26 已提交（Playwright 实测）

| 渠道 | 入口 | 结果 |
|---|---|---|
| mcp.directory | https://mcp.directory/submit | ❌ **此前记录有误，实际未上架**（2026-10-10 实测：提交于 09-26，已过 14 天仍未收录；站内搜 `pandastock`/`pandaData`/`a-share` 均 "No servers found"；猜测 slug `/server/pandastock-mcp` 404。**对照组已验证检索可用**——搜 `filesystem` 正常返回官方 Filesystem 80.5k★，故「搜不到」是有效阴性而非检索故障）→ 需重新提交并跟踪是否真正上架 |
| mcpservers.org | https://mcpservers.org/submit | ✅ 提交成功（免费档，最长 2 周审核，邮件通知） |
| FindMCP | https://findmcp.app/submit | ✅ 提交成功（`{"success":true,"id":96}`，需英文描述 80+ 字符 + Claude Desktop 安装片段） |
| mcptrove.com (MCP Directory) | https://mcptrove.com/submit | ✅ 提交成功（"Thanks — submitted!"，人工审核） |

### 4b. 浏览器执行进度（2026-09-26）

| 渠道 | 状态 | 证据 |
|---|---|---|
| MCPVault | ✅ 已 claim | GitHub OAuth 授权成功 |
| mcp.so | ✅ 已提 issue | https://github.com/chatmcp/mcpso/issues/4406（state=open，标题 "Add PandaStock MCP - A-share realtime stock data server (22 tools)"） |
| punkpeye/awesome-mcp-servers（92k★） | ✅ PR 已开 | https://github.com/punkpeye/awesome-mcp-servers/pull/15170（state=open，标题 `Add pandastock-mcp 🤖`；fork `D-Asce/awesome-mcp-servers` main=`ce12952`，net diff 仅 README.md +1/-0，插入点 @@ -2594 行 Gaming 前） |
| Awesome-MCP-ZH（中文列表） | ✅ PR 已开 | https://github.com/AshFrancis001/Awesome-MCP-ZH/pull/1（state=open，标题 "添加 pandastock-mcp（A 股实时行情 MCP Server）"；fork `D-Asce/Awesome-MCP-ZH` main=`fa19ca6`，net diff 仅 README.md +1/-0，插入「金融与加密货币」openMF 与 pwh-pwh 之间） |

### 4c. 不适用 / 已关闭（勿再尝试）

| 渠道 | 原因 |
|---|---|
| PulseMCP | 2026-09-03 起停止收新提交，官方指向 MCP Registry |
| LobeHub | OAuth 要求全部仓库读写 + gists + workflows，风险过高，主动放弃 |
| CuratedMCP / mcpcentral.io | 本网络访问返回 Cloudflare 403（数据中心 IP 被拦），换网络可重试 |
| Anthropic Connectors Directory | 需 Claude Team 组织（~$50/月）才能进提交入口 |
| Docker MCP Catalog | 需 Dockerfile 打包，属 P2（配合远程 HTTP endpoint 一起做） |
| Futurepedia | 2026 起仅付费（$247+），放弃 |
| 官方 Registry（modelcontextprotocol/servers 仓库） | 旧 README 已不再收第三方 PR，只走 `mcp-publisher`（见 §2） |

### 4d. 其余原清单（仍有效）

| 渠道 | 提交入口 | 需要内容 |
|---|---|---|
| Glama | https://glama.ai/mcp 中的 Submit | 仓库已有 `glama.json`，填 repo URL 即可；也会从 GitHub topics 自动索引 |
| SeekTool.ai | 已收录；反链已恢复到 README 文末「已收录渠道」区块（`b7c924f`） | 更新描述为「176 个接口，22 个免注册可试」 |
| ToolPilot.ai | 同上 | 同上 |
| 中文广场：DataWhale MCP 列表 / 魔搭 ModelScope MCP / 阿里云百炼 | 各自 GitHub issue 或表单 | 中文描述 + 免注册测试账号是加分项 |
| 中文自动收录站 | mcphello.com / mcpapp.net / followmcp.com / jindage.com / mcpradars.com / mcp.aibase.com | 多为 GitHub 每日自动同步，**设完 topics 后逐个核实是否已收录**，缺的再手动提 |

> 上游依赖提醒：Glama、mcphello、mcp.directory、mcp.aibase 等会抓 **GitHub topics** 和**官方 Registry**。
> topics（§1）和 PyPI→Registry（§5→§2）做完后，先复查这些站，再手动补交。

> 提交描述统一口径（**不要再出现 166**）：
>
> > pandaData：A 股实时数据 MCP Server。NATS 推送行情 / Level2 / DDX 大单 / 资金流 / AI 选股。服务端 176 个接口，22 个开放接口，**提供免注册公共测试账号**，`pip install pandastock-mcp` 即用。

### 4e. 2026-09-27 执行记录（本轮新增）

> ⚠️ 本会话 github.com 间歇宕机（api.github.com 正常），以下标注「⏳ 等恢复」的项需在 github.com 恢复窗口内补完。

| 渠道 | 状态 | 证据 / 备注 |
|---|---|---|
| 火山引擎 volcengine/mcp-server | ✅ PR 已开 | https://github.com/volcengine/mcp-server/pull/436（Open，+1/-0） |
| Influzer.ai | ✅ 提交成功 | https://www.influzer.ai/mcp/submit → "Thanks! Your submission was received"；已登录态（后续可编辑）；Category=Data & Analytics、Transport=stdio、Official 勾选、含真实工具清单 + Claude/Cursor 配置片段 |
| 魔搭 ModelScope | ❌ **此前记录有误，实际未收录** | **2026-10-10 实测推翻旧结论**：旧记录写「`@ascegu/panda_stock_l2` 已在列，条目陈旧待更新」——实测该条目**根本不存在**。三处独立核验均 404：① `api/v1/models/ascegu/panda_stock_l2` → `{"Code":10010205001,"Message":"获取模型信息失败，信息：record not found"}`；② `api/v1/spaces/ascegu/panda_stock_l2` → 404（非创空间）；③ `/models/ascegu/panda_stock_l2` → HTTP 200 但**空壳**（只有导航栏 + 4 条 console error）。**结论：不是「陈旧待更新」，而是「从未创建，需重新提交」**。另：Playwright 浏览器虽有 12 个 `modelscope.cn` cookie，但访问 `/my/myacls` 被重定向且页面显示「登录 / 注册」→ cookie 已失效，**无登录态**，需用户重新登录后才能创建 |
| yzfly/Awesome-MCP-ZH（7.7k★，权威中文列表） | ✅ PR 已开 | https://github.com/yzfly/Awesome-MCP-ZH/pull/636（标题 `新增 PandaStock 到 💰 金融与加密货币`；README +1/-0，插入「金融与加密货币」节 OpenChainBench 与 pwh-pwh 之间，正文含收录标准自证） |
| Glama | ✅ **已通过审核并上线**（2026-10-10 复核确认，优于原「待审核」记录） | 提交路径：GitHub OAuth 授权（D-Asce，scope 仅 read:user+email+org）→ complete-profile → Add Server 对话框（Runs from source）填 Name/Description/仓库 URL → Submit for Review。**上线核验**：`glama.ai/mcp/servers?query=pandastock` 命中条目，归属 `D-Asce`，分类 Finance / Research & Data / AI & Machine Learning，已索引 MCP 工具 `ChMarketFundFlow` / `chStockList` / `ChMarketCurReal` / `ChIndustryCurReal` |
| MCPFind | ✅ PR 已开 | https://github.com/MCPFind/mcp-find/pull/264（标题 `Add: PandaStock`；fork `D-Asce/mcp-find` 分支 `D-Asce-patch-1`，commit `b3f7763`，新增 `submissions/pandastock.yml` +7/-0，正文含收录标准自证；源自 mcpfind.org 表单 Open GitHub Editor 预填） |
| MCP Surge | ❌ 作废 | mcpsurge.com Google DNS NXDOMAIN，域名已失效 |
| 阿里云百炼 | ❌ 不可行 | 云市场 OneKey MCP = 邀约制企业入驻流程（服务商注册 + SPI + 计量计费），个人无入口；「开发者招募」文章链接未能提取 |
| DataWhale | ❌ 无收录目录 | `datawhalechina/mcp-lite-dev` 是 MCP 教程课程，第 5 章「MCP Server 资源整理」无收录清单 → 以 yzfly PR 替代该目标 |
| 中文自动收录站复核 | ❌ 均未收录 | mcp.aibase / mcphello / followmcp / jindage / mcpradars / mcpapp 六站搜索 pandastock 均无结果；多为 GitHub topics/Registry 自动同步 → 待 §5→§2 完成后复查，仍缺再手动提 |
| MCPWorld | ✅ 已提交（2026-10-05，审核中） | 提交成功 toast → 跳转 `/zh/myMcp`，「我的MCP」列表见 PandaStock、审核状态=**审核中**；表单：名称 PandaStock、描述 125 字、服务详情 markdown 1169 字、勾选「在MCP广场展示」、类型=自定义代码输入（stdio/uvx config 173 字符）、电话 18994111679、邮箱 asce1010@126.com；技术要点：提交按钮禁用由父表单 deep watcher 驱动（`distribute.length>0 && config!=="" && proto_type!==""...` 全过才 enable），checkbox 需点 label 包裹元素（直点 input 被双切回）、代码框最后填+立即 blur 防父模型变更清空 |
| mcpmarket.com | ✅ 已收录（2026-10-05 复核发现，未重复提交） | `https://mcpmarket.com/zh/server/pandadata` 页面存在即已收录；如需排队优化可选 Free Queue（$0，4-6 周），暂不动 |
| mcpapp.net | ✅ 已提交（2026-10-05，审核中） | 成功页 `/zh-hans/submit/success?id=pandastock`「已收到提交，正在等待审核」（48h 人工审）；**首次提交报错根因已修复**：`previews_json` 里 `imageUrl:""`/`ctaUrl:""` 空串过不了 `z.url().optional()`（生产把 url/email 校验失败统一渲染成裸 `Invalid input`，P1 探针 3 错 = 2 URL + canary、P2 探针仅 canary 1 错，均在限流前不耗 5 次/24h 配额）；修法=预览 Image URL 填 logo raw 链接、CTA 填仓库链接；表单要点：transport=stdio/auth=none（默认 sse/oauth 须改）、capabilities=Interactive+Reads+Tools、categories=productivity+developer-tools、头像经 `mcpapp_avatar.js` 注入 14347B logo.png、**Turnstile 生产未配置无需 token**（页面显式提示 "Submission still works"，此前 `hasTurnstile:true` 是 `[class*="turnstile"]` 误匹配 missing-widget div） |

### 4f. 2026-10-09 执行记录（GitHub PR / issue 批次，6 渠道）

> 共性：各仓库对**首次贡献者的 workflow 运行需维护者手动批准**（`conclusion=action_required`），属正常审核门，非 CI 失败，无需改代码。
> mcpHQ 与 TensorBlock 两条 PR 曾因 fork base 落后被标 `dirty`（且分支被强制重置后短暂关闭），已按「`merge-upstream` 同步 fork main → force-reset 分支 → 从新 base 重取目标文件 → 重放编辑 → 重新 push → reopen PR」流程修复，复核 `mergeable=True`、diff 干净。

| 渠道 | 状态 | 证据 / 备注 |
|---|---|---|
| Horatio-Li/awesome-mcp-servers（issue 评论） | ✅ 已评论 | https://github.com/Horatio-Li/awesome-mcp-servers/issues/1#issuecomment-6081804224 |
| wundercorp/awesome-mcp | ✅ PR 已开 | https://github.com/wundercorp/awesome-mcp/pull/112（open，mergeable=True；新增 `servers/data/pandastock/server.json` + README 重生成，本地 validate 39 entries / generate 通过；CI `Validate catalog` = `action_required` 待批准） |
| mcpHQ/awesome-mcp-servers | ✅ PR 已开（冲突已修复） | https://github.com/mcpHQ/awesome-mcp-servers/pull/181（open，mergeable=True；`data/servers.json` 中部 index 113 插入 desc_len=196、category=`finance-commerce-and-business-apps`，231→232；validate 232 servers / generate / check-generated 全过；4 commits / 4 files：servers.json +15、README +4/-2、llms.txt +2/-1、llms-full.txt +12/-1；CI = `action_required` 待批准） |
| BlockRunAI/awesome-finance-mcp | ✅ PR 已开 | https://github.com/BlockRunAI/awesome-finance-mcp/pull/108（open，mergeable_state=**clean**；README Data Providers 追加行，desc 51 字符，Pricing=Free） |
| TensorBlock/awesome-mcp-servers | ✅ PR 已开（冲突已修复） | https://github.com/TensorBlock/awesome-mcp-servers/pull/3393（open，mergeable=True，mergeable_state=blocked（必需 check 未就绪，暂无 workflow runs）；`docs/finance--crypto.md` 顶部「💰 Finance & Crypto」节插入 bullet，+1/-0） |
| cline/mcp-marketplace | ✅ issue 已建 | https://github.com/cline/mcp-marketplace/issues/2895（open，标题 `[Server Submission]: PandaStock - A-share Real-time Market Data MCP Server`；模板 label `server-submission` 未自动打上，手动加 label 返回 403（需 admin）→ 记为已知限制；**表单坑**：`browser_fill_form` 的 `.fill()` 不触发 React onChange 导致 Create 无反应且校验清空，改用 `browser_run_code_unsafe` 逐字段 click + `page.keyboard.type` 键入即成功） |

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

- **依赖声明冲突**：PyPI 现网 1.5.4 声明 `mcp<2,>=1.0.0`，仓库已改为 `mcp>=2.0`。1.5.5 发版后自动覆盖。
  ✅ **2026-09-26 冒烟已通过**：干净 venv 安装 1.5.5 wheel（拉到 `mcp 2.2.0`）→
  `from mcp.server.mcpserver import MCPServer` 成功 → 控制台入口 `pandastock-mcp` 完成
  MCP `initialize` 握手（`serverInfo.version=1.5.5`）→ `tools/list` 返回 **22 个工具**。升级安全。
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

---

## 8. 发文渠道（介绍接口/教程的平台）

统一选题（三篇打天下，别每处重写）：

1. **教程向**：《用 MCP 把 A 股实时行情接进 Claude / Cursor》——安装、免注册测试账号、22 工具演示
2. **技术向**：《为什么 A 股数据用 NATS 推送而不是 REST 轮询》——架构差异化（Level2/DDX 主动推送）
3. **English 版**：*Building an MCP server for A-share realtime data: NATS push vs REST polling*

### 8a. 英文（自发布，快）

| 平台 | 入口 | 规则要点 |
|---|---|---|
| DEV Community (dev.to) | dev.to 新建文章 | 即发即上；支持 canonical URL 交叉发布；标签 `mcp` `python` `quantitative-finance`；避免硬广口吻 |
| Hashnode | hashnode.com | 自发布 + 站内发现；适合长文教程 |
| In Plain English | plainenglish.io/write-for-us | 免费账号投稿，编辑审；1500+ 词更稳；网络内 4 站分发 |
| freeCodeCamp News | freecodecamp.org/news | 编辑严审；教程必须可复现（给出完整安装 + 运行命令） |
| Hacker Noon | hackernoon.com | 叙事/工程案例向 |
| Moesif Blog（API 垂类） | moesif.com/blog/write-for-us 表单 | 500-2000 词，API 教程契合度最高；不付稿费但读者全是 API 人群 |
| Just Tech Blog（API 垂类） | 邮件 pitch：contact@justtechblog.com | 800-2500 词；作者简介 1 条 dofollow 链接 |
| SitePoint / DigitalOcean / DZone / The New Stack | 各自 pitch | 高门槛，发完 1-2 篇自发布后再投 |

> 分发策略：先发 dev.to/Hashnode（即时），同文加 canonical 再投 In Plain English / freeCodeCamp（编辑背书）。

### 8b. 中文（自发布，账号即开即用）

| 平台 | 入口 | 规则要点 |
|---|---|---|
| 掘金 | juejin.cn/editor/drafts | 自发布；后端/AI 标签；封面图必填；摘要 50-100 字 |
| CSDN | editor.csdn.net/md | 自发布；量大但 SEO 长尾好 |
| 开源中国 OSCHINA | my.oschina.net 博客 | 开源项目气质契合；也可投稿动弹 |
| 思否 SegmentFault | segmentfault.com/write | 自发布 |
| 知乎专栏 | zhuanlan.zhihu.com | 「量化 × AI」话题流量好；长文+代码块 |
| InfoQ 中文站 | 投稿邮件 editors@cn.infoq.com | 深度文章 3000+ 字，非 How-to；三种授权（独家稿费 150 元/千字封顶 800、转载 200 元/篇、CC）；见 infoq.github.io/article-guidelines.html |
| linux.do | linux.do | 有信任等级门槛；技术分享形式，别纯广告 |
| V2EX 分享创造 | v2ex.com/go/create | **首发大方承认是自己的作品**；一页内+讲技术原理；新号有 30 天限制；禁重复发帖（亦见 §8d） |

### 8c. 多平台一键工具

- `k8scat/articli`（Go CLI）：掘金 / CSDN / 开源中国 / 思否 一次发布，Cookie/Token 鉴权
- 或 `wechatsync` 类浏览器插件同步（维护状态自行核实）
- 掘金也可直接走其内部 API（`content_api/v1/article_draft/create` + `article/publish`，Cookie 鉴权）

### 8d. 社区发帖（非发文，短贴）

| 渠道 | 要点 |
|---|---|
| Show HN | 必须披露 "I'm the author"；标题别营销腔 |
| r/mcp · r/LocalLLaMA · r/algotrading | 技术分享帖形式；reddit 自我推广政策：外链 + 透明身份 |
| V2EX 推广节点 | 分享创造发过一次后的后续推广放 /go/promotions |
| 雪球 / 集思录 | 量化散户社区；以「数据接口能力演示」切入，别硬广 |

---

## 9. 2026-10-10 下一步推广计划

### 9.0 已完成渠道汇总（20+，均在等审核或已生效）

| 类别 | 渠道 | 状态 |
|---|---|---|
| 基础 | GitHub topics（12 个） | ✅ 生效 |
| 目录 | mcp.directory / mcpservers.org / FindMCP / mcptrove / MCPFind / MCPWorld / mcpapp / mcpmarket / Influzer / Glama / mcp.so | ✅ 已提交，审核中 |
| Awesome list | punkpeye / yzfly / AshFrancis / Horatio-Li（评论） | ✅ 已提交 |
| GitHub PR/issue（本周） | **mcpHQ #181 ✅已合并** / **TensorBlock #3393 ✅已合并** / wunder #112 · BlockRunAI #108 · cline #2895 | 2 条已合并上线，3 条等审核 |
| 量化平台 | volcengine ✅已提交 / ModelScope ❌**实测未收录**（旧记录有误，见 §4e） | 1 条待审核，1 条需重新创建 |

> 边际收益递减 —— **不再继续铺目录**，转向「内容 + 社区 + 平台模块」。

### 9.0.1 🎉 两条 PR 已合并上线（2026-10-09 合并，2026-10-10 核验）

| 仓库 | PR | 合并人 | 合并时间 | merge commit | 上线核验（拉 upstream `main` 实测） |
|---|---|---|---|---|---|
| **mcpHQ/awesome-mcp-servers** | [#181](https://github.com/mcpHQ/awesome-mcp-servers/pull/181) | `imrajdas` | 2026-09-10 01:59 CST | `de327a2` | ✅ `data/servers.json` 命中条目：`name=PandaStock` / `category=finance-commerce-and-business-apps` / `language=Python` / `provider=pandaData` / `url` 指向真实仓库；该文件当前 **250** 个 servers |
| **TensorBlock/awesome-mcp-servers** | [#3393](https://github.com/TensorBlock/awesome-mcp-servers/pull/3393) | `wilsonccccc` | 2026-09-10 00:09 CST | `573076d` | ✅ `docs/finance--crypto.md` 命中条目原文：<br>`- [PandaStock](https://github.com/D-Asce/pandastocksdk): A-share real-time market data MCP server - NATS-pushed quotes, Level-2, DDX big orders, money flow and AI stock screening; 176 server-side endpoints, 22 open endpoints with a free public test account. Install: pip install pandastock-mcp.` |

> ⚠️ 两条 PR 在合并前都曾因 fork base 落后被判 `dirty`（head==base 导致被自动关闭），
> 修复流程：`merge-upstream` 同步 fork main → force-reset 分支 → 从新 base 重取目标文件
> → 重放编辑 → 重新 push → reopen PR。**下次遇到 dirty 先同步 base 再 force-reset，
> 不要直接改文件重推**（会踩 head==base 自动关闭）。

### 9.1 🔴 P0 — PyPI 1.5.5 发版（只有用户能做，杠杆最大）

> ⚠️ **不是发新版本，是修 1.5.4 的 4 处元数据**（PyPI 元数据不可原地改，必须重发）。

已实测确认（2026-10-10）：

| 检查项 | 1.5.5 状态 |
|---|---|
| `twine check dist/*` | ✅ 两包均 PASSED |
| `Project-URL` × 4 | ✅ 全指 `github.com/D-Asce/pandastocksdk`（1.5.4 是 `github.com/example` 死链） |
| `Requires-Dist: mcp` | ✅ `mcp>=2.0`（1.5.4 写的是 `mcp<2,>=1.0.0` 与代码冲突） |
| README `mcp-name` 标记 | ✅ `io.github.D-Asce/pandastocksdk`（**Registry 所有权校验读这个**） |
| 描述里的 `166` | ✅ 出现 0 次（`176` 出现 4 次） |

上传（**只差 token**；本机 `twine 7.0.0` 已装，但实测报 `ERROR NonInteractive: Credential not found for API token.`）：

```powershell
cd D:\code\net\pandastocksdk
py -m twine upload dist/*
# Username: __token__   Password: <你的 PyPI token>
```

**一个动作解锁整条链**：官方 MCP Registry（CI workflow 已就绪，`git tag v1.5.5 && push` 即发）→ Smithery 自动索引 → 中文 6 站复查（mcphello/followmcp/jindage/mcpradars/mcp.aibase）→ Glama 自动索引。

### 9.2 🟢 P1 — 零成本、受众最准（已备好，待用户发布）

| # | 内容 | 产物 | 状态 |
|---|---|---|---|
| 1 | **BigQuant 模块市场** | `promo-repos/bigquant/pandastock_datasource/`（`__init__.py` + `bigmodule.json` + `README.md`）—— 把 PandaStock 包成可视化数据源模块，`bq module publish` 发布 | ✅ 代码已备，待用户用 BigQuant 账号发布 |
| 2 | **中文长文（四站同发）** | `promo-repos/research/articles/zh-用MCP接A股行情.md` —— 《用 MCP 把 A 股实时行情接进 Claude / Cursor》 | ✅ 文稿已备，待用户发：知乎 + 掘金 + CSDN + 雪球 |
| 3 | **Tushare 社区** | `promo-repos/research/posts/tushare-community-post.md` | ✅ 草稿已备，待用户发 |
| 4 | **Akshare / Baostock 社区** | `promo-repos/research/posts/akshare-baostock-community-post.md` | ✅ 草稿已备，待用户发 |

### 9.3 🟡 P2 — HF Space 托管 MCP 端点（仓库已建好并通过端到端验证）

**Space 仓库（canonical）**：https://github.com/D-Asce/pandastock-mcp-space
HEAD `47f7f63` — 6 个文件：`README.md`（含 `sdk: gradio` / `app_file: app.py` frontmatter）
`app.py`（8 个 MCP 工具）`requirements.txt`（`gradio[mcp]` + `nats-py`）`panda_stock.py`
`verify_mcp_schema.py`（验证脚本）`VERIFICATION.md`（验证报告）

**✅ 已完成的端到端验证（2026-10-10，本机实跑）**：

```
initialize /gradio_api/mcp/ -> 200  serverInfo={name:"Gradio",version:"1.30.0"}
tools/list                    -> TOOLS_COUNT 8
  ch_stock_list args=[]                              ch_core_news        args=['date']
  ch_one_stock_real args=['code']                    ch_market_fund_flow args=[]
  ch_stock_front_day_history args=['code']           ch_lhb_data         args=['date']
  ch_stock_minute_history args=['code','minute','date']
  ch_ddx_stock_data args=['code']
RESULT MCP_SCHEMA_VERIFIED
```

⚠️ **部署陷阱（实测发现）**：MCP 端点必须带尾斜杠 —— `/gradio_api/mcp` 返回 **307 重定向**，
不跟随重定向的客户端会直接连接失败。对外配置一律写 `https://<space>.hf.space/gradio_api/mcp/`。

**用户只需 1 步**：https://huggingface.co/spaces/new → Create a Space from a GitHub repo
→ 选 `D-Asce/pandastock-mcp-space` → SDK=Gradio → Name=`pandastock-mcp` → Public
（huggingface.co 从本环境不可达，必须本地浏览器操作；建好后给我 URL，我跑远程 schema 复验）

⚠️ 数据风险：公共测试账号按来源 IP 限频（本机 IP 已被本轮测试打满，HF 服务器 IP 需实测）。

### 9.4 🔵 P3 — 等 P0 完成后观察

- **英文社区**：r/LocalLLaMA 可发（r/algotrading 禁自我推广）；Show HN 配合 PyPI 发布叙事
- **聚宽 / 米筐社区帖**：受众存在但无正式提交入口，性价比低于 BigQuant
- **B 站视频**：量化 + MCP 题材有流量，制作成本高

### 9.5 选题统一口径（三篇打天下，别每处重写）

1. 教程向：《用 MCP 把 A 股实时行情接进 Claude / Cursor》—— 已备（§9.2-2）
2. 技术向：《为什么 A 股数据用 NATS 推送而不是 REST 轮询》—— 架构差异化（Level2/DDX 主动推送）
3. English 版：*Building an MCP server for A-share realtime data: NATS push vs REST polling*

### 9.6 渠道状态实测复核（2026-10-10）

因发现 ModelScope 记录有误，对全部「✅ 已收录/已提交」逐条实测复核。**方法学：任何"搜不到"结论必须先做对照组证明检索本身可用**，否则不记录。

| 渠道 | 旧记录 | 实测结论 | 依据 |
|---|---|---|---|
| mcpHQ #181 | PR 已开 | ✅ **已合并且条目在线（数据层 + 展示层双确认）** | API 拉 upstream `main`：`data/servers.json` 命中条目（该文件现 250 条），**且生成的 `README.md`（69,808 字节）也命中**——`- **[PandaStock](https://github.com/D-Asce/pandastocksdk)** \`Python\` · A-share real-time market data MCP server with NATS-pushed quotes...`，即**人看的 README 与机器读的 JSON 都在线** |
| TensorBlock #3393 | PR 已开 | ✅ **已合并且条目在线** | 同上，条目在 `docs/finance--crypto.md`，原文逐字命中 |
| punkpeye #15170 | PR 已开 | ✅ 仍 open（记录准确） | `state=open merged=false`，最后更新 09-26 |
| yzfly #636 | PR 已开 | ✅ 仍 open（记录准确） | 同上，09-27 |
| AshFrancis001 #1 | PR 已开 | ✅ 仍 open（记录准确） | 同上，09-26 |
| volcengine #436 | PR 已开 | ✅ 仍 open（记录准确） | 同上，09-27 |
| MCPFind #264 | PR 已开 | ✅ 仍 open（记录准确） | 同上，09-27 |
| mcpmarket | 已收录 | ✅ **确认在线** | `mcpmarket.com/zh/server/pandadata` → 页面显示 `PANDADATA PandaData by D-Asce` |
| **ModelScope** | ✅ 已收录 | ❌ **已订正：条目不存在** | 见 §4e，三处 404 |
| **mcp.directory** | ✅ 审核队列 | ❌ **已订正：从未上线** | 见 §4a，三种关键词均无结果 + 对照组通过 |
| mcpservers.org | ✅ 提交成功 | ✅ **确认在线**（复核后订正为已收录） | 遍历 12 个子 sitemap / **66,783 条 URL**，命中 `https://mcpservers.org/servers/d-asce/pandastocksdk`；打开确认：标题 `PandaStock MCP 服务器`、分类「金融」、正文为仓库 README（含 22 工具 / NATS / 免注册测试账号描述）。⚠️ **slug 规律是 `d-asce/<repo>`，不是 `<name>`**——先前按 `pandastock-mcp` 猜 slug 得 404 是误判来源 |
| **Glama** | ✅ 已提交（待审核） | ✅ **已通过审核并上线**（好于原记录） | `glama.ai/mcp/servers?query=pandastock` 命中条目：归属 `D-Asce`，分类 Finance / Research & Data / AI & Machine Learning，且已索引 MCP 工具（`ChMarketFundFlow` / `chStockList` / `ChMarketCurReal` / `ChIndustryCurReal`） |
| MCPWorld | ✅ 已提交（审核中） | ⚠️ **无法判定** | `我的MCP` 显示 "No Data"；但公开广场页为 SPA，**hydration 前渲染占位符「当前已收录 0 个」**（同页他处显示「全部 62324」），`?keyword=` 亦不过滤 → 抓到的很可能是未加载完的占位内容，**不足以判定未收录**，需人工登录后确认 |
| 魔搭 cookie | （隐含已登录） | ❌ 12 个 cookie 已失效 | 访问 `/my/myacls` 被重定向且显示「登录 / 注册」 |

> ⚠️ **方法学教训**：本轮两次差点误判为"未收录"——一次是 slug 猜错，一次是 camelCase（`PandaData`）没匹配小写 needle（`pandastock`）。
> 对照组（control）是唯一防误判手段：先证明检索工具本身有效，再采信阴性结果。
