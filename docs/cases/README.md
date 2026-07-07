# 案例库（proj-* 跨项目学习闭环 · ORD-36）

集中存放**用 proj-* 流水线实现的项目的复盘案例**（PMBOK Lessons Learned Register / case base）。是 proj-* 的**慢/外层双环学习反馈机制**：单个项目的经验 → 沉淀为案例 → 被未来项目消费 → 必要时回头修订 `INV/ORD/skill`（治理变量）。

## 这不是什么

- **不是** write-only 日志。文献头号失败模式 = 案例写完没人看（NASA LLIS / KM 项目废弃根因「缺知识蒸馏机制」）。**消费比存储重要**——案例 §消费记录 为空 = 尚未闭环。
- **不是**新 skill。捕获 + 消费由 **proj-plan 既有职责扩展**承载（阶段 Close 捕获 / Round A 启动消费 · ORD-36），不新增 skill。
- **不是**领域内容库。存的是「**用 proj-* 的过程经验**」（哪条决策有效、哪里卡、该不该改流程），不是某项目的业务数据。

## 怎么产生一个案例（捕获）

项目收尾（proj-plan 末阶段 `review.md` 经验教训）时：**AI 从该项目自身的 `DECISIONS.md` + `change-log.md` + `review.md` 派生案例草稿**（用 [case-template](../../skills/proj-plan/assets/case-template.md)）→ **人审定稿** → 落到本目录 `NN-{项目}.md`。外部项目（如另一 repo 的小说项目）同理：AI 据其 artifact 起草，人审后放这里。

## 怎么用一个案例（消费 · 闭环）

新项目 **proj-plan Round A（Initiate / charter）** 或 **proj-experts/proj-shape 启动研判**时：查阅本库**相似类型**的案例，把可复用建议带入 charter / 风险 / ORD。消费后**回填被消费案例的 §消费记录**——这是闭环的证据。

## 双环要求（防假学习）

每个案例**必填 §治理变量检视**：至少指出本案例促使重新检视的一条 `INV/ORD/skill`（该不该改 / candidate）。只改 checklist 不动治理变量 = 单环假学习（Argyris）。

## 索引

| 案例 | 项目 | 类型 | 日期 | 一句话 | 检视的治理变量 | 已被消费 |
|------|------|------|------|--------|----------------|----------|
| _（暂无；第 1 个案例 = 小说项目 · EXP-10 dogfood）_ | | | | | | |

> 状态：EXP-10（案例库闭环 dogfood）`pending` — 待第 1 个案例（小说项目复盘）写入 + 被第 2 个项目消费以验证闭环。详见 `docs/discuss/DECISIONS.md` EXP-10 / `19-案例库-跨项目学习闭环.md`。
