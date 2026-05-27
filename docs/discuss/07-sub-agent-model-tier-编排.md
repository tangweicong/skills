# 07-sub-agent model-tier 编排（Opus 规划 + Composer 执行）

| 字段 | 值 |
|------|-----|
| 轮次 | 07 |
| 主题 | Cursor sub-agent + 模型分层编排（Opus 规划/评审 + Composer 执行）的成本可行性 |
| 日期 | 2026-05-27 |
| 状态 | confirmed · synced · v1.3（EXP 案例精化：EXP-03 = N/A 废止；EXP-04 案例改为 proj-run 完整 SKILL.md 起草 @ 2026-05-27）|
| 讨论方法 | `best-minds-grounded` |
| 写入格式 | 完整 |
| 承接 | `temp.md` L9 TODO；06 轮 Q3 暂缓项的重启；INV-04（idea-pmo 不含执行）+ ORD-10（覆盖边界） |

## 用户输入（本轮）

用户原话：

> 现在大部分的 AI 工具都在改成 token 计费，像 opus 这种模型的费用非常高，明显无法在整个项目周期全流程使用。所以可能通过 skill 结合 cursor 的 sub-agent 模式，用 opus 模型来规划/评审，用 composer 模型来做具体执行，以达到节省费用的目的吗？

**本议题归属**：用户问的是「**execute 阶段**的 sub-agent 编排能否引入 idea-pmo 体系，让节省成本」。按 INV-04，idea-pmo 不含 execute；所以本议题如果有结论，落地形式应是**「idea-pmo 内的 sub-agent handoff 契约」+「独立 execute 编排约定」**，而非 idea-pmo 内嵌 execute。

## 框定问题（讨论前预设）

| Q | 问题 |
|---|------|
| Q1 | Cursor sub-agent 当前能否真正实现按 task 指定不同模型？（技术可行性）|
| Q2 | Opus / Composer 价差是否大到值得做 model-tier？（经济性）|
| Q3 | 双模型编排会损失多少质量？（trade-off）|
| Q4 | 这件事在 idea-pmo skill 内部该放在哪？落到 manifest？落到 sub-skill？落到独立 execute skill？|
| Q5 | 有无既有最佳实践（Aider architect / Claude Code subagents / APM）可直接借鉴？|

## 已查证事实

> 真实性三档标签：【原话】= 直接引用；【已公开立场】= 转述官方/作者公开输出；【模拟推理】= 基于上述事实做的本轮推理（**非作者原意**）。

### F1 · Cursor sub-agent 真实约束（来源：[Cursor Forum bug #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736)、[Cursor Subagents 完整指南](https://medium.com/@codeandbird/cursor-subagents-complete-guide-5853e8d39176)）

【已公开立场】Cursor 官方（@deanrie，2026-02-15）：sub-agent model 通过 `.cursor/agents/<name>.md` 的 YAML frontmatter `model` 字段设置；合法值 = `inherit` / `fast` / 具体 model 名（如 `claude-4.6-opus-high-thinking`）。

【原话】Cursor 官方（2026 update）："accounts on legacy request-based pricing are currently not part of the expanded model selection feature for subagents... the only model options for subagents are: omit the `model` parameter (inherits the parent model) or use `fast`"。

【已公开立场】subagent 设计 = 独立 context window + 父只看 final summary + 支持 `is_background: true`（异步）/ `readonly: true`（只读 auditor）。description 字段决定父 agent 何时 delegate。

### F2 · 价差与质量数据（来源：[Officechai 报道](https://officechai.com/ai/cursors-composer-2-5-places-3rd-in-artificial-analysis-coding-agent-index-is-10-60x-cheaper-than-variants-above-it/)、[Lushbinary 对比](https://lushbinary.com/blog/composer-2-5-vs-claude-opus-4-7-vs-gpt-5-5-coding-comparison/)、[Pondero cost math](https://pondero.ai/coding/guides/cursor-composer-2-5-benchmarks-pricing-may-2026/)）

| 模型 | input $/M | output $/M | 用途 |
|------|-----------|------------|------|
| Composer 2.5 Standard | $0.50 | $2.50 | 后台/批量 agent（subagent 默认） |
| Composer 2.5 Fast | $3.00 | $15.00 | 交互 IDE 默认 |
| Claude Opus 4.7 | ~$15 | ~$75 | 高阶规划/评审 |

【已公开立场】Artificial Analysis Coding Agent Index（2026-05）：
- Claude Code Opus 4.7 Max = 67 分（第 1）；Composer 2.5 = 63 分（第 3）
- per-task cost：Opus 4.7 Max = **$4.14**；Composer 2.5 Standard = **$0.07**
- **quality 差 ~6%、cost 差 ~60x**

