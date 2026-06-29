# 12-proj-run 通用化 + 唯一入口 orchestrator + loop engineering

| 字段 | 值 |
|------|-----|
| 轮次 | 12 |
| 主题 | 把 proj-run 改为「通用 + 用户唯一入口」并应用 loop engineering 形成规划-执行-验证闭环——可行性与架构设计 |
| 日期 | 2026-06-29 |
| 状态 | confirmed（用户已拍板 4 大 fork → ORD-28~31）|
| 讨论方法 | `proj-experts` |
| 写入格式 | 完整（架构/方向争议轮）|
| 承接 | proj-run SKILL.md（已发布 stable）；INV-04（规划≠执行）+ ORD-17/18（proj-run=PMP Executing 承载者）+ ORD-19（3 Mode α/β/γ · Cursor 相关）+ ORD-16（Cursor sub-agent 约束）|

## 用户输入（本轮）

> 关于 proj-run 这个 skill，我有一些新的想法。现在的设计是基于 cursor 的，但我觉得 proj-run 应该改成通用的，且是用户使用的唯一入口，用户不需要去手动调用其他 skill，用户描述/提出问题，由 AI 判断是否需要调用什么工具，由 proj-run 去代理与用户的交互，其他 skill 是底层的工具。而且我觉得还可以在 proj-run 上去应用 loop engineering，形成规划-执行-验证的循环闭环。

拆成 4 个诉求：
1. **通用化** — proj-run 现在 Cursor 专属，改成 runtime 无关。
2. **唯一入口** — 用户只跟 proj-run 交互，不手动调其他 skill。
3. **AI 自动路由 + 代理交互** — AI 判断调用哪个工具；其他 skill 降为底层工具。
4. **loop engineering** — 在 proj-run 上做规划-执行-验证闭环。

> **proj-shape 边界说明**：本 skill 只产出设计决定（候选 ORD）+ 架构 + 可验证尝试（EXP）+ 继续/中止判据；**不写** 编码步骤与排期。诉求里「详细实现方案」在本轮 = 架构与决定层；真正的 phase 级实现计划由 **proj-plan** 承接（恰好是本轮被讨论的 skill 之一）。

## 事实与假设

### 轻量框定（查证前问题清单）

