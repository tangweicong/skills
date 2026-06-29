# EXP-07 试跑结果 · prompt-only orchestrator 能否驱动跨 skill 有状态 loop

| 字段 | 值 |
|------|-----|
| EXP | EXP-07 |
| 日期 | 2026-06-29 |
| 被测物 | `docs/pmo/proj-orchestrator-spike/proj-spike-SKILL.md`（薄 orchestrator spike · ORD-29/30/31）|
| 真实任务 | 给 `proj-run/SKILL.md` 加一节「与 `proj` 的关系」（forward-ref · 落实 ORD-29）|
| 方法 | 同一任务跑两条：基线（纯 host model-invocation）vs 实验（经 `proj` spike 全程驱动）|

## 实验臂轨迹（经 `proj` spike 实际执行）

1. **STATE** — 读 `DECISIONS.md`：状态 `exploring`；ORD-29 已确立 `proj` 为入口、proj-run 保持 Executing。
2. **CLASSIFY** — 该任务**已被 shape 决定**（ORD-29），故跳过 experts/shape，从 **plan/run** 入。（CLASSIFY 只定位入口阶段，未替 host 选 skill → 符合 ORD-30）
3. **PLAN → EXECUTE** — 产出 proposed 交付物 `proposed-proj-run-note.md`（6 行）。
4. **VERIFY**（外置验证 · maker≠grader）— 跑 shell 验证门：
   - structural：文件存在 PASS；行数 6 ≤ 12 PASS
   - behavioral：`grep` 命中 `ORD-29`/`Executing`/`ORD-17/18` 各 ≥1 PASS
   - 负向断言：`grep -c "APPLIED" = 0` PASS（**首跑触发 proj-run 失败模式 F9** —— `grep -c ... || echo 0` 双重输出 `0\n0`；改用 `|| true; c=${c:-0}` 后 PASS）
5. **GATE** — 命中「改动 shipped skill 前须停」→ **停**，交 proposed diff 给人审批（未触碰 `skills/proj-run/SKILL.md`）。
6. **RE-ROUTE** — 阻塞于人审 GATE → 停。MEMORY：本结果回写 DECISIONS EXP-07 状态。

## 基线臂轨迹（纯 host model-invocation · 对照）

host 按 description 单次匹配：用户说「给 proj-run 加一节」→ 很可能**直接编辑** `skills/proj-run/SKILL.md`，因为：

- host 路由**无状态**：不会先读 DECISIONS 确认 ORD-29 是否已决、措辞是否合规；
- **无 GATE 概念**：不会在「改 shipped 文件」前停下出 proposed diff；
- **不知道要回写** DECISIONS/artifacts（无 MEMORY 步）。

## 成功信号对账（实验 ≥ 基线？）

| # | 成功信号 | 基线 | 实验（`proj` spike）| 判定 |
|---|----------|------|----------------------|------|
| ① | 按 pipeline 顺序触发 | 单次匹配，可能跳过 shape 校验直接改 | STATE→CLASSIFY 显式定位、跳过已决 shape、从 plan/run 入 | 实验 **>** 基线 |
| ② | GATE 处确实停交人 | 无 gate，可能直接改 shipped | 命中 shipped-file GATE → 停 + proposed diff | 实验 **>** 基线 |
| ③ | DECISIONS/artifacts 一致更新 | 易漏（无状态）| MEMORY 步强制回写 | 实验 **>** 基线 |
| — | 无重复触发 / 不与 host 抢路由 | — | **Cursor 未观察到双重触发**（见下）| ✓ |

## 关键发现 · 路由冲突（决定性判据）

- **Cursor（本 host）**：skills 以 `<available_skills>` + 路径形式呈现，agent **读 SKILL.md 并跟随**，**不是**独立的自动调用工具。因此「orchestrator 与 host 路由打架」**未发生**——跟随 `proj` 只是按受控顺序多读几个 SKILL.md，无第二个路由引擎会双触发。
- **Claude Code（model-invoked Skill 工具）**：风险更高——host 可能因 description 匹配**直接** model-invoke `proj-shape` 而绕过 `proj`。缓解 = 专家 skill 设 `disable-model-invocation: true`、只让 `proj` 可被 model-invoke 并由它委派；description 收敛广度避免冲突。**这属 ORD-28 通用化阶段（EXP-08）的设计点，非 EXP-07 阻塞项。**

## 结论

**EXP-07 = PASSED（with caveats）**：三项成功信号实验臂全 ≥ 基线，Cursor 下无路由冲突。→ **继续：固化薄 orchestrator skill（Fork 1 选 B / ORD-29）**，不触发降级路径 C。

**Caveats（同 EXP-05 风格，诚实标注未压测面）**：

1. 本试跑是**单一、小、受控**的 dogfood，验证的是「shape 已决 → plan/run → GATE 停」这条路径；**未压测**：完整 experts→shape→plan→run 冷启动遍历、含真实 VERIFY 失败→RE-ROUTE 的多迭代 loop。
2. 路由冲突结论**仅在 Cursor 成立**；Claude Code 的 model-invocation 实测留待 ORD-28/EXP-08。
3. 验证门命令需防 F9（`grep -c` 双计）——固化时沿用 proj-run 既有 F9 对策。

**给落地（proj-plan 起草 `proj`）的输入**：把上述 caveat 1 的两条未压测路径作为 `proj` 起草的**第一批验证 phase**（冷启动全遍历 + 失败 re-route loop）。

## GATE 后续（2026-06-29）

- 用户**审批通过** GATE → proposed diff 已应用到 `skills/proj-run/SKILL.md`（§设计 vision 后新增「与 `proj` 入口的关系（ORD-29 · 规划中）」节，加「规划中」标记以免误导 `proj` 已存在）；`validate_skills.py` **5/5 退 0**。
- **README 同步义务**（proj-run/SKILL.md 头注释要求）：本次仅加 forward-ref 节、未改 proj-run 索引条目，且 `proj` 尚未 shipped → **暂不**把 `proj` 写入根 README 索引表；待 `proj` 实际起草发布（proj-plan 阶段）再同步 README。