【已公开立场】Cursor announcement（@Pondero 转述）：Composer 2.5 "matches Opus 4.7 and GPT-5.5 on SWE-Bench Multilingual 79.8% and CursorBench v3.1 63.2%"。

### F3 · Aider architect/editor 模式真实数据（来源：[Aider blog 2024-09-26](https://aider.chat/2024/09/26/architect.html)、[DeployHQ 2026 guide](https://www.deployhq.com/guides/aider)）

【原话】Aider blog（Paul Gauthier）："Splitting up 'code reasoning' and 'code editing' in this manner has produced SOTA results on aider's code editing benchmark. Using o1-preview as the Architect with either DeepSeek or o1-mini as the Editor produced the SOTA score of 85%."

【已公开立场】2026 推荐配对（DeployHQ）：
- 主推：`aider --architect --model gpt-5 --editor-model gpt-5-mini`
- 备选：`aider --architect --model opus --editor-model sonnet`
- "architect-mode runs typically cost 30-50% less than the same task done by the architect model alone"

【已公开立场】设计原理："frontier models reason brilliantly but sometimes mangle structured diff output, while cheaper models are precise about diffs but weaker at planning"。

### F4 · Anthropic Claude Code 官方编排建议（来源：[Claude Code agents docs](https://code.claude.com/docs/en/agents.md)、[Subagents SDK docs](https://code.claude.com/docs/en/agent-sdk/subagents)、[DEV pattern survey](https://dev.to/wilsonhoe/why-your-multi-agent-system-breaks-at-3-am-orchestration-patterns-that-survive-production-1efi)）

【原话】Anthropic Claude Code docs："Subagents \[are\] delegated workers inside one session that do a side task in their own context and return a summary. Use \[them\] when: a side task would flood your main conversation with search results, logs, or file contents you won't reference again."

【已公开立场】4 种并行模式：subagents（同 session 内） / agent view（独立 session） / agent teams（实验性，shared task board + peer messaging，2026-02-05 launch）/ worktrees（文件隔离）。subagent model 字段同 Cursor。

【已公开立场】DEV 社区 pattern survey 推荐"**Supervisor + Specialists** 是默认选择，96.3% 成功率"；强调"blast radius containment — subagent 出错只污染自己的 context"。

### F5 · APM 框架 model assignment 立场（来源：[APM repo](http://github.com/sdi2200262/agentic-project-management)、[APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md)、[APM-Auto fork](http://github.com/sdi2200262/apm-auto)）

【已公开立场】APM 原生设计 Planner / Manager / Workers 三角色**均在独立 context**，但**不强制不同模型**——通过 `.apm/bus/` Message Bus（文件级跨 session 通信）连接，由用户人工 shuttle 消息。

【已公开立场】APM-Auto（官方 fork，Claude Code 适配）："replaces the user-mediated Worker model with autonomous subagent dispatch — the Manager spawns ephemeral subagents via `Agent()` to execute Tasks, reviews their output, and continues without requiring you to shuttle messages between chats"。

【已公开立场】APM 设计强调每个 Worker 的 Task Prompt 必须 self-contained（含 objective、instructions、validation criteria、所有 context）—— context isolation 是核心契约，model 选择是次要 lever。

## 推理（非事实、非待验证）

> 以下标 【模拟推理】 = 基于上述事实做的本轮推理，**非任何作者原意**；推理路径可追溯，结论可质疑。

### 关于 Q1（技术可行性）

【模拟推理】当前（2026-05-27）状态：Cursor subagent 的 model 字段对 **legacy request-based plan 不可靠**——会被 server 端 silently fallback 到父 model。这意味着：

- 想做 "Opus 规划 + Composer 执行" 的精确编排，**目前最稳的实现是反过来用**：**Opus 当父 agent**（手动控制 / 高 cost），通过 `is_background: true` subagent 把执行委派给继承父 model... **不行**——这样 subagent 还是 Opus。
- 真正可行的实现是：**Composer 2.5 当父 agent**（默认 IDE 体验），**手动 `@opus` 切换模型**做规划/评审环节（不依赖 subagent model 字段）。这是 plan-aware 的实现，但**不是 sub-agent 自动调度**。
- 等 Cursor 完成 model 字段 rollout（usage-based plan 已开始），才能真正写 `.cursor/agents/planner-opus.md` 自动 dispatch。

### 关于 Q2 + Q3（经济性 + quality）

【模拟推理】Composer 2.5 vs Opus 4.7 的 cost-quality Pareto 数据非常明确：

