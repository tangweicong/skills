# 阶段计划 — phase-01 · proj-run 完整版起草 + EXP-04 试跑

| 字段 | 值 |
|------|-----|
| WBS | 1.0 + 2.0 + 3.3 + 4.0 + 5.0 |
| roadmap | phase-01（单 phase 设计）|
| 状态 | 已开 GATE-3 待用户确认 |
| GATE-3 | 进阶段前用户确认本 plan + acceptance.md |

## 目标

完成 `skills/proj-run/SKILL.md` 完整版（覆盖 v0 骨架，落实 ORD-18~22）+ `skills/proj-run/assets/` 5 个 templates；同步采集 EXP-04 v1.4 试跑数据（token cost + GATE 通过率 + analyze + validate）；passed 时触发后续 ORD-15 升级动作（不在本阶段执行）。

## 任务

| # | 任务 | 执行者 | 前置 | 人工预估 | 关联 | 状态 |
|---|------|--------|------|----------|------|------|
| T-01 | 起草 `skills/proj-run/assets/dispatch-manifest-template.md`（ORD-21 5 字段闭环模板 + 完整示例）| subagent:coder（composer-2.5-fast）| — | — | WBS 2.1 / ORD-21 | ☐ |
| T-02 | 起草 `skills/proj-run/assets/acceptance-template.md`（validation 结果 + token cost + escalate 标记）| subagent:coder | — | — | WBS 2.2 / ORD-15 输出契约 | ☐ |
| T-03 | 起草 `skills/proj-run/assets/cursor-agents-template.md`（Mode α YAML frontmatter + legacy warning）| subagent:coder | — | — | WBS 2.3 / ORD-19 Mode α | ☐ |
| T-04 | 起草 `skills/proj-run/assets/message-bus-template.md`（Mode β 占位 · `.apm/bus/` 目录结构 + 触发条件 + 不含 runtime 明示）| subagent:coder | — | — | WBS 2.4 / ORD-19 Mode β | ☐ |
| T-05 | 起草 `skills/proj-run/assets/validation-gate-template.md`（3 类 gate + 失败 escalate 标准流程）| subagent:coder | — | — | WBS 2.5 / ORD-22 | ☐ |
| T-06 | **Opus 直写** `skills/proj-run/SKILL.md` 完整版（覆盖 v0 骨架，引用 T-01~T-05 templates）| AI（Opus 父）| T-01~T-05 全 validation 通过 | — | WBS 1.0 全 L2（1.1~1.7）| ☐ |
| T-07 | analyze checklist 对 proj-run/SKILL.md + 5 templates + PM artifacts 跑 | subagent:auditor（composer-2.5-fast, readonly）| T-06 | — | WBS 4.x / analyze | ☐ |
| T-08 | **Opus 直写** 跑 validate_skills.py + 同步 DECISIONS.md（EXP-04 状态 + token 数据回写）+ 更新 skills/README.md proj-run 行 + 写 phase-01/review.md | AI（Opus 父）| T-07 通过 | — | WBS 4.3 + 5.0 | ☐ |

**执行者**：`AI`（当前 Opus 父）· `subagent:coder` / `subagent:auditor`（composer-2.5-fast）· 见 proj-plan/assets/agent-handoff.md

## Handoff（sub-agent 任务）

> 完整 5 字段闭环 dispatch 信息见下方 `## Sub-agent dispatch manifest`（ORD-21 5 字段闭环）；本节仅做摘要。

