# 项目章程 — proj-run skill 起草项目（含 EXP-04 试跑）

| 字段 | 值 |
|------|-----|
| 版本 | 1.0（Round B 定稿）|
| GATE-1 | 2026-05-27 待通过 |
| 基于 | `initiation-charter.md` + DECISIONS（含 08 轮 ORD-18~22 + EXP-04 v1.4）|

## 综合叙述

本项目"形状" = **proj-* 流水线自反式应用**：用 proj-shape（08 轮决议） → proj-plan（Round A/B/phase-01 规划） → proj-run（dispatch sub-agent 执行）三段流水线，把 `proj-run` skill 自身从 v0 骨架推到完整版。**这是一个动作两个收益的设计**：交付 = proj-run 完整版（满足 ORD-17 触发的下一步）；试跑数据 = EXP-04 v1.4 验证（model-tier 经济性 + GATE 一次通过率）。

**重量策略**（沿用 proj-plan 模式 T）：机器（我，Opus）维护 charter / WBS / phase-roadmap / integration-plan / change-log / artifact-index / risk-register（简表）；用户只读 manifest 中 4 项（initiation-charter+tailoring-decision 已通过 GATE-0；charter+wbs 待 GATE-1；phase-01/plan 待 GATE-3）。

**Coach hybrid 复用**：模式 T + TR-02 简表组合已由 EXP-01 在 docs/pmo/（proj-plan 发布项目）验证 passed；本项目沿用，不重复 tailoring 设计；本项目独立 namespace `docs/pmo/proj-run-draft/` 避免污染历史遗产。

**EXP-04 测量嵌入**：试跑数据采集贯穿全部 GATE，最终回写 `phase-01/acceptance.md` 与 `docs/discuss/DECISIONS.md` EXP-04 行；passed / aborted 判定见 §成功标准。

## 成功标准 · 非目标 · 权限

| 成功 | 非目标 | 权限 |
|------|--------|------|
| 6 条 checkbox 全过：proj-run/SKILL.md 完整版 + 5 templates + 08 轮文档 + DECISIONS 同步 + validate_skills.py + EXP-04 v1.4 cost ≥3x + GATE ≥80% | 实现 Mode α/β runtime；改 proj-plan/proj-experts/proj-shape；改 docs/pmo/（EXP-01 遗产）；本轮新建 phase-02 | GATE → 用户（ORD-11 Sponsor + PM 关键决策）|
| EXP-04 passed → 后续触发 ORD-15 manifest 段升级为强制 | 在本项目内执行 ORD-15 升级（属后续动作） | 新决定 → proj-shape（不在 proj-plan / proj-run 内创建） |
| EXP-04 aborted → 阻塞 ORD-15 升级；回 proj-shape 开 09 轮分析失败模式 | 阈值未达即视为不彻底（按 v1.4 阈值客观判定）| sub-agent dispatch → AI（评审；validation 反复失败 escalate 给用户）|

## 范围与边界（链 initiation-charter §范围）

**在范围内**（6 项）：
1. `skills/proj-run/SKILL.md` 完整版起草（覆盖 ORD-18~22 + 工作流 + 失败模式 + 触发词；≤600 行；中文双层标题）
2. `skills/proj-run/assets/` 5 templates（dispatch-manifest / acceptance / cursor-agents / message-bus / validation-gate）
3. `docs/pmo/proj-run-draft/` 全套 PM artifact（Round A 已完成 + Round B 本节 + phase-01 待 GATE-3）
4. EXP-04 试跑度量与回写 DECISIONS.md
5. 更新 `skills/README.md` proj-run 行（v0 骨架 → 完整版）
6. （仅 EXP-04 passed 时触发的后续动作 placeholder：更新 proj-plan/assets/plan-template.md manifest 段为强制 · 不在本项目执行）

**显式非目标**（6 项 · 同 initiation-charter）：见 `initiation-charter.md` §显式非目标。

## 与 DECISIONS 追溯

| 主题 | DECISIONS ID |
|------|-------------|
| 人只读 manifest（≤5）| INV-01, ORD-05, ORD-09 |
| 双轮启动 Round A/B | ORD-03 |
| Coach hybrid + GATE-0 | ORD-04 |
| 目录命名 proj-run（含 namespace 子目录）| ORD-01, ORD-17 |
| 不含执行（proj-plan 不启动 sub-agent；本项目的 sub-agent dispatch 属 EXP-04 试跑性质）| INV-04 |
| Round A 固定 2 项 | ORD-09 |
| Vision 声明（Supervised-AI mode）| ORD-11 |
| Sub-agent dispatch manifest 承诺字段 | ORD-15 |
| Cursor 约束披露 | ORD-16 |
| 建立 proj-run skill | ORD-17 |
| **本项目核心交付**（ORD-18~22 落实到 proj-run/SKILL.md + assets）| ORD-18~22 |
| **本项目核心验证**（EXP-04 v1.4 阈值）| EXP-04 |

## 修订记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-27 | Round B 初稿；待 GATE-1 通过 |