- **执行密集场景**（output token 主导：multi-file edit / terminal session / refactor patches）：Composer 2.5 Standard 的 **30x output 价差**直接对应 30x 月度成本差异（Lushbinary 数据：$220/mo vs $6600/mo at 100 runs）
- **规划密集场景**（推理深度主导：架构决策 / 评审 / risk analysis）：Opus 4.7 的 +4 index 分（67 vs 63）值不值 60x cost？取决于决策本身的下游放大效应——一个错误规划决定可能浪费 10 小时执行成本，所以**规划用 Opus 性价比高**。

这正是 Aider architect/editor 模式的核心洞察（F3 引用 Paul Gauthier 原话）：**前 frontier model 推理强但 diff 易错；便宜模型 diff 精确但推理弱**——所以分工。30-50% cost 节省的公开数据是这个洞察的实证。

### 关于 Q4（在 idea-pmo 里放哪）

【模拟推理】3 个层次的可能落地位置：

| 层 | 范围 | 是否归 idea-pmo | 风险 |
|---|------|----------------|------|
| L1 · **sub-agent handoff 契约** | "phase-NN/plan.md 生成时附 sub-agent dispatch manifest"（artifact 级契约） | **归** idea-pmo（艺术 artifact） | 低；不违反 INV-04 |
| L2 · **model-tier 编排策略** | "规划/评审用 X 模型；执行用 Y 模型" 的具体规则 | **不归** idea-pmo（属 execute 域）| 中；放 idea-pmo 会违反 INV-04 |
| L3 · **跨 sub-agent 通信** | message bus / artifact-index 作为 source of truth | **部分归** idea-pmo（artifact-index 已在）| 低；只是扩展 artifact-index 含 sub-agent dispatch 元数据 |

**最小可行落地** = L1 + L3 扩展，**不引入 L2**。L2 留给独立的 `execute-orchestrator` skill 或对话级约定。

这与 06 轮 vision 一致：idea-pmo 是 PM 规划 + handoff 契约的"棒交接接口"，不是 execute orchestrator。

### 关于 Q5（借鉴）

【模拟推理】4 个学派都给出了部分答案，但**没有任何一个**给出 "Cursor sub-agent + PMP 体系内的 model-tier" 的完整方案。需要本 skill 自创组合：

- 借鉴 Aider architect/editor 的**模型分工原理**（F3）
- 借鉴 Anthropic Supervisor+Specialists 模式（F4）
- 借鉴 APM message bus（F5）作为跨 sub-agent 通信备用方案（当 Cursor sub-agent 不够时）
- 借鉴 Cursor `.cursor/agents/*.md` 文件格式（F1）作为主推 dispatch 方式

## 方法专属输出（best-minds-grounded · 4 视角 + 关切→路径）

### 视角 A · Cursor team / Aman Sanger 派（Composer 2.5 设计意图）

【已公开立场】Cursor 把 Composer 2.5 定位为 "Pareto frontier" —— 用 10-60x cost 优势换 ~6% quality 让步，目标是让 background/batch agent 经济上可持续。这正是 sub-agent isolation 设计的目的：把贵 model 留给真正需要深度推理的"焦点对话"，把便宜 model 给可隔离的 specialist。

**对本议题立场**【模拟推理 · Cursor 派】：**强支持**用 Composer 当 subagent 默认执行模型。但当前 model 字段 bug + plan 限制意味着这个图景尚未完全 GA。

**关切**：用户的 plan 类型决定能否真正 dispatch；legacy plan 用户做不到。
**→ 路径**：（a）先确认用户 plan 类型 → 决定走 L1（自动 dispatch）还是手动 `@opus` 切换；（b）等 rollout GA 后切到 L1。

### 视角 B · Aider 作者 Paul Gauthier 派（architect/editor 哲学）

【原话】"Splitting up code reasoning and code editing... has produced SOTA results"；【已公开立场】"frontier models reason brilliantly but sometimes mangle structured diff output, while cheaper models are precise about diffs but weaker at planning"。

**对本议题立场**【模拟推理 · Aider 派】：**强支持**用 model-tier；但坚持要"自动验证 + 失败重试"机制——单纯把 Opus output 喂给 Composer 不够，必须有 lint/test 验证关。

**关切**：sub-agent 之间的契约如果不够严格，规划层（Opus）的设计意图会在执行层（Composer）丢失或被错误解读，节省的 cost 被多轮重试吃掉。
**→ 路径**：每个 sub-agent handoff manifest 必须包含 (1) objective、(2) validation criteria（如 lint / test 命令）、(3) iteration budget；执行 sub-agent 不通过 validation 则 escalate 回父，**不允许**直接交付。

### 视角 C · Anthropic Claude Code 派（Supervisor + Specialists）

【原话】"a side task would flood your main conversation with search results, logs, or file contents you won't reference again"。

