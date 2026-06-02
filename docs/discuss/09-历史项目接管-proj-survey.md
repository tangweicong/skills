# 09-历史项目接管-proj-survey

| 字段 | 值 |
|------|-----|
| 轮次 | 09 |
| 主题 | 历史项目接管能力 → 新增 proj-survey skill |
| 日期 | 2026-06-01 |
| 状态 | discussed |
| 讨论方法 | `manual`（grounded reasoning：基于通读现仓库 4-skill 契约的事实 + 体系内一致性推理 + 用户 GATE 拍板；非多专家 proj-experts 面板） |
| 写入格式 | 完整（架构议题，推理进入 ORD/EXP） |

> 方法说明：本轮无外部前沿争议、核心是「现有 4-skill 体系缺口诊断 + 新 skill 定位」，事实可由通读本仓库直接查证，故用 `manual` 而非召集专家面板。

## 用户输入（本轮）

承接上一轮「proj-plan 是否具备接管历史项目能力」的结论（不具备，仅 greenfield 取向）。用户否决了「在 proj-plan 内做最小增量」的方案，提出目标效果：

1. 自动分析当前项目，生成**现状基线**（AI 自动，**不需要人工整理**）；
2. 若有已有文档能明确**未完成工作** → 自动生成后续规划；
3. 若无法明确未完成工作 → 只做**完整性评审**，说明已完成工作是否无缺失/遗漏、是否有 bug。

并问：完全接管历史项目还需做哪些工作？我列的这些有没有问题？是否需要再拆一个 skill？

## 事实与假设

### 已查证事实（均出自本仓库通读）

- 现有 4 skill 是一条**正向 greenfield 流水线**：`proj-experts`（分析）→ `proj-shape`（讨论/商业论证）→ `proj-plan`（规划）→ `proj-run`（执行）；信息均从「人的想法」出发往前流，**无任一 skill 读取既有系统**。出处：四个 `skills/*/SKILL.md`。
- `proj-plan` 入口**硬依赖** `docs/discuss/DECISIONS.md`（`ready-for-implementation` 或用户显式授权）。出处：`skills/proj-plan/SKILL.md` frontmatter `compatibility` + §0 前置。
- `proj-plan` 的 `project-context-template.md` / WBS 模板**无「已有资产 / 现状 / 已完成范围」字段**，WBS 默认全部条目为「待做」。出处：`skills/proj-plan/assets/project-context-template.md`、`wbs-template.md`。
- 「三分离（已查证事实 / 推理 / 待验证假设）」是 `proj-shape` 的看家认知学纪律。出处：`skills/proj-shape/SKILL.md` §事实基础。
- 体系**已有「按 PMP 关注点拆 skill」的先例**：`ORD-17` 为「执行」这个独立关注点把 `proj-run` 拆出，理由含「proj-shape 拆分先例」。出处：`DECISIONS.md` ORD-17。

### 推理（非事实、非待验证）

- **推理 · 体系一致性**：用户 3 点本质 = **1 个新能力（逆向盘点/Discovery）+ 2 个置信度分支**；分支条件不应是「文档是否存在」，而应是「**意图（to-be）是否可信重建**」——因为历史项目文档通常陈旧/残缺，真相源是代码+测试+git+issue。依据 proj-shape §事实基础「测试即规格、来源须带出处」的纪律外推。
- **推理 · 逻辑约束**：第 3 点「断言无缺失/无 bug」存在硬伤——**无参照规格（intent）不能断言完整**，而第 3 点触发条件恰是 intent 不可重建；此时「完整」只能退化为**内部一致性**。静态评审只能给 likely-bug + 置信度，给不出「无 bug」保证。依据形式逻辑（无 oracle 不可判定正确性）。
- **推理 · ORD-17 先例**：brownfield discovery 是与 discuss-new / decompose / execute 并列的**独立生命周期关注点**（read-existing），且第 3 点审计产出不归属任何现有 skill → 应新拆 skill，而非折叠。依据 `DECISIONS.md` ORD-17 拆分纪律。
- **推理 · INV-01 精神**：用户要「自动、不需人工整理」可满足于 **baseline 生成全自动**；但「走 plan 还是 audit」是高风险路径决策，应保留 GATE（人仅审批、不整理），与 `INV-01`（人=关键决策）一致。

