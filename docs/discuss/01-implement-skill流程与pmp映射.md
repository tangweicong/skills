# 01-implement-skill流程与pmp映射

> **2026-05-27 命名变更注记（轮次 07 决定）**：skills 集体重命名：`best-minds-grounded` → `proj-experts`、`idea-discuss` → `proj-shape`、`idea-pmo` → `proj-plan`；新增 `proj-run`（执行调度，骨架版）。本文档作为历史快照沿用讨论时的旧名，**正文不动**；引用时按上表换算。完整说明见 `07-sub-agent-model-tier-编排.md` + `DECISIONS.md`。

| 字段 | 值 |
|------|-----|
| 轮次 | 01 |
| 主题 | 落地 skill 流程定位：轻量 PMP × Shape Up × SDD 映射 |
| 日期 | 2026-05-19 |
| 状态 | discussed |
| 分析层 | best-minds-grounded（完整执行） |

## 用户输入（本轮）

### 原始问题（@2026-05-19 初）

用户反馈当前 `idea-implement`「效果不太对」：

1. **细节不明确** — skill 边界、层次不清。
2. **流程不满意** — 应是 discuss 之后的**总结、设计、规划**；**不限技术**，任何领域适用。
3. **层次错位** — **高维、粗粒度、指导性**；细节应在**进入具体阶段**时再定。
4. **PMP 直觉** — `discuss` ≈ 可行性分析；落地 skill ≈ 项目启动 + 章程授权 + WBS 词典 + WBS 分解 → 再执行阶段设计。
5. **重量担忧** — 喜欢 PMP 项目化思维，但怕流程太重；AI 可写文档，**人读的信息量**仍可能过大。

### 补正请求（同日复盘）

- 首轮分析**未按** `idea-discuss` 要求走 `best-minds-grounded`，仅做了泛 WebSearch + agent 归纳。
- 要求：**按 idea-discuss 完整流程重做**，重写相关 discuss 文档。

## 事实与假设

### best-minds-grounded · 轻量框定（查证前问题清单）

| # | 若 TA 在场，会先确认什么 | 为何重要 |
|---|--------------------------|----------|
| Q1 | PMBOK 对「小项目 / 个人项目」是否**官方主张裁剪（tailoring）**而非照搬全套？ | 回应「PMP 会不会太重」 |
| Q2 | 有无成熟的 **「粗规划 → 授权 → 细规划延后」** 分层范例（不限软件）？ | 回应层次错位 |
| Q3 | AI 工作流下如何控制 **人类阅读负担**（gate / rolling / 分 artifact）？ | 回应信息量担忧 |
| Q4 | `idea-discuss` 的 DECISIONS 在 industry artifact 中最接近什么？落地 skill 应补什么？ | 避免 discuss / implement 重复 |
| Q5 | 当前 `idea-implement` SKILL.md 的实际产出结构是什么？ | 对照用户意图找偏差 |

### 已查证事实

**PMBOK / PMI**