**对本议题立场**【模拟推理 · Anthropic 派】：**支持**，但提醒 Supervisor 必须保持权威（96.3% 成功率的 pattern）。subagent 的设计哲学是 "blast radius containment"——cost 节省是副产品，主目的是 context 隔离让父保持决策清晰。

**关切**：如果把 sub-agent 主要当 cost 优化工具用，会牺牲 context isolation 的本意——比如塞太多 task 进一个 subagent → 自己的 context 也爆了。
**→ 路径**：sub-agent task 边界按 "context 是否需要回溯" 划分（需回溯 → 不该 sub-agent），不按 model cost 划分；cost 是结果，不是判据。

### 视角 D · APM 学派 / CobuterMan 派（message bus + Planner/Manager/Workers）

【已公开立场】"each agent operating in its own context with only the information it needs"；APM-Auto fork 用 Claude Code subagent 让 Manager 自动 dispatch ephemeral Worker。

**对本议题立场**【模拟推理 · APM 派】：**强支持**，且认为这种 model-tier 编排是 APM 三角色架构的自然延伸——Planner（Opus）→ Manager（Opus）→ Workers（Composer）。Manager 层用 Opus 是必要的——因为 Manager 要做 task review + reassignment。

**关切**：依赖 Cursor 内置 sub-agent 当前 mature 度不够；APM 自己的 message bus 方案重但可控。
**→ 路径**：本 skill 提供**两个模式**让用户选：Mode α（轻：依赖 Cursor sub-agent + dispatch manifest，等 GA）；Mode β（重：APM 风格 message bus，每个 sub-agent 一个独立 session/chat）。

### 收敛（4 视角的共识）

1. **价差成立** — 4 派都同意 Composer 执行 + Opus 规划/评审在经济上合理（F2 + F3 数据）
2. **质量风险可控** — 通过 validation gate（Aider）+ context isolation（Anthropic）+ Manager review（APM）三道关
3. **当前 Cursor sub-agent 不够 mature** — 必须设计降级方案
4. **归属边界** — idea-pmo 只管 handoff manifest（artifact-level），不管 model orchestration（execute-level，未来另起 skill）

## 讨论正文

### 1. 是否在 idea-pmo skill 内做这件事？

**结论**：**不**直接做。但 idea-pmo **必须**给 sub-agent 编排留接口。

理由（基于 06 轮 vision + INV-04 + ORD-10）：
- idea-pmo 覆盖边界 = Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close（ORD-10）
- INV-04: idea-pmo **不含**执行
- sub-agent model-tier 编排本质属于 execute 域

**接口设计**（L1 + L3，归 idea-pmo）：
- 每个 `phase-NN/plan.md` 末尾**新增可选段** `sub-agent dispatch manifest` —— 列出本阶段适合 sub-agent 的 task + 推荐 specialist 类型（reviewer / coder / auditor 等）+ validation criteria；**不指定具体 model**（由 execute 层决定）
- `artifact-index.md` 扩展 schema —— 记录 sub-agent 产出的 artifact（避免 source of truth 分裂）

**execute 层（不归 idea-pmo）**：后续可起独立 skill `execute-orchestrator` 或留给对话级约定，负责 model 选择、Cursor `.cursor/agents/*.md` 文件生成、validation 重试等。

### 2. 当前 Cursor sub-agent 约束的处理

按 F1，先确认用户 plan 类型：

| Plan 类型 | 推荐做法 |
|----------|---------|
| Usage-based（扩展 model 选择已 rollout）| 走 Mode α — 真正的 `.cursor/agents/<name>.md` 自动 dispatch |
| Legacy request-based | 走 Mode γ（**手动切换**模型）— 父 agent 在 IDE 中 `@composer` 默认执行，规划/评审节点手动 `@opus` 切换；不依赖 sub-agent model 字段 |
| 不确定 | 优先 Mode γ + Mode β（APM message bus）作为重场景备份 |

### 3. cost 假设的量级估算（基于 F2 数据）

【模拟推理】假设一个中等复杂度项目（idea-pmo 试跑过的 docs/pmo 项目级别）：
- Plan 阶段（Round A + B + analyze + reviews）：~50 万 input + ~10 万 output tokens
  - 全 Opus 4.7：$15 × 0.5 + $75 × 0.1 = **$15**
  - 全 Composer 2.5 Standard：$0.50 × 0.5 + $2.50 × 0.1 = **$0.50**（30x 差）