### 待验证 / 未查证

- AI 自动读中等/大型 repo 产出的现状基线「事实层」准确率是否足够支撑分支判定（→ EXP-05）。
- 「intent 可信重建」是否存在可操作的 GATE 判据（→ EXP-06）。

### 方法专属输出

本轮 `manual`，省略方法专属输出节；推理见上节，均挂体系内出处。

## 讨论

### 用户 3 点的重构与 pushback

| 用户点 | 本质 | pushback / 结论 |
|--------|------|-----------------|
| 1 自动→现状基线 | 逆向盘点（全新能力） | 每条 finding 须三分离标注（事实/推理/待验证） |
| 2 文档明确未完成→规划 | Gap→Plan 分支 | 分支判据改为「意图可否可信重建」；来源优先级 测试>代码>git/issue>docs>用户口述 |
| 3 无法明确→完整性评审 | Audit 分支 | **不能**作「无缺失/无 bug」保证；产出=findings+置信度；无 intent 时「完整」仅限内部一致性 |

第 2 / 3 点实为同一流程的两个**置信度分支**，非两件事。

### 架构选项与决议（用户 GATE 确认）

| 方案 | 评价 | 决议 |
|------|------|------|
| ① 新拆 skill `proj-survey` | 匹配 ORD-17 先例；审计分支不归现有 skill | **采纳**（用户选 new_skill / name=survey） |
| ② 扩 proj-shape | 污染其「磨清模糊想法」身份；审计分支不产正向 DECISIONS | 否 |
| ③ 扩 proj-plan | discovery 太大不能当 planning 子步 | 否（用户上轮已否） |

审计分支：**作为 proj-survey 终端分支，v1 不独立成第 6 个 skill**（用户选 terminal；遵循 proj-shape「待第 2 个真实需求再抽象」反过早抽象原则）。

### 双入口流水线

```text
正向(新项目):  proj-experts → proj-shape → proj-plan → proj-run
接管(历史项目): proj-survey → ┬─[intent 可信]→ proj-plan → proj-run
                              └─[intent 不可信]→ 审计报告(终端)
                                                 └→(可选)回 proj-shape 与人补 intent → proj-plan
```

审计分支回流 proj-shape：intent 无法从代码重建时，本就该回到 proj-shape 与人讨论补出 to-be，复用正向流水线。

### 完全接管的缺口清单（3 点之外）

- 意图来源排序 + 冲突解决规则（必做）
- 现状基线三分离标注（必做，复用 proj-shape）
- proj-survey→proj-plan 衔接：proj-plan 加 brownfield 入口 + WBS 三态（已完成/进行中/待做）（必做）
- 分支 GATE 可操作判据（必做，EXP-06）
- 大型 repo 可扩展性：分层读取 repo map→依赖图→按需深入（真未知，EXP-05）
- 审计 findings 落地位置（待定：`docs/survey/`？）
- 接管后 baseline 刷新机制（可延后到 v2）

## 可验证尝试与继续/中止

### EXP-05（→ 汇总 ID 见 DECISIONS）

| 项 | 内容 |
|----|------|
| 假设 | AI 自动读中等规模 repo 能产出「事实层」足够准的现状基线，支撑分支判定 |
| 尝试方案 | 在本 skills 仓库自身（dogfood）或一个已知中等 repo 跑 baseline 生成，人工核对事实层误报率 |
| 成功信号 | 事实层误报 < 阈值（待定）；分支判定（可 plan vs 仅 audit）与人判一致 |
| **继续** | 误报率达标 → 固化 baseline 生成流程进 proj-survey 工作流 |
| **中止** | 大 repo 一次读不完 / 误报率高 → 降级路径 B：人指认重点目录 + AI 局部分析 |
| 来源 | `09-…md` §讨论；推理 · 体系一致性 |

