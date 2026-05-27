# 项目管理计划索引（整合管理）

> **PMP**：项目管理计划 = 各子计划 + 基准的**整合入口**（非复制全文）。  
> **SDD**：本文件 + `artifact-index.md` 为 AI 的 plan 层 truth source；人类仍只读 manifest。

| 字段 | 值 |
|------|-----|
| 模式 | T / F |
| 版本 | 1.0 |
| GATE | Round B 定稿后生效 |
| 章程 | `charter.md` |

## 子计划索引

| 知识领域 | artifact | 读者 | 状态 | 说明 |
|----------|----------|------|------|------|
| 整合 | 本文 | AI | | 索引 |
| 范围 | `charter.md` + `wbs.md` | 人(GATE) | | 范围基准 |
| 进度 | `phase-roadmap.md` + `phase-NN/plan.md` | AI / 人(GATE-3) | | 滚动 wave |
| 变更 | `change-log.md` | AI | | 整体变更控制 |
| 质量 | `phase-NN/acceptance.md` | 人 | | 按阶段验收 |
| 风险 | `risk-register.md` | AI | T: TR-02 时 | 简/完整 |
| 干系人 | `stakeholder-register.md` | AI | F / TR-03 | |
| 沟通 | `communication-plan.md` | AI | F / TR-03 | |
| 质量计划 | `quality-plan.md` | AI | F 可选 | |

## 基准声明

| 基准 | 来源 | 变更途径 |
|------|------|----------|
| 范围基准 | charter + wbs | `change-log.md` → 重大变更回 proj-shape |
| 进度基准（粗） | phase-roadmap 里程碑 | 阶段 review 滚动修订 |
| 细进度 | phase-NN/plan | 仅本阶段内修订 |

## 刻意不含（tailoring）

- 成本基准、采购管理、CPM/甘特、逐任务 RACI — 见 `tailoring-decision.md` 命中规则

## DECISIONS 链接

| ID | 在本计划中的体现 |
|----|------------------|
| INV-xx | |
| ORD-xx | |
| EXP-xx | 见 risk-register 或 phase review |
