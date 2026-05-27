# Changelog

本仓库 [Agent Skills](./README.md) 的变更历史。版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)；格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

> **同步约定**：变更日志与 [`docs/discuss/DECISIONS.md`](./docs/discuss/DECISIONS.md) 互为参考——DECISIONS 是决定层 source of truth（INV/ORD/EXP + 来源 + 变更日志）；本文件是仓库交付层时间线（skill 文件级 / artifact 级变化）。

---

## [1.1.0] — 2026-05-27

08 轮：proj-run 完整版起草 + EXP-04 model-tier 试跑。

### Added

- `skills/proj-run/SKILL.md` 完整版 1.0（283 行）：覆盖 v0 骨架；新增 13 章节（vision / 立场声明 / PMP 6 Executing 边界 / 3 Mode 表 / dispatch 决策树 / dispatch manifest 5 字段闭环 / Validation gate 3 类 / 工作流 / Circuit breaker / 失败模式 F1~F10 / 触发词 / 不触发本 skill / 模板索引）
- `skills/proj-run/assets/` 5 个 templates（共 497 行）：
  - `dispatch-manifest-template.md`（141 行 · ORD-21 5 字段闭环模板 + 示例）
  - `acceptance-template.md`（82 行 · validation 结果 + token cost + escalate 标记 + GATE 联动）
  - `cursor-agents-template.md`（113 行 · Mode α YAML frontmatter + ORD-16 legacy warning）
  - `message-bus-template.md`（62 行 · Mode β `.apm/bus/` 占位 · 无 runtime）
  - `validation-gate-template.md`（99 行 · structural/lint/behavioral 3 类 + escalate 流程）
- `docs/discuss/08-proj-run-skill起草.md`：4 视角分析（PMP / Aider architect / Anthropic Supervisor+Specialists / APM 三角色 · 沿用 07 轮 F1-F5 URL 不重搜）+ ORD-18~22 草案 + EXP-04 v1.4 阈值修订 + 试跑结果回写
- `docs/pmo/proj-run-draft/` 全套 PM artifact（独立 namespace 避免污染历史 EXP-01 遗产）：project-context / tailoring-decision / initiation-charter / human-read-manifest / charter / wbs / phase-roadmap / integration-plan / change-log / risk-register / artifact-index / phase-01/{plan, acceptance, review}
- `CHANGELOG.md`（本文件）
- DECISIONS.md 新增决定 ORD-18~22（proj-run 实现细节）：
  - **ORD-18** · proj-run PMP 6 Executing 边界声明：承接 3 项（Direct & Manage Project Work + Manage Quality + Manage Project Knowledge），其余 7 项刻意外置
  - **ORD-19** · proj-run 3 Mode 表（α 自动 dispatch / β APM message bus 占位 / γ 手动模型切换）+ 触发条件
  - **ORD-20** · Sub-agent dispatch 决策树：按 context 回溯需求判定，**不**按 cost
  - **ORD-21** · Dispatch manifest 5 字段闭环（objective / specialist / validation criteria / iteration budget / escalate）强制
  - **ORD-22** · Validation gate 3 类（structural / lint / behavioral）+ 失败 escalate 流程

### Changed

- `skills/README.md`：proj-run 行从 v0 骨架更新为完整版 1.0（链 ORD-18~22）
- `README.md`（顶层）：3 skill → 4 skill 完整重写；旧名（best-minds-grounded / idea-discuss / idea-pmo）→ proj-* 体系（与 07 轮重命名对齐）；新增 PMP 4 大 Process Group 对应表 + 4 节点流水线图 + proj-run 完整说明节
- `docs/pmo/README.md`：从单项目进度页改写为多项目 namespace 索引；明示 `docs/pmo/`（根）= EXP-01 历史遗产（proj-plan 发布 · 已关闭），新项目走 `docs/pmo/<project>/` 子目录
- DECISIONS.md 顶部说明段 + 变更日志：同步 08 轮决议 + EXP-04 试跑结果（状态 = ABORTED with valuable insights）
- EXP-04 v1.3 → **v1.4** 阈值修订：
  - 成功 cost ≤ 1/5 baseline → **≤ 1/3 baseline**（≥3x 节省）
  - 中止 cost < 3x → **< 2x**
  - 理由：Cursor sub-agent 当前仅可调度 `composer-2.5-fast`（价差 ~5x）不可调度 `composer-2.5-standard`（价差 30x；详见 [Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736)）；用户 B1=relax 确认

### Trial outcome（EXP-04 v1.4）

