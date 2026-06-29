# EXP-07b · 判据 + 驱动任务（sandbox dogfood）

> 压测 `proj` 的两条 loop 形态（EXP-07 caveat 1 未覆盖面）。**全部产物沙盒在本目录**，不污染 live `DECISIONS.md`，不碰 shipped skill。本 spike 在**显式 EXP 授权**下以高自主连跑（circuit breaker 仍生效），每个 GATE 处标注「默认档此处 STOP 交人」。

## 被测物
`skills/proj/SKILL.md` §有界 loop 的两条形态：
1. **冷启动全遍历** experts→shape→plan→run（EXP-07 只测了 plan/run 尾段）。
2. **VERIFY 失败 → RE-ROUTE 多迭代**（EXP-07 未触发真实失败→重试→escalate）。

## 驱动任务（真实、小、自指）
「`proj` 的 CLASSIFY 现靠读 `DECISIONS.md` 散文推断 pipeline 入口阶段；是否该在 `DECISIONS.md` 加一个**机读 `pipeline-state` 块**让 CLASSIFY 更稳？」
— 天然横跨 4 段（值不值 → experts；定/否 → shape；如采纳怎么做 → plan；落地+验证 → run），且 run 段有可机判的 VERIFY 目标（块能否被 grep 出必填字段）。

## 成功信号（experiment 须达标）

### 形态 1 · 冷启动全遍历
- S1 顺序正确：STATE→CLASSIFY 后按 experts→shape→plan→run 推进，**无跳段、无乱序**。
- S2 每段 VERIFY 真实跑（至少 run 段为可机判 shell 门）。
- S3 每个 GATE 被正确识别为停点（升 ready-for-implementation / 改 shipped 文件前 / proj-plan GATE）。
- S4 每步 MEMORY 回写（沙盒 state 文件随阶段推进而更新）。

### 形态 2 · 失败 RE-ROUTE
- S5 注入的 VERIFY 失败被检出（非自评 · maker≠grader）。
- S6 iteration budget 内重试，预算耗尽 → 按该专家 escalate 规则回**正确**的上一阶段。
- S7 circuit breaker 生效：累计失败 > 3 → abort 交人（不无限循环）。

### 横切
- S8 无路由冲突 / 双触发（延续 EXP-07 Cursor 结论）。

## 继续 / 中止
- **继续**（S1–S8 全达标）→ `proj` v1 两条 loop 形态验证完成；EXP-07b passed；`proj` 标记 stable。
- **中止**（顺序错乱 / re-route 去错阶段 / 越过 circuit breaker 仍循环）→ 记 defect 于 `proj/SKILL.md`，回 proj-shape 修订 ORD-31 loop 规格。

## 沙盒边界
- 真实 VERIFY shell 命令照跑（防 F9）。
- 驱动任务的「采纳」结论**仅沙盒**——是否真给 `DECISIONS.md` 加 `pipeline-state` 块，留作本 spike 之外的独立决定（见 result §后续）。
