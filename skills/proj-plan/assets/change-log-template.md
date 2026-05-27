# 变更日志（整体变更控制）

> **PMP**：实施整体变更控制的最小实现。  
> **SDD**：规范变更须留痕；推翻 INV/ORD 须回 `proj-shape`，此处记录 plan 层变更。

| 字段 | 值 |
|------|-----|
| 模式 | T / F |
| 最后更新 | YYYY-MM-DD |

## 变更记录

| ID | 日期 | 类型 | 描述 | 影响 artifact | 关联 DECISIONS | 决策人 | 状态 |
|----|------|------|------|---------------|----------------|--------|------|
| CHG-01 | | 范围/进度/计划/… | | wbs.md | | 用户 GATE | 已批准 |

**类型**：范围 · 进度 · 计划 · 风险 · 质量 · 其他

**状态**：提议 · 已批准 · 已实施 · 已拒绝 · 回 discuss

## 与 DECISIONS 的分工

| 变更层级 | 处理 |
|----------|------|
| 新 INV/ORD/EXP | **proj-shape**；本 log 仅引用 ID |
| charter/wbs/roadmap 修订 | 本 log + 更新对应 artifact + artifact-index 版本 |
| phase plan 内任务调整 | 直接改 `phase-NN/plan.md`；**不必**记 CHG（阶段内） |

## 规则

- GATE 未过的 artifact **不得**通过变更 log 绕过（INV-03）
- 每条已批准变更须同步 `artifact-index.md` 版本列
