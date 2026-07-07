# 16-显化「有界多样性 + 人供给必要多样性」于 proj（纯文档）

| 字段 | 值 |
|------|-----|
| 轮次 | 16 |
| 主题 | backlog #3（收敛 2 · Ashby）：在 `proj/SKILL.md` 把「自动臂有界多样性 by design + 人在 GATE/分岔供给必要多样性」从散落的 circuit-breaker/GATE 脚注**升为一条系统级显式设计立场**（纯文档，不改任何机制）|
| 日期 | 2026-06-30 |
| 状态 | **已实现**（用户 GATE = accept diff + 升 ORD-34）→ VERIFY 全过；**round 13 三收敛 backlog 至此收尾** |
| 讨论方法 | `proj-experts`（承接 round 13 收敛 2 · Ashby/Thom/Bertalanffy 三镜，收敛型轻量轮）|
| 写入格式 | 轻量 |
| 承接 | `13-…md` §收敛 2 + §视角 A「关切→路径」+ §同步注记 backlog #3；`proj/SKILL.md`（shipped · ORD-29/30/31）；round 14（ORD-32）+ round 15（ORD-33）已落实，#3 为 backlog 收尾项 |

## 用户输入（本轮）

> 继续 #3

→ 推进序最后一项 = backlog #3（收敛 2，纯文档显化，最低风险）。本轮 = 出 proposed diff → GATE → 实现。

## 事实与假设

### 已查证事实（读现状）

- **F1 · 立场目前是隐式的**：`proj/SKILL.md` 已含构成「有界多样性」的三个机制，但**各自为政、未被统一命名**：
  - circuit breaker（§autonomy slider 节）：「累计 VERIFY 失败 > 3 / 推翻 INV·ORD / 双重触发 → abort + 交人」= 把多种失败**塌缩成单一响应**。
  - GATE 清单：在 shipped 改动 / ready-for-implementation / GATE-0~3 / EXP 中止处**停交人** = 在不连续点放人。
  - autonomy slider：默认 bounded（到 GATE 必停）/ 高自主（显式授权）= 可调增益。
  - §设计 vision：人 = Sponsor + 关键决策（go-no-go / trade-off / abort-retry）。
  来源：`skills/proj/SKILL.md` 行 88–104 + 45–53。
