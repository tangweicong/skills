# WBS（工作分解结构）— proj-run skill 起草项目

> L1 可交付成果 / L2 子项；**阶段顺序与划分**见 `phase-roadmap.md`；L3+ 任务在 `phase-01/plan.md` rolling 补充。

| 字段 | 值 |
|------|-----|
| 模式 | **T**（TR-01 + TR-02 简表）|
| GATE-2 | 2026-05-27 待通过 |

## WBS 树

| ID | 名称 | 完成定义（一句话）| 关联 DECISIONS |
|----|------|-------------------|----------------|
| **1.0** | **proj-run skill 主文档完整版** | `skills/proj-run/SKILL.md` 覆盖 ORD-18~22 + 工作流 + 失败模式 + 触发词 + validate_skills.py 通过 + ≤600 行 + 中文双层标题 | ORD-17, ORD-18~22 |
| 1.1 | PMP 6 Executing 边界节 | 承接 3 项 + 刻意外置 7 项明列 | ORD-18 |
| 1.2 | 3 Mode 表节 | α/β/γ + 触发条件 + 选择决策树 | ORD-19, ORD-16 |
| 1.3 | Sub-agent dispatch 决策树节 | context 回溯判据；不按 cost | ORD-20 |
| 1.4 | Dispatch manifest schema 节 | 5 字段闭环 + 示例引用 1.1 模板 | ORD-21 |
| 1.5 | Validation gate 3 类节 | structural / lint / behavioral + 失败 escalate 流程 | ORD-22 |
| 1.6 | 工作流节（前置 → dispatch → validation → escalate → acceptance）| 串接 1.1-1.5 | INV-03, INV-04 延续 |
| 1.7 | Circuit breaker + 失败模式 + 触发词 + 模板索引 | 与 proj-plan/SKILL.md 风格对齐 | INV-03 |
| **2.0** | **proj-run/assets/ 5 templates** | 5 个 template 文件齐 + structural validation 通过 | ORD-18~22 落实层 |
| 2.1 | `dispatch-manifest-template.md` | 含 5 字段闭环表格 + 字段说明 + 完整示例 + `rg -c "model:" = 0` 自校验 | ORD-21 |
| 2.2 | `acceptance-template.md` | 含 validation 结果段 + token cost 段 + escalate 标记段 + GATE 联动段 | ORD-15 输出契约 |
| 2.3 | `cursor-agents-template.md` | YAML frontmatter（description/tools/is_background/readonly/model）+ legacy plan warning | ORD-19 Mode α |
| 2.4 | `message-bus-template.md` | `.apm/bus/` 目录结构 + 触发条件 + "不含 runtime" 明示 | ORD-19 Mode β |
| 2.5 | `validation-gate-template.md` | 3 类 gate 标准段 + 每类示例命令 + 失败 escalate 流程 | ORD-22 |
| **3.0** | **PM artifact 全集** | `docs/pmo/proj-run-draft/` 全套 + analyze 通过 + 全 GATE 通过 | INV-01~03, ORD-03, ORD-04, ORD-09 |
| 3.1 | Round A artifact（已完成）| project-context / tailoring-decision / initiation-charter / human-read-manifest | GATE-0 ☑ |
| 3.2 | Round B artifact（本节完成中）| charter / wbs / phase-roadmap / integration-plan / change-log / artifact-index / risk-register | GATE-1+2 |
| 3.3 | phase-01 artifact | plan（含 dispatch manifest） / acceptance / review | GATE-3 |
| **4.0** | **EXP-04 试跑度量与回写** | cost 实际数据 + GATE 通过率 + analyze + validate 结果回写 DECISIONS.md EXP-04 行 | EXP-04 v1.4 |
| 4.1 | token cost 采集 | 每节点（Round A / B / phase-01 plan / dispatch / SKILL 直写 / 同步）记录 input/output tokens 估算 | EXP-04 |
| 4.2 | GATE 一次通过率 | 4 GATE 通过/总数 ≥ 80% | EXP-04 |
| 4.3 | DECISIONS 回写 | EXP-04 状态 = passed / aborted + 数据表 | EXP-04 |
| **5.0** | **skills/README.md 同步** | proj-run 行从"骨架 v0"更新为"完整版"+ 链 ORD-18~22 | README 维护 |

## 依赖

- 2.0（templates）→ 1.0（SKILL.md 引用 templates 路径，必须先有 templates 再写 SKILL.md 的"模板索引"节）→ 但本项目中 1.0 可以同时写"模板索引"节（路径已知），不必严格串行；执行顺序见 phase-01/plan
- 3.3（phase-01）→ 必须 3.2 完成（GATE-1+2 通过）
- 4.0（EXP-04 度量）→ 贯穿全 phase，无 hard dependency；4.3 必须 1.0 + 2.0 + 3.0 全完成后执行
- 5.0 → 必须 1.0 完成后
