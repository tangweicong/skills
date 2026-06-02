# 规划交接 · {项目名}（分支 A · 交 proj-plan）

| 字段 | 值 |
|------|-----|
| 触发 | GATE-S 判定 intent 可信重建 → 可 plan |
| 基线 | `docs/survey/{YYYY-MM-DD}-baseline.md` |
| 日期 | {YYYY-MM-DD} |

> 本文件是 **proj-survey → proj-plan 的衔接契约**（类比 proj-shape → proj-plan 的 DECISIONS）。
> proj-plan 的 **brownfield 入口**（见 proj-plan SKILL.md §Brownfield 接管入口 · ORD-26）读本文件：**已完成范围作为既成约束（WBS 标「已完成」三态，不再规划），未完成工作作为 WBS「待做/进行中」项**。

## 既成约束（已完成 · 不进 WBS 待做）

> 给 proj-plan：这些是既有事实/资产，WBS **不得**把它们当新工作。

| # | 已完成项 | 依赖关系 | 来源（基线 F#）|
|---|---------|---------|---------------|
| C1 | … | … | F… |

## 未完成工作（WBS 三态种子）

| # | 工作项 | 状态 | 优先级 | 来源 |
|---|--------|------|--------|------|
| W1 | … | 待做 / 进行中 | | issue#/基线 F# |

## 重建的成功标准 / 范围边界（供 charter）

- 成功标准（做成什么样）：…
- 显式非目标：…

## 已知风险 / 待验证（供 risk + EXP）

- 基线 [待验证] 项中影响规划的：…

## 交接确认

- [ ] 人确认本 handoff 可作为 proj-plan brownfield 入口
