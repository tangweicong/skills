# 变更日志（整体变更控制）— proj-run skill 起草项目

> **PMP**：实施整体变更控制的最小实现。
> **SDD**：规范变更须留痕；推翻 INV/ORD 须回 `proj-shape`，此处仅记录 plan 层变更。

| 字段 | 值 |
|------|-----|
| 模式 | T |
| 最后更新 | 2026-05-27 |

## 变更记录

| ID | 日期 | 类型 | 描述 | 影响 artifact | 关联 DECISIONS | 决策人 | 状态 |
|----|------|------|------|---------------|----------------|--------|------|
| — | — | — | 无变更（项目刚开 Round B，无既批 GATE 后的变更）| — | — | — | — |

**类型**：范围 · 进度 · 计划 · 风险 · 质量 · 其他

**状态**：提议 · 已批准 · 已实施 · 已拒绝 · 回 discuss

## 与 DECISIONS 的分工

| 变更层级 | 处理 |
|----------|------|
| 新 INV/ORD/EXP | **proj-shape**（09 轮）；本 log 仅引用 ID |
| EXP-04 阈值修订（已 v1.3 → v1.4）| 已在 08 轮 proj-shape 完成；本 log 不重复 |
| charter/wbs/roadmap 修订 | 本 log + 更新对应 artifact + artifact-index 版本 |
| phase-01/plan 任务调整 | 直接改 `phase-01/plan.md`；**不必**记 CHG（阶段内）|

## 规则

- GATE 未过的 artifact **不得**通过变更 log 绕过（INV-03）
- 每条已批准变更须同步 `artifact-index.md` 版本列
- 本项目预期变更点：(1) phase-01 plan 中 sub-agent dispatch 计划如有 iteration（如某 template 重写），不记 CHG（阶段内）；(2) 若 EXP-04 aborted 需 abort 本项目，记 CHG-01 "abort"

## 后续触发条件

| 触发 | 动作 | 影响 artifact |
|------|------|---------------|
| EXP-04 passed | 触发后续动作：升级 proj-plan/assets/plan-template.md manifest 段为强制（ORD-15 修订条款）| **不在本项目内执行**；记为 CHG（plan 层"非目标"），由后续单独项目处理 |
| EXP-04 aborted | abort 本项目；回 proj-shape 开 09 轮分析失败模式 | CHG-01 "abort"；本 change-log + artifact-index 状态全 abort |
