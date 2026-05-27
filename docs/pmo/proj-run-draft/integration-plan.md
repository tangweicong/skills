# 项目管理计划索引（整合管理）— proj-run skill 起草项目

> **PMP**：项目管理计划 = 各子计划 + 基准的**整合入口**（非复制全文）。
> **SDD**：本文件 + `artifact-index.md` 为 AI 的 plan 层 truth source；人类仍只读 manifest。

| 字段 | 值 |
|------|-----|
| 模式 | T（TR-01 + TR-02 简表）|
| 版本 | 1.0 |
| GATE | Round B 定稿后生效 |
| 章程 | `charter.md` |

## 子计划索引

| 知识领域 | artifact | 读者 | 状态 | 说明 |
|----------|----------|------|------|------|
| 整合 | 本文 | AI | 启用 | 索引 |
| 范围 | `charter.md` + `wbs.md` | 人（GATE-1+2）| 启用 | 范围基准 |
| 进度 | `phase-roadmap.md` + `phase-01/plan.md` | AI / 人（GATE-3）| 启用 | 单 phase 滚动 |
| 变更 | `change-log.md` | AI | 启用（空表头）| 整体变更控制 |
| 质量 | `phase-01/acceptance.md` | AI | 启用（phase-01 时）| 含 EXP-04 v1.4 阈值判定 |
| 风险 | `risk-register.md` | AI | 启用（TR-02 简表）| EXP-04 中止信号 + 降级路径 |
| 干系人 | `stakeholder-register.md` | — | **未启用** | 无外部 stakeholder（TR-03 未命中）|
| 沟通 | `communication-plan.md` | — | **未启用** | 同上 |
| 质量计划 | `quality-plan.md` | — | **未启用** | validation 已由 acceptance + analyze + validate_skills 覆盖 |

## 基准声明

| 基准 | 来源 | 变更途径 |
|------|------|----------|
| 范围基准 | charter（§范围）+ wbs（5 个 L1）| `change-log.md` → 重大变更回 proj-shape 开 09 轮 |
| 进度基准（粗）| phase-roadmap M-01~M-05 里程碑 | phase-01 review 时滚动修订；项目预期 1 阶段完成 |
| 细进度 | phase-01/plan | 仅本阶段内修订（不记 CHG）|
| **EXP-04 baseline 基准** | ≈ $6.75（proj-plan SKILL+21 assets / 1066 行 × Opus blended × 3x 迭代因子）| 不修订（已锁定 · 详见 `phase-01/acceptance.md` 度量段）|

## 刻意不含（tailoring · 沿用 proj-plan ORD-10 边界）

- 成本基准（PMP 成本管理 4 过程；01 轮刻意省略；本项目仅在 EXP-04 度量段记 token cost 数据）
- 采购管理（无采购需求）
- CPM/甘特、资源平衡、逐任务 RACI（个人项目无需）
- 全量 WBS 词典 L3+（rolling 进 phase-01/plan）
- F 模式产物（stakeholder / communication / quality plan · 未启用）

## DECISIONS 链接

| ID | 在本计划中的体现 |
|----|------------------|
| INV-01 | manifest ≤5 项强制；本项目 4 项满足 |
| INV-02 | phase-roadmap 无任务表；细任务仅在 phase-01/plan |
| INV-03 | GATE 串行；analyze 失败不得标 GATE 通过 |
| INV-04 | proj-plan 不含执行；本项目 sub-agent dispatch 是 EXP-04 试跑性质，文档只规划，执行环节标 "本项目 EXP-04 测试性质" 不入 proj-plan SKILL.md |
| ORD-03 | 双轮启动 Round A（已完）→ Round B（本节）|
| ORD-04 | Coach hybrid T 模式（沿用 EXP-01 验证模式）|
| ORD-09 | Round A 固定 2 项 |
| ORD-15 | dispatch manifest 段：v0 可选；本项目 phase-01/plan 仍按 5 字段闭环写（**示范用**，不改 proj-plan template）|
| ORD-17 | proj-run 独立 skill；本项目交付即 proj-run 完整版 |
| ORD-18~22 | 落实到 SKILL.md 5 个章节 + 5 个 templates |
| EXP-04 | 见 `risk-register.md` R-01 + `phase-01/acceptance.md` 度量段 |
