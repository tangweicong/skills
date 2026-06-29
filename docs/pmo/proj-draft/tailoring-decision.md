# Tailoring 决策 — `proj` orchestrator skill 起草

| 字段 | 值 |
|------|-----|
| 状态 | 草案 → GATE-0 待确认 |
| 建议模式 | **T**（裁剪最小）+ JIT 右调 |
| 命中规则 | TR-01（个人/AI 辅助/无监管）|
| 依据 DECISIONS | INV-01~04 + ORD-28~31 + EXP-07 |

## 建议摘要

**建议模式 T，且按 JIT（ORD-27）进一步右调**。理由：(1) 个人 + AI、无外部 stakeholder（TR-01）；(2) 不命中 TR-04（无合规/审计）；(3) **范围已被 ORD-29/30/31 + 验证过的 spike 高度锁定**——剩余工作接近「把 spike 转正 + 压 caveat + validate」，规模小于 EXP-04（proj-run 起草）；(4) 单 phase 即可。

## 两个执行档（GATE-0 请选其一）

| 档 | Round A | Round B 产物 | phase | GATE 节奏 | 适用 |
|----|---------|--------------|-------|-----------|------|
| **T-full**（默认 mode T）| 4 件已生成 | charter / wbs / phase-roadmap / integration-plan / change-log / artifact-index | phase-01/{plan,acceptance,review} | GATE-0 / GATE-1+2 合并 / GATE-3 | 想完整 dogfood 流水线（同 proj-run-draft 先例）|
| **T-lean**（JIT 极简）| 复用本 4 件 | **charter + wbs（合一精简）+ artifact-index** | phase-01/{plan,acceptance} | GATE-0 / **GATE-1+2+3 一次合并** | 范围已锁、求快；senior-eng 视角对 100 行 skill 更相称 |

> 我的建议：**T-lean**。范围由 ORD/ spike 锁死，phase-roadmap/integration-plan/change-log 对单 phase 小 skill 是仪式 > 价值（撞 JIT「推迟细节」+ 简约）。但 **mode 由你定**（GATE-0；agent 不得单方面定）。

## 产物清单（T-lean · 推荐）

| 路径 | 读者 | 阶段 |
|------|------|------|
| `proj-draft/project-context.md` | 人（Round A）| 已生成 |
| `proj-draft/tailoring-decision.md` | 人（GATE-0）| 本文档 |
| `proj-draft/initiation-charter.md` | 人（GATE-0）| 已生成 |
| `proj-draft/human-read-manifest.md` | 人（GATE 串）| 已生成 |
| `proj-draft/charter.md` | 人（GATE-1）| Round B |
| `proj-draft/wbs.md` | 人（GATE-2）| Round B（L1–L2 精简）|
| `proj-draft/artifact-index.md` | AI | Round B（SDD truth source）|
| `proj-draft/phase-01/plan.md` | 人（GATE-3）| Rolling |
| `proj-draft/phase-01/acceptance.md` | AI | Rolling（含 EXP-07 caveat 自检）|

**T-lean 不生成**：phase-roadmap（单 phase，无多阶段排序需要）/ integration-plan（无多子计划可索引）/ change-log（小项目，变更直接记 DECISIONS）/ review（acceptance 已含收尾自检）/ risk·stakeholder·communication·quality（F 专属，不命中）。

> 选 **T-full** 则补回 phase-roadmap / integration-plan / change-log / review。

## 规则对账

- **TR-01** 命中 → 模式 T
- TR-02 不命中（EXP-07 已 passed，无 in-flight 影响路线的 EXP；EXP-08 属独立后续，不在本项目范围）
- TR-03 / TR-04 / TR-05 / TR-06 均不命中

## GATE-0 确认

- [ ] 确认模式：**T-lean**（推荐）/ T-full / override：________
- [ ] 确认产物清单
- 确认人 / 日期：________________________
