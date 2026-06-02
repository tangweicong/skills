# Changelog

本仓库 [Agent Skills](./README.md) 的变更历史。版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)；格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

> **同步约定**：变更日志与 [`docs/discuss/DECISIONS.md`](./docs/discuss/DECISIONS.md) 互为参考——DECISIONS 是决定层 source of truth（INV/ORD/EXP + 来源 + 变更日志）；本文件是仓库交付层时间线（skill 文件级 / artifact 级变化）。

---

## [1.3.0] — 2026-06-02

新增第 5 个 skill `proj-survey`（brownfield 历史项目接管入口）。09 轮立项 + EXP-05 dogfood 试跑（passed）+ 10 轮起草发布。

### Added

- **`skills/proj-survey/SKILL.md`**（191 行 · brownfield 接管入口）：读既有系统 → 三分离现状基线 → 意图(to-be)重建评估 → GATE-S 人审批分支（可 plan → proj-plan / 仅 audit → 审计报告，可回流 proj-shape）；含真相源优先级（测试>代码>git>docs>口述）、不可违背 S-1~4、工作流 0–6、分支判据（provisional · EXP-06 待验证）、大 repo 分层降级、失败模式
- `skills/proj-survey/assets/` 3 个 templates：`baseline-template.md`（现状基线 · 三分离 + 已完成/未完成/质量/待验证 + 意图评估 + GATE-S 摘要 + 误报率自检）/ `audit-report-template.md`（分支 B · 内部一致性 findings + 置信度，不作保证）/ `survey-handoff-template.md`（分支 A → proj-plan · 既成约束 + WBS 三态种子）
- `docs/discuss/09-历史项目接管-proj-survey.md`：立项讨论（ORD-23~26 + EXP-05/06）；`docs/discuss/10-proj-survey起草.md`：起草执行轮
- `docs/survey/2026-06-01-baseline.md`：EXP-05 dogfood 产物（本仓库自动现状基线）
- DECISIONS.md 新增 ORD-23~26（proj-survey 立项 + 分支判据 + 审计终端 + proj-plan 衔接）+ EXP-05/06

### Trial outcome（EXP-05）

- **passed**：本仓库 dogfood 自动现状基线，事实层 **0/16 误报 = 0%** < 10% 阈值（用户「全对」）；分支判定「可 plan」与人判一致
- **caveat**：本 repo 属「intent 易重建」简单端，**未压测 intent 不可重建难例**（→ EXP-06 仍 pending，已嵌入 proj-survey §分支判据为 provisional + GATE-S 兜底）

### Changed

- **`skills/proj-plan/SKILL.md`**（302 → 319 行）落实 ORD-26 brownfield 入口：新增 `## Brownfield 接管入口（ORD-26）` 节（读 proj-survey handoff 代替 DECISIONS）+ §0 前置改「入口二选一」+ Round A/B 加 brownfield 子步 + WBS 标三态
- `skills/proj-plan/assets/wbs-template.md`：WBS 树新增「状态（brownfield）」列（已完成/进行中/待做；已完成=既成约束不重新规划）
- `skills/proj-plan/assets/project-context-template.md`：新增「项目类型（新建/接管）」+「上游来源」字段 + 「现状基线摘要（仅 brownfield）」节
- `skills/proj-survey/assets/survey-handoff-template.md`：移除「ORD-26 待落实」caveat（已落实，指向 proj-plan §Brownfield 接管入口）

### 待落实（下一步）

- **EXP-06**：找一个 intent 难重建的真实 repo 压测分支判据（暂放）

---

## [1.2.0] — 2026-05-28

proj-shape 新增三段式入口（BRAINSTORM → 苏格拉底澄清轮 → 专家讨论轮），降低初次表达负担 + 用苏格拉底六问为专家轮框定方向；同时合并双 README（删除 `skills/README.md`，统一到根 README）。

### Added

- `skills/proj-shape/assets/brainstorm-template.md`（51 行 · 用户自留草稿模板）：5 个开放问句（想解决什么 / 为什么做 / 服务谁 / 成功长什么样 / 不打算做什么）+ 自由叙述区 + 给 AI 的话（可选跳过苏格拉底的留痕位）；明示"不写事实查证 / 专家视角 / INV/ORD/EXP"——越简短越好
- `skills/proj-shape/SKILL.md` 新增 `## 三段式入口（首次使用本 skill）` 节：三段式总表（阶段 / 产出 / 主导 / 退出条件）+ 5 条规则 + **苏格拉底六问类别**表（澄清 / 追假设 / 找原因 / 看推论 / 换视角 / 元问 · AI 按需挑 3–5 个，非全套打）+ "不抽 skill 的理由"声明（六问足够薄 · inline 即可 · 未来有跨项目复用需求再抽 `socratic-grounded` 独立 skill）
- `skills/proj-shape/SKILL.md` 新增 `### BRAINSTORM.md（初始想法草稿）` 子节（与 `DECISIONS.md` 子节平行结构 · 含路径 / 创建 / 完成门槛 / 冻结时机 / 决定关系 / 同步要求）
- 根 `README.md` 的 proj-shape 节新增**三段式入口**总表（BRAINSTORM / 苏格拉底澄清轮 / 专家讨论轮）+ 跳过条件说明 + 典型用法更新（自动建 BRAINSTORM → 六问 → proj-experts 攻防）

### Changed

