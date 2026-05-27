# Tailoring 决策 — proj-run skill 起草项目

| 字段 | 值 |
|------|-----|
| 状态 | 草案 → GATE-0 待确认 |
| 建议模式 | **T**（裁剪最小） |
| 命中规则 | TR-01（个人/AI 辅助 / 无监管）+ TR-02（含 EXP-04 影响路线）|
| 依据 DECISIONS | INV-01~04 + ORD-01~22 + EXP-04 v1.4 |

## 建议摘要

**建议模式 T**。理由：(1) 个人开发者 + AI 辅助，无外部 stakeholder（命中 TR-01）；(2) 含 EXP-04 影响路线但只是单 EXP 单 phase，TR-02 触发条件下 risk-register 维持简表即可，无需启用 F 模式全套 risk 流程；(3) 不命中 TR-04（无合规/审计/合同），无需 F 模式；(4) 项目规模与 EXP-01 (proj-plan 发布) 相当，沿用 T 模式有先例验证（EXP-01 passed）。

## 产物清单（模式 T · 最小集 + TR-02 简表）

| 路径 | 读者 | 阶段 | 说明 |
|------|------|------|------|
| `docs/pmo/proj-run-draft/project-context.md` | 人（Round A）| Round A | 已完成 |
| `docs/pmo/proj-run-draft/tailoring-decision.md` | 人（GATE-0）| Round A | 本文档 |
| `docs/pmo/proj-run-draft/initiation-charter.md` | 人（GATE-0）| Round A | Round A 章程草案 |
| `docs/pmo/proj-run-draft/human-read-manifest.md` | 人（GATE 串）| Round A | ≤5 项硬上限 |
| `docs/pmo/proj-run-draft/charter.md` | 人（GATE-1）| Round B | Round B 章程定稿 |
| `docs/pmo/proj-run-draft/wbs.md` | 人（GATE-2）| Round B | L1–L2 |
| `docs/pmo/proj-run-draft/phase-roadmap.md` | AI（人可选 GATE-2 扫读）| Round B | 单 phase 项目，roadmap 内容简 |
| `docs/pmo/proj-run-draft/integration-plan.md` | AI | Round B | PMP 整合索引 |
| `docs/pmo/proj-run-draft/change-log.md` | AI | Round B | 整体变更控制 |
| `docs/pmo/proj-run-draft/artifact-index.md` | AI | Round B | SDD truth source；含本项目 proj-run + assets 5 文件 + sub-agent 产出登记 |
| `docs/pmo/proj-run-draft/risk-register.md` | AI | Round B | **TR-02 简表**：EXP-04 中止信号 + 降级路径 |
| `docs/pmo/proj-run-draft/phase-01/plan.md` | 人（GATE-3）| Rolling | 含 `## Sub-agent dispatch manifest` 段（ORD-21 5 字段闭环；本项目示范使用）|
| `docs/pmo/proj-run-draft/phase-01/acceptance.md` | AI | Rolling | EXP-04 token cost 数据回写位置 |
| `docs/pmo/proj-run-draft/phase-01/review.md` | AI | Rolling | lessons + circuit breaker 检查 |

**不生成**（F 模式专属，本项目不启用）：`stakeholder-register.md`（无外部 stakeholder）/ `communication-plan.md`（同上）/ `quality-plan.md`（validation 已由 acceptance + analyze + validate_skills.py 覆盖，无需额外 quality plan）。

## 理由

- 规则 **TR-01**：单人 + AI 辅助 + 无监管 → 模式 T；最小产物集 = charter / wbs / phase-roadmap / integration-plan / change-log / artifact-index
- 规则 **TR-02**：含 EXP-04（v1.4 阈值修订）且假设影响路线（model-tier 是否经济可持续）→ 追加 risk-register（简表）；不升 F 模式
- 规则 **TR-03**：不命中（无外部 stakeholder）
- 规则 **TR-04**：不命中（无合规/审计）
- 规则 **TR-05**：不命中（纯软件）
- 规则 **TR-06**：不命中（DECISIONS 状态 = `ready-for-implementation`，未 blocked）
- 对接 DECISIONS：INV-01~04 全适用；ORD-01~22 全适用；EXP-04 v1.4 为本项目核心验证目标

## GATE-0 确认

- [ ] 用户确认模式：**T**（override：__________）
- [ ] 用户确认产物清单（11 项 + 3 phase-01 子项）
- 确认人 / 日期：__________________________
