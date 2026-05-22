# 阶段路线图（粗粒度进度计划）

| 字段 | 值 |
|------|-----|
| 模式 | T |
| GATE-2 | 2026-05-19 通过 |
| 对应 WBS | 1.0, 2.0 |

## 阶段一览

| 阶段 | 名称 | 目标 | 映射 WBS | 入口条件 | 出口条件 / 里程碑 |
|------|------|------|----------|----------|-------------------|
| phase-01 | EXP 验证与 skill 补全 | 试跑双轮流程 + 补 PMP/SDD 模板 | 1.0, 2.0–2.2 | GATE-2 通过 | acceptance 通过；EXP-01/02 passed |

## 阶段依赖

```text
Round A (GATE-0) ──→ Round B (GATE-1/2) ──→ phase-01 (GATE-3) ──→ 项目收尾
```

| 依赖 | 说明 |
|------|------|
| phase-01 依赖 GATE-2 | wbs + roadmap 定稿后才 rolling plan |

## 里程碑

| ID | 名称 | 所属阶段 | 完成定义 | 关联 GATE |
|----|------|----------|----------|-----------|
| M-01 | skill 模板齐全 | phase-01 | phase-roadmap + integration + analyze 模板存在 | GATE-3 |
| M-02 | EXP 闭环 | phase-01 | DECISIONS 中 EXP-01/02 = passed | review |

## 与 WBS 的分工

| 文档 | 回答 |
|------|------|
| `wbs.md` | 可交付成果 1.0 / 2.x |
| 本文 | 仅 phase-01 一段；无任务行 |
| `phase-01/plan.md` | 具体任务与验收 |
