# Tailoring 决策

| 字段 | 值 |
|------|-----|
| 状态 | **已确认**（GATE-0 @2026-05-19） |
| 建议模式 | **T**（裁剪） |
| 命中规则 | **TR-01**（个人 AI 辅助、无监管） |
| 依据 DECISIONS | ORD-01, ORD-04, ORD-08；EXP-01 |

## 建议摘要

本仓库为个人 skills 维护，无合规交付；采用 **模式 T**：charter + WBS L2 + phase-roadmap + **integration-plan** + **change-log** + artifact-index + rolling phase。

## 产物清单

| 路径 | 读者 | 阶段 | 说明 |
|------|------|------|------|
| initiation-charter.md | 人 Round-A | A | GATE-0 |
| tailoring-decision.md | 人 Round-A | A | GATE-0 |
| charter.md | 人 GATE-1 | B | 定稿 |
| wbs.md | 人 GATE-2 | B | L1–L2 |
| phase-roadmap.md | AI | B | 粗进度；无任务表 |
| integration-plan.md | AI | B | PMP 整合索引 |
| change-log.md | AI | B | 变更控制 |
| artifact-index.md | AI | B | SDD 索引 |
| phase-01/plan.md | 人 GATE-3 | Rolling | 进阶段时 |
| skills/idea-pmo/** | AI | 执行* | *非 idea-pmo 内，属实现 |

## 理由

- **TR-01**：单人 AI 辅助 skills 仓库 → 默认 T
- **ORD-08**：EXP-01 试跑需验证双轮流程，非 TR-04 全量场景
- 无 EXP 阻塞；DECISIONS 已 ready

## GATE-0 确认

- [x] 用户确认模式：**T**
- [x] 用户确认产物清单
- 确认人：用户 @2026-05-19「可以开工，Round A 固定 2 项」