- Execute 阶段（5 phases × 平均 80 万 input + 30 万 output）：
  - 全 Opus 4.7：$15 × 4 + $75 × 1.5 = **$172.50**
  - 全 Composer 2.5 Standard：$0.50 × 4 + $2.50 × 1.5 = **$5.75**（30x 差）
  - **混合（Opus 规划 + Composer 执行）：~$15 plan + ~$5.75 execute = $20.75**（vs 全 Opus $187.50）→ **9x 节省**

净结论：**用 Opus 规划 + Composer 执行的 model-tier 在量级上确实节省 ~9x cost**（与 Aider 30-50% 差距大是因为 Composer 比 DeepSeek/Sonnet 更便宜）；用户的假设**经济上成立**。

### 5. 是否拆分独立 skill（用户 @本轮追问）

**用户原话**："那我觉得是不是可以再建一个 skill 专门用于管理 sub-agent？保持 idea-pmo 的独立性？就像跟 idea-discuss 的拆分"

【模拟推理】**支持拆分**，且这是更对的方向（强于本节 §1 原方案 "L1 + L3 留接口 + 不引入 L2"，因为 L2 留给"对话级约定"是模糊的、不可治理的）。

**与 idea-discuss/best-minds-grounded 拆分的差异**（避免误类比）：

| 拆分 | 轴 | 动机 | 接口承诺字段 |
|------|-----|------|--------------|
| idea-discuss ↔ best-minds-grounded | **横向 · 方法可插拔** | 同一框架换不同分析方法 | 方法 skill → idea-discuss：3 类输出（已查证事实 / 推理 / 待验证假设）|
| idea-pmo ↔ **新 skill** | **纵向 · PMP 过程组隔离** | Plan 与 Execute 是 PMBOK 6 不同 Process Group | idea-pmo → 新 skill：`phase-NN/plan.md` + `## Sub-agent dispatch manifest`（artifact + 执行契约）|

**命名候选**（待用户选）：

| 候选 | 优点 | 缺点 |
|------|------|------|
| **`idea-execute`** | 延续 `idea-discuss` → `idea-pmo` → `idea-execute` 体系命名；对应 PMP Initiating → Planning → Executing 三过程组；不绑定 sub-agent 这个具体技术 | 名字稍泛 |
| `phase-runner` | 强调"跑 idea-pmo 的 phase plan" | 与现有 idea-* 体系不一致 |
| `sub-agent-orchestrator` | 直白描述功能 | 过度聚焦 sub-agent 这个机制；未来加 worktree / agent teams 会名实不符 |
| `execute-orchestrator` | execute 域通用编排，描述准确 | 与 idea-* 体系不一致 |

**关切 → 路径**：
- 关切：拆分后是否会变成 3 个 skill 互相依赖、用户负担增加？
- 路径：3 个 skill 接口都是 **artifact-level 文件契约**（DECISIONS.md / phase-NN/plan.md），用户不需要直接调用——idea-pmo skill 触发时已读 DECISIONS，idea-execute skill 触发时已读 phase plan；3 个 skill 的"触发词"互不冲突。

**关切 → 路径**：
- 关切：现在拆 vs 等 EXP-04 之后拆，时机问题
- 路径：**接口契约现在就定**（ORD-17，规定 phase-NN/plan.md 该有什么字段才能 ready 给 idea-execute）；**skill 实现可后置**（EXP-04 试跑过程中迭代）。这样 idea-pmo 现在改的 manifest 段不会白改。

### 6. EXP 案例精化（v1.3 · 2026-05-27 用户追问）

**触发**：用户 @追问"exp-04 和 exp-03 你有合适的测试案例吗"，重审后发现两个 EXP 都有需要修订的地方。

#### 6.1 EXP-04 案例选错（原 i18n 案例不能验证 model-tier 核心假设）

【模拟推理】原推荐的 EXP-04 案例 "proj-experts 加 i18n" 重审后发现**与假设不匹配**：

- EXP-04 核心假设：Opus 规划 + Composer 执行的 model-tier 在**有规划深度的真实流水线**下省钱不降质
- i18n 任务本质：静态翻译，没规划深度 → **不需要 Opus**，全 Composer 都能跑通
- 结果：测出来"省钱但质量没差"是**假阳性**——因为本任务本就不需要规划深度，验证不出 Aider architect/editor 模式的核心洞察（F3）

**重选案例**：用 proj-* 流水线给 **`proj-run` 起草完整 SKILL.md + assets 模板**（自然嵌套）：

| 维度 | 评估 |
|------|------|
| 规划深度 | **高** — 接口设计 / 3 mode 实现 / 失败模式 / template schema 都需要 Opus 强推理 |
| 执行规模 | 中 — 1 个 SKILL.md（~400 行）+ 5-8 个 template；Composer 甜区 |
| sub-agent 分派天然性 | **强** — 每个 template 独立写，Composer subagent 自然分派 |
| 基线可比性 | **强** — proj-plan SKILL.md 是 06 轮全 Opus 写的，token 数据可直接对比 |
| 双重收益 | **强** — 跑完同时完成 08 轮目标（ORD-17 + EXP-04 passed 触发） |

