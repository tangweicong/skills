# EXP-07b 结果 · `proj` 两条 loop 形态真实压测

| 字段 | 值 |
|------|-----|
| EXP | EXP-07b（承接 EXP-07 caveat 1）|
| 日期 | 2026-06-29 |
| 被测物 | `skills/proj/SKILL.md` §有界 loop 两形态：①冷启动全遍历 ②VERIFY 失败→RE-ROUTE |
| 方法 | 沙盒 dogfood（`docs/pmo/proj-07b-spike/`）：真实小自指任务驱动 experts→shape→plan→run + 真实 shell VERIFY + 注入失败 + 有界 loop 控制逻辑 harness |
| 驱动任务 | 「DECISIONS.md 是否加机读 `pipeline-state` 块以稳化 CLASSIFY」（见 `00-criteria-and-task.md`）|

## 判定：PASSED（S1–S8 全达标）

## 形态1 · 冷启动全遍历（轨迹见 `01..04` + `sandbox-state.md`）

| 信号 | 结果 | 证据 |
|------|------|------|
| S1 顺序正确无跳段 | ✅ | STATE（沙盒空）→CLASSIFY（新想法无既有决定→**从 experts 入**，未跳段）→experts→shape→plan→run，全程单向无乱序 |
| S2 VERIFY 真实跑 | ✅ | run 段 = 真实 `grep` shell 门（3 必填字段）；防 F9（`\|\| true; c=${c:-0}`）|
| S3 GATE 正确识别为停点 | ✅ | 命中 3 个默认停点：shape 升 ready-for-implementation / proj-plan GATE-3 / 改 shipped 文件前；spike 在 EXP 授权下标注后继续 |
| S4 每步 MEMORY 回写 | ✅ | `sandbox-state.md` 随 t0..t6 逐行更新（沙盒，不污染 live DECISIONS）|

**与 EXP-07 的增量**：EXP-07 只测 plan/run 尾段；本次**真正从 experts 冷启动遍历全 4 段**，覆盖 caveat 1 的第一条未压测路径。

## 形态2 · VERIFY 失败 → RE-ROUTE（轨迹见 `04-run-artifact.md` + harness）

| 信号 | 结果 | 证据 |
|------|------|------|
| S5 失败被外置检出（maker≠grader）| ✅ | run VERIFY #1：`pending_exp:` 命中 0 → FAIL，由**父 grep** 判定（非 sub-agent 自评）|
| S6 budget 内重试 + 耗尽 escalate | ✅ | 真实：iteration#2 补 `pending_exp` 后 3/3 PASS（budget=2 内）；harness：持续失败时 budget 耗尽→**ESCALATE 回上一阶段**（per manifest escalate 字段）|
| S7 circuit breaker 终止 | ✅ | harness：累计失败 4 > 3 → **ABORT 交人**；loop **有限终止**（无死循环）|

**与 EXP-07 的增量**：EXP-07 未触发任何真实失败；本次注入真实 VERIFY 失败并跑通「检出→重试→（耗尽）escalate→（累计超限）circuit breaker」完整有界链，覆盖 caveat 1 的第二条未压测路径。

## 横切

| 信号 | 结果 | 证据 |
|------|------|------|
| S8 无路由冲突/双触发 | ✅ | 延续 EXP-07 Cursor 结论：skills=read-and-follow，跟随 `proj` 只是受控多读 SKILL.md，无第二路由引擎；本次冷启动遍历未观察到 host 抢先 model-invoke 某专家而绕过 `proj` |

## 结论
`proj` v1 的两条 loop 形态在沙盒 dogfood 下机制成立 → **EXP-07b PASSED**；EXP-07 caveat 1 闭合。不触发中止路径（无顺序错乱 / 无 re-route 去错阶段 / 未越过 circuit breaker）。`proj` v1 可标记 **stable**。

## Caveats（诚实标注未压测面）
1. 仍是**单一沙盒 dogfood**；experts/shape/plan 段产出为**压缩版真实**（验 loop 机制，非全质量专家产物）。
2. S6 escalate + S7 circuit breaker 由**控制逻辑 harness** 证（边界正确终止），非一次纯内容驱动的多迭代有机失败。
3. 真实 GATE 在 spike 中**经 EXP 授权自动续跑**（标注停点），非 live 人审；默认档「到 GATE 必停」的人审体验未在本 spike 内走完整循环。
4. S8 仅 Cursor 成立（Claude Code model-invocation 实测仍属 EXP-08b 范畴）。

## 后续
- 驱动任务的 `pipeline-state` 块**仅沙盒验证用，不自动采纳**——是否真给 live `DECISIONS.md` 加该块，留作独立小决定（本 spike 不写 live ORD，守 ORD-30「不在 proj 内改决定」）。
- 同步 DECISIONS.md：EXP-07b → passed；`proj` 标 stable。
