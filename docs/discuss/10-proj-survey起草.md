# 10-proj-survey起草

| 字段 | 值 |
|------|-----|
| 轮次 | 10 |
| 主题 | proj-survey skill 起草（承接 09 轮 ORD-23~26 + EXP-05 passed）|
| 日期 | 2026-06-02 |
| 状态 | discussed |
| 讨论方法 | `manual`（执行/起草轮：决定已在 09 轮定稿，本轮落实为 skill 文件 + EXP-05 流程固化）|
| 写入格式 | 轻量（无新争议；推理已在 09 轮标注三元组）|

## 用户输入（本轮）

EXP-05 passed（事实层 0/16 误报、分支判定与人判一致）后，用户选择「开 round 10 起草 proj-survey 工作流 + assets（把 baseline 生成流程固化；EXP-06 作为工作流内的待验证 GATE 带着走）」。

## 事实与假设

### 已查证事实

- EXP-05 = **passed**（`docs/survey/2026-06-01-baseline.md`；事实层 0/16 误报 < 10% 阈值；分支判定「可 plan」与人判一致）。出处：DECISIONS EXP-05 行。
- 现有 4 skill 结构基准（frontmatter / vision / 立场声明借鉴-自创 / 工作流 / 失败模式 / 触发词 / 模板索引）。出处：`skills/proj-{experts,shape,plan,run}/SKILL.md`。
- validator 约束：name 须与目录同名、≤64、小写连字符；description ≤1024；SKILL.md ≤600 行。出处：`scripts/validate_skills.py`。

### 推理

- **推理 · EXP-05 外推**：本仓库属「intent 易重建」简单端，分支判据（EXP-06）未被真正压测；故 proj-survey 的 §分支判据标 provisional + 以 GATE-S 人审批兜底。依据 EXP-05 caveat。

### 待验证

- EXP-06（intent 不可重建难例的分支判据）仍 pending；嵌入 proj-survey §分支判据作为工作流内待验证 GATE。

## 讨论

本轮为执行轮，落实 09 轮 ORD-23~26：

| ORD | 在 proj-survey 的落实位置 |
|-----|--------------------------|
| ORD-23（立项 + 双入口）| §设计 vision 流水线图 + frontmatter |
| ORD-24（分支判据=intent 可重建 + 三分离 + 来源优先级）| §真相源优先级 + §三分离标注 + §分支判据 |
| ORD-25（审计=终端分支 + findings/置信度不作保证 + 内部一致性 + 回流 proj-shape）| §不可违背 S-2 + 分支 B + audit-report-template |
| ORD-26（→ proj-plan 衔接 + WBS 三态 + 自动生成+人 GATE）| §角色分工 + GATE-S + survey-handoff-template（标 ORD-26 待落实）|

EXP-05 跑通的流程（采集→实跑测试→三分离基线→意图评估→分支）固化为 §工作流 0–6 + baseline-template（直接源自 dogfood 产物）。

## 可验证尝试与继续/中止

本轮无新 EXP；EXP-06 维持 pending，已嵌入 proj-survey §分支判据（provisional + GATE-S 兜底）。

## 本轮决定

### 已确定 — 普通决定（落实，无新 ORD）

- [x] **落实**：`skills/proj-survey/SKILL.md`（191 行）+ 3 assets（baseline / audit-report / survey-handoff）已起草 v1；validator 5/5 退 0。
  **来源**：本轮执行；承接 09 轮 ORD-23~26 + EXP-05 passed

### 待确认（下轮继续）

- ~~ORD-26 后半~~ **已落实**（2026-06-02 同轮）：proj-plan §Brownfield 接管入口 + §0 入口二选一 + Round A/B 子步 + WBS 三态列 + project-context 项目类型字段；validator 5/5 退 0
- EXP-06：需一个 intent 难重建的真实 repo 压测分支判据（先放着）
- findings 落地目录 `docs/survey/` 暂定（沿用 EXP-05），未正式确认

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-23~26 | 落实状态更新（待建→已起草 v1 / ORD-26 部分待落实）| ✓ |
| EXP-06 | 维持 pending（嵌入 proj-survey）| ✓ |

讨论状态同步：维持 `deciding`（proj-survey v1 已起草，但 EXP-06 pending + ORD-26 后半未落实）

同步完成时间：2026-06-02 09:50

## 开放问题（下轮）

1. proj-plan brownfield 入口 + WBS 三态的最小改法（ORD-26 后半）。
2. EXP-06 压测用的 intent 难重建 repo 选取。
3. proj-survey 是否需要在真实第三方 repo 上再跑一次（EXP-05 仅 dogfood）。

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-06-02 | proj-survey v1 起草 + EXP-05 流程固化 |