- PMBOK 第 7 版原则 **「Tailor based on context」**：项目管理**系统应匹配环境**，照搬大企业 PM 体系会失败（案例：中型公司聘用大厂 PM 一次性导入全套）。[Tailor based on context](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/)
- **何时裁剪**：对 minimalist 体系可**先少裁剪、随进展 gradual enrich**；「upfront tailoring 宜最小，否则易做出过重、过 formal 的系统」。[When to tailor](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s4-when-to-tailor/)
- **Rolling wave planning**（PMBOK 术语）：近期工作细规划，远期高层级；是 **progressive elaboration（渐进明细）** 的一种，适用于 waterfall 与 agile。[PM Study Circle / PMBOK 引述](https://pmstudycircle.com/rolling-wave-planning/)

**Ryan Singer · Shape Up**

- **Shaping 三属性**（公开原文）：工作应 **rough（留空间）**、**solved（宏观方案已连通）**、**bounded（明确不做什么）**；过细如 wireframe 会锁死；过粗如几个词则无法权衡。[Principles of Shaping](https://basecamp.com/shapeup/1.1-chapter-02)
- **双轨**：shaping track 与 building track **分离**；shaping 未完成的工作不进入 building；「work on the shaping track is kept private … until the commitment has been made to bet on it」。[Principles of Shaping §Two tracks](https://basecamp.com/shapeup/1.1-chapter-02)
- **Betting table**：shaped pitch 经利益相关方 **一次性授权** 后进入 cycle；「The highest people in the company are there. There's no step two to validate the plan」；**只 bet 一个 cycle ahead**，保持选项开放。[The Betting Table](https://basecamp.com/shapeup/2.2-chapter-08)
- **Circuit breaker**：周期内未 ship 则默认不延期，回到 shaping 重新 frame——与 EXP 中止 / 回 discuss 类似。[The Betting Table §Circuit breaker](https://basecamp.com/shapeup/2.2-chapter-08)
- **No backlogs**：不把 shaped 工作堆入无限 backlog；重要想法会带着 context 回来。[Bets, Not Backlogs](https://basecamp.com/shapeup/2.1-chapter-07)

**GitHub Spec Kit · SDD**

- 推荐链路：`constitution → specify → clarify/checklist → plan → tasks → analyze → implement`；**tasks 在 plan 之后**；production 路径含多个 **quality gate**。[Quick Start](https://github.github.com/spec-kit/quickstart.html)
- 内置 workflow 在 specify/plan 之间设 **gate**（approve/reject），防止未审 spec 进入 plan。[Workflows](https://github.github.com/spec-kit/reference/workflows.html)
- 复杂项目建议 **phased implementation**，避免 agent context 饱和。[Quick Start §Phased Implementation](https://github.github.com/spec-kit/quickstart.html)

**本仓库 skills（现状）**

- `idea-discuss`：产出 `DECISIONS.md`（INV/ORD/EXP）；**明确不含** MVP、排期、实现清单；讨论就绪 = 最小决策集闭合 + 未知变 EXP。[`skills/idea-discuss/SKILL.md`](../../skills/idea-discuss/SKILL.md)
- `idea-implement`（当前）：启动时产出 `architecture.md` + `phase-plan.md` + **同步** `phase-01/task-list` + `acceptance`；含阶段内直接执行工作流。[`skills/idea-implement/SKILL.md`](../../skills/idea-implement/SKILL.md)

### 专家视角讨论（best-minds-grounded）

#### 视角 A · PMBOK 裁剪派（代表：PMI 原则体系，非单人原话）

**会说的（有出处）**：你的「怕 PMP 太重」与官方一致——重的是 **未裁剪的 artifact 全集**，不是 PM 思维本身。对小/个人/AI 辅助项目，应 **minimal upfront tailoring + rolling elaboration**，而非启动时写满 WBS 词典。

**外推（非 PMI 原话）**：依据 tailoring + rolling wave 原则，`idea-discuss` 已完成的 DECISIONS 相当于 **business case + 关键约束**；落地 skill 的「启动包」人类必读应控制在 **1 页 charter + 1 页 WBS 树**；WBS 词典 L3+ 属于 planning 过程组，**进阶段再写**才符合 PMBOK 裁剪精神。

#### 视角 B · Ryan Singer（Shape Up）

**会说的（有出处）**：shaping 产出的是 **pitch**——rough + solved + bounded，不是 task 清单。building 周期内才展开实现细节。shaping 与 building 是 **两条轨**，且 betting table 是 **授权关口**。

**外推（非 Ryan 原话）**：依据 shaping/building 分离 + pitch 三属性，用户要的「高维总结与规划」≈ **对 DECISIONS 的 pitch 化综合**（charter），而非 `architecture.md` 这种易偏技术的命名。`idea-discuss` ≈ shaping track（含研究、权衡、EXP）；落地 skill 启动 ≈ **写 pitch + betting table（用户确认 charter）**；`phase-NN/plan` ≈ building cycle 内才展开的细项。当前 `idea-implement` 在启动时写 `phase-01/task-list`，相当于 **在 shaping 阶段交付 wireframe 级细节**，与 Shape Up 明确反对的做法同型。

#### 视角 C · Spec Kit / SDD 维护者

**会说的（有出处）**：artifact 严格分步：spec（what/why）→ plan（how 宏观）→ tasks（可执行）→ implement；中间有 **gate** 控制人审节点；大项目 **分 phase implement**。

**外推（非 Spec Kit 作者原话）**：依据 command 分层 + gate 设计，`DECISIONS` ≈ constitution + specify 的沉淀；落地 skill 缺的是 **plan 层（粗）与 tasks 层（细）的硬分离**，以及 **charter/WBS 批准 gate**。AI 可一次生成全部文档，但 skill 应规定 **gate 通过前不得生成 tasks**——这正是控制「信息量」的机制，而非少写 PMP 名词。

#### 三视角收敛（讨论层综合，非任一专家原话）

| 维度 | PMBOK 裁剪 | Shape Up | Spec Kit | 对 skill 设计的含意 |
|------|------------|----------|----------|---------------------|
| 讨论/可行性 | business case | shaping | specify/clarify | `idea-discuss` 已覆盖 |
| 综合叙述 | charter | pitch | constitution/spec | 落地 → **charter.md** |
| 粗分解 | L1-L2 WBS | bounded scope | plan | 落地 → **wbs.md**（≤2 层） |
| 授权 | sponsor sign-off | betting table | gate | 用户确认 charter |
| 细项 | rolling dictionary | build cycle | tasks | **phase-NN/plan** 进入时 |
| 控制重量 | minimal upfront | no backlog | gates | 人类必读 ≤2 页；tasks 延后 |

### 待验证 / 未查证

- 「charter + L1/L2 WBS + gate + 滚动 phase plan」在**非软件项目**（如装修、写作、组织变革）上的可读性 —— **EXP-01**。
- 规划 skill 与执行 skill **拆 vs 合** 哪种更符合你的使用习惯 —— 待用户确认。
- WBS 词典 **独立文件 vs 嵌入 wbs.md** —— **EXP-01** 试跑时对比。

## 讨论

### 1. 首轮分析缺了什么（过程复盘）

| idea-discuss 要求 | 首轮实际 | 后果 |
|-------------------|----------|------|
| 优先 best-minds-grounded | 仅 WebSearch + agent 外推 A–D | 结论方向大致对，但**不可追溯、无专家对照** |
| 事实 / 外推分离 | 外推无专家挂靠 | 用户无法评估建议权重 |
| 不写 MVP/排期 | ✓ 遵守 | — |

本轮已补：**轻量框定 → 定向查证 → 三专家视角 → 标注外推**。

### 2. 当前 idea-implement 相对用户意图的偏差（ grounded 后仍成立）

| 用户意图 | 当前 skill | 专家共识下的偏差 |
|----------|------------|------------------|
| 总结 + 规划，非执行 | 含阶段内直接执行（工作流 B） | 混合 planning / executing（三视角均反对） |
| 高维、粗、指导性 | architecture + phase-plan | charter/pitch 层尚可；**命名偏技术** |
| 细节进阶段 | 启动即写 phase-01 task-list | 违反 rolling wave / Shape Up / Spec Kit tasks 顺序 |
| 任何领域 | architecture、AI 任务表 | charter + WBS 更领域中立 |
| 控制信息量 | 未定义 human-readable 上限 | 缺 **gate + 必读页数约束** |

**结论（讨论层）**：问题本质是 **artifact 分层与授权关口** 未设计，不是「模板字段不够多」。

### 3. 推荐流程：轻量 PMP 思维 + Shape Up 纪律 + SDD gate

不必 full PMBOK；取三源 **最小交集**：

```text
┌──────────────────────────────────────────────────────────────────┐
│  idea-discuss  （≈ shaping + 可行性 + DECISIONS/EXP）            │
│  产出：INV / ORD / EXP / ready-for-implementation                │
└────────────────────────────┬─────────────────────────────────────┘
                             │ 硬闸门：讨论就绪 + 无阻塞 EXP
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  落地 · Initiate  （人类必读 ≤ ~2 页）                            │
│  · charter.md  — 对 DECISIONS 的 pitch 化综合：                   │
│      为何做 / 成功标准 / 范围边界 / 决策权限 / 显式非目标         │
│      （rough + solved + bounded；非复制 INV/ORD 表）              │
└────────────────────────────┬─────────────────────────────────────┘
                             │ GATE-1：用户确认 charter（= betting table / 授权）
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  落地 · Plan（粗）                                                │
│  · wbs.md — L1 阶段 / L2 可交付成果（≤2 层）                      │
│  · wbs 条目仅含：名称 + 一句话完成定义 + 关联 INV/ORD/EXP         │
│    （词典深层 → 进入该工作包时再滚动补充）                         │
└────────────────────────────┬─────────────────────────────────────┘
                             │ GATE-2：用户确认 WBS（可选合并 GATE-1）
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  落地 · 阶段设计（Rolling）— 仅对「当前/近期」工作包              │
│  · phase-NN/plan.md   — 本阶段目标、任务、AI/人工、完成定义       │
│  · phase-NN/acceptance.md — 人工验收手册                          │
│  · phase-NN/review.md — 评审：完成度 / 问题 / EXP 验证 / 下阶段   │
│    （circuit breaker：未过 acceptance → 不进入下一工作包）          │
└────────────────────────────┬─────────────────────────────────────┘
                             ▼
                    执行（独立 skill 或对话；不在规划 skill 内）
```

**与 full PMP 的刻意差异**

| Full PMP 常含 | 本流程保留 | 省略或延后 |
|---------------|------------|------------|
| 12 节章程 | 1 页 charter（6 节以内） | 预算分解、完整风险登记 |
| WBS 到 work package + 全量词典 | L1–L2 + 滚动词典 | 远期 L3+、CPM |
| RACI | charter 中一句决策权限 | 逐任务 RACI |
| CCB | DECISIONS 修订 → 回 discuss | 正式变更委员会 |
| 全周期排期 | 人工步骤可估时；AI 步骤不估人工时长 | 甘特 / 资源平衡 |

**信息量控制（回应你的核心担忧）**

| 角色 | 启动阶段读什么 | 不读什么 |
|------|----------------|----------|
| 人类 | charter；可选 wbs 树（1 页） | phase plan、tasks、词典细节 |
| AI | 全部（按需生成） | — |
| skill 规则 | GATE 未过不得生成 tasks | 禁止启动时 scaffold phase-01 task-list |

### 4. discuss ↔ 落地 skill 内容分工（防重复）

| 内容 | idea-discuss | 落地 skill |
|------|--------------|------------|
| INV / ORD 条文 | ✓ 权威源 | charter **引用 ID**，不重辩论 |
| EXP 定义与继续/中止 | ✓ | review **更新状态** |
| 成功标准 / 非目标 | ✓ 条目 | charter **叙述综合** |
| 工作包 / 任务 / 验收步骤 | ✗ | phase plan / acceptance |
| 授权 | ready 闸门 | charter 用户确认（GATE-1） |
| 新决定 | ✓ | ✗ → 回 discuss |

**握手点**：`DECISIONS ready-for-implementation` + **`charter` GATE-1 通过** = 项目启动授权。

### 5. 方案对比（grounded 更新）

| 方案 | 概要 | 优点 | 风险 |
|------|------|------|------|
| **A** 修补 idea-implement | 保留 architecture/phase-plan，仅推迟 task-list | 改动小 | 命名与层次仍混；三视角对照弱 |
| **B** 三源轻量映射（**讨论推荐**） | charter + wbs + gate + rolling phase plan | 领域中立；与你 PMP 直觉一致；有 PMI/Shape Up/SDD 三重对照 | 需重写 skill；词汇偏 PM |
| **C** Spec-Kit 命名 | constitution/spec/plan/tasks | SDD 生态一致 | 「任何领域」感受差 |
| **D** 仅 charter + phase | 去掉 WBS | 最轻 | 分解与跟踪弱 |

**讨论倾向**：**B**，并吸收 Shape Up 的 **双轨 + circuit breaker** 与 Spec Kit 的 **gate**，而非引入 full PMBOK 文档树。

### 6. 待决分叉（需你确认，不写入 DECISIONS）

1. **B vs D**：要不要独立 WBS 层？（讨论倾向：要，但限 L1–L2）
2. **拆 skill**：`idea-plan`（启动+规划+阶段设计） vs `idea-execute`（执行）？
3. **EXP-01 试跑项目**：有无真实小项目（可非技术）？
4. **WBS 词典形态**：独立 `wbs-dictionary.md` vs 合并 `wbs.md` 表格？

## 可验证尝试与继续/中止

### EXP-01

| 项 | 内容 |
|----|------|
| 假设 | 「charter（≤1 页）+ L1/L2 wbs + GATE + 滚动 phase plan」在阅读量与层次感上优于现有 idea-implement |
| 尝试方案 | 选**小型真实项目**（建议：本 skills 仓库「重写 idea-implement 为 B 方案」或用户指定的非技术项目）；生成 `docs/implement/` 仅含 charter + wbs；**故意不写** phase-01 tasks；用户 ≤5 分钟阅读后反馈 |
| 成功信号 | ①「这是总结和规划，不是细节清单」② charter 与 DECISIONS 分工一眼可辨 ③ 不感 PMP 文档洪水 ④ 能说出 GATE 后才会细化的预期 |
| **继续** | 按 B 方案重写 `idea-implement`（或拆 plan/execute） |
| **中止** | 仍觉重 → 方案 D；charter/WBS 分工仍混 → 回 discuss 修订 DECISIONS 结构 |
| 来源 | `01-implement-skill流程与pmp映射.md` §EXP-01 |

### EXP-02

| 项 | 内容 |
|----|------|
| 假设 | 在 EXP-01 通过前提下，**gate 写进 skill** 比「靠 agent 自觉」更能防止 task 前置 |
| 尝试方案 | 用同一项目走完整 GATE-1 → wbs → GATE-2 → phase-01/plan；观察是否仍出现「启动即细任务」 |
| 成功信号 | phase plan 仅在 GATE-2 后出现；review 能回写 EXP 状态 |
| **继续** | gate 成为 idea-implement 硬规则 |
| **中止** | gate 流于形式 → 改为单一合并 gate 或 checklist |
| 来源 | `01-implement-skill流程与pmp映射.md` §EXP-02 |

## 本轮决定

### 已确定 — 原则性不变量（新增/修订）

（无 — 以下 INV 草案待用户显式确认）

### 已确定 — 普通决定（新增/修订）

（无 — 以下 ORD 草案待用户显式确认）

### 待确认（下轮继续）

**INV 草案**

- **INV-01**：落地 skill 的人类必读启动产物以 **charter + L1/L2 WBS** 为上限；**细任务仅允许在 phase-NN/plan 中出现**。
- **INV-02**：落地 skill **不包含执行**（编码/交付操作）；执行由独立 skill 或对话完成，规划 skill 止于阶段 review。

**ORD 草案**

- **ORD-01**：用 `charter.md` 替代 `architecture.md`；用 `wbs.md` 替代 `phase-plan.md`。
- **ORD-02**：初次规划**禁止**创建任何 `phase-NN/plan` 或 task-list，直至 GATE-1（+ 可选 GATE-2）通过。
- **ORD-03**：skill 必须定义 **GATE-1（charter 确认）**；GATE-2（WBS 确认）可选，小项目可合并。
- **ORD-04**：AI 步骤不给人工时长预估；人工步骤在 phase plan 中标注预估时间。

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| EXP-01 | 修订（ grounded 后更新假设与方案） | ✓ |
| EXP-02 | 新增 | ✓ |

讨论状态同步：`exploring` → **`deciding`**（三源对照完成；INV/ORD 草案待用户确认；建议 EXP-01 后再标 ready-for-implementation）

同步完成时间：2026-05-19

## 开放问题（下轮）

1. 确认 **INV-01 / INV-02** 与 **ORD-01–04** 草案，或指出修订。
2. **B vs D**、**拆 skill vs 单 skill 双模式** 的偏好。
3. EXP-01 试跑项目选哪个？
4. 是否在 `idea-discuss/SKILL.md` 增加硬约束：「未完成 best-minds-grounded 则视为事实基础未完成」？

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-19 | 初稿（未走 best-minds-grounded，已作废） |
| 2.0 | 2026-05-19 | 完整重写：best-minds-grounded 轻量框定 + 三专家视角 + 三源收敛流程 |
