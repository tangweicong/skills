# WBS — `proj` orchestrator skill 起草（greenfield · L1–L2）

> 模式 T-lean；无阶段顺序表（在 phase-01/plan）。greenfield 无三态列。

| WBS | 工作包 | 说明 |
|-----|--------|------|
| **1** | **`skills/proj/SKILL.md` 主文档** | |
| 1.1 | frontmatter（name/description）| `name: proj`；description 含触发词 + 「单一入口/orchestrator」语义，**收敛广度**避免与其他 skill 冲突（R1）|
| 1.2 | 定位声明（是什么/不是什么 · ORD-30）| 显式「不重做 host model-invocation」|
| 1.3 | 固定专家集调用表（ORD-29）| experts/shape/plan/survey/run 5 行 + 各自产出 |
| 1.4 | 有界 loop（ORD-31）| STATE→CLASSIFY→PLAN→EXECUTE→VERIFY→GATE?→RE-ROUTE→MEMORY；含冷启动全遍历 + 失败 re-route（EXP-07 caveat 落点）|
| 1.5 | autonomy slider + circuit breaker（ORD-31）| 默认档 = phase 内自迭代 / GATE 停 |
| 1.6 | GATE 清单 + 反模式 + 触发词 | |
| **2** | **README 集成** | |
| 2.1 | 索引表 5 → 6 skill | 加 `proj` 行 |
| 2.2 | `proj` 详细节 | 简述 + 与流水线关系 |
| **3** | **既有 skill 一致性** | |
| 3.1 | `proj-run/SKILL.md`「（规划中）」→ 转正 | 去掉「规划中」标记 |
| **4** | **验证与收尾** | |
| 4.1 | `validate_skills.py` 退 0 | |
| 4.2 | acceptance（含 EXP-07 caveat 自检）| |
| 4.3 | 回写 DECISIONS（ORD-29 落实 + 状态）| |

## GATE-2（合并入 GATE-1+2+3）

- [ ] 用户确认 WBS
