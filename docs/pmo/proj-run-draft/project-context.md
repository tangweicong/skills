# 项目上下文 — proj-run skill 完整版起草（EXP-04 试跑双重目标）

| 字段 | 值 |
|------|-----|
| 项目名 | proj-run skill 完整版起草 + EXP-04 试跑（双重目标） |
| 领域 | 软件 · Cursor Agent Skill 元开发 |
| 规模 | 个人 + AI（无团队）|
| 监管 | 无 |
| 外部 stakeholder | 无（仓库作者 = 唯一 stakeholder）|
| 物理/线下依赖 | 无 |
| 基于 DECISIONS | 2026-05-27（含 08 轮 ORD-18~22 + EXP-04 v1.4）|

## 简述

把 `skills/proj-run/SKILL.md` 从 v0 骨架升级为完整版（覆盖工作流 / 3 mode 实现 / dispatch manifest 完整 schema / validation gate / 失败模式 / 触发词），并补 `skills/proj-run/assets/` 5 个必要 templates。**同一动作** = EXP-04 试跑案例（验证 Opus 规划 + Composer Fast 执行的 model-tier 在 ≥3x cost 节省下能保持 GATE 一次通过率 ≥80%）。

## 输入

- `docs/discuss/DECISIONS.md`（含 INV-01~04 + ORD-01~22 + EXP-04 v1.4 全表）
- `docs/discuss/08-proj-run-skill起草.md`（4 视角分析 + 收敛 + 决定）
- 参照：`skills/proj-plan/SKILL.md` + `skills/proj-plan/assets/`（21 文件，作为风格基准 + 接口对齐基线）
- 参照：`skills/proj-run/SKILL.md` v0 骨架（保留 vision / 接口契约 / Cursor 约束披露 3 节，扩写其余）

## 输出

- `skills/proj-run/SKILL.md` 完整版（覆盖 v0；预估 350-420 行；硬上限 600 行）
- `skills/proj-run/assets/` 5 个 templates：
  - `dispatch-manifest-template.md`（ORD-21 5 字段闭环）
  - `acceptance-template.md`（输出契约：validation 结果 + token cost + escalate 标记）
  - `cursor-agents-template.md`（Mode α · ORD-19）
  - `message-bus-template.md`（Mode β · ORD-19 占位，无 runtime）
  - `validation-gate-template.md`（ORD-22 三类 gate）
- `docs/pmo/proj-run-draft/` 全套 PM artifact（Round A + B + phase-01 + acceptance）
- EXP-04 试跑数据回写到 `docs/discuss/DECISIONS.md`

## 约束

- **INV-04**：proj-plan 不含执行；本项目的"执行"环节由本轮试跑性质的 sub-agent dispatch 承担——记为 EXP-04 的实操数据，不入 proj-plan SKILL.md 主流程
- **INV-01**：人只读 human-read-manifest（≤5）；本项目 Round A 固定 2 项 + GATE-1/2/3 槽位
- **INV-03**：manifest GATE 未过不得生成下游 artifact；本项目严格执行 GATE-0 → GATE-1 → GATE-2 → GATE-3 串行
- **ORD-15**：proj-plan 的 manifest 段在本轮 EXP-04 passed 后才升级为强制（按 ORD-21 5 字段闭环）；试跑中仍可生成（这是 proj-run 自带的强制，不是 proj-plan）
- **命名规范**：`skills/proj-run/SKILL.md` 第一行用中文双层标题 `# 执行调度（proj-run）`
- **validate_skills.py 通过**：SKILL.md 须有 YAML frontmatter（含 name / description）；name 须 = 目录名 = `proj-run`；description 非空 ≤1024 字符；SKILL.md ≤600 行
- **EXP-04 v1.4 阈值**：success cost ≤ 1/3 baseline（baseline ≈ $6.75）；abort cost < 2x；GATE 一次通过率 ≥80%；analyze + validate_skills 通过
- **不在本项目内**写新 INV/ORD（属 proj-shape 域）；试跑中新发现的决定要回 proj-shape 走 09 轮

## 成功标准（链 EXP-04 v1.4 + 任务书完成 checkbox）

- [ ] `skills/proj-run/SKILL.md` 完整版（含工作流 / 3 mode 实现细节 / 失败模式 / 触发词；覆盖 v0 骨架）
- [ ] `skills/proj-run/assets/` 5 个必要 templates 完成且 validation 通过
- [ ] `docs/discuss/08-proj-run-skill起草.md` 完成（已完成 · 含 4 视角 + 决定 + 同步状态）
- [ ] `docs/discuss/DECISIONS.md` 同步（已完成本轮 ORD-18~22 + EXP-04 v1.4；试跑后再回写 EXP-04 状态 + token 数据）
- [ ] `uv run scripts/validate_skills.py` 通过
- [ ] EXP-04 试跑 cost ≤ 1/3 baseline（≥3x 节省）；GATE 一次通过率 ≥80%；analyze 通过

## 非目标

- 不实现 Mode α 的真实 `.cursor/agents/*.md` 文件（只写 template）
- 不实现 Mode β 的 `.apm/bus/` runtime 脚本（只写 template + 触发条件）
- 不修改 proj-plan/assets/plan-template.md（ORD-15 manifest 段升级到强制属于 EXP-04 passed 后的后续动作，本轮只验证 EXP-04 假设，不预先把 manifest 段写进 proj-plan）
- 不修改 proj-experts / proj-shape（本轮不涉及边界变更）
- 不修改 docs/pmo/（EXP-01 试跑遗产；本轮在 docs/pmo/proj-run-draft/ 子目录独立运作）
- 不在本轮新建 phase-02（rolling 原则：先做 phase-01，发现规模需要再开 phase-02）

## 待用户确认（GATE-0）

- [ ] 用户确认本 project-context.md
- [ ] 用户确认 tailoring-decision.md（建议模式 T）
- [ ] 用户确认 initiation-charter.md
- [ ] 用户确认 human-read-manifest.md Round A 配置（2 项 + 3 GATE 槽位）

GATE-0 通过 → 开 Round B（charter / wbs / phase-roadmap / integration-plan / change-log / artifact-index + analyze）。