**新增中止信号**：`cost 节省 < 3x` 也是中止——说明案例规模仍不够大，不能真正分离 plan vs execute 的 cost 占比；需要更大案例（如开源前发布 v1.0）。

#### 6.2 EXP-03 在本仓库不可执行（废止 N/A）

【模拟推理】EXP-03 = 模式 F 试跑（TR-04 命中合规/审计/合同交付场景）。重审后承认 4 个事实：

| 事实 | 影响 |
|------|------|
| EXP-03 在 06 轮**只在文字描述出现**，从未进入 DECISIONS.md 待验证表 | "废止"实际上是正式宣告它从未真正建立 |
| 本仓库不天然有 TR-04 命中项目（用户是 PM agent 工具作者，不做合规业务） | 真实场景验证不可能 |
| 虚构场景（医疗审批 / 金融合规等）验证价值低 | 验证不出"真实可用"，只能验证"模板齐全" |
| F 模式 template 已存在于 `skills/proj-plan/assets/` | 未来真实命中 TR-04 的用户可开箱使用，不需要本仓库先跑过 |

**结论**：EXP-03 标记 **N/A**（不是 pending）——避免"永远 pending"的技术债；明示 F 模式 template 已就绪、真实场景试跑留给未来真实需要的用户。本仓库不强制自跑虚构场景。

**对 06 轮决议的影响**：06 轮"模式 F 仍待 EXP-03 试跑"的描述从"pending"改为"template 已就绪 · 真实场景试跑 N/A"。06 轮历史文件正文**不动**（按 idea-discuss 协议），通过 DECISIONS.md 顶部说明段 + 本节做"覆盖式"修订。

#### 6.3 关切 → 路径

- 关切：EXP-04 新案例（自嵌套）会不会有"作者偏心"效应——自己测自己评？
- 路径：使用客观可量化指标（token count + validate_skills.py 通过/失败 + analyze checklist）+ 第三方对比基线（proj-plan SKILL.md 06 轮全 Opus 写的 token）。质量评估不靠主观打分。

- 关切：废止 EXP-03 会不会让 F 模式的 template 永远停留在"未验证"状态？
- 路径：F template 在本仓库的位置是"开箱可用的模板库"而非"已验证的最佳实践"——这是诚实定位；未来如有真实 TR-04 用户跑过，可由该用户回写 EXP-03'（带真实案例数据）。

### 4. 验证假设的最小可重复实验（EXP-04 草案）

按 best-minds-grounded "无现成方案 → 给推理路径 + 候选方向 + 待验证假设"：

| 字段 | 内容 |
|------|------|
| **假设** | "Opus 规划/评审 + Composer 执行" 在 idea-pmo 走完一个真实小项目，total cost 比全 Opus 节省 ≥ 5x，且 GATE 通过率不降 |
| **尝试** | 用一个已知的小项目（e.g., 给 best-minds-grounded skill 加 i18n），按 idea-pmo Round A → B → phase-01 走全流程；plan/review/analyze 节点用 Opus，phase 执行用 Composer 2.5 Standard；记录每节点 input/output token + 是否通过 GATE |
| **成功信号** | (1) total cost ≤ 1/5 of all-Opus baseline；(2) GATE-0/1/2 一次通过率 ≥ 全 Opus 跑的 80%；(3) analyze checklist 通过 |
| **中止信号** | (1) Composer 在执行阶段反复 validation 失败（> 3 次/phase）→ 模型 capability 不够；(2) Opus plan output 无法被 Composer 正确执行（context handoff 设计失败）；(3) Cursor sub-agent 关键 feature 缺失阻塞 |
| **继续** | passed → 把"handoff manifest 段"加入 `phase-NN/plan.md` 模板；起草 `execute-orchestrator` skill（独立） |
| **中止** | 维持现状，记录失败模式到 06 轮 vision 段的"边缘 case" |

## 本轮决定

> **同步状态**：ORD-15~17 + EXP-04 + 集体重命名**已于 2026-05-27 同步至 `DECISIONS.md` 并落实到 `skills/proj-plan/SKILL.md` + `skills/proj-run/SKILL.md`（骨架 v0）+ `skills/README.md`**（用户确认 Q1=一并 / Q2.1=c 命名方案 c / Q2.2=a 中文双层标题 / Q2.3=a 立即重命名 / Q3=b ORD-15+骨架 / Q4=a EXP-04 选 proj-experts i18n / Q5=a 08 轮起草 proj-run 完整 SKILL.md）。下文条目内容**不动**，作为 07 轮决议存档。

