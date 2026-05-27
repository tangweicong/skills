# 人类必读清单（Human Read Manifest） — proj-run skill 起草项目

> **硬上限 5 项**（ORD-05）。Round A **固定 2 项**（ORD-09）。其余为 GATE 槽位。

| # | 标记 | 文档 | GATE | 状态 | 预估阅读 |
|---|------|------|------|------|----------|
| 1 | **[Round-A]** | `initiation-charter.md` | GATE-0（与 #2 合并）| ☑ 已通过 | ~3 min |
| 2 | **[Round-A]** | `tailoring-decision.md` | GATE-0 | ☑ 已通过 | ~2 min |
| 3 | | `charter.md` | GATE-1 | ☑ 已通过 | ~3 min |
| 4 | | `wbs.md` | GATE-2 | ☑ 已通过（含 6 个参考文档 + analyze 全过）| ~2 min |
| 5 | | `phase-01/plan.md`（含 dispatch manifest 段）| GATE-3 | ☑ 已通过 + phase-01 完成（acceptance 部分通过 · EXP-04 ABORTED · 主交付全过）| ~5 min |

**图例**：☐ 待读 · ☑ 已通过 · 🔒 GATE 未开 · ⊘ 跳过（须备注）

## GATE 记录

| GATE | 通过 | 日期 | 确认人 |
|------|------|------|--------|
| GATE-0 | ☑ | 2026-05-27 | 用户（approve · Round A → Round B）|
| GATE-1 | ☑ | 2026-05-27 | 用户（approve · GATE-1+2 合并）|
| GATE-2 | ☑ | 2026-05-27 | 用户（approve · GATE-1+2 合并 · analyze 全 7 硬规则过）|
| GATE-3 | ☑ | 2026-05-27 | 用户（approve · 开始 sub-agent dispatch）|

## 说明

- Round A 结束前：人**只读** #1–#2（initiation-charter + tailoring-decision）
- GATE-0 通过后解锁 #3–#4 生成与审阅
- GATE-2 通过后解锁 #5 生成与审阅（含 `## Sub-agent dispatch manifest` 段 · ORD-21 5 字段闭环示范）
- GATE-3 通过后由 AI 执行 phase-01 的 sub-agent dispatch；执行结果回写 acceptance.md（**不在 manifest**，遵守 INV-01）
- **禁止**要求阅读 `artifact-index.md` / `integration-plan.md` / `change-log.md` / `risk-register.md` 及未列出的全量树（INV-01）

## 与 EXP-04 试跑的关联

| GATE | EXP-04 度量点 |
|------|---------------|
| GATE-0 | 起算点；之前的 Opus 工作（08 轮文档 + DECISIONS 同步 + Round A）记作 plan 阶段 cost |
| GATE-1 | Round B 中段；charter 定稿后 |
| GATE-2 | Round B 末端；wbs + roadmap + integration + change-log + artifact-index + risk 后；analyze 通过 |
| GATE-3 | phase-01 plan 定稿 + dispatch manifest 写好；sub-agent dispatch 之前 |
| GATE-3 后 | sub-agent dispatch + Opus 评审 + iteration；写入 acceptance.md（含 token cost 实际数据 + EXP-04 v1.4 阈值比对）|

GATE 一次通过率 = 一次审过的 GATE 数 ÷ 总 GATE 数；本项目 4 GATE，达 80% 需至少 4 个一次过（4/4=100% 或 ≥4/5=80%；实际 4/4 才满足）。