| 任务 # | 角色 | 输入 | 完成定义 | 结果回写 |
|--------|------|------|----------|----------|
| T-01 | subagent:coder | dispatch prompt（自含，见 manifest）+ proj-plan/assets/plan-template.md（参照风格）| `skills/proj-run/assets/dispatch-manifest-template.md` 文件存在且通过 5 项 validation | acceptance.md §Sub-agent dispatch log + artifact-index.md 登记 |
| T-02 | subagent:coder | 同上 + proj-plan/assets/acceptance-template.md（参照）+ proj-run/SKILL.md v0（接口契约段）| `skills/proj-run/assets/acceptance-template.md` 文件存在 + 通过 4 项 validation | 同上 |
| T-03 | subagent:coder | 同上 + Cursor Forum 156736 URL（legacy warning 出处）+ Cursor sub-agents 指南 URL（YAML 结构）| `skills/proj-run/assets/cursor-agents-template.md` 文件存在 + 通过 4 项 validation | 同上 |
| T-04 | subagent:coder | 同上 + APM 仓库 URL（参照 `.apm/bus/` 结构）| `skills/proj-run/assets/message-bus-template.md` 文件存在 + 通过 3 项 validation | 同上 |
| T-05 | subagent:coder | 同上 + analyze-checklist.md 结构（参照）| `skills/proj-run/assets/validation-gate-template.md` 文件存在 + 通过 4 项 validation | 同上 |
| T-07 | subagent:auditor（readonly）| proj-run/SKILL.md + 5 templates + PM artifacts | analyze checklist 7 硬规则结果表 | acceptance.md §Analyze 段 |

## 交付物

1. `skills/proj-run/SKILL.md` 完整版（覆盖 v0；≤600 行）
2. `skills/proj-run/assets/dispatch-manifest-template.md`
3. `skills/proj-run/assets/acceptance-template.md`
4. `skills/proj-run/assets/cursor-agents-template.md`
5. `skills/proj-run/assets/message-bus-template.md`
6. `skills/proj-run/assets/validation-gate-template.md`
7. `skills/README.md` proj-run 行更新
8. `docs/pmo/proj-run-draft/phase-01/acceptance.md` 完整 + 回写
9. `docs/pmo/proj-run-draft/phase-01/review.md`
10. `docs/discuss/DECISIONS.md` EXP-04 状态回写

## 活动依赖（本阶段内，PMP 排列活动顺序 · 最小）

```text
T-01 ─┬─→ T-06 ─→ T-07 ─→ T-08
T-02 ─┤
T-03 ─┤ （T-01~T-05 可并行 dispatch，但本试跑顺序串行以便 Opus 逐个评审 + 记录 token）
T-04 ─┤
T-05 ─┘
```

**串行执行理由**：本试跑核心是测 model-tier 经济性，并行 dispatch 会增加 Opus 父评审时的 context 切换成本，影响 token 估算准确性。串行 dispatch + 逐个评审，便于精确归因每个 task 的 input/output token。

---

## Sub-agent dispatch manifest（ORD-15 + ORD-21 5 字段闭环 · 强制示范）

> **本段是 ORD-21 5 字段闭环的强制示范**。proj-plan 当前 plan-template.md 中 manifest 段为 v0 可选；本项目作为 EXP-04 试跑，**主动采用强制 5 字段格式**；EXP-04 passed 后此格式将固化进 proj-plan/assets/plan-template.md（属后续动作，不在本阶段执行）。
>
> **不指定具体 model**——按 ORD-15 承诺字段精神，本 manifest 仅说明 specialist 类型；具体 model 由 proj-run 决定（本试跑选 `composer-2.5-fast`，理由：legacy plan 限制 + 试跑路径 B2=Hybrid 已确认）。

### Manifest schema 字段说明

| 字段 | 含义 | 强制 |
|------|------|------|
| objective | task ID + 一句话目标 | ✓ |
| specialist | sub-agent 角色（coder / reviewer / auditor / explorer）| ✓ |
| validation criteria | **可由父 agent 一行 shell/grep 命令判定的**判据列表 | ✓ |
| iteration budget | 失败重试次数上限 | ✓ |
| escalate 规则 | 超出 budget 时的回退路径（回 Opus 父 / 回 proj-plan / 回 proj-shape） | ✓ |

### Dispatch 详表（6 个 sub-agent task · T-01~T-05 + T-07）

---

#### T-01 · dispatch-manifest-template.md