- 状态：**ABORTED with valuable insights**
- baseline ≈ $6.75；actual ≈ $4.26（中位估算 · ±20%）；节省 ~1.58x（< 2x 中止阈值，故 ABORTED）
- 4 成功信号中 3 个全过：GATE 一次通过率 **100%（4/4）** · analyze **7/7 pass** · validate_skills.py **退 0** · 仅 cost 信号未达
- **核心洞察**：Opus plan 阶段固定成本占 baseline ~37% / 占 actual ~58%；Composer Fast 执行层仅占 actual ~8%；model-tier 真正生效需 ≥ $10.5 baseline 让 plan 成本占比 < 33%
- **正面验证**：5/5 templates 一次过 validation · 0 escalate · ORD-21 5 字段闭环 + ORD-22 三类 gate 设计有效
- **触发后续动作**：ORD-15 manifest 段**保持 v0 可选不升级**（按"EXP-04 aborted 则保持 v0 可选不强制"修订条款）；不开 09 轮（失败模式已 observed 并写入 SKILL.md §失败模式 F1~F10）

---

## [1.0.0] — 2026-05-27

07 轮：sub-agent model-tier 编排议题 + skill 集体重命名 + proj-run 骨架 + EXP 案例精化 v1.3。

### Added

- 新 skill `proj-run`（骨架版本 v0）：承接 PMP Executing Process Group；当前仅定义接口契约 + Cursor 约束披露（ORD-16）；完整工作流待 EXP-04 试跑后开 08 轮起草
- DECISIONS.md 新增决定 ORD-15~17 + EXP-04（v1.3）：
  - **ORD-15** · proj-plan 在 `phase-NN/plan.md` 模板新增可选段 `## Sub-agent dispatch manifest` 作为对下游 proj-run 的承诺字段（task ID + specialist 类型 + validation criteria + iteration budget；**不指定具体 model**）
  - **ORD-16** · Cursor sub-agent `model` 字段在 legacy plan 被 server 端忽略的约束披露；推荐 3 mode 降级（α 自动 / β APM message bus / γ 手动切换）
  - **ORD-17** · 建立独立下游 skill `proj-run` 专管 PMP Executing；与 proj-plan 接口契约 = `phase-NN/plan.md`（必含 manifest）
  - **EXP-04 v1.3** · 试跑案例精化：原"proj-experts 加 i18n"（规划深度不够）改为"用 proj-* 流水线给 proj-run 起草完整 SKILL.md + assets"（自然嵌套；08 轮目标本身）
- `docs/discuss/07-sub-agent-model-tier-编排.md`：4 视角分析（Cursor team / Aider / Anthropic / APM）+ ORD-15~17 + EXP-04 案例

### Changed

- **集体重命名**（用户选 proj-* 前缀体系）：
  - `best-minds-grounded` → **`proj-experts`**（专家研判 · Initiating · Business Case）
  - `idea-discuss` → **`proj-shape`**（想法收敛 · Initiating · 多轮决议）
  - `idea-pmo` → **`proj-plan`**（项目蓝图 · Initiate + Planning + 规划侧 M&C + Closing）
- 4 个 skill 全部第一行使用**中文双层标题**格式（`# 中文名（proj-xxx）`）
- `skills/README.md`：3 skill 表 → 4 skill 表（含 PMP 4 大 Process Group 对应列）
- `skills/proj-plan/SKILL.md`：落实 ORD-15（plan-template manifest 段 v0 可选）+ ORD-17（衔接 proj-run）
- 历史轮次文件（01-06）正文不动；引用旧名作为历史快照保留

### Deprecated

- 旧 skill 名 `best-minds-grounded` / `idea-discuss` / `idea-pmo` 仅作历史名；新项目用 proj-* 名

### Resolved

- **EXP-03 = N/A 废止**：06 轮"模式 F 试跑"设计意图从未进入 DECISIONS 待验证表；本仓库不天然有 TR-04 命中（合规/审计/合同交付）项目；F 模式 template 已存在于 `skills/proj-plan/assets/` 供未来真实命中用户开箱使用；不在本仓库做虚构场景试跑

---

## [0.6.0] — 2026-05-27

06 轮：Vision 回归与表达层校准。

### Added