> **命名映射**：本轮决议时旧名 → 落实时新名：`idea-execute` → **`proj-run`**；下文 §讨论 5 中提到的"新 skill"即 `proj-run`。其他 3 个 skill：`best-minds-grounded` → `proj-experts`、`idea-discuss` → `proj-shape`、`idea-pmo` → `proj-plan`。


### 已确定 — 普通决定（新增）

- [x] **ORD-15**（confirmed · synced）：**idea-pmo 边界声明 · sub-agent 范围**——sub-agent / model-tier 编排**不归** idea-pmo（属 execute 域，违反 INV-04），归独立的下游 skill（见 ORD-17）。idea-pmo 仅在 `phase-NN/plan.md` 模板**新增段** `## Sub-agent dispatch manifest`，作为**对下游 execute skill 的"承诺字段"**（类比 idea-discuss → idea-pmo 的 `DECISIONS.md` 承诺）；含 task + specialist 类型 + validation criteria，**不指定具体 model**；`artifact-index.md` schema 扩展登记 sub-agent 产出避免 source of truth 分裂。  
  **来源**：本轮 §讨论 1 + §讨论 5（用户 @本轮追问拆分）；推理 · INV-04 + ORD-10 + Anthropic Supervisor+Specialists；依据 [Anthropic Claude Code docs](https://code.claude.com/docs/en/agents.md) + [APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md)  
  → 同步至 DECISIONS.md `ORD-15`

- [x] **ORD-16**（confirmed · synced）：**Cursor sub-agent 约束披露**——sub-agent dispatch manifest 的下游 execute 实现依赖 Cursor `.cursor/agents/*.md` 当前**有 plan 类型限制**（legacy request-based plan 的 `model` 字段被 server 端忽略，详见 [Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736)）；用户在 usage-based plan rollout 前应优先用「**手动切换模型**」方式（父 agent 在 IDE 中 `@composer` 默认 + 规划/评审节点 `@opus`），不强依赖 sub-agent 自动 dispatch。**披露位置**：新 skill（ORD-17）SKILL.md 立场声明节（之前草案是 idea-pmo SKILL.md，拆分后归下游）。  
  **来源**：本轮 §F1；推理 · Cursor 派 + Aider 派的共同关切  
  → 同步至 DECISIONS.md `ORD-16`

- [x] **ORD-17**（confirmed · synced；命名 `idea-execute` → `proj-run`）：**建立独立下游 skill `idea-execute`**（候选名，待用户选）专管 PMP **Execute Process Group**；与 idea-pmo 的接口契约 = 后者输出 `phase-NN/plan.md`（必含 `## Sub-agent dispatch manifest` 段），前者承接并执行（含 model 选择 / Cursor `.cursor/agents/*.md` 生成 / validation gate / 失败 escalate 回 `phase-NN/acceptance.md`）；**保持 idea-pmo INV-04 不变**。命名遵循 idea-* 体系——对应 PMP Initiating（idea-discuss + best-minds-grounded）→ Planning（idea-pmo）→ Executing（idea-execute）。本轮**只定接口契约**，skill 实现在 EXP-04 试跑后迭代起草。  
  **来源**：本轮 §讨论 5；用户 @本轮原话；推理 · PMBOK 6 Process Groups 边界 + idea-discuss 拆分先例  
  → 同步至 DECISIONS.md `ORD-17`

### 待验证尝试（新增）

- [x] **EXP-04**（confirmed · synced · **v1.3 案例精化**；原案例 proj-experts 加 i18n **作废** —— 见 §讨论 6.1；新案例 = **用 proj-* 流水线给 `proj-run` 起草完整 SKILL.md + assets**）：**Opus 规划 + Composer 执行的 model-tier 试跑**。新方案：proj-shape 走 08 轮决议 → proj-plan Round A → B → phase-01 出 plan + dispatch manifest → 规划/评审/analyze 用 Opus；每个 template 文件 dispatch 给 Composer 2.5 Standard subagent 写，Opus 父 agent 评审；记录 token + GATE + analyze。  
  **成功信号**：total cost ≤ 1/5 全 Opus baseline（baseline = proj-plan SKILL.md 06 轮全 Opus 写的实际 token 数）；GATE-0/1/2 一次通过率 ≥ 80%；analyze 通过；最终 proj-run SKILL.md 通过 `validate_skills.py`。  
  **继续**：把 manifest 段 schema 固化进 `phase-NN/plan.md` 模板；proj-run 完整 SKILL.md 同步发布；后续 skill 起草用相同 model-tier 模式。  
  **中止**：Composer validation 反复失败（> 3 次/template）/ Opus plan 无法被 Composer 正确解读 / Cursor sub-agent 关键 feature 阻塞 / **cost 节省 < 3x**（说明案例规模仍不够大，需更大案例如开源前发布 v1.0）。  
  **来源**：本轮 §讨论 4；推理 · 收敛点 1+2  
  → 同步至 DECISIONS.md `EXP-04`

### 故意不做（边界）

- **不**在 idea-pmo 内嵌 model 选择规则 — 属 execute 域，违反 INV-04（model 选择由 `idea-execute` skill 决定，见 ORD-17）
- **不**在 idea-pmo 内生成 `.cursor/agents/*.md` 文件 — 同上
- **不**指定具体 model 名（如 "Opus 4.7" vs "Opus 4.6"）—— 模型版本会过时；本轮决定只规定"分工原则"，不规定具体型号
- **不**在本轮起草 `idea-execute` skill 的 SKILL.md / 模板 — 只定接口契约（ORD-17 + ORD-15 的 manifest 段 schema），实现等 EXP-04 试跑后迭代

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-15 | 新增 · 承诺字段 | ✓ 已同步（2026-05-27）|
| ORD-16 | 新增 · 披露位置到 proj-run/SKILL.md | ✓ 已同步（2026-05-27）|
| ORD-17 | 新增 · 建立 proj-run 独立 skill；本轮只定接口契约 + 骨架 | ✓ 已同步（2026-05-27）|
| EXP-04 | 新增 · 案例精化 v1.3：原 proj-experts i18n 作废 → **proj-run 完整 SKILL.md + assets 起草**（自然嵌套）| ✓ 已同步（pending · 待 08 轮起草触发）|
| EXP-03 | **N/A 废止** · 06 轮设计意图从未进表；本仓库不天然 TR-04；F template 已就绪 | ✓ 已同步（顶部说明段澄清；变更日志记录）|
| INV-04 + ORD-01 | 引用名同步（idea-pmo → proj-plan） | ✓ 已同步 |
| ORD-12 | 引用名同步（best-minds-grounded → proj-experts） | ✓ 已同步 |
| 其它已有决定 | 内容不变；引用名同步 | ✓ |

讨论状态：维持 **`ready-for-implementation`**（本轮新增 ORD/EXP 是 idea-pmo 边界精化 + 试跑计划，不影响过程闭合判定）

同步完成时间：**2026-05-27**（用户全部确认；DECISIONS.md + skills/ 已落实；proj-run 骨架已创建；完整工作流等 EXP-04 试跑后开 08 轮）。

## 开放问题（本轮答复）

1. **ORD-15 + ORD-16 + ORD-17 + EXP-04 是否一并确认入表？** → **Q1=a 一并**（已落实）
2. **新 skill 命名定哪个？** → **Q2.1=c**（用户选 `proj-*` 前缀体系，重命名所有 4 个 skill 为 `proj-experts` / `proj-shape` / `proj-plan` / `proj-run`）+ **Q2.2=a 中文双层标题** + **Q2.3=a 立即重命名**（已落实）
3. **本轮决定通过后，立即落实哪些？** → **Q3=b ORD-15 + proj-run 骨架**（已落实）
4. **EXP-04 试跑选哪个项目？** → **Q4=a proj-experts 加 i18n**（已记入 DECISIONS）
5. **proj-run 完整 SKILL.md 何时起草？** → **Q5=a EXP-04 passed 后开 08 轮**（已记入 DECISIONS）

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-27 | sub-agent model-tier 编排讨论；4 视角推理 + EXP-04 草案；不违反 INV-04 |
| 1.1 | 2026-05-27 | 用户 @追问拆分独立 skill；新增 §讨论 5 + ORD-17 草案（idea-execute）；ORD-15/16 措辞调整；Q1-Q5 5 选项 |
| 1.2 | 2026-05-27 | 用户全部确认（Q1=a / Q2.1=c / Q2.2=a / Q2.3=a / Q3=b / Q4=a / Q5=a）；集体重命名（旧 idea-* + best-minds-grounded → proj-*）；DECISIONS.md 同步；proj-run 骨架创建；本文档状态 → confirmed · synced；命名 `idea-execute` → `proj-run` |
| 1.3 | 2026-05-27 | 用户追问 EXP 案例 → 追加 §讨论 6 案例精化：EXP-04 案例从"proj-experts i18n"（不能验证 model-tier 价值）改为"proj-run 完整 SKILL.md + assets 起草"（自然嵌套）；EXP-03 废止 N/A（本仓库不天然有 TR-04 项目）；DECISIONS.md 已同步 |
