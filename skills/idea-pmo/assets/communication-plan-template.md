# 沟通计划

> **PMP**：规划沟通管理。  
> **触发**：模式 F，或 TR-03。人类仍只读 manifest；本文件供 AI 执行时对齐。

| 字段 | 值 |
|------|-----|
| 最后更新 | YYYY-MM-DD |

## 沟通矩阵

| 信息 | 受众 | 渠道 | 频率 | 负责人 | artifact |
|------|------|------|------|--------|----------|
| 启动授权 | 用户 | manifest [Round-A] | Round A | AI | initiation-charter, TD |
| 章程定稿 | 用户 | manifest GATE-1 | 一次 | AI | charter.md |
| WBS + 路线图 | 用户 | manifest GATE-2 | 一次 | AI | wbs, phase-roadmap |
| 阶段验收 | 用户 | manifest GATE-N | 每阶段 | AI | acceptance.md |
| 变更 | 用户 | change-log 摘要 | 按需 | AI | change-log.md |

## 原则

- **INV-01**：不得要求用户阅读本文件全文；仅 manifest 列出的 GATE 文档为人读
- 机器维护 artifact 变更通过 `artifact-index` + `change-log` 追踪