| 字段 | 值 |
|------|-----|
| **objective** | 起草 `skills/proj-run/assets/dispatch-manifest-template.md`：含 ORD-21 5 字段闭环 schema 表 + 字段说明 + 完整 dispatch 示例（≥2 个示例 task） + manifest 段使用规则 |
| **specialist** | `subagent:coder` |
| **validation criteria** | (1) `test -f skills/proj-run/assets/dispatch-manifest-template.md` 退 0；(2) `rg -c "model:" skills/proj-run/assets/dispatch-manifest-template.md` 退 1 命中（仅说明性单元素，禁止指定具体 model 名）；(3) `wc -l skills/proj-run/assets/dispatch-manifest-template.md` ≤ 200 行；(4) `rg -c "objective\|specialist\|validation criteria\|iteration budget\|escalate" skills/proj-run/assets/dispatch-manifest-template.md` ≥ 5 命中（5 字段齐）；(5) markdown 表格结构对齐 proj-plan/assets/plan-template.md（父 agent 人工对齐评审）|
| **iteration budget** | 2 |
| **escalate 规则** | 失败 2 次 → escalate 给 Opus 父：(a) 第一次失败 → 给 sub-agent 失败原因 + 修订要点 + 重试；(b) 第二次失败 → Opus 父直接接手改写为目标版本，不再 retry；(c) 如修订后仍发现 schema 需变更 → 标 R-06 "需要新决定"，回 proj-shape 09 轮（abort 本试跑）|

---

#### T-02 · acceptance-template.md

| 字段 | 值 |
|------|-----|
| **objective** | 起草 `skills/proj-run/assets/acceptance-template.md`：包含 validation 结果段（structural / lint / behavioral 3 类对应 ORD-22）+ token cost 段（input/output token 估算表）+ escalate 标记段 + GATE 联动说明段 |
| **specialist** | `subagent:coder` |
| **validation criteria** | (1) `test -f` 退 0；(2) `rg -c "validation\|token cost\|escalate\|GATE" skills/proj-run/assets/acceptance-template.md` ≥ 4 命中（4 段齐）；(3) `wc -l` ≤ 100 行；(4) 含 structural/lint/behavioral 3 类 validation 子段（rg -c "structural\|lint\|behavioral" ≥ 3）|
| **iteration budget** | 2 |
| **escalate 规则** | 同 T-01 |

---

#### T-03 · cursor-agents-template.md

| 字段 | 值 |
|------|-----|
| **objective** | 起草 `skills/proj-run/assets/cursor-agents-template.md`：YAML frontmatter 模板（含 description / tools / model / is_background / readonly 字段示例）+ Cursor sub-agents 用法说明 + **legacy plan model 字段失效 warning**（出处 Cursor Forum #156736）+ 一个完整 example agent 文件示范 |
| **specialist** | `subagent:coder` |
| **validation criteria** | (1) `test -f` 退 0；(2) `rg -c "description:\|tools:\|model:\|is_background:\|readonly:"` ≥ 5 命中（5 字段示范）；(3) `wc -l` ≤ 120 行；(4) `rg -c "legacy\|Cursor Forum\|156736"` ≥ 1（warning 段必含出处）|
| **iteration budget** | 2 |
| **escalate 规则** | 同 T-01 |

---

#### T-04 · message-bus-template.md

| 字段 | 值 |
|------|-----|
| **objective** | 起草 `skills/proj-run/assets/message-bus-template.md`：Mode β 占位模板，含 `.apm/bus/` 目录结构示例 + 触发条件说明（跨 IDE session / 单 sub-agent 输出 > 父 context）+ **明示"不实现 runtime，仅提供 template"**（避免过早抽象） + APM 框架出处引用 |
| **specialist** | `subagent:coder` |
| **validation criteria** | (1) `test -f` 退 0；(2) `rg -c "\.apm/bus/\|message-bus\|APM"` ≥ 3 命中；(3) `wc -l` ≤ 80 行；(4) `rg -c "不实现\|不包含 runtime\|no runtime\|占位\|placeholder"` ≥ 1（明示非实现）|
| **iteration budget** | 2 |
| **escalate 规则** | 同 T-01 |

---

#### T-05 · validation-gate-template.md