- `skills/proj-shape/SKILL.md`：
  - frontmatter `description` 加入 `brainstorm 初始想法捕获, 苏格拉底澄清, 三段式入口` 关键词
  - 顶部 HTML 注释新增「下一版改动（三段式入口）」段，记录 4 条本版改动
  - `## 项目目录结构` 目录树加入 `BRAINSTORM.md` 与 `01-苏格拉底澄清.md`
  - `### 讨论方法调用约定` 默认方法行：**Round 01 默认 `socratic-grounded`**（用户明示「想法够清楚」可跳过到 `proj-experts`，在 BRAINSTORM「给 AI 的话」或 round 01 frontmatter 留痕）；**Round 02+ 默认 `proj-experts`**
  - 工作流 §0「准备目录、BRAINSTORM 与轮次」：BRAINSTORM 不存在时**自动创建空模板**（不等用户提问）；存在但本轮 = round 01 时判断走苏格拉底/跳过；本轮 ≥ round 02 且 BRAINSTORM 仍可改时**冻结**（追加冻结注记，正文只读）
  - 工作流 §3「事实基础 + 讨论」：默认方法按轮次区分；新增**苏格拉底澄清轮特殊约定**——本轮不产 `INV`/`ORD`（除非用户显式确认升级），命题以「候选 ORD」「候选 EXP 假设」形式落到「本轮决定 → 待确认」节留给专家轮攻防；默认单轮（如必要多轮则文件名 `01-苏格拉底-焦点A.md`、`02-苏格拉底-焦点B.md`，专家轮从 `03-` 起）；苏格拉底过程中允许用户回改 BRAINSTORM
  - 触发词加入 `brainstorm · BRAINSTORM · 初始想法 · 想法捕获 · 苏格拉底澄清 · socratic-grounded · 三段式入口 · 六问`
- 根 `README.md`：
  - proj-shape 详细节加三段式入口（如上 Added 末项）；完整链路 step 1 提及 BRAINSTORM 自动建模板
  - 末尾「开发与贡献」节移除 `skills/README.md` 链接；改为「本文件即 4 skill 索引（不再单独维护 skills/README.md）」
- `CONTRIBUTING.md`：提交流程 step 2 从「更新 `skills/README.md` 索引表」改为「更新根 `README.md` 的 4 skill 索引表与对应 skill 详细节」
- 4 个 SKILL.md（proj-shape / proj-experts / proj-plan / proj-run）顶部 HTML 注释：「请同步更新 skills/README.md」→「请同步更新根 README.md 的 4 skill 索引表与本 skill 详细节」

### Removed

- **`skills/README.md`**（17 行 · 删除）—— 与根 `README.md` 的 4 skill 索引表重叠；维护两份增加同步成本却不带来新信息。该文件原有内容：
  - 4 skill 精简表 → **保留**在根 README 的索引表（行 7–12）+ 各 skill 详细节
  - `2026-05-27 集体重命名` notice → 已记录在 CHANGELOG `[1.0.0]` 段，**不再保留**冗余 notice
  - `<!-- 新增 skill 后…运行 validate_skills.py -->` 编辑约定 → **已挪到** `CONTRIBUTING.md` 提交流程节

### Design notes（不开 ORD · 仅记录设计动机）

- **本次改动未走 `docs/discuss/` 轮次留痕**：属 skill 内迭代（用户在对话中直接讨论确认），不开新 ORD/EXP；若未来三段式入口实际使用中暴露问题，再补开 09 轮讨论
- **苏格拉底不抽独立 skill**：六问类别足够薄，inline 在 `proj-shape/SKILL.md` 即可；与 `proj-experts`（需独立技术——专家模拟、三档标签）的判定不同
- **苏格拉底默认推荐但可跳过**：避免硬性强制变成形式主义；信号通道 = BRAINSTORM「给 AI 的话」节或对话明示
- **BRAINSTORM 冻结时机 = 进入 round 02 后**（而非写完即冻）：苏格拉底的价值之一就是让用户发现"原来我真正想做的不是这个"，需要回改窗口
- **苏格拉底轮只产候选命题不产决定**：与专家轮职责分开——苏格拉底负责"问出可被打靶的命题"，专家轮负责"攻防 + 沉淀 INV/ORD"
- **不动 `assets/round-template.md` 与 `assets/decisions-template.md`**：round-template 已有 `discussion_method` 字段足够；BRAINSTORM 不进 DECISIONS 同步循环
- **双 README 合并到根 README**：根 README = 项目主页（landing + 详细介绍）；原 `skills/README.md` 仅是 4 skill 速查索引，与根 README 重叠；删除后所有 skill 编辑约定指向根 README + CONTRIBUTING.md，single source of truth

### Compatibility

- 既有项目（`docs/discuss/` 已存在 round 01+）不受影响：BRAINSTORM 仅在不存在时自动创建；既有 round 01 不会被改名为「苏格拉底澄清」
- 新项目首次使用 proj-shape 时，第 0 步会自动建空 BRAINSTORM 模板；用户可立即跳过（在「给 AI 的话」明示）直接走 proj-experts，零阻塞
- 历史 PM artifact（`docs/pmo/proj-run-draft/*`）与历史讨论轮次（`docs/discuss/07-*.md`、`08-*.md`）中引用 `skills/README.md` 的位置**不动**（SDD 留痕约定 · 仅作历史快照）；CHANGELOG `[1.0.0]`/`[1.1.0]` 中提及 `skills/README.md` 的条目也不动（描述当时确实做了什么）

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
