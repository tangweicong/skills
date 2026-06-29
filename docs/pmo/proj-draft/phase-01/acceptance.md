# phase-01 验收 — `proj` orchestrator skill 起草

| 字段 | 值 |
|------|-----|
| 状态 | **通过**（2026-06-29 执行完成）|

## 验收清单

### structural
- [x] `skills/proj/SKILL.md` 存在
- [x] 行数 142 ≤ 600

### lint
- [x] `uv run scripts/validate_skills.py` 退 0
- [x] 报告 "6 skill(s) validated"

### behavioral（决定可见性 · grep 计数见 phase-01 执行日志）
- [x] 含 `ORD-29`(4)/`ORD-30`(5)/`ORD-31`(6) 各 ≥1
- [x] ORD-30 显式声明「不重做 host model-invocation」（`不重做`=4 · `model-invocation`=4）
- [x] 含「有界」(10) +「autonomy slider」(5) +「circuit breaker」(3)

### EXP-07 caveat 设计层自检
- [x] loop 节含「冷启动全遍历」落点
- [x] loop 节含「VERIFY 失败 → RE-ROUTE 多迭代」落点
- [x] caveat 真实压测去向已注明（见下处置记录 → 后续 EXP-07b）

### 集成
- [x] README 索引 6 skill（`6 skill`=2 · `./skills/proj/` 链接=2）+ `proj` 详细节
- [x] `proj-run/SKILL.md`「规划中」标记已转正（`规划中`=0）
- [x] DECISIONS：ORD-29/30/31 标记落实 + 状态更新（见 DECISIONS 变更日志 2026-06-29）

## EXP-07 caveat 处置记录

- 两条 caveat（冷启动 experts→shape→plan→run 全遍历 / VERIFY 失败→RE-ROUTE 多迭代）目前**仅设计层覆盖**——已写入 `skills/proj/SKILL.md` §有界 loop 的「两条必须支持的 loop 形态」，**尚未真实端到端压测**。
- **去向**：登记为后续 **EXP-07b**（在一个真实多阶段任务上让 `proj` 全程驱动冷启动 + 注入一次 VERIFY 失败观察 re-route），由用户择机启动；不阻塞 `proj` v1 发布。

## 收尾自检（T-lean · 替代 review.md）

- [x] circuit breaker 未触发
- [x] lessons learned：
  1. 对「范围已被 ORD + 验证过 spike 锁定」的小 skill，T-lean + GATE 合并显著降仪式，JIT 判断正确。
  2. spike→shipped 几乎零返工（EXP-07 spike 结构直接升级），印证「先 spike 验证再起草」的价值。
  3. 验证门 grep 统一用 `|| true; c=${c:-0}` 防 F9，全程未再触发 F9。
- [x] 无新 INV/ORD 被本 phase 私自创建（ORD-29/30/31 均为轮次 12 既有决定的落实）。