| # | 待查问题 | 查证结论（摘要） |
|---|----------|------------------|
| Q1 | 「用户不手动调 skill，AI 判断调哪个」在 Agent Skills 平台是不是已经原生具备？ | **是**——Agent Skills 默认 model-invoked，host 每轮读各 skill `description` 做纯 LLM 推理决定加载哪个，无路由代码 [Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |
| Q2 | 「唯一入口 + 把任务拆给固定的几个专家 skill」对应哪个成熟 agent 模式？ | **Supervisor / Routing**（固定专家集）而非 Orchestrator-workers（运行时动态生成子任务）[Agent Patterns Catalog](https://www.agentpatternscatalog.org/patterns/orchestrator-workers/) + [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| Q3 | 「loop engineering」是不是一个有出处的成熟概念？包含哪些要件？ | **是**——Addy Osmani 2026-06 命名；5 要件 = trigger / verifiable goal / actions(tools) / external verification / memory [Loop Engineering](https://addyo.substack.com/p/loop-engineering) |
| Q4 | 全自主 loop 与本项目「人在环（Supervised-AI mode）」是否冲突？ | 有张力——loop engineering 默认「把你从环里拿掉」；但 Karpathy 主张 autonomy slider + keep AI on the leash + 人做 verifier [Karpathy YC 2025](https://www.latent.space/p/s3) |

### 已查证事实

- **F1 · Agent Skills 默认 model-invoked（关键事实，直接影响诉求 2/3）**：host 启动时只把各 skill 的 `name`+`description`（约 100 token/skill）放进上下文；用户发 prompt 后，host **用纯 LLM 推理**判断意图是否匹配某 skill 的 description，匹配则加载完整 SKILL.md（progressive disclosure）。"no regex, no keyword matching, no ML-based intent detection... decision happens inside Claude's forward pass" [Lee Hanchung 深度解析](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/) + [Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)。`disable-model-invocation: true` 可让某 skill 只能被用户手动 `/name` 调用 [cnblogs 译](https://www.cnblogs.com/YzpJason/p/19591391)。
- **F2 · Supervisor vs Orchestrator-workers 的区分**："Supervisor routes work to a fixed set of pre-existing specialist agents; orchestrator-workers decides the sub-tasks at run time." [Agent Patterns Catalog](https://www.agentpatternscatalog.org/patterns/orchestrator-workers/)。proj-* 是**固定的 5 个既有专家**，所以用户诉求对应 **Supervisor + Routing**，不是 Orchestrator-workers。
- **F3 · Anthropic「先求最简，必要才加复杂度」**："find the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all... Routing classifies an input and directs it to a specialized followup task." [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **F4 · Loop engineering 5 要件 + 验证必须外置**：trigger（schedule/event/用户）、verifiable goal、actions(tools)、**external verification**（单测/二号模型，别让写代码的 agent 自评）、memory。"you split the verifier sub-agent from the maker to make the loop's 'it's done' mean something... 'done' is a claim and not a proof." `/loop` 按节奏重跑，`/goal` 跑到可验证停机条件成立 [Loop Engineering · Addy Osmani](https://addyo.substack.com/p/loop-engineering)。注：用户本机已装 `loop` skill（`/loop 5m /foo`）。
- **F5 · Flow engineering（loop 的近亲，更聚焦单任务内迭代）**：AlphaCodium（CodiumAI）提出，plan→generate→run tests→fix→iterate；GPT-4 pass@5 19%→44%。"Generating additional useful tests is easier than generating correct code." [arXiv 2401.08500](https://arxiv.gg/abs/2401.08500)
- **F6 · Karpathy partial autonomy / autonomy slider**："keep AI on the leash" + "generation-verification loop" + "humans in the loop... it's the decade of agents not the year"；"Demo is works.any(), product is works.all()" [Latent Space · Karpathy S3](https://www.latent.space/p/s3) + [YC keynote](https://www.youtube.com/watch?v=LCEmiRjPEtQ)

### 推理（非事实、非待验证）

- **推理 · proj-experts · 视角 A（Anthropic Applied AI）**：用户说的「唯一入口、AI 判断调用」在「单次路由」层面**已被 host 的 model-invocation 实现**（F1）。所以新建一个 prompt-only 的「路由器」去决定调哪个 skill，会**部分重复** host 已做的事，触碰 F3「别为了 agent 而 agent」。真正未被覆盖的增量 = **跨 skill 的有状态序列 + GATE/loop 编排**（host 的路由是无状态单次的，不懂 experts→shape→plan→run 的先后与 gate）。依据 [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) 的 routing/orchestrator 区分。
- **推理 · proj-experts · 视角 B（Loop engineering · Osmani）**：proj-* 已经零散具备 loop 5 要件——trigger=用户请求；verifiable goal=INV/ORD 成功标准；actions=5 个 skill + sub-agent dispatch；external verification=validation gate（ORD-22）+ GATE-N + circuit breaker；memory=DECISIONS.md + docs/pmo artifacts。所以 loop engineering 在本项目**主要是命名 + 接线**（把已存在的件接成显式外层 loop），**真正新的**是「按 verification 结果决定下一步跑哪个 skill」的**外层重路由 loop**。这与 ORD-27 给 JIT「命名既有机制 + 补判据」是同构动作。依据 [Loop Engineering 5 building blocks](https://addyo.substack.com/p/loop-engineering)。
- **推理 · proj-experts · 视角 C（Karpathy · partial autonomy）**：loop engineering 原文默认「把人拿出环」（F4），与本项目 INV 精神（Supervised-AI mode · 人审 GATE）直接张力。建设性消解 = 把 loop 做成**有界 loop + autonomy slider**：phase 内自迭代（plan→execute→verify），到 GATE 处**停下交人**；现有 GATE-0/1/2/3 + circuit breaker 就是「leash」。这样 loop 与人在环不是二选一，而是 autonomy slider 上的一档。依据 [Karpathy autonomy slider / keep on leash](https://www.latent.space/p/s3)。

### 待验证 / 未查证

- **U1**：一个 **prompt-only 的 SKILL.md orchestrator** 能否可靠驱动跨 skill 的有状态 loop（而不是与 host 原生 model-invocation 互相抢路由 / 双重触发）。→ EXP-07。
- **U2**：proj-run 的 dispatch 层（3 Mode α/β/γ）能否被抽象成 runtime 无关接口 + 适配器，而不丢现有能力、也不比直接写更复杂。→ EXP-08。
- **U3**（非阻塞）：「唯一入口」在 skills 世界靠的是 orchestrator 的 description 足够「广」以接住泛化请求——description 过广可能与其他 skill 触发冲突（F1 的 conflict resolution）。属落地措辞问题，留 proj-plan/落地阶段。

### 方法专属输出（proj-experts）

#### 视角 A · Anthropic Applied AI（Building Effective Agents 作者立场 · Schluntz/Zhang）

**选用理由**：本题核心争议轴 = 「该不该建一个路由/编排层」。Anthropic 这篇是 routing / orchestrator-workers / 「先求最简」的权威出处，且 Agent Skills model-invocation 是其平台行为。

**【已公开立场】**：(1) 「先找最简方案，必要才加复杂度，可能根本不用 agentic 系统」；(2) Routing = 把输入分类后导向专门后续任务；Orchestrator-workers 的关键是**子任务运行时才确定**。[Anthropic](https://www.anthropic.com/engineering/building-effective-agents)

**【模拟推理】**：依据上面两条 + F1（Skills 已 model-invoked）+ F2（proj-* 是固定专家集），推理路径：用户要的「AI 判断调哪个 skill」≈ Routing，而 Routing 的单次版**host 已经做了**；proj-* 是**固定** 5 专家 → 不是 orchestrator-workers（不需要运行时造子任务）→ 所以新层若只做「选哪个 skill」是重复造轮子；新层**唯一站得住的职责** = host 给不了的**跨 skill 有状态序列 + gate + loop**（= Supervisor 模式 + 一个状态机）。

**关切 → 路径**：关切 = 建独立 orchestrator skill 可能与 host model-invocation 双重路由、违反「先求最简」。达成原目标的路径 = 把新层职责**显式收窄**为「pipeline 状态机 + loop + GATE 编排 + facade」，并在 SKILL.md 写明「**不**重做 host 的 skill 选择」；或更简的 C 方案（不建 skill，只在 pipeline 文档写入口+loop 约定）。

#### 视角 B · Addy Osmani（Loop Engineering 命名者）

**选用理由**：用户第 4 诉求直接用了「loop engineering」这个词；Osmani 是该词 2026-06 的命名者与 5 要件定义者。

**【原话】**："A loop here can be thought of as a recursive goal where you define a purpose and the AI iterates until complete." / "you split the verifier sub-agent from the maker to make the loop's 'it's done' mean something... 'done' is a claim and not a proof." [addyo.substack.com](https://addyo.substack.com/p/loop-engineering)

**【模拟推理】**：依据 5 要件，把 proj-* 现有件逐一对位（见视角 B 推理条）——结论是 loop engineering 在本项目 = **命名 + 接线既有件**，新增的只有「按 verification 结果重路由下一个 skill」的外层循环。最关键的「verification 外置、maker≠grader」原则**已经**被 proj-run ORD-22 validation gate（父 agent 跑、sub-agent 不自评）满足——这是本项目已具备的强基础。

**关切 → 路径**：关切 = loop 默认无人值守会「无人值守地犯错」（Osmani 原话警告）。路径 = 见视角 C：有界 loop + GATE 停。

#### 视角 C · Andrej Karpathy（partial autonomy / autonomy slider）

**选用理由**：本题最大设计张力 = 「自主 loop」vs 本项目 INV「人审 GATE（Supervised-AI mode，已由 ORD-11 确立）」。Karpathy 是 autonomy slider / keep-on-leash / 人在环的最直接出处，且本项目既有讨论（ORD-11/12）已大量引用其「LLM as simulator」。

**【原话】**："it's less Iron Man robots and more Iron Man suits that you want to build... build partial autonomy products... there should be an autonomy slider in your product." / "keep the AI on the leash." [Karpathy YC keynote 转录](https://www.latent.space/p/s3)

**【模拟推理】**：依据 autonomy slider + generation-verification loop，推理路径：不要把 proj-run 的 loop 设计成「全自主 /goal 一把梭」；设计成**滑杆**——默认档 = phase 内自迭代、到 GATE 停交人审（对齐现有 INV + circuit breaker）；高自主档 = 用户显式授权某 phase 全自动（仍保留 circuit breaker 兜底）。这恰好把 Osmani 的 loop 与本项目的人在环 INV 调和成「同一根滑杆上的两档」，而非互斥。

**关切 → 路径**：关切 = 「唯一入口 + 自主 loop」若做过头，会让用户失去 Karpathy 强调的「快速人审小 diff」能力（"works.any() vs works.all()"）。路径 = loop 每跑完一档产出**人可快速验收的小单元**（acceptance.md + DECISIONS diff），而非一次吐一大坨。

#### 收敛（【模拟推理】，非任一专家原话）

三视角一致收敛到：**诉求方向可行且有真实出处支撑，但「唯一入口/AI 路由」的多数能力 host 已原生具备，真正的增量是「跨 skill 有状态 loop + GATE 编排 + facade」**。因此：
1. 把「genericize proj-run」与「新增 orchestrator 入口」拆成**两个正交决定**（前者是 proj-run 内部去 Cursor 化；后者是流水线之上的新层）。
2. orchestrator 职责**收窄**为 Supervisor + 状态机 + 有界 loop，明确不重做 host 路由。
3. loop = autonomy slider 上「phase 内自迭代 / GATE 停」一档，调和 INV。

## 讨论

### 诉求 1 · 通用化 proj-run（去 Cursor 化）——可行，且与诉求 2/3/4 正交

proj-run 是 5 个 skill 里**唯一**重度 Cursor 绑定的（3 Mode α/β/γ、`.cursor/agents/`、ORD-16 Cursor sub-agent 约束、Task tool）；experts/shape/plan/survey 基本 runtime 无关。所以「通用化」= 把 proj-run 的 **dispatch 层**抽象成一个 runtime 无关接口（「dispatch capability」），Cursor 是其中一个适配器，另可加 Claude Code subagents 适配器 / 纯对话 fallback 适配器。

- 这件事**不依赖**诉求 2/3/4，可单独做（候选 ORD-A 把它独立出来）。
- 风险（→ EXP-08）：抽象后若 Cursor 专属能力大量从接口缝里漏出来，或接口比「直接写」更绕，就违反简约。降级路径 B = proj-run 保留 Cursor 实现 + 文档注明「其他 runtime 自行适配」，不强抽象。

### 诉求 2/3 · 唯一入口 + AI 自动路由——大部分 host 已做，增量在「有状态」

这是本轮**最重要的纠偏**（视角 A + F1）：

| 用户想要的 | host（Claude Code/Cursor）是否已提供 | 真正的缺口 |
|------------|--------------------------------------|------------|
| 用户不手动调 skill | ✅ skills 默认 model-invoked | — |
| AI 判断调哪个 skill | ✅ 每轮按 description 纯 LLM 推理 | — |
| 单次把请求导向某专家 | ✅ = Routing，host 内建 | — |
| **跨 skill 的先后序列**（experts→shape→plan→run）+ **gate** + **按验证结果重路由** | ❌ host 路由是无状态单次的 | **这才是要建的东西** |

所以「proj-run 作为唯一入口」若理解成「重做一个路由器决定调哪个 skill」= 重复 host 已做的（违反 F3 简约）。若理解成「一个懂 pipeline 先后 + gate + loop 的 **Supervisor/状态机**」= 真实增量。**建议按后者定义**（候选 ORD-B）。

「代理与用户的交互」在这个定义下成立且有价值：Supervisor 持有 DECISIONS/pipeline 状态，知道现在该问用户哪个 GATE、该把哪个 skill 的产出摊给用户看——这是 host 无状态路由给不了的。

### 诉求 1+2+3 合并的**形态三选一**（Fork 1 · 待用户拍板）

| 选项 | 做法 | 优点 | 代价 / 风险 |
|------|------|------|-------------|
| **A. repurpose proj-run** | 把 proj-run 本身改成入口 orchestrator | 符合用户字面表述（「proj-run 改成…」）| **破坏 PMP 4 过程组干净映射**（proj-run = Executing 是 ORD-17/18 + 与 experts/shape/plan 并列的定位）；「run/执行调度」之名误导；Executing 职责被稀释 |
| **B. 新建薄 orchestrator skill（如 `proj`）置于流水线之上** | 新 skill 只做 Supervisor+状态机+loop+facade；proj-run 仍专管 Executing；通用化作为独立 ORD | 保住 PMP 干净映射；职责单一；新层薄 | 多一个 skill；需保证它不与 host model-invocation 抢路由（→ EXP-07）|
| **C. 最小方案 · 不建 skill** | 在 README / 一份 pipeline 文档里写「入口 + loop + 跨 skill 状态契约」约定，靠 host model-invocation + 各 skill 既有「不触发本 skill→回退」守卫自然串起来 | 最简约（贴合你 rule #2）；零新增 skill；改动外科手术级 | 「唯一入口」体验最弱（没有一个显式被调的 facade）；loop 编排靠文档约定而非可执行 skill，约束力弱 |

**倾向**：B（薄 orchestrator skill）做入口+loop，**叠加**一个独立 ORD 做 proj-run 通用化；并把 C 作为 EXP-07 失败时的降级路径 B。理由：B 既给「唯一入口」一个真实落点，又不破坏既有 PMP 映射；薄身保证不过度工程。但**这是方向性选择，应由你拍板**——尤其 A vs B 关乎是否动 ORD-17/18。

> 任何 fork 都**不应推翻 INV-04**（规划≠执行）：orchestrator 是更上层的调度者，它**调用** proj-plan 与 proj-run，而不是把执行塞进规划。这条是边界护栏。

### 诉求 4 · loop engineering——命名+接线既有件 + 一条新外层 loop + autonomy slider

对位 5 要件（视角 B）：

| loop 要件 | proj-* 现有落点 | 缺口 |
|-----------|----------------|------|
| trigger | 用户请求（入口）| — |
| verifiable goal | INV/ORD 成功标准 + validation gate（ORD-22）| — |
| actions/tools | 5 skill + sub-agent dispatch | — |
| external verification | validation gate + GATE-N + circuit breaker（**maker≠grader 已满足**）| — |
| memory | DECISIONS.md + docs/pmo + acceptance.md | — |
| **外层重路由** | （无）按 verification 结果决定下一个跑哪个 skill | **新增** |

所以 loop engineering ≈ ORD-27 式动作（命名既有 + 补一条判据/接线），新增的只有外层 loop。关键设计 = **有界 loop + autonomy slider**（视角 C）：默认 phase 内自迭代、到 GATE 停交人；circuit breaker 是硬护栏。这调和了 Osmani 的「无人值守 loop」与本项目 Supervised-AI INV——做成滑杆的两档而非二选一。

### 可行性结论

**可行**。四个诉求都有真实出处支撑、与既有架构无根本冲突。两点必须钉住以免走偏：
1. 别把「唯一入口/AI 路由」做成重复 host model-invocation 的路由器（F1/F3）——增量在「有状态 loop + gate 编排」。
2. loop 必须是「有界 + GATE 停 + autonomy slider」，不能推翻人审 GATE 的 INV（视角 C）。

## 可验证尝试与继续/中止

### EXP-07（草案）· prompt-only orchestrator 能否可靠驱动跨 skill 有状态 loop

| 项 | 内容 |
|----|------|
| 假设 | 一个薄 orchestrator skill 能可靠驱动 experts→shape→plan→run 的有状态 loop（含 GATE 停 + 按验证结果重路由），且**不**与 host 原生 model-invocation 互相抢路由/双重触发 |
| 尝试方案 | 在本仓库选 1 个真实小任务（如「给某 skill 加一节」），分两条跑：(基线) 无 orchestrator，纯靠 host model-invocation 逐个触发 skill；(实验) 经 orchestrator 全程驱动。对比两者 |
| 成功信号 | orchestrator 路径在三项上 ≥ 基线：①按正确 pipeline 顺序触发；②在 GATE 处确实停下交人；③DECISIONS/artifacts 一致更新；且**无**与 host 路由的重复触发/打架 |
| **继续** | 三项达标且无路由冲突 → 固化为薄 orchestrator skill（Fork 1 选 B）|
| **中止** | orchestrator 与 host model-invocation 双重路由/互相打架，或并不优于基线 → 降级路径 B：放弃独立 orchestrator，改 **Fork 1 选 C**（pipeline 文档 + 跨 skill 状态契约，不建 skill）|
| 来源 | `12-…md` §诉求 2/3 + Fork 1；推理 · proj-experts 视角 A；依据 [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) + [Agent Skills model-invocation](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |

### EXP-08（草案）· proj-run dispatch 能否 runtime 无关化

| 项 | 内容 |
|----|------|
| 假设 | proj-run 的 3 Mode dispatch 可抽象成 runtime 无关「dispatch capability」接口 + 适配器，不丢现有能力、也不比直接写更复杂 |
| 尝试方案 | 把 α/β/γ 抽象成接口；写 Cursor 适配器 + ≥1 个非 Cursor 适配器骨架（Claude Code subagents 或纯对话 fallback）；在本仓库跑一次 dispatch+validation |
| 成功信号 | 同一 plan.md 在 ≥2 runtime 下都能驱动一次 dispatch + validation；SKILL.md 核心流程无 runtime 专属硬编码 |
| **继续** | 达标 → genericize proj-run（候选 ORD-A）|
| **中止** | Cursor 专属能力大量泄漏 / 接口比直接写更复杂 → 降级路径 B：proj-run 保留 Cursor 实现 + 文档注明「其他 runtime 自行适配」，不强抽象 |
| 来源 | `12-…md` §诉求 1；推理 · proj-experts 视角 A；依据 ORD-16/19（Cursor 约束 + 3 Mode）|

## 本轮决定

> 本轮为**架构争议轮**，4 大 fork 均需用户拍板；故**不向 DECISIONS.md 写入任何已确定决定**，仅登记 EXP 草案 + 讨论状态。下列为**候选**，待确认后才升 ORD。

### 已确定 — 原则性不变量（新增/修订）

- 无。

### 已确定 — 普通决定（新增/修订）

> 用户本轮拍板 4 大 fork：Fork1=**B**（新建薄 skill）、Fork4=**bounded**、通用化时机=**separate**、命名=**`proj`**。候选 ORD-A~D 据此定稿为 ORD-28~31。

- [x] **决定 → ORD-28**（原候选 ORD-A）：把「genericize proj-run（去 Cursor 化 · dispatch capability 接口 + 适配器）」与「新增 orchestrator 入口」**拆成两个正交决定**；通用化作为**独立后续**推进（不在本期），本期聚焦 orchestrator + loop。
  **来源**：`12-…md` §诉求 1 + §Fork 1；用户 @本轮（generic_timing=separate）；推理 · proj-experts 视角 A
  → 同步至 DECISIONS.md `ORD-28`
- [x] **决定 → ORD-29**（原候选 ORD-C · Fork 1=B）：新增**薄 orchestrator skill `proj`** 置于 proj-* 流水线之上，作为用户**总入口 / facade**，调用 experts/shape/plan/survey/run 各专家；**proj-run 保持 PMP Executing 定位不变**（ORD-17/18 不动，INV-04 不触及）。
  **来源**：`12-…md` §Fork 1 三选一表；用户 @本轮（fork1=B, naming=proj）；推理 · proj-experts 视角 A（Supervisor 模式）；依据 [Agent Patterns Catalog](https://www.agentpatternscatalog.org/patterns/orchestrator-workers/)
  → 同步至 DECISIONS.md `ORD-29`
- [x] **决定 → ORD-30**（原候选 ORD-B）：`proj` 职责**收窄** = 跨 skill 状态机 + 规划-执行-验证 loop + GATE 编排 + facade；**不重做** host 原生 model-invocation 的 skill 选择（避免重复 host 已做的事 + 简约）。
  **来源**：`12-…md` §诉求 2/3；推理 · proj-experts 视角 A；依据 [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) + [Agent Skills model-invocation](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
  → 同步至 DECISIONS.md `ORD-30`
- [x] **决定 → ORD-31**（原候选 ORD-D · Fork 4=bounded）：`proj` 的 loop = **有界 loop + autonomy slider**（phase 内自迭代、到 GATE 停交人、circuit breaker 兜底）；loop 5 要件映射既有 trigger/goal/tools/verification(ORD-22)/memory(DECISIONS+artifacts)，**命名+接线**而非新机制（类比 ORD-27），新增仅「外层重路由 loop」。
  **来源**：`12-…md` §诉求 4；用户 @本轮（fork4=bounded）；推理 · proj-experts 视角 B/C；依据 [Loop Engineering · Osmani](https://addyo.substack.com/p/loop-engineering) + [Karpathy autonomy slider](https://www.latent.space/p/s3)
  → 同步至 DECISIONS.md `ORD-31`

### 对既有决定的修订

- 无。Fork 1 选 B → **不触及** ORD-17/18（proj-run 仍专管 Executing）；INV-04 不变（`proj` 是更上层调度者，调用 plan/run，不把执行塞进规划）。

### 待确认（下轮继续）

- 无未闭合 fork（4 个已拍板）。**剩余为落地阶段验证**：EXP-07（`proj` orchestrator 可靠性，中止→降级 Fork C）+ EXP-08（proj-run 通用化，独立后续）。
- 进入落地（交 proj-plan 起草 `proj`）须用户**显式确认开工**；本轮未单方面设 `ready-for-implementation`。

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-28 | 新增 | ✓ |
| ORD-29 | 新增 | ✓ |
| ORD-30 | 新增 | ✓ |
| ORD-31 | 新增 | ✓ |
| EXP-07 | 新增（pending）| ✓ |
| EXP-08 | 新增（pending）| ✓ |

讨论状态同步：维持 `exploring`（4 大 fork 已拍板 → ORD-28~31 确立；但 `proj` 的核心可行性系于 EXP-07 尚未跑、且用户未显式确认开工，故未升 `ready-for-implementation`；现有 5 skill 仍 shipped/stable；proj-survey 线 EXP-06 未变）

同步完成时间：2026-06-29 10:55

## 开放问题（下轮 · 已用 AskQuestion 抛给用户）

1. **Fork 1**：orchestrator 形态 = A repurpose proj-run / B 新建薄 skill / C 最小 pipeline 文档？
2. **Fork 4**：loop 自主度默认档 = 有界+GATE 停（推荐）/ 更高自主？
3. **通用化时机**：proj-run 去 Cursor 化（ORD-A）本期与 orchestrator 一起做，还是独立后续？
4. **命名**（若 Fork 1 选 B）：`proj` / `proj-orchestrate` / `proj-flow` / `proj-loop`？

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-06-29 | 初稿：proj-run 通用化 + 唯一入口 orchestrator + loop engineering 可行性与架构；grounded（Anthropic/Osmani/Karpathy）；候选 ORD-A~D 待拍板；EXP-07/08 草案 |
| 1.1 | 2026-06-29 | 用户拍板 4 fork（B/bounded/separate/`proj`）→ 候选 ORD-A~D 定稿为 ORD-28~31，同步 DECISIONS；维持 exploring（未显式开工）|

## 同步注记（2026-06-29 · EXP-07 试跑）

- 用户选「先跑 EXP-07 验证可行性」→ 在 `docs/pmo/proj-orchestrator-spike/` 建薄 orchestrator spike（`proj-spike-SKILL.md`）并在本仓库 dogfood 一个真实小任务（给 proj-run 加 forward-ref 节，产出 proposed diff，未改 shipped skill）。
- **结果 = EXP-07 passed (with caveats)**：三项成功信号实验臂全 ≥ 基线（顺序触发 / GATE 停交人 / MEMORY 回写）；**Cursor 下无路由冲突**（skills = read-and-follow，无第二路由引擎双触发）；过程复现 proj-run F9（`grep -c` 双计）。
- **caveat**：单一小受控 dogfood，未压测 experts→shape→plan→run 冷启动全遍历 + 失败 re-route 多迭代；路由冲突结论仅 Cursor 成立（Claude Code 留 EXP-08/ORD-28 的 `disable-model-invocation` 缓解）。
- **后续**：EXP-07 达标 → 不触发降级路径 C；继续 Fork B（交 proj-plan 起草 `proj`，把两条未压测路径作首批验证 phase）。已同步 DECISIONS.md EXP-07 状态 + 变更日志。详见 `docs/pmo/proj-orchestrator-spike/exp-07-result.md`。
- **落地完成（同日）**：用户授权 → proj-plan(T-lean · `docs/pmo/proj-draft/`) GATE-0 + GATE-1+2+3 合并全过 → **`proj` v1 shipped**（`skills/proj/SKILL.md` 142 行 · validate 6/6 退 0 · acceptance 全过）；ORD-29/30/31 落实、README 扩 6 skill、proj-run「规划中」转正。两条 loop 形态仅设计层覆盖 → 转 **EXP-07b**（真实压测 · pending · 不阻塞 v1）。

## 同步注记（2026-06-29 · EXP-08 + ORD-28 落地）

- 用户选「先 ORD-28/EXP-08」→ 在 `docs/pmo/proj-run-generic-spike/` 跑 EXP-08 spike（接口 + 3 adapter + conversation-fallback 实跑 dispatch+validation），未改 shipped skill。
- **结果 = EXP-08 passed**：①≥2 runtime = conversation-fallback 实跑（spawn→collect→validate 全 PASS · 含 5 字段闭环 + cursor-token=0 负断言）+ Cursor adapter EXP-04 历史验证；②核心流程无 runtime 专属硬编码（core 7 组件中 5 个本就 runtime 无关，不动）；**关键发现**：抽象面极小（仅「spawn+collect」），3 Mode 降为 cursor adapter 内部策略、0 能力丢失 → **未触发 abort 条件**（不比直接写更复杂）。
- **caveat**：claude-code adapter 仅骨架（`model_selectable=true` 路径未实跑，无 Claude Code 环境）→ 转 **EXP-08b**（pending · 非阻塞）。
- **落地（同日 · 用户授权 full apply）**：`skills/proj-run/SKILL.md` dispatch 层重构为 **DispatchCapability 接口 + cursor/conversation-fallback/claude-code 三 adapter**；ORD-16 降为 cursor adapter `model_selectable=false` 属性；README 同步；validate 6/6 退 0。已同步 DECISIONS.md（ORD-28 已落实 / EXP-08 passed / EXP-08b 新增 / 变更日志 / 状态行）。详见 `docs/pmo/proj-run-generic-spike/exp-08-result.md`。

## 同步注记（2026-06-29 · EXP-07b 压测）

- 用户选「EXP-07b」→ 在 `docs/pmo/proj-07b-spike/` 跑沙盒 dogfood，压测 `proj` 两条 loop 形态（EXP-07 caveat 1 未覆盖面），不污染 live DECISIONS、不碰 shipped skill。
- 驱动任务（真实小自指）：「DECISIONS.md 是否加机读 `pipeline-state` 块稳化 CLASSIFY」，天然横跨 experts→shape→plan→run 4 段。
- **结果 = EXP-07b passed（S1–S8 全达标）**：①**冷启动全遍历**真从 experts 起跑、无跳段/乱序、3 GATE 正确识别为停点、MEMORY 逐步回写、run 段真实 grep VERIFY（防 F9）；②**失败 RE-ROUTE** 注入真实 VERIFY 失败 → 父外置检出（maker≠grader）→ budget 内重试通过 + harness 证 budget 耗尽→escalate / 累计>3→circuit breaker **有限终止**（无死循环）；③S8 无路由冲突（延续 Cursor 结论）。
- **EXP-07 caveat 1 闭合** → `proj` v1 标 **stable**。**caveat**：单一沙盒、专家段压缩版、escalate/cb 由控制逻辑 harness 证、GATE 经 EXP 授权自动续跑（非 live 人审）。已同步 DECISIONS.md（EXP-07b passed + 状态行 + 变更日志）。详见 `docs/pmo/proj-07b-spike/exp-07b-result.md`。

## 同步注记（2026-06-29 · EXP-08b · spec-ready / 实跑阻塞于登录）

- 用户选「EXP-08b」→ 验本机 Claude Code 环境：`claude` **v2.1.81 已装**、`~/.claude` 有 config，但 `claude -p` 返回 **`Not logged in`**，且无 `ANTHROPIC_API_KEY`/`CLAUDE_CODE_OAUTH_TOKEN`。
- **实证硬化（非记忆 · 直接 CLI 验证）**：`--model <alias|full>` 存在 → **CLI 层 model 可选**（`model_selectable=true` 直接证据，**与 Cursor ORD-16「subagent model 被 server 忽略」相反**）；`--agents <json>`（native subagent）/ `-p` headless / `--output-format json`（`modelUsage`）/ `--max-budget-usd` / `--permission-mode acceptEdits` 齐 → 受控 dispatch 已 wired。
- **阻塞**：真实 spawn 需用户先 `claude /login`（交互 OAuth · 不可代办）。已在 `adapters.md §3` 写**一条 ready-to-run 命令**（headless dispatch + collect + VERIFY + model 校验），登录后即可一步实跑。
- **用户拍板 = accept_partial**：EXP-08b 标 **spec-ready / 实跑阻塞于登录**（model_selectable=true 已由 `--model` flag 佐证）；非阻塞 `proj` v1。已同步 DECISIONS.md（EXP-08b 实验行 + 状态行 + 变更日志）。
