# 项目上下文 — `proj` orchestrator skill 起草

| 字段 | 值 |
|------|-----|
| 项目名 | 把 `proj` 从 EXP-07 spike 升级为 shipped skill |
| 项目类型 | greenfield（新建第 6 个 skill）|
| 领域 | 软件 · Agent Skill 元开发 |
| 规模 | 个人 + AI（无团队）|
| 监管 | 无 |
| 外部 stakeholder | 无（仓库作者 = 唯一 stakeholder）|
| 基于 DECISIONS | 2026-06-29 轮次 12（ORD-28~31 + EXP-07 passed with caveats）|

## 简述

把 `docs/pmo/proj-orchestrator-spike/proj-spike-SKILL.md`（EXP-07 已验证的 ~70 行 spike）升级为 shipped **`skills/proj/SKILL.md`**——proj-* 流水线的**用户总入口 orchestrator**：跨 skill 状态机 + 有界 plan-execute-verify loop + GATE 编排 + facade（ORD-29/30/31）。

## 输入

- `docs/discuss/DECISIONS.md`（ORD-28~31 + EXP-07）
- `docs/discuss/12-proj-run通用化与orchestrator-loop.md`（grounded 讨论 + 三视角）
- `docs/pmo/proj-orchestrator-spike/`（spike + exp-07-result.md）
- 参照：`skills/proj-{experts,shape,plan,survey,run}/SKILL.md`（风格基线 + 被调用接口）

## 输出

- `skills/proj/SKILL.md`（shipped；预估 ~120–160 行；硬上限 600）
- 根 `README.md` 索引表 + `proj` 详细节（5 → 6 skill）
- `skills/proj-run/SKILL.md`「（规划中）」标记 → 改为正式（proj shipped 后）
- `DECISIONS.md` 标记 ORD-29 落实

## 约束

- **INV-04**：proj-plan 不含执行；实际写 `skills/proj/SKILL.md` 属执行环节（对话/proj-run），本 skill 只产出 plan
- **ORD-30**：`proj` **不重做** host 原生 model-invocation 的 skill 选择
- **ORD-31**：loop = 有界 + autonomy slider（phase 内自迭代 / GATE 停 / circuit breaker）
- **validate_skills.py 通过**：`name: proj` = 目录名；description 非空 ≤1024；SKILL.md ≤600 行
- 不写新 INV/ORD（属 proj-shape 域）

## 成功标准

- [ ] `skills/proj/SKILL.md` shipped + `validate_skills.py` 退 0
- [ ] 体现 ORD-29/30/31（facade/Supervisor + 收窄职责 + 有界 loop + GATE 清单）+ 显式声明「不重做 host 路由」
- [ ] 根 README 索引更新为 6 skill
- [ ] acceptance 覆盖 EXP-07 两条 caveat（冷启动 experts→shape→plan→run 全遍历 + 失败 re-route loop）的**设计层**自检；真实压测留 acceptance 记录或后续 EXP-07b

## 非目标

- **不做** proj-run 通用化 / 跨 runtime 适配器（ORD-28 separate · EXP-08 独立后续）
- **不改** experts/shape/plan/survey 正文（仅 README 增 `proj`；各 skill 可选「经 proj 入口」一行留待后续，避免大面积触碰 shipped）
- 不新建 phase-02（rolling：先 phase-01，发现规模需要再开）

## 待用户确认（GATE-0）

- [ ] 本 project-context.md
- [ ] tailoring-decision.md（建议模式 T · 且提供 lean 选项）
- [ ] initiation-charter.md
- [ ] human-read-manifest.md（Round A 2 项 + GATE 槽位）
