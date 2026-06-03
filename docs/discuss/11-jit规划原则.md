# 11-Just-In-Time 规划原则

| 字段 | 值 |
|------|-----|
| 轮次 | 11 |
| 主题 | 给 proj-plan 加「Just-In-Time / 恰好足够 / 在对的时间规划」原则——是否已有、能否加、是否冲突 |
| 日期 | 2026-06-03 |
| 状态 | confirmed · synced（ORD-27 已落实到 SKILL.md + README）|
| 讨论方法 | `proj-experts` |
| 写入格式 | 完整 |
| 承接 | proj-plan SKILL.md（已发布 stable）；INV-02（细任务仅在 phase plan）+ ORD-04/06（模式 T/F · just enough process）+ §PMP 计划分层表 |

## 用户输入（本轮）

> 对于当前的 proj-plan skill，我想加一个规划原则，那就是 Just-In-Time，像 JIT 编译一样，在对的时间做恰好足够的规划，而不是做超长期的规划。这个原则在原本的能力中有体现吗？能加上吗？会与原有的原则有冲突吗？

三个子问题：(1) 已有体现？(2) 能加？(3) 与原有原则冲突？

## 事实与假设

### 轻量框定（查证前问题清单）

| # | 待查问题 | 查证结论（摘要） |
|---|----------|------------------|
| Q1 | PM 行业有没有「JIT 规划」的既有术语？ | 有——**Rolling Wave Planning** 与 **Progressive Elaboration**，均为 PMBOK 正式术语 [PMBOK via PM Study Circle](https://pmstudycircle.com/rolling-wave-planning/) |
| Q2 | 软件/敏捷侧有没有更贴近「JIT 编译」直觉的原则？ | 有——Lean 的 **Last Responsible Moment (LRM)**，Poppendieck 提出；敏捷语境下常直接称 "just in time" [agilepainrelief](https://agilepainrelief.com/glossary/last-responsible-moment/) |
| Q3 | 这些原则会不会主张「什么都别提前定」？ | 不会——两家都明确：架构/骨架/授权类决策**故意提前**；只把**细节/分解深度**推迟。LRM 原文："a bias toward late commitment must not degenerate into a bias toward no commitment" [codinghorror](https://blog.codinghorror.com/the-last-responsible-moment/) |
| Q4 | proj-plan 现有机制里哪些已经是 JIT？ | rolling phase plans、INV-02、WBS 仅 L1–L2、phase-roadmap「无任务表」、"全量 WBS 词典 L3+ rolling 进 phase plan"、模式 T/F「just enough process」——见下「推理」 |

### 已查证事实

- **F1 · Rolling Wave Planning（PMBOK 正式术语）**：PMBOK 原文定义——"work to be accomplished in the near term is planned in detail, while work further in the future is planned at a higher level. It is a form of progressive elaboration applicable to work packages, planning packages, and release planning when using an Agile or Waterfall approach." [PMBOK 6th, §6.2.2.3 via O'Reilly](https://www.oreilly.com/library/view/q-as/9781628254624/a_chapter06.xhtml)、[PM Study Circle](https://pmstudycircle.com/rolling-wave-planning/)
- **F2 · Progressive Elaboration（PMBOK 正式术语，rolling wave 的上位概念）**："continuously improving and detailing a plan as more detailed and specific information and more accurate estimates become available." [projectmanagement.com wiki](https://www.projectmanagement.com/wikis/295452/progressive-elaboration)（引 PMBOK part 2, ch.3, p.565）。两者关系：progressive elaboration = 原则；rolling wave = 把原则落成「有触发点的操作模型」 [Plane blog](https://plane.so/blog/rolling-wave-planning-in-project-management-when-and-how-to-use-it)
- **F3 · Last Responsible Moment（Lean，Poppendieck）**："the moment at which failing to make a decision eliminates an important alternative. If commitments are delayed beyond the last responsible moment, then decisions are made by default." [codinghorror 引 Poppendieck](https://blog.codinghorror.com/the-last-responsible-moment/)。判据：「delay until the cost of not deciding exceeds the benefit of delaying」 [agilepainrelief](https://agilepainrelief.com/glossary/last-responsible-moment/)
- **F4 · LRM 自带边界（防退化为"不规划"）**：Poppendieck 原文——"Certain architectural concepts such as usability design, layering, and component packaging are best made early... A bias toward late commitment must not degenerate into a bias toward no commitment." [1library 引 Poppendieck](https://1library.net/article/the-last-responsible-moment-lean-software-development.yr8gro7z)
- **F5 · JIT ↔ LRM 在敏捷语境被直接画等号**："In Agile, speed... it's about making them just in time. Deciding too early can waste resources by locking in plans prematurely. Waiting too long risks... The LRM strikes a balance." [Wallack on LRM/JIT](https://www.linkedin.com/posts/shawnwallack_a-moment-on-the-last-responsible-moment-activity-7290004840070488064-i29Y)

### 推理（非事实、非待验证）

- **推理 · proj-experts · 视角 A（PMBOK rolling wave）**：proj-plan 现有结构**已经是 rolling wave 的实现**，只是没被命名为「原则」。证据逐条对应——INV-02（细任务**仅**在 `phase-NN/plan.md`）= rolling wave 的「近期细 / 远期粗」；`phase-roadmap.md`「粗进度，**无任务表**」= 远期高层；"全量 WBS 词典 L3+ rolling 进 phase plan 而非启动期" = work package 按推进逐步分解；"仍不写 phase-NN/plan，直至进阶段" = 触发点驱动的 wave。依据 [PMBOK rolling wave 定义](https://www.oreilly.com/library/view/q-as/9781628254624/a_chapter06.xhtml) 与 SKILL.md §「PMP 计划 ≠ 仅 WBS」表 + §工作流 Rolling 节。
- **推理 · proj-experts · 视角 B（Lean LRM）**：现有 proj-plan 体现了 rolling（**推迟细节**），但**没有显式的「决策时机判据」**——即「什么时候算到了该展开的那一刻」。LRM 补的正是这一条：「推迟到 不决策的代价 > 等待的收益 的那一刻」。这是现有 skill 缺的**可操作触发判据**（现在的触发是隐式的「进阶段就写 plan」，但没说「为什么是现在、能不能更晚」）。依据 [LRM 判据](https://agilepainrelief.com/glossary/last-responsible-moment/)。
- **推理 · proj-experts · 视角 B 的边界警告**：LRM 同时自带「防退化」条款（F4）——骨架/架构/授权类决策**故意提前**。映射到 proj-plan：charter（授权）、WBS L1–L2（范围骨架）、phase-roadmap（阶段骨架）就是「故意提前的那部分」。所以一个**措辞粗糙的 JIT 原则**（「一切都推迟」）会和这些**故意提前**的产物打架；而**措辞正确的 JIT 原则**（「推迟的是*细节展开深度*与*可逆决策*，不是*骨架与不可逆授权*」）恰恰**解释**了为什么这些产物提前——非但不冲突，反而是它们的理论依据。

### 待验证 / 未查证

- 无需 EXP。本轮是「为既有、已验证的机制补一个命名 + 一条判据」，不引入未证实假设；rolling wave 机制本身已在前 10 轮 + EXP-01 试跑中验证可用。

### 方法专属输出（proj-experts）

#### 视角 A · PMBOK / PMI 规划学派（rolling wave + progressive elaboration）

**选用理由**：proj-plan 自我定位就是 PMBOK 6/7/8 派生；判断「是否已有体现」必须用 PMI 自己的术语对账。

**【已公开立场】**：PMBOK 把「近期细、远期粗、随推进逐步细化」定义为 rolling wave planning（progressive elaboration 的一种），明确适用于 agile 与 waterfall [O'Reilly 引 PMBOK §6.2.2.3](https://www.oreilly.com/library/view/q-as/9781628254624/a_chapter06.xhtml)。

**【模拟推理】**：用户的「JIT 规划」= PMBOK 的 rolling wave。proj-plan **已经在做**，但在 SKILL.md 里它是**散落的机制**（INV-02、phase-roadmap 无任务表、WBS L1–L2、"just enough process"），不是**一条被命名的首要原则**。把它显化为原则 = 把隐性不变量提上台面，且能挂真实 PMI 术语，符合 skill 现有「借鉴/自创」纪律（ORD-12/13）。

#### 视角 B · Lean / Agile 学派（Poppendieck · Last Responsible Moment）

**选用理由**：用户的类比是「JIT **编译**」——这是软件/lean 直觉，不是 PMI 直觉。最贴近的成熟原则是 LRM，且 LRM 在敏捷语境就被叫做 "just in time"（F5）。

**【原话】**（Poppendieck，转引）："delay commitment until the last responsible moment, that is, the moment at which failing to make a decision eliminates an important alternative." [codinghorror](https://blog.codinghorror.com/the-last-responsible-moment/)

**【模拟推理】**：LRM 给 proj-plan 补的是**判据**而非机制——「为什么现在展开这一阶段、能不能再等」。同时 LRM 自带「不可退化为不规划」的护栏（F4），正好对上 proj-plan 里 charter/WBS 骨架/phase-roadmap 的**故意提前**。

**关切 → 路径**：视角 B 担心一个被滥用的 JIT 会变成「借口跳过 phase-roadmap / 跳过 charter」（撞 SKILL.md 失败模式「仅 WBS 无 phase-roadmap → 计划不完整」）。路径 = 原则措辞里写死**适用对象 = 细节展开深度 + 可逆决策**，**非适用对象 = 范围/授权骨架**；并明确「推迟 ≠ 省略 artifact」。

#### 收敛（【模拟推理】，非任一专家原话）

两派一致：JIT 不是新行为，是**给已存在的 rolling-wave 机制命名 + 补一条 LRM 时机判据 + 写清边界**。冲突只来自措辞粗糙；措辞正确则零冲突且**增强自洽**。

## 讨论

### Q1：原本能力里有体现吗？——有，且很深，但未命名

proj-plan 已经把 JIT/rolling-wave **作为机制**散布在多处：

| 现有机制 | 在 SKILL.md 的位置 | 对应 JIT/rolling-wave 的哪一面 |
|----------|--------------------|-------------------------------|
| INV-02：细任务**仅**在 `phase-NN/plan.md` | §不可违背 | 近期才细化（核心） |
| `phase-roadmap.md`「粗进度，**无任务表**」 | §PMP 计划分层表 + INV-02 | 远期只保持高层 |
| WBS 仅 L1–L2，"全量 L3+ rolling 进 phase plan" | §故意刻意不做 + §工作流 Round B | work package 按推进分解 |
| "仍不写 phase-NN/plan，直至进阶段" | §工作流 Round B step 5 | 触发点驱动展开 |
| 模式 T「Tailored Minimum · just enough process」 | §Coach hybrid + ORD-04/06 | 恰好足够（breadth 轴） |

**结论**：用户要的原则在**行为上已经实现**。缺的是两样：(a) 一个**被命名的首要原则**（现在读 SKILL.md 要靠读者自己从五处拼出来）；(b) 一条**显式的「何时展开」判据**（现在是隐式的「进阶段就写」）。

### Q2：能加吗？——能，且建议加，但定位是「命名 + 补判据」而非「新增行为」

按你自己的「简约优先 / 外科手术式修改」原则，**不该**为重复造一个新机制。这里的增量价值是**显化与收敛**，三件事：

1. **命名**：在 SKILL.md 立一条原则——「JIT 规划 / 恰好足够」，一句话点明 = PMBOK rolling wave + Lean LRM 的本地化，并挂真实 URL（符合 ORD-12/13/14 的借鉴/自创纪律：JIT 编译是你的类比，rolling wave/LRM 是真实出处）。
2. **补判据**：把隐式触发显化为 LRM 式判据——「一个规划细节**推迟到「再不展开就会因缺信息而被迫默认决策」的那一刻**才展开」。这条是现有 skill 真正缺的。
3. **写边界**（关键）：适用对象 = **细节展开深度 + 可逆决策**；非适用对象 = **范围骨架（WBS L1–L2）/ 阶段骨架（phase-roadmap）/ 授权（charter）/ 不可逆决策**——这些**故意提前**。

定位上它更像 ORD-04（模式 T/F）的**孪生轴**：T/F 管「做哪些 artifact」（**广度**轴）；JIT 管「每个 artifact 的细节何时展开到多深」（**时间/深度**轴）。两轴正交、互补。

### Q3：与原有原则冲突吗？——无根本冲突；唯一风险是措辞，且可被边界条款消解

逐条对账：

| 原有原则 | 关系 | 说明 |
|----------|------|------|
| INV-02（细任务仅在 phase plan） | **强化** | JIT 就是 INV-02 的"为什么" |
| INV-01（人只读 ≤5） | 中立/弱强化 | 推迟细节 → 人更少被迫提前读细节 |
| INV-03（GATE 未过不下游） | 中立 | GATE 是质量门，JIT 是时机；正交 |
| INV-04（不含执行） | 中立 | 不同维度 |
| ORD-04/06（模式 T/F · just enough） | **互补孪生轴** | T/F = 广度；JIT = 深度/时机 |
| charter / WBS L1–L2 / phase-roadmap **提前生成** | **潜在张力 → 被边界消解** | 朴素 JIT「全推迟」会撞它们；但 rolling wave（F1）与 LRM（F4）都明确骨架**故意提前**——正确措辞下 JIT 反而**论证**了为什么只到 L1–L2、为什么 roadmap 无任务表 |
| 失败模式「仅 WBS 无 phase-roadmap → 不完整」 | **潜在张力 → 被边界消解** | 必须写明「推迟细节 ≠ 省略 artifact」，否则会被当跳过借口 |

**唯一真实风险**：把原则写成「能不做的规划都别做 / 一切推迟」。这会同时撞 charter/roadmap 的提前生成与「计划完整性」失败模式。**消解方式**：原则正文带死「适用对象/非适用对象」边界（见 Q2 第 3 点），并加一句「JIT 约束的是*展开时机与深度*，不是*是否产出该 artifact*」。

### 落点建议（仅描述放哪，不在本 skill 写实现步骤）

- 形态：proj-plan SKILL.md 顶部「设计 vision」之后、或「立场声明」内新增一条**规划原则**；术语标注「JIT 为本 skill 借用的类比；行业出处 = PMBOK rolling wave / progressive elaboration + Lean LRM」并挂 F1–F4 的 URL。
- 是否升 INV？**不建议**。它不是「违背即换项目」的不可变量级（rolling wave 是技术不是底线），且与现有 INV 是「强化/互补」而非并列约束。**建议为普通决定 ORD**，可随经验调整措辞。

## 可验证尝试与继续/中止

本轮无 EXP。理由见「待验证/未查证」节——机制已存在且经 EXP-01 验证，本轮只补命名 + 判据 + 边界，不引入未证实假设。

## 本轮决定

### 已确定 — 原则性不变量（新增/修订）

- 无。

### 已确定 — 普通决定（新增/修订）

- [x] **决定 → ORD-27**：proj-plan SKILL.md 新增**规划原则「JIT / 恰好足够规划」**——
  (a) 命名既有 rolling-wave 机制 + 挂真实出处（rolling wave / progressive elaboration / LRM；JIT 编译为类比，标「借用」）；
  (b) 判据 = LRM 式「推迟到 不决策代价 > 等待收益 的那一刻才展开」；
  (c) **边界**：适用 = 细节展开深度 + 可逆决策；非适用 = 范围骨架/阶段骨架/授权/不可逆决策（这些故意提前）；
  (d) 一句「推迟 ≠ 省略 artifact」防滥用；
  (e) 定位为 ORD-04 模式 T/F（广度轴）的孪生**时间/深度轴**，**不升 INV**。
  **来源**：`11-jit规划原则.md` §讨论；用户 @本轮原话 + @本轮拍板（adopt + 落点=设计 vision 后独立小节）；推理 · proj-experts 视角 A/B；依据 [PMBOK rolling wave](https://www.oreilly.com/library/view/q-as/9781628254624/a_chapter06.xhtml) + [progressive elaboration](https://www.projectmanagement.com/wikis/295452/progressive-elaboration) + [LRM](https://blog.codinghorror.com/the-last-responsible-moment/)
  → 已同步至 DECISIONS.md `ORD-27`；已落实到 `skills/proj-plan/SKILL.md` §规划原则·JIT + 根 README

### 对既有决定的修订

无。

### 待确认（下轮继续）

- 无未闭合项。

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-27 | 新增 | ✓（普通决定表 + 变更日志 + 最后更新 meta）|

讨论状态同步：维持 `deciding`（proj-survey 线 EXP-06 未闭合；本轮 ORD-27 已闭合落实，不改变整体状态）

同步完成时间：2026-06-03 11:05

## 开放问题（下轮）

- 无。两问已在本轮闭合：用户确认 adopt ORD-27；落点选「设计 vision 后独立小节『规划原则 · JIT』」。

## 同步注记（2026-06-03）

- 用户「继续」→ ORD-27 **一致性回灌**到相邻 artifact（**非新决定**，属 ORD-27 落实扩展）：
  - `skills/proj-plan/assets/tailoring-rules.md`：顶部加「广度轴（T/F）vs JIT 时间/深度轴正交 + 推迟≠省略」交叉引用，防止把模式 T 误当成「省略细节」。
  - `skills/proj-run/SKILL.md` §设计 vision：加一段「继承 ORD-27——只执行当前 rolling-wave 阶段；执行侧『恰好足够』= 既有的 §dispatch 决策树 + iteration budget，**不新增机制**」。
- 评估结论：proj-run **不**单设 JIT 章节（会与 dispatch 决策树/iteration budget 重复，违反简约），改为「命名既有纪律 + 交叉引用」。
- validate_skills.py 5/5 退 0。

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-06-03 | 初稿：JIT 规划原则评估（已有体现/能否加/冲突）；候选 ORD-27 待确认 |
| 1.1 | 2026-06-03 | 用户拍板 adopt ORD-27；落实到 SKILL.md + README；一致性回灌 tailoring-rules + proj-run（落实扩展）|