- DECISIONS.md 新增决定 ORD-10~14：
  - **ORD-10** · proj-plan（时名 idea-pmo）PMP **覆盖边界声明** = Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close；**不含** Execute / 成本 / 采购
  - **ORD-11** · SKILL.md 必含 **vision 声明段**——人 = Sponsor + PM 关键决策权；AI = PM 执行 + analyst + artifact 维护；对应 [Supervised-AI mode](https://arxiv.org/html/2601.16392v1)
  - **ORD-12** · SKILL.md 必含「**借鉴 / 自创**」立场声明节；自创术语（Coach hybrid、模式 T/F、GATE-N）显式标注「本 skill 自创」+ 链 discuss 出处
  - **ORD-13** · `assets/pmp-sdd-map.md` 修订——拆为「PMBOK 借鉴 / SDD 借鉴（机制层）/ 本 skill 自创」三段；**去除 SDD 命令 1:1 映射**；保留机制借鉴
  - **ORD-14** · SKILL.md 立场声明节须含**基准版本声明**——PMBOK 6 / 7 tailoring / 8 AI Appendix；每条须带 URL
- `docs/discuss/06-vision回归与表达层校准.md`：vision 声明草案 + 借鉴/自创立场声明 + SDD 立场修正 + PMBOK 基准声明
- `skills/idea-pmo/SKILL.md`（时名）+ `skills/idea-pmo/assets/pmp-sdd-map.md`：落实 ORD-10~14

### Changed

- **ORD-04 修订**：Coach hybrid 加注脚「本 skill 自创术语；对接 PMBOK 7 tailoring 4 步骤」；条文内容不变

---

## [0.5.0] — 2026-05-21

05 轮：idea-pmo PMP 覆盖再评审。

### Added

- `docs/discuss/05-idea-pmo-pmp-coverage-rereview.md`：再评审 04 轮缺口；确认边界内 PMP 过程闭合；EXP-03 草案（模式 F 试跑 · 后于 07 轮废止 N/A）+ ORD-10 草案（后于 06 轮确认）

### Status

- 讨论状态从 05 轮初始的 `deciding` → 待 06 轮确认 ORD-10 后变 `ready-for-implementation`

---

## [0.4.0] — 2026-05-21

04 轮：idea-pmo PMP 缺口与实现债评审。

### Added

- `docs/discuss/04-idea-pmo-pmp-gap-review.md`：PMP 知识领域 × Process Group 缺口分析；实现债清单；EXP-03 / EXP-04 草案（待后续轮次确认）

---

## [0.1.0] — 2026-05-22

仓库初次公开发布（含 01-03 轮已落地的 3 个 skill）。

### Added

- 3 个 skill 初始发布：
  - **best-minds-grounded**（后于 07 轮重命名为 proj-experts）：Grounded 模拟器思维框架；先查证再模拟专家观点；输出按三档真实性标签
  - **idea-discuss**（后于 07 轮重命名为 proj-shape）：以实现为导向的多轮想法讨论框架；`docs/discuss/` + `DECISIONS.md` + EXP 表
  - **idea-pmo**（后于 07 轮重命名为 proj-plan）：承接 DECISIONS 的 PMP 分层规划 skill；`docs/pmo/` + Coach hybrid + 双轮启动 + GATE-N + manifest≤5
- `docs/discuss/` 01-03 轮文档：implement skill 流程与 pmp 映射 / AI 全量 PMP 与智能裁剪 / idea-pmo 两轮启动与决定收敛
- DECISIONS.md 初版（INV-01~04 + ORD-01~09 + EXP-01/02）：
  - **INV-01** · 人类**只读** `human-read-manifest.md`（≤5 项）；**禁止**要求人读全量 PM artifact 树
  - **INV-02** · 细任务与验收**仅**在 rolling `phase-NN/plan.md`
  - **INV-03** · manifest **GATE 未通过**不得生成下游 artifact
  - **INV-04** · idea-pmo（时名）不含执行（后于 07 轮明确执行归 proj-run）
  - **ORD-01** · skill 名（idea-pmo · 时名） + 目录 `docs/pmo/`
  - **ORD-02** · `charter.md` + `wbs.md`
  - **ORD-03** · 双轮启动 Round A → GATE-0 → Round B
  - **ORD-04** · Coach hybrid + GATE-0
  - **ORD-05** · manifest ≤5 项
  - **ORD-06** · 模式 F 须 artifact-index；T 须简表
  - **ORD-07** · AI 不给人工时长
  - **ORD-08** · EXP-01 试跑本仓库
  - **ORD-09** · Round A 固定 2 项
  - **EXP-01** · 双轮 + Coach + manifest≤5 可行（试跑后 passed）
  - **EXP-02** · GATE 防 task 前置（试跑后 passed）
- 顶层 README.md + skills/README.md + 模板 + `scripts/validate_skills.py` 校验脚本
- 试跑产出：`docs/pmo/`（根 · proj-plan 发布项目 · Round A + B + phase-01 全 GATE 过 · EXP-01/02 passed · 已关闭）

### Notes

- 后续 04~06 轮在公开仓库前后陆续 discuss-only 推进；07 轮做集体重命名 + 加 proj-run；08 轮完成 proj-run 完整版