- **F2 · Ashby 必要多样性定律**（round 13 已 grounded）：「only variety can absorb variety」；调节器能吸收的扰动多样性 ≤ 其自身动作多样性。是信息律。来源：[Ashby's Law](https://grahamberrisford.com/Bookvol2/1%20Ashbys%20law.htm)（round 13 F2）。
- **F3 · 收敛 2 的「关切→路径」原文**：自动 loop 按设计有界多样性、circuit breaker 塌缩失败、人是部署在突变点的高多样性调节器；「**但目前只隐含在多条局部规则里，未被升为系统级立场**」；路径 = 「在 `proj` 显式命名」。来源：`13-…md` §视角 A 关切→路径 + §收敛 2。

### 推理（承接 round 13）

- **推理 · 模拟推理 · Ashby/Thom/Bertalanffy（收敛 2）**：把三个散落机制统一表述为一条「有界多样性 by design + 人供给必要多样性」立场，提升可理解性（读者不会误以为 loop 能自洽兜住一切），且与既有 Supervised-AI（ORD-31）零冲突。依据 `13-…md` §收敛 2。
- **推理 · 边界（防过度）**：依据用户 rule #2/#3 + round 13 §讨论 3 表（本项标「值得·低成本·纯文档显化不改机制」）——**只加文字，不新增/改动任何 loop/GATE/circuit-breaker 机制**。

### 待验证 / 未查证

- 无新 EXP。本项为纯文档，VERIFY = (a) `validate_skills.py` 仍退 0（含 C1–C4）；(b) 同步根 README（proj 节若需）；(c) 不改任何机制描述（diff 仅新增立场段 + 立场表一行）。

## 方法专属输出（proj-experts）

收敛轮（轻量）：多视角分析已在 round 13 §视角 A/E/F 完成；此处仅落地显化，省略独立多视角节。

## 讨论 · proposed diff（交人 GATE）

### 改动点 1：`proj/SKILL.md` 新增一小节（置于 §autonomy slider + circuit breaker 之后、§GATE 清单 之前）

```markdown
## 设计立场：有界多样性 + 人在分岔供给必要多样性（Ashby）

按 Ashby 必要多样性定律「only variety can absorb variety」，调节器能吸收的扰动多样性受其**自身动作多样性上限**约束。本 skill 的自动臂**按设计是有界多样性**——circuit breaker 把多种失败模式**塌缩**成单一响应（abort + 交人）、GATE 在不连续点（分岔）**停**、iteration budget 限制重试；它**不**试图自动吸收项目情境的全部扰动。

**必要多样性由人在 GATE / 分岔 / abort-retry 处供给**：人是恰好部署在突变点的高多样性调节器（即 §设计 vision 的 Sponsor + 关键决策）。

> 即：自动 loop 的「有界」**不是能力缺陷而是显式设计选择**——把高多样性决策留给人，与 Supervised-AI 立场（ORD-31）一致。circuit breaker / GATE / autonomy slider 是这条立场的三个落点，而非彼此孤立的规则。
```

### 改动点 2：§立场声明（借鉴/自创）表新增一行

```markdown
| **Ashby** Law of Requisite Variety | 自动臂有界多样性 by design；人在 GATE/分岔供给必要多样性 | [Ashby's Law](https://grahamberrisford.com/Bookvol2/1%20Ashbys%20law.htm) |
```

### 不改什么（守边界）

- circuit breaker 阈值、GATE 清单、autonomy 档位、loop 步骤——**一字不动**（纯显化，非改机制）。
- 不升 INV（与 round 13 §讨论 3「系统级不变量·谨慎」一致，不借机加 system-INV）。
- 收敛 2 之外的候选 4/5（设计期/使用期序参量、survey→plan 回退边）本轮**不纳入**（低优先 · 用户 backlog 未选）。

## 可验证尝试与继续/中止

无新 EXP。VERIFY 内联：改后 `uv run scripts/validate_skills.py` 须仍退 0（6 skill + C1–C4）；README 若涉 proj 节同步则一并；diff 仅新增（无删改既有机制行）。

## 本轮决定

### 已确定 — 普通决定（新增/修订）

- **ORD-34（新增）**：`proj/SKILL.md` 显化「有界多样性 + 人供给必要多样性」立场（纯文档 · 改动点 1+2）。在 circuit breaker 后新增 §设计立场小节（Ashby「only variety can absorb variety」→ 自动臂有界多样性 by design / 人在 GATE·分岔·abort-retry 供给必要多样性 / 是 ORD-31 落地表述）+ 立场表 Ashby 行；README proj 节同步一行。**不改任何 loop/GATE/circuit-breaker 机制、不升 INV、不纳入候选 4/5**。落实 round 13 收敛 2（Ashby/Thom/Bertalanffy 三镜）。
  **来源**：`13-…md` §收敛 2 + §视角 A 关切→路径；ORD-31（本项为其显化）；Ashby 必要多样性（F2）；用户 @本轮 GATE（accept diff + 升 ORD-34）
  → 已落地 `proj/SKILL.md` + README + 同步 DECISIONS `ORD-34` + 变更日志。

## VERIFY（实现后已执行）

- `uv run scripts/validate_skills.py` → `ok: 6 skill(s) validated + cross-artifact (C1–C4)` 退 0（C4 已校验本轮 ORD-34 同步行 ∈ DECISIONS）。
- diff 仅新增（§设计立场小节 + 立场表 1 行 + README 1 行）；circuit breaker 阈值 / GATE 清单 / autonomy 档位 / loop 步骤逐行核对**未改**。

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-34 | 新增 | ✓ |

讨论状态同步：维持 `deciding`（backlog #3 = ORD-34 已落实；round 13 三收敛 backlog 全收尾；6 skill 仍 shipped/stable）。

同步完成时间：2026-06-30

## 开放问题（本轮 GATE · 已回答）

1. proposed diff → 用户 **accept 原 diff**。
2. 是否升 ORD → 用户选 **升 ORD-34**（与 #1/#2 同样可追溯性）。

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-06-30 | draft：backlog #3 收尾项；proposed diff（proj 新增「有界多样性+人供给必要多样性·Ashby」小节 + 立场表一行）；守边界=纯文档不改机制、不升 INV、不纳入候选 4/5；候选 ORD-34 待 GATE |
| 1.1 | 2026-06-30 | 用户 GATE = accept diff + 升 ORD-34；落地 `proj/SKILL.md`（§设计立场 + 立场表 Ashby 行）+ README proj 节；VERIFY 全过（6 skill + C1–C4 退 0）；round 13 三收敛 backlog 收尾 |
