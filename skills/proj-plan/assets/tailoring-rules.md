# Tailoring 规则库（Coach hybrid · 规则侧）

> AI 读 `DECISIONS` + `project-context` 后，用本表 **约束建议**；最终模式须 **GATE-0 用户确认**。

## 规则 ID 与默认模式

| 规则 ID | 条件（满足任一即命中） | 建议模式 | 最小产物集（T） | F 额外产物 |
|---------|------------------------|----------|-----------------|------------|
| TR-01 | 个人/单人 AI 辅助；无外部监管 | **T** | charter, wbs L2, phase-roadmap, **integration-plan**, **change-log**, artifact-index | — |
| TR-02 | 存在 EXP-xx 且假设影响路线 | **T** | + **risk-register（简表）** | risk-register 完整节 |
| TR-03 | ≥2 外部 stakeholder 或需对外交付 | **T** | + stakeholder-register（简） | + communication-plan |
| TR-04 | 合规/审计/合同交付 | **F** | — | 全量 PM 树（见下） |
| TR-05 | 物理世界/线下为主 | **T** | plan 中人工步骤显式 | quality-plan 扩展 |
| TR-06 | DECISIONS 讨论状态曾 blocked | **T** | 先 resolve EXP | — |

**默认**：无命中 TR-04 → 建议 **T**；命中 TR-04 → 建议 **F**（用户可 override 为 T）。

## 模式 T 默认产物（PMP 最小计划集）

| artifact | PMP 对应 |
|----------|----------|
| `charter.md` | 章程 / 范围说明书 |
| `wbs.md` | 创建 WBS |
| `phase-roadmap.md` | 制定进度计划（rolling 远期） |
| `integration-plan.md` | 项目管理计划（整合索引） |
| `change-log.md` | 整体变更控制 |
| `phase-NN/plan.md` | 定义活动 + 估时（rolling 近期） |
| `phase-NN/acceptance.md` | 确认范围 / 控制质量 |
| `phase-NN/review.md` | 监控 + 收尾 |

## 模式 F 额外产物（机器维护，人仍只读 manifest）

- `risk-register.md`（简表 + 完整节）
- `stakeholder-register.md`
- `communication-plan.md`
- `quality-plan.md`（按需）
- Round B 后运行 [analyze-checklist.md](analyze-checklist.md) 全项

## 过程组启用

| 过程组 | T | F |
|--------|---|---|
| Initiate | ✓ | ✓ |
| Plan | ✓（rolling wave） | ✓ |
| Execute | ✗（非本 skill） | ✗ |
| Monitor & Control | review + change-log + analyze | + 风险监督 |
| Close | review + close checklist | + 同上 |

## 输出 schema（tailoring-decision.md 必填）

- 命中规则 ID 列表
- 建议模式 T/F
- 产物清单（路径 + 读者：人/AI）
- 理由（链 DECISIONS ID）
- 用户 override 空白（GATE-0 填）

## 参考

- PMP × SDD 对照：[pmp-sdd-map.md](pmp-sdd-map.md)