| 字段 | 值 |
|------|-----|
| **objective** | 起草 `skills/proj-run/assets/validation-gate-template.md`：ORD-22 三类 gate（structural / lint / behavioral）的标准段 + 每类示例命令 + 失败 escalate 标准流程 + 与 dispatch manifest iteration budget 联动 |
| **specialist** | `subagent:coder` |
| **validation criteria** | (1) `test -f` 退 0；(2) `rg -c "structural\|lint\|behavioral"` ≥ 3 命中（3 类齐）；(3) `wc -l` ≤ 120 行；(4) `rg -c "escalate\|iteration\|budget"` ≥ 3 命中 |
| **iteration budget** | 2 |
| **escalate 规则** | 同 T-01 |

---

#### T-07 · analyze checklist auditor

| 字段 | 值 |
|------|-----|
| **objective** | 对 `skills/proj-run/SKILL.md` + `skills/proj-run/assets/` 5 templates + `docs/pmo/proj-run-draft/` PM artifacts 跑 proj-plan/assets/analyze-checklist.md 全 7 硬规则；输出结果表（pass/fail + 证据 1 行）；建议软规则项 |
| **specialist** | `subagent:auditor`（readonly · composer-2.5-fast）|
| **validation criteria** | (1) 返回结果表含 7 硬规则全部行；(2) 每条 fail 必须给出证据 1 行（如哪个文件/哪个表格违规）；(3) 给出 ≥3 条软规则项建议；(4) 不修改任何文件（readonly 强制） |
| **iteration budget** | 1（auditor 不应需要 iterate；如失败说明规则定义有歧义 → Opus 父接手解释）|
| **escalate 规则** | 失败 1 次 → Opus 父直接跑 checklist 替代（不再 retry sub-agent）|

---

### Dispatch 决策树（ORD-20）

> 本表说明为什么 T-01~T-05 + T-07 适合 sub-agent，T-06 + T-08 不适合。

| Task | "输出是否需要被父 agent 持续回溯" | "是否 fire-and-forget" | "context 是否一致性密集" | dispatch 决策 |
|------|----------------------------------|----------------------|-------------------------|---------------|
| T-01~T-05 | 否（template 写完归档到 assets/，父只在 validation/SKILL.md 引用时回到文件路径）| 是 | 否（每个 template 独立）| ✓ sub-agent |
| T-06（SKILL.md 直写）| **是**（SKILL.md 内 7 章节需相互引用 + 引用 templates + 持续修订）| 否 | **是**（章节一致性 + 边界守护）| ✗ Opus 直写 |
| T-07（analyze）| 否（一次性审核报告，父引用结果即可）| 是 | 否（独立审核任务）| ✓ sub-agent（readonly auditor）|
| T-08（同步 + validate + review）| **是**（DECISIONS.md 跨文档一致性 + 与 proj-run/SKILL.md 双向引用）| 否 | **是** | ✗ Opus 直写 |

### iteration & escalate 总策略

- 单 task 失败 ≤ budget：Opus 父给修订要点 → 重 dispatch
- 单 task 失败 > budget：按 escalate 规则（T-01~T-05 → Opus 父接手；T-07 → Opus 父跑 checklist）
- 全 phase sub-agent 失败 > 3 次（跨 task 累计）：触发 EXP-04 中止信号 R-02 → abort phase + 回 proj-shape 09 轮
- 任何 task 发现需要新 INV/ORD：触发 R-06 → 立即停手 + 回 proj-shape 09 轮（不在本试跑内改决定）

---

## GATE-3 确认

- [ ] 用户确认本 plan.md（含 8 task + dispatch manifest 5 字段闭环 + 决策树 + iteration 策略）
- [ ] 用户确认 `acceptance.md`（GATE-3 通过后由 AI 在 dispatch 过程中逐步填）
- [ ] 用户确认按本试跑路径执行（B2=Hybrid + 串行 dispatch + Opus 评审）

GATE-3 通过 → 开始 T-01 dispatch（首个 sub-agent 触发；同时启动 EXP-04 token 精细计量）。