> **执行结果（2026-06-02）= passed**：本仓库 dogfood 自动现状基线（`docs/survey/2026-06-01-baseline.md`），事实层 **0/16 误报 = 0%** < 10% 阈值（用户「全对」）；分支判定「可 plan」与人判一致。阈值定为 **<10%**。**caveat**：本 repo 属「intent 易重建」简单端，难例（intent 不可重建 → 审计分支）未压测，留 EXP-06。

### EXP-06

| 项 | 内容 |
|----|------|
| 假设 | 「intent 可信重建」存在可操作的 GATE 判据 |
| 尝试方案 | 设计判据 + 在 2–3 个真实 repo 上验证分支判定 |
| 成功信号 | 判据稳定可复现，分支判定与人判一致 |
| **继续** | 判据稳定 → 写入 proj-survey 分支 GATE |
| **中止** | 判不准 → 降级路径 B：默认走更保守的审计分支 + 人确认 |
| 来源 | `09-…md` §讨论；推理 · 逻辑约束 |

## 本轮决定

### 已确定 — 普通决定（新增）

- [x] **决定**：建立第 5 个 skill `proj-survey` 专管 brownfield 逆向盘点；双入口流水线。
  **来源**：用户 @本轮 GATE（arch=new_skill, name=survey）；推理 · ORD-17 先例 → 同步 `ORD-23`
- [x] **决定**：分支判据 = 「意图(to-be)是否可信重建」（非「文档是否存在」）；现状基线复用 proj-shape 三分离；意图来源优先级 测试>代码>git/issue>docs>用户口述。
  **来源**：用户 @本轮；推理 · 体系一致性 → 同步 `ORD-24`
- [x] **决定**：审计分支（intent 不可信）作为 proj-survey 终端分支，v1 不独立成 skill；产出=findings+置信度，**不**作「无缺失/无 bug」保证；无 intent 时「完整」仅限内部一致性；可回流 proj-shape 补 intent。
  **来源**：用户 @本轮 GATE（audit=terminal）；推理 · 逻辑约束 → 同步 `ORD-25`
- [x] **决定**：proj-survey→proj-plan 衔接 = proj-plan 加 brownfield 入口（读 baseline 代替/补充 DECISIONS）+ WBS 三态（已完成/进行中/待做）；「自动」= baseline 生成全自动 + 人仅在分支 GATE 审批（对齐 INV-01），人只读 ≤N 项摘要。
  **来源**：用户 @本轮；推理 · INV-01 精神 → 同步 `ORD-26`

### 待确认（下轮继续）

- 审计 findings 落地目录（`docs/survey/` vs 其它）
- 大型 repo 分层读取的具体策略（依 EXP-05 结果定）
- 接管后 baseline 刷新机制（v1 是否纳入）
- proj-plan WBS 三态的具体 schema 改法

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-23 | 新增 | ✓ |
| ORD-24 | 新增 | ✓ |
| ORD-25 | 新增 | ✓ |
| ORD-26 | 新增 | ✓ |
| EXP-05 | 新增 → **passed**（2026-06-02） | ✓ |
| EXP-06 | 新增 | ✓ |

讨论状态同步：`ready-for-implementation` → `deciding`（新增 proj-survey 设计线，EXP-05/06 pending + 4 项待确认未闭合；现有 4 skill 仍 shipped/stable，不受影响）

同步完成时间：2026-06-01 16:45

## 开放问题（下轮）

1. proj-survey 工作流分段（盘点→基线→意图重建→分支 GATE→{handoff proj-plan | 审计报告}）的具体步骤与 assets 模板。
2. 现状基线模板字段（三分离标注 schema + 已完成范围登记）。
3. proj-plan brownfield 入口与 WBS 三态的最小改法。

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-06-01 | 初稿：proj-survey 立项 + ORD-23~26 + EXP-05/06 |
