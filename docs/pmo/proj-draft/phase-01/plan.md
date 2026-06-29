# phase-01 计划 — `proj` orchestrator skill 起草

| 字段 | 值 |
|------|-----|
| 模式 | T-lean（单 phase）|
| 状态 | 草案 → GATE-3（合并入 GATE-1+2+3）|
| 执行者 | **全部 AI 父 agent 直写**（无 sub-agent dispatch）|

> **无 `## Sub-agent dispatch manifest` 段**：按 proj-run §dispatch 决策树（ORD-20），SKILL.md 跨章节一致性写作是 sub-agent **反模式**（章节互相引用、validation 难一行判定整体一致性）→ 父 agent 直写。亦呼应 EXP-04 洞察（小项目 model-tier 不经济）。

## 任务表

| ID | 任务 | WBS | 执行者 | 依赖 | validation（一行可判）|
|----|------|-----|--------|------|----------------------|
| T-01 | 写 `skills/proj/SKILL.md`（frontmatter + 定位 + 专家表 + 有界 loop + slider + GATE 清单 + 反模式 + 触发词）| 1.1–1.6 | AI | — | `test -f skills/proj/SKILL.md` |
| T-02 | README 索引 5→6 + `proj` 详细节 | 2.1–2.2 | AI | T-01 | `grep -c "proj" README.md ≥ 1`（新增行）|
| T-03 | `proj-run/SKILL.md`「（规划中）」转正 | 3.1 | AI | T-01 | `grep -c "规划中" skills/proj-run/SKILL.md = 0` |
| T-04 | 跑 `validate_skills.py` | 4.1 | AI | T-01..03 | 退出码 0 + "6 skill(s) validated" |
| T-05 | 写 acceptance（含 EXP-07 caveat 自检）+ 回写 DECISIONS | 4.2–4.3 | AI | T-04 | acceptance 全 checkbox |

## 活动依赖

T-01 → (T-02, T-03 并行) → T-04 → T-05。串行为主。

## 验收门（behavioral · ORD-22 风格 · 防 F9 用 `|| true; c=${c:-0}`）

- structural：`skills/proj/SKILL.md` 存在；行数 ≤ 600。
- behavioral：SKILL.md 含 `ORD-29`/`ORD-30`/`ORD-31` 各 ≥1；含 `不重做`/`model-invocation` 语义（ORD-30 显式声明）；含「有界」+「autonomy slider」+「circuit breaker」。
- lint：`validate_skills.py` 退 0 且报 6 skill。
- EXP-07 caveat 自检：SKILL.md 的 loop 节明确含「冷启动 experts→shape→plan→run 全遍历」+「VERIFY 失败→RE-ROUTE 多迭代」两条落点。

## GATE-3（合并入 GATE-1+2+3）

- [ ] 用户确认 phase-01 计划 → 解锁执行（执行 = 非本 skill · INV-04）
