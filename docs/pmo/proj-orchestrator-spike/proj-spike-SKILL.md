---
name: proj
description: >-
  SPIKE (EXP-07, not installed). Single user-facing entry / facade for the proj-*
  pipeline. Thin Supervisor + bounded plan-execute-verify loop over the fixed
  specialist skills (proj-experts / proj-shape / proj-plan / proj-survey / proj-run).
  Routes by pipeline stage + DECISIONS state, stops at GATEs for human approval
  (autonomy slider default = bounded). Does NOT re-implement host skill selection.
---

# proj （orchestrator spike · EXP-07）

> 本文件是 **EXP-07 的被测物**，放在 `docs/pmo/proj-orchestrator-spike/`，**未安装**。
> 目的：验证「一个 prompt-only 的薄 orchestrator 能否可靠驱动跨 skill 的有状态 loop，且不与 host 原生 model-invocation 抢路由」。
> 落实 ORD-29（薄入口 skill）/ ORD-30（职责收窄）/ ORD-31（有界 loop + autonomy slider）。

## 这个 skill 是什么 / 不是什么

- **是**：流水线之上的 Supervisor + 状态机 + 有界 loop + facade。持有「现在到哪一阶段、该停哪个 GATE、下一步跑哪个专家」的**跨 skill 状态**。
- **不是**：一个「决定调用哪个 skill」的路由器。host 的 model-invocation 已按 description 做单次路由（ORD-30）；本 skill **不重做**这件事，只负责 host 给不了的**有状态序列 + gate + loop**。

## 固定专家集（Supervisor 调用对象）

| 阶段 | 专家 skill | 产出 |
|------|-----------|------|
| 商业论证 | `proj-experts` | 专家视角（无状态，按需）|
| 决议收敛 | `proj-shape` | `docs/discuss/` + DECISIONS.md |
| 规划 | `proj-plan` | `docs/pmo/phase-NN/plan.md`（含 dispatch manifest）|
| 执行 | `proj-run` | `acceptance.md` + 产出登记 |
| 接管 | `proj-survey` | 现状基线（brownfield 入口）|

## 有界 loop（核心 · ORD-31）

```text
trigger（用户请求）
  └─ STATE：读 DECISIONS.md → 当前讨论状态 + 已有决定 + 待验证 EXP
  └─ CLASSIFY：判断入口阶段（新想法→experts/shape；已有决议→plan；brownfield→survey）
       ※ 不重做 host 路由：CLASSIFY 只定位「pipeline 入口阶段」，不替 host 选 skill
  └─ LOOP（有界）：
       1. PLAN    → 跟随该阶段专家 skill 的 SKILL.md
       2. EXECUTE → 该专家产出 artifact
       3. VERIFY  → 跑该阶段的验证（proj-run validation gate ORD-22 / validate_skills.py / DECISIONS 同步检查）
       4. GATE?   → 命中 GATE 或触及 shipped 文件/不可逆改动 → **STOP，交人审批**（autonomy slider 默认档）
       5. RE-ROUTE→ 据 VERIFY 结果 + STATE 决定下一阶段，或回到 1；循环上限见 budget
  └─ MEMORY：每步把决定/产出回写 DECISIONS.md + docs/pmo artifacts（source of truth）
```

**autonomy slider（ORD-31）**：默认 = phase 内自迭代、GATE 停交人；高自主档 = 用户显式授权某段无人值守（circuit breaker 仍兜底）。

**circuit breaker**：累计验证失败 > 3 / 专家产出推翻 INV/ORD / host 与本 loop 出现双重触发 → abort + 交人。

## GATE 清单（默认停点）

- 改动 **shipped skill / 不可逆文件** 前 → 停，出 proposed diff 交人。
- proj-shape `ready-for-implementation` 升级 → 停（须用户显式确认）。
- proj-plan 各 GATE-0/1/2/3 → 停。
- EXP 的「中止」条件命中 → 停 + 走降级路径 B。

## 反模式

- 把本 skill 写成「按关键词选 skill」→ 重复 host model-invocation（违反 ORD-30）。
- loop 跨 GATE 连续自动跑而不停 → 违反 ORD-31 默认档 + Supervised-AI INV。
- 验证让产出方自评 → 违反 maker≠grader（验证须外置：父跑命令 / 二号视角）。
