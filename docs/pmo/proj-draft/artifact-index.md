# Artifact Index — `proj` orchestrator skill 起草（SDD truth source）

> AI 维护；人不必读（INV-01）。登记本项目全部 artifact + 产出归属，防 source of truth 分裂。

## PM artifacts（docs/pmo/proj-draft/）

| 文件 | 阶段 | 状态 |
|------|------|------|
| project-context.md | Round A | ☑ |
| tailoring-decision.md | Round A | ☑（T-lean）|
| initiation-charter.md | Round A | ☑ |
| human-read-manifest.md | Round A | ☑（GATE-0 过）|
| charter.md | Round B | ☑ |
| wbs.md | Round B | ☑ |
| artifact-index.md | Round B | 本文件 |
| phase-01/plan.md | Rolling | ☑（待 GATE-3）|
| phase-01/acceptance.md | Rolling | 待执行回填 |

## 交付物（执行后产出 · 非本 skill 写）

| 文件 | 来源任务 | 状态 |
|------|----------|------|
| `skills/proj/SKILL.md` | T-01 | 待执行 |
| `README.md`（6 skill 索引 + proj 节）| T-02 | 待执行 |
| `skills/proj-run/SKILL.md`（规划中→转正）| T-03 | 待执行 |

## analyze 校验（Round B 后）

见本文件「analyze 结论」节（下）。

## analyze 结论

- 一致性：charter 成功标准 ↔ wbs 工作包 ↔ plan 任务 ↔ acceptance 验收项 四者对齐（见下表）。
- 覆盖：ORD-29/30/31 + EXP-07 caveat 全部有对应 WBS/任务/验收项。
- 无悬空：无「成功标准无任务」或「任务无验收」。

| ORD/目标 | WBS | 任务 | 验收项 |
|----------|-----|------|--------|
| ORD-29 facade/Supervisor | 1.3 | T-01 | behavioral ORD-29 |
| ORD-30 收窄·不重做路由 | 1.2 | T-01 | behavioral ORD-30 显式声明 |
| ORD-31 有界 loop+slider | 1.4–1.5 | T-01 | behavioral loop/slider/breaker |
| EXP-07 caveat | 1.4 | T-01 | EXP-07 caveat 自检 |
| 集成 6 skill | 2,3 | T-02,03 | 集成 |
| validate | 4.1 | T-04 | lint |
