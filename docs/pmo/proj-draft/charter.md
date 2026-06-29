# 项目章程（Charter · 定稿） — `proj` orchestrator skill

| 字段 | 值 |
|------|-----|
| 状态 | Round B 定稿 → GATE-1（合并）|
| 模式 | T-lean |
| 上游 | DECISIONS ORD-29/30/31 + EXP-07 passed |

## 1. 目的与价值

补 proj-* 流水线缺失的**用户总入口**：薄 Supervisor + 有界 plan-execute-verify loop + facade，让用户「描述问题」即可触发「AI 编排 5 个专家 skill → 在 GATE 处交人」的闭环；**不**重做 host 已具备的 model-invocation 路由（ORD-30）。

## 2. 范围

| | 内容 |
|---|------|
| **范围内** | `skills/proj/SKILL.md`（固定专家集 + 有界 loop + GATE 清单 + autonomy slider + 反模式 + 触发词）；根 README 扩 6 skill；proj-run「规划中」标记转正 |
| **范围外** | proj-run 通用化 / 跨 runtime 适配器（ORD-28 · EXP-08 后续）；experts/shape/plan/survey 正文不改 |

## 3. 成功标准（验收基线）

1. `skills/proj/SKILL.md` shipped；`uv run scripts/validate_skills.py` 退 0（6 skill）。
2. ORD-29（facade/Supervisor）、ORD-30（收窄·不重做 host 路由，**显式声明**）、ORD-31（有界 loop + autonomy slider + circuit breaker）三决定在 SKILL.md 可见。
3. README 索引 + `proj` 详细节一致（6 skill）。
4. acceptance 含 EXP-07 两条 caveat 的**设计层自检**：冷启动 experts→shape→plan→run 全遍历路径 + 含失败 VERIFY→RE-ROUTE 的多迭代 loop 在 SKILL.md 有明确落点。

## 4. 关键约束 / 不变量

- INV-04：本 skill 只规划，实际写 `proj` 属执行（对话/proj-run）。
- ORD-30 / ORD-31 守界；不写新 INV·ORD（proj-shape 域）。
- SKILL.md ≤600 行；`name: proj` = 目录名。

## 5. 干系人

- Sponsor + PM 决策 = 用户；PM 执行 + artifact 维护 = AI。无外部干系人。

## 6. 高层风险

- R1：`proj` description 过广 → host 侧触发冲突。缓解：description 收敛 + 设计注记；实测留 ORD-28/EXP-08。
- R2：spike→shipped 出现非预期返工。缓解：spike 已 EXP-07 验证，偏差小；单 phase 可吸收。

## GATE-1（合并入 GATE-1+2+3）

- [ ] 用户确认章程
