# 阶段路线图（粗粒度进度计划）— proj-run skill 起草项目

> **PMP**：制定进度计划（rolling wave 远期层）；**不是**任务表（INV-02）。
> **SDD**：plan 层（宏观 how/when）；细任务仅在 `phase-01/plan.md`。

| 字段 | 值 |
|------|-----|
| 模式 | T |
| GATE-2 | 2026-05-27 待通过 |
| 对应 WBS | 1.0 + 2.0 + 3.0 + 4.0 + 5.0（全部由 phase-01 承担）|

## 阶段一览

| 阶段 | 名称 | 目标（一句话）| 映射 WBS | 入口条件 | 出口条件 / 里程碑 |
|------|------|----------------|----------|----------|-------------------|
| phase-01 | proj-run 完整版起草 + EXP-04 试跑 | 完成 SKILL.md + 5 templates + EXP-04 度量回写 | 1.0 + 2.0 + 3.3 + 4.0 + 5.0 | GATE-2 通过 | acceptance 通过（含 EXP-04 v1.4 阈值判定）+ validate_skills.py 通过 |

**单 phase 设计理由**：项目规模适中（SKILL.md ~400 行 + 5 templates ~150 行/个 = ~1150 行总输出）；EXP-04 试跑要求一次跑完同一流水线收集数据（拆 phase 会引入额外 plan/acceptance overhead 干扰度量）；rolling 原则：若试跑中发现规模过大或失败模式需独立处理，再开 phase-02。

## 阶段依赖（逻辑顺序，非甘特）

```text
phase-01 ──→ （如需要 phase-02）
```

| 依赖 | 说明 |
|------|------|
| phase-02 | 仅在 phase-01 acceptance 失败 / EXP-04 aborted 时考虑开新阶段（如：sub-agent 大量失败需重新设计 dispatch 策略，开 phase-02 单独修缮）|

## 里程碑

| ID | 名称 | 所属阶段 | 完成定义 | 关联 GATE |
|----|------|----------|----------|-----------|
| M-01 | phase-01 plan + dispatch manifest 定稿 | phase-01 | `phase-01/plan.md` 含 `## Sub-agent dispatch manifest` 段（ORD-21 5 字段闭环），8 个 task 全部 specialist + validation + budget + escalate 完整 | GATE-3 |
| M-02 | 5 templates 全部 sub-agent 产出 + validation 通过 | phase-01 | `skills/proj-run/assets/` 5 文件存在 + 每个通过 structural + behavioral validation | — |
| M-03 | SKILL.md 完整版（Opus 直写）+ validate_skills.py 通过 | phase-01 | `skills/proj-run/SKILL.md` 覆盖 v0 + validate 退 0 + ≤600 行 | — |
| M-04 | EXP-04 数据回写 DECISIONS + analyze 通过 | phase-01 | DECISIONS EXP-04 状态 = passed / aborted；analyze-checklist 全 7 硬规则通过 | — |
| M-05 | acceptance 通过 + review 完成 | phase-01 | `phase-01/acceptance.md` 全 checkbox 通过；`phase-01/review.md` 含 lessons + circuit breaker 检查 | — |

## 与 WBS 的分工

| 文档 | 回答的问题 |
|------|------------|
| `wbs.md` | **做什么**（1.0 SKILL / 2.0 templates / 3.0 PM artifacts / 4.0 EXP 度量 / 5.0 README 同步）|
| 本文 | **何时、分几段、段间依赖与出入口**（仍不含任务行）|
| `phase-01/plan.md` | **怎么做**（活动/任务、执行者、验收 + dispatch manifest 5 字段闭环示范）|

## 滚动明细说明

- L3+ 活动、工期、资源 → `phase-01/plan.md`（GATE-3 时确定）
- phase-02 不在本轮预定义；若 phase-01 acceptance 通过则项目关闭，不开 phase-02
