# 已确定决定

> **给其它 skill / 用户**：执行计划、实现、新讨论前，**先读本文**即可掌握共识，无需通读 `docs/discuss/NN-*.md` 全文。  
> 历史细节与推理过程见各轮次文件；本文仅维护**当前有效**的决定汇总。  
> **同步**：与 `docs/discuss/NN-*.md` 互相同步更新；禁止只改本文件或只改轮次其一。

最后更新：2026-06-02（轮次 10 · `proj-survey` v1 起草发布——`skills/proj-survey/SKILL.md`（191 行）+ 3 assets；validator 5/5 退 0；EXP-05 流程固化进工作流；EXP-06 嵌入 §分支判据为 provisional + GATE-S 兜底；ORD-26 后半=proj-plan brownfield 入口/WBS 三态仍待落实；详见 `10-proj-survey起草.md`）

历史最后更新：2026-06-01（轮次 09 · 历史项目接管能力立项 → 新增第 5 个 skill `proj-survey`：ORD-23~26 + EXP-05/06；双入口流水线 = 正向 experts→shape→plan→run / 接管 survey→{plan | 审计终端}；详见 `09-历史项目接管-proj-survey.md`）

历史最后更新：2026-05-27（轮次 08 收尾 · proj-run 完整版 1.0 已发布 + EXP-04 v1.4 = **ABORTED with valuable insights**；项目级交付全过（GATE 100% + analyze 7/7 + validate 退 0 + 5 templates 0 escalate），仅 cost 信号未达：估算 actual ~$4.26 vs baseline $6.75，节省 ~1.58x < 2x 中止阈值；核心洞察 = plan 阶段 Opus 固定成本占 baseline ~37% / 占 actual ~58%，model-tier 需 ≥ $10.5 baseline 项目才能 ≥3x 节省；ORD-15 v0 可选**保持**不升级 · 修订条款触发条件 = EXP-04 aborted；轮次 07 sub-agent model-tier 编排 + skill 集体重命名 + EXP 案例精化 v1.3）

**讨论状态**：`deciding`（轮次 09 起：现有 4 skill 仍 `ready-for-implementation` 且 shipped/stable；新增 **proj-survey 设计线**处于 `deciding`——EXP-05/06 pending + 4 项待确认未闭合，未到可建状态）

> **2026-05-27 集体重命名**（轮次 07 决定）：`best-minds-grounded` → `proj-experts`、`idea-discuss` → `proj-shape`、`idea-pmo` → `proj-plan`；新增 `proj-run`（骨架版）。下文条目内容**不变**，引用名同步更新。历史轮次文件（01-06）正文不动，沿用旧名作为历史快照。

> proj-plan 在 tailoring 边界内（Initiate + Plan rolling + 规划侧 M&C + 阶段 Close；不含 Execute/成本/采购）**过程已闭合** — 见 `05-idea-pmo-pmp-coverage-rereview.md`（**注**：历史文件名沿用旧 skill 名 idea-pmo，不改）。**模式 F 状态调整**：从原"待 EXP-03 试跑"改为 **N/A**——本仓库不天然有 TR-04 命中的合规/审计/合同交付项目，虚构场景验证价值低；F 模式 template 已完整存在于 `skills/proj-plan/assets/`，供未来真实命中 TR-04 的用户开箱使用，本仓库不做真实场景试跑（07 轮 §讨论 6 决定）。
>
> 表达层校准：vision 声明（人=Sponsor+PM 决策、AI=PM 执行+artifact 维护；Supervised-AI mode）+ 借鉴/自创立场声明 + 真实 URL 出处 已通过 ORD-11~14 确立 — 见 `06-vision回归与表达层校准.md`。
>
> Sub-agent model-tier 编排议题（ORD-15~17 + EXP-04）：proj-plan 边界守护（只规定 dispatch manifest 承诺字段，不规定 model 选择）；新独立 skill `proj-run` 承接 PMP Executing；EXP-04 试跑后开 08 轮起草 proj-run 完整工作流。详见 `07-sub-agent-model-tier-编排.md`。
>
> **08 轮 proj-run 完整版起草 + EXP-04 试跑启动**（ORD-18~22 + EXP-04 v1.4）：proj-run 内部实现细节落地——PMP 6 Executing 承接 3 项 + 刻意外置 7 项（ORD-18）；3 Mode 表（α/β/γ）+ 触发条件（ORD-19）；Sub-agent dispatch 决策树按 context 回溯需求判定（ORD-20）；Dispatch manifest 5 字段闭环（ORD-21）；Validation gate 3 类（ORD-22）。EXP-04 阈值 v1.3 → v1.4 修订：成功 cost 由 ≤1/5 放宽至 ≤1/3，中止 cost 由 <3x 放宽至 <2x（理由：Cursor sub-agent 当前仅可调度 composer-2.5-fast 不可调度 standard；用户 B1=relax 确认）。详见 `08-proj-run-skill起草.md`。
>
> **08 轮收尾 + EXP-04 试跑结果**（2026-05-27 同日完成）：proj-run 完整版 1.0 已发布（`skills/proj-run/SKILL.md` 283 行 + `skills/proj-run/assets/` 5 templates；validate_skills.py 4/4 退 0；ORD-18~22 全落实；GATE-0/1/2/3 全 ☑ 一次通过率 100%；analyze 7/7 pass · T-08 修复后）。**EXP-04 v1.4 = ABORTED with valuable insights**：cost 信号未达（估算 actual ~$4.26 / baseline $6.75 / 节省 ~1.58x < 2x 中止阈值）；4 成功信号中 3 个全过仅 cost 未达。核心洞察 = Opus plan 阶段 ~$2.48 占 baseline ~37%、占 actual ~58% 为固定成本主导；Composer Fast 执行层 ~$0.35 仅占 actual ~8%；model-tier 真正生效需 ≥ $10.5 baseline 项目让 plan 成本占比 < 33%；本试跑案例规模不足。**正面验证**：Composer Fast 对结构化模板任务质量充分（5/5 一次过 + 0 escalate），ORD-21 5 字段闭环 + ORD-22 三类 gate 设计有效。**ORD-15 manifest 段保持 v0 可选不升级**（EXP-04 aborted 触发"不升级"分支）。详见 `08-proj-run-skill起草.md` + `docs/pmo/proj-run-draft/phase-01/{acceptance,review}.md`。

## 讨论就绪检查

| # | 硬条件 | 满足 |
|---|--------|------|
| 1 | 成功标准已写入 INV/ORD | ☑ |
| 2 | 无阻塞性待确认（或已登记 EXP-xx） | ☑ |
| 3 | 前沿/未知已有 EXP + 失败降级路径 B | ☑ |
| 4 | 原则性不变量未在摇摆 | ☑ |

**结论**：现有 4 skill（greenfield 流水线）讨论与试跑均就绪、shipped/stable，新项目直接使用。**新增 proj-survey 线（轮次 09–10）处于 `deciding`**：架构已 GATE 确认（ORD-23~26），**v1 已起草发布**（EXP-05 passed + skill 文件 + 3 assets，validator 退 0）；**ORD-26 已全部落实**（proj-survey + proj-plan brownfield 入口 + WBS 三态，10 轮）；**唯一未闭合项** = EXP-06（intent 难重建难例压测，已嵌入 §分支判据 provisional + GATE-S 兜底）。

## 原则性不变量

| ID | 决定 | 来源（必填） | 确立日期 |
|----|------|--------------|----------|
| INV-01 | 人类**只读** `human-read-manifest.md`（**≤5 项**）；**禁止**要求人读全量 PM artifact 树 | `02-…md`、`03-…md`；用户 @轮次02 | 2026-05-19 |
| INV-02 | 细任务与验收**仅**在 rolling `phase-NN/plan.md` | `01-…md`、`02-…md` | 2026-05-19 |
| INV-03 | manifest **GATE 未通过**不得生成下游 artifact | `02-…md` | 2026-05-19 |
| INV-04 | **proj-plan** 不含**执行**（执行归 `proj-run`，见 ORD-17）| `01-…md`、`03-…md`；07 轮加 proj-run 衔接 | 2026-05-19 |

## 普通决定

| ID | 决定 | 来源（必填） | 确立日期 | 备注 |
|----|------|--------------|----------|------|
| ORD-01 | skill **proj-plan**（原名 idea-pmo，07 轮重命名）；目录 **docs/pmo/** | `02-…md` §5 | 2026-05-19（07 轮重命名）| 已发布 |
| ORD-02 | `charter.md`、`wbs.md` | `01-…md` | 2026-05-19 | |
| ORD-03 | **双轮启动** Round A → GATE-0 → Round B | `02-…md` §2 | 2026-05-19 | 试跑 ✓ |
| ORD-04 | **Coach hybrid** + GATE-0（**本 skill 自创术语**；对接 [PMBOK 7 tailoring 4 步骤](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf)） | `02-…md` O2、O3；`06-…md` ORD-04 修订 | 2026-05-19（06 轮加注脚） | 自创术语，对接 PMBOK 7 |
| ORD-05 | manifest **≤5 项** | `02-…md` §3 | 2026-05-19 | |
| ORD-06 | 模式 F 须 artifact-index；T 须简表 | `02-…md` | 2026-05-19 | |
| ORD-07 | AI 不给人工时长 | `01-…md` | 2026-05-19 | |
| ORD-08 | EXP-01 试跑本仓库 | `03-…md` | 2026-05-19 | passed |
| ORD-09 | Round A **固定 2 项** | 用户 @开工 | 2026-05-19 | 试跑 ✓ |
| ORD-10 | proj-plan PMP **覆盖边界声明** = Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close；**不含** Execute / 成本 / 采购；需求输入由 proj-shape 承担 | `05-…md` §6 草案；`06-…md` 确认；[PMI Tailoring PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) | 2026-05-27 | 已落实到 SKILL.md + pmp-sdd-map.md |
| ORD-11 | SKILL.md 必含 **vision 声明段**——人 = Sponsor + PM 关键决策；AI = PM 执行 + analyst + artifact 维护；对应 [Supervised-AI mode](https://arxiv.org/html/2601.16392v1) | `06-…md` §收敛；用户 @本轮原话；推理 · Agentic PM 学派；依据 [arXiv 2601.16392](https://arxiv.org/html/2601.16392v1) + [PMI Sponsor](https://www.pmi.org/learning/library/importance-of-project-sponsorship-9946) | 2026-05-27 | 已落实到 SKILL.md |
| ORD-12 | SKILL.md 必含「**借鉴 / 自创**」立场声明节；自创术语（Coach hybrid、模式 T/F、GATE-N）显式标注「本 skill 自创」+ 链接 discuss 出处 | `06-…md` §讨论 1；推理 · PMI 派关切→路径；依据 proj-experts principle #7 真实性三档标签 | 2026-05-27 | 已落实到 SKILL.md |
| ORD-13 | `assets/pmp-sdd-map.md` 修订——拆为「PMBOK 借鉴 / SDD 借鉴（机制层）/ 本 skill 自创」三段；**去除 SDD 命令 1:1 映射**；保留机制借鉴（constitution↔INV、gate↔GATE-N、analyze↔analyze-checklist）；每段加真实 URL | `05-…md` 外推 · SDD（识别未落实）；`06-…md` §视角 B；推理 · Spec Kit 范式；依据 [spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md) | 2026-05-27 | 已落实到 pmp-sdd-map.md |
| ORD-14 | SKILL.md 立场声明节须含**基准版本声明**——PMBOK 6 过程组（覆盖矩阵基准）+ [PMBOK 7 tailoring](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf)（Coach hybrid 依据）+ PMBOK 8 AI 立场（[人/AI 责任分工依据](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence)）；每条须带 URL | `06-…md` §视角 A；推理 · PMI 派 | 2026-05-27 | 已落实到 SKILL.md |
| ORD-15 | proj-plan `phase-NN/plan.md` 模板**新增可选段** `## Sub-agent dispatch manifest` 作为对下游 `proj-run` 的**承诺字段**（task ID + specialist 类型 + validation criteria + iteration budget；**不指定具体 model**）；`artifact-index.md` schema 扩展登记 sub-agent 产出（INV-03 精神） | `07-…md` §讨论 1 + §讨论 5；推理 · INV-04 + ORD-10 + Anthropic Supervisor+Specialists；依据 [Anthropic Claude Code docs](https://code.claude.com/docs/en/agents.md) + [APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md) | 2026-05-27 | 已落实 proj-plan/SKILL.md（v0 manifest 可选；EXP-04 passed 后升级强制）|
| ORD-16 | **Cursor sub-agent 当前约束披露**——`model` 字段在 legacy plan 被 server 端忽略，仅 usage-based plan 的扩展支持已 rolling out；推荐 3 mode 降级（α 自动 dispatch / β APM message bus / γ 手动模型切换）；披露位置 = `proj-run/SKILL.md` 立场声明 | `07-…md` §F1 + §视角 A/B；推理 · Cursor 派 + Aider 派；依据 [Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736) | 2026-05-27 | 已落实到 proj-run/SKILL.md |
| ORD-17 | 建立独立下游 skill **`proj-run`** 专管 PMP **Executing Process Group**；与 proj-plan 接口契约 = `phase-NN/plan.md`（必含 manifest）；保持 proj-plan INV-04 不变；命名遵循 proj-* 体系（proj-experts → proj-shape → proj-plan → proj-run 对应 PMP 4 大 Process Group）；**本轮只定接口契约 + 骨架 SKILL.md**；完整工作流 EXP-04 passed 后开 08 轮起草 | `07-…md` §讨论 5；用户 @本轮原话；推理 · PMBOK 6 Process Groups 边界 + proj-shape 拆分先例 | 2026-05-27 | 已落实到 proj-run/ 骨架（v0）|
| ORD-18 | **proj-run PMP 6 Executing 边界声明**——承接 3 项（Direct & Manage Project Work / Manage Quality / Manage Project Knowledge），其余 7 项刻意外置（与 proj-plan ORD-10 同构纪律）| `08-…md` §视角 A 收敛；推理 · proj-experts · 视角 A；依据 [PMBOK 7 tailoring](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) deliberate choice 原则 | 2026-05-27 | 落实到 proj-run/SKILL.md §PMP Executing 边界节（EXP-04 试跑后）|
| ORD-19 | **proj-run 3 Mode 表 + 触发条件**——Mode α（自动 dispatch · usage-based plan）/ Mode β（message bus · 跨 session 或重场景）/ Mode γ（手动模型切换 · legacy plan）；Mode 选择按 plan 类型 + 是否跨 session 决定，**不**按 cost；Mode β 仅提供 template 不实现 runtime | `08-…md` §视角 D 收敛；推理 · proj-experts · 视角 D；依据 [APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md) + 07 轮 ORD-16 | 2026-05-27 | 落实到 proj-run/SKILL.md §3 Mode 表节 |
| ORD-20 | **proj-run Sub-agent dispatch 决策树**——第一判据 = "task 输出是否需要被父 agent 持续回溯"；**需回溯 → 不该 sub-agent**；判据**不**包含 cost（cost 是 by-product）| `08-…md` §视角 C 收敛；推理 · proj-experts · 视角 C；依据 [Claude Code agents docs](https://code.claude.com/docs/en/agents.md) "side task" 定义 | 2026-05-27 | 落实到 proj-run/SKILL.md §dispatch 决策树节 |
| ORD-21 | **proj-run Dispatch manifest 5 字段闭环（强制）**——每条 sub-agent task 必含 (1) objective / (2) specialist 类型 / (3) **可由父 agent 一行命令判定的** validation criteria / (4) iteration budget / (5) 失败 escalate 规则；落实在 proj-run/assets/dispatch-manifest-template.md + 升级 proj-plan/assets/plan-template.md（**v0 可选 → EXP-04 passed 后强制**——见 ORD-15 修订）| `08-…md` §视角 B 收敛；推理 · proj-experts · 视角 B；依据 [Aider blog 2024-09-26](https://aider.chat/2024/09/26/architect.html) architect-mode 闭环结构 | 2026-05-27 | 落实在 proj-run/assets/ + proj-plan 升级（EXP-04 passed 后）|
| ORD-22 | **proj-run Validation gate 3 类**——(1) structural（文件存在 / 字段齐 / 行数上限）/ (2) lint（validate_skills.py / markdown 结构 / YAML frontmatter）/ (3) behavioral（关键字 grep / 负向断言如 `rg -c "model:" = 0`）；任一失败按 ORD-21 iteration budget 重试；超出 budget escalate 给 Opus 父或 GATE | `08-…md` §视角 B 收敛延伸；推理 · proj-experts · 视角 B 细化 | 2026-05-27 | 落实到 proj-run/assets/validation-gate-template.md + proj-run/SKILL.md §Validation gate 节 |
| ORD-23 | **建立第 5 个 skill `proj-survey`** 专管 brownfield 逆向盘点（读既有系统 → 现状基线 → 分支）；**双入口流水线**：正向 `proj-experts→proj-shape→proj-plan→proj-run`，接管 `proj-survey → {intent 可信→proj-plan→proj-run | intent 不可信→审计终端}`；命名遵循 proj-* 体系 | `09-…md` §讨论；用户 @本轮 GATE（arch=new_skill, name=survey）；推理 · ORD-17 拆分先例 | 2026-06-01 | **已起草 v1**（`skills/proj-survey/SKILL.md` 191 行 + 3 assets；10 轮）|
| ORD-24 | **proj-survey 分支判据 = 「意图(to-be)是否可信重建」**（**非**「文档是否存在」）；现状基线每条 finding 复用 proj-shape **三分离**（事实/推理/待验证）标注；意图来源优先级 = 测试 > 代码结构 > git log/issue > docs/README > 用户口述（含冲突解决规则，待 EXP） | `09-…md` §讨论；用户 @本轮；推理 · 体系一致性（proj-shape 三分离外推） | 2026-06-01 | **已落实**到 proj-survey §真相源优先级 + §三分离标注 + §分支判据（10 轮）|
| ORD-25 | **审计分支（intent 不可信）作为 proj-survey 终端分支，v1 不独立成第 6 个 skill**；产出 = **findings + 置信度**，**不**作「无缺失 / 无 bug」保证；无 intent 时「完整性」仅限**内部一致性**（死代码/未接线模块/TODO/测试通过状态/文档漂移/已知反模式）；审计分支可回流 `proj-shape` 与人补 intent | `09-…md` §讨论；用户 @本轮 GATE（audit=terminal）；推理 · 逻辑约束（无 oracle 不可判定正确性）+ proj-shape 反过早抽象 | 2026-06-01 | **已落实**到 proj-survey S-2 + 分支 B + audit-report-template（10 轮）|
| ORD-26 | **proj-survey → proj-plan 衔接** = proj-plan 加 **brownfield 入口**（读 baseline 代替/补充 DECISIONS）+ **WBS 三态**（已完成/进行中/待做，避免把已完成当新工作）；「自动」= **baseline 生成全自动 + 人仅在分支 GATE 审批**（对齐 INV-01；人不整理，只拍板），人只读 ≤N 项摘要（复用 human-read-manifest 精神） | `09-…md` §讨论；用户 @本轮（要 AI 自动、不需人工整理）；推理 · INV-01 精神 | 2026-06-01 | **已全部落实**：proj-survey 侧（§角色分工 + GATE-S + handoff 模板）+ **proj-plan brownfield 入口**（SKILL.md §Brownfield 接管入口 + §0 入口二选一 + Round A/B + WBS 三态列 + project-context 项目类型字段）（10 轮）|

## 待验证尝试（落地阶段执行）

| ID | 假设 | 尝试方案 | 成功信号 | 继续 | 中止 | 来源 | 状态 |
|----|------|----------|----------|------|------|------|------|
| EXP-01 | 双轮 + Coach + manifest≤5 可行 | 本仓库 docs/pmo 试跑 | GATE 可决策；用户愿用双轮 | 发布 skill ✓ | — | `03-…md` §EXP-01 | **passed** |
| EXP-02 | GATE 防 task 前置 | phase-01 在 GATE-2 后 | plan 仅 GATE-2 后出现 | 硬规则 ✓ | — | `01-…md` §EXP-02 | **passed** |
| EXP-05 | AI 自动读中等规模 repo 能产出「事实层」足够准的现状基线，支撑分支判定 | 在本 skills 仓库自身（dogfood）或一个已知中等 repo 跑 baseline 生成，人工核对事实层误报率 | 事实层误报 < 阈值（**定为 <10%**）；分支判定（可 plan vs 仅 audit）与人判一致 | 误报率达标 → 固化 baseline 生成流程进 proj-survey 工作流 | 大 repo 一次读不完 / 误报率高 → 降级路径 B：人指认重点目录 + AI 局部分析 | `09-…md` §可验证尝试 EXP-05；产物 `docs/survey/2026-06-01-baseline.md` | **passed**（2026-06-02）：事实层 **0/16 误报 = 0%** < 10% 阈值（用户「全对」）；分支判定 = **可 plan**（intent 可信重建）与人判一致。**但**：本 dogfood repo 是「intent 易重建」的简单端，**未压测 EXP-06 的难例**（intent 不可重建 → 审计分支）。继续 → 可固化 baseline 流程进 proj-survey 工作流 |
| EXP-06 | 「intent 可信重建」存在可操作的 GATE 判据 | 设计判据 + 在 2–3 个真实 repo 上验证分支判定 | 判据稳定可复现，分支判定与人判一致 | 判据稳定 → 写入 proj-survey 分支 GATE | 判不准 → 降级路径 B：默认走更保守的审计分支 + 人确认 | `09-…md` §可验证尝试 EXP-06 | **pending**（10 轮已嵌入 proj-survey §分支判据为 **provisional** + GATE-S 人审批兜底；待 intent 难重建真实 repo 压测）|
| EXP-04 | **v1.4**（08 轮修订）：Opus 规划 + Composer **Fast** 执行的 model-tier 在 proj-plan + proj-run 协同流水线下，cost ≤ **1/3** baseline 且 GATE 通过率 ≥ 80% | **用 proj-* 流水线给 `proj-run` 起草完整 SKILL.md + assets 模板**（沿用 v1.3 案例）：proj-shape 走 08 轮决议 → proj-plan Round A → B → phase-01 出 plan + dispatch manifest → 规划/评审/analyze 用 Opus；T-01~05/07 dispatch 给 composer-2.5-fast sub-agent；T-06/08 Opus 直写（B2=Hybrid 路径）；记录 token + GATE + analyze | (1) total cost ≤ **1/3** baseline（baseline = proj-plan SKILL.md + 21 assets 总行数 × Opus blended rate × 3x 迭代因子 ≈ $6.75；B3=skill_plus_assets 已确认）；(2) GATE-0/1/2 一次通过率 ≥ 80%；(3) analyze 通过；(4) validate_skills.py 通过 | 把 manifest 段 schema（ORD-21 5 字段闭环）固化进 phase-NN/plan.md 模板（**ORD-15 v0 可选 → 强制**）；proj-run 完整 SKILL.md 同步发布；后续 skill 起草用相同 model-tier 模式 | Composer validation 反复失败（> 3 次/template）/ Opus plan 无法被 Composer 正确解读 / Cursor sub-agent 关键 feature 阻塞 / cost 节省 < **2x**（说明案例规模不够大）| `07-…md` §讨论 4 + EXP-04 草案 + §讨论 6；`08-…md` §讨论 3.3 v1.4 阈值修订；用户 B1=relax + B2=hybrid + B3=skill_plus_assets | **ABORTED with valuable insights**（08 轮试跑完成 2026-05-27）：4 成功信号中 3 个全过（GATE 一次通过率 100% = 4/4 · analyze 7/7 pass · validate_skills.py 退 0），仅 cost 信号未达——估算 actual ~$4.26 vs baseline $6.75 / 节省 ~1.58x < 2x 中止阈值。**核心洞察**：Opus plan 阶段 ~$2.48 占 baseline ~37% / 占 actual ~58% 为固定成本主导；Composer Fast 执行层 ~$0.35 仅占 actual ~8%；要实现 ≥3x 节省需 ≥ $10.5 baseline 项目让 plan 成本占比 < 33%。**正面验证**：5/5 templates 一次过 validation + 0 escalate；ORD-21 5 字段闭环 + ORD-22 三类 gate 设计有效。**触发后续动作分支**：ORD-15 v0 可选 → **保持不升级**（按"EXP-04 aborted 则保持 v0 可选不强制"修订条款）。详见 `docs/pmo/proj-run-draft/phase-01/{acceptance,review}.md` |

## 变更日志

| 日期 | 操作 | ID | 来源 | 说明 |
|------|------|-----|------|------|
| 2026-05-19 | 新增 | EXP-01 | `01-…md` | 初建 |
| 2026-05-19 | 修订 | EXP-01 | `03-…md` | 合并 EXP-03 |
| 2026-05-19 | 新增 | EXP-02 | `01-…md` | |
| 2026-05-19 | 新增 | INV-01–04, ORD-01–09 | `03-…md` | |
| 2026-05-19 | 状态 | — | 用户开工 | ready-for-implementation |
| 2026-05-19 | 状态 | EXP-01 | phase-01 review | **passed** |
| 2026-05-19 | 状态 | EXP-02 | phase-01 review | **passed** |
| 2026-05-21 | 评审 | — | `04-idea-pmo-pmp-gap-review.md` | PMP 缺口与实现债清单；EXP-03/04 草案待确认 |
| 2026-05-21 | 再评审 | — | `05-idea-pmo-pmp-coverage-rereview.md` | 边界内 PMP 过程闭合；ORD-10/EXP-03 待确认 |
| 2026-05-27 | 新增 | ORD-10~14 | `06-vision回归与表达层校准.md` | vision 显化 + 借鉴/自创立场 + SDD 立场修正 + PMBOK 基准声明；ORD-10 承接 05 轮 |
| 2026-05-27 | 修订 | ORD-04 | `06-vision回归与表达层校准.md` | 加注脚「本 skill 自创术语；对接 PMBOK 7 tailoring 4 步骤」；条文内容不变 |
| 2026-05-27 | 落实 | ORD-10~14 | `skills/idea-pmo/SKILL.md`、`skills/idea-pmo/assets/pmp-sdd-map.md` | 表达层校准已落地；前 5 轮决定内容**不动** |
| 2026-05-27 | 重命名 | — | `07-sub-agent-model-tier-编排.md` | 集体重命名：best-minds-grounded → proj-experts；idea-discuss → proj-shape；idea-pmo → proj-plan；新增 proj-run（骨架）。下文条目引用名已同步；前 5 轮历史文件正文不动 |
| 2026-05-27 | 新增 | ORD-15~17, EXP-04 | `07-sub-agent-model-tier-编排.md` | sub-agent model-tier 编排：proj-plan 加 dispatch manifest 承诺字段；Cursor 约束披露；建立独立 proj-run skill；Opus 规划+Composer 执行 EXP |
| 2026-05-27 | 落实 | ORD-15~17 | `skills/proj-plan/SKILL.md`、`skills/proj-run/SKILL.md`（骨架 v0）| ORD-15/17 已落实；proj-run 完整工作流 EXP-04 passed 后开 08 轮起草 |
| 2026-05-27 | 废止 | EXP-03 | `07-…md` §讨论 6 | 06 轮设计意图（模式 F 试跑）从未进入 EXP 表；本仓库不天然有 TR-04 命中项目；F 模板已存在供未来用户开箱使用，**不**做真实场景试跑；EXP-03 标记 N/A |
| 2026-05-27 | 修订 | EXP-04 | `07-…md` §讨论 6 | 试跑案例从"proj-experts 加 i18n"（规划深度不够，不能验证 model-tier 价值）改为"用 proj-* 流水线给 proj-run 起草完整 SKILL.md + assets"（自然嵌套；规划深度高；执行规模适中；08 轮目标本身——双重收益）|
| 2026-05-27 | 新增 | ORD-18~22 | `08-proj-run-skill起草.md` | proj-run skill 内部实现细节：PMP 6 Executing 边界（承接 3 + 外置 7）/ 3 Mode 表（α/β/γ）/ Sub-agent dispatch 决策树 / Dispatch manifest 5 字段闭环 / Validation gate 3 类。4 视角分析（PMP / Aider / Anthropic / APM）沿用 07 轮 F1-F5 URL 不重搜 |
| 2026-05-27 | 修订 | EXP-04 | `08-…md` §讨论 3.3 | 阈值 v1.3 → v1.4：成功 cost 由 ≤1/5 放宽至 ≤1/3，中止 cost 由 <3x 放宽至 <2x；理由：Cursor sub-agent 当前仅可调度 composer-2.5-fast 不可调度 standard（F6 新增事实）；用户 B1=relax 确认 |
| 2026-05-27 | 修订 | ORD-15 | `08-…md` §本轮决定 | manifest 段 v0 可选 → **EXP-04 passed 后升级为强制**（按 ORD-21 5 字段闭环执行）；若 EXP-04 aborted 则保持 v0 可选不强制 |
| 2026-05-27 | 落实 | ORD-18~22 | `skills/proj-run/SKILL.md` 1.0（283 行） + `skills/proj-run/assets/` 5 templates | proj-run 完整版发布：PMP 6 Executing 边界 / 3 Mode 表 / dispatch 决策树 / 5 字段闭环 manifest schema / Validation gate 3 类 + 工作流 / Circuit breaker / 失败模式（含 EXP-04 试跑观察 F1~F10）/ 触发词 / 模板索引 |
| 2026-05-27 | 状态 | EXP-04 | `docs/pmo/proj-run-draft/phase-01/{acceptance,review}.md` | **ABORTED with valuable insights**：actual ~$4.26 / baseline $6.75 / 节省 ~1.58x < 2x 中止阈值；GATE 100%、analyze 7/7、validate 退 0、5/5 templates 一次过；plan 阶段 Opus 固定成本占 actual 58% 是算术天花板；model-tier 真正生效需 ≥ $10.5 baseline 项目 |
| 2026-05-27 | 维持 | ORD-15 | `08-…md` 修订条款 | manifest 段**保持 v0 可选不升级**（EXP-04 aborted 触发"不升级"分支）|
| 2026-06-01 | 新增 | ORD-23~26, EXP-05/06 | `09-历史项目接管-proj-survey.md` | 历史项目接管能力立项：新增第 5 个 skill proj-survey（逆向盘点→现状基线→分支）；分支判据=意图可否可信重建+三分离；审计=终端分支+findings/置信度不作保证；proj-plan 加 brownfield 入口+WBS 三态；自动生成+人 GATE 审批 |
| 2026-06-01 | 状态 | — | `09-…md` | `ready-for-implementation` → `deciding`（proj-survey 设计线 EXP-05/06 pending + 4 待确认未闭合；现有 4 skill 仍 shipped/stable）|
| 2026-06-02 | 状态 | EXP-05 | `docs/survey/2026-06-01-baseline.md` | **passed**：本仓库 dogfood 自动现状基线，事实层 0/16 误报（用户「全对」），分支判定「可 plan」与人判一致；阈值定 <10%。caveat：未压测 intent 不可重建难例（留 EXP-06）|
| 2026-06-02 | 落实 | ORD-23~25 | `skills/proj-survey/SKILL.md`（191 行）+ 3 assets | proj-survey v1 起草：双入口流水线 / 真相源优先级 / 三分离 / 分支判据(provisional) / GATE-S / 审计终端分支 / 失败模式 / 触发词 / 模板索引；validator 5/5 退 0；EXP-05 流程固化 |
| 2026-06-02 | 部分落实 | ORD-26 | `skills/proj-survey/` | proj-survey 侧已落实（角色分工/GATE-S/handoff 模板）；proj-plan 后半另记 |
| 2026-06-02 | 落实 | ORD-26 | `skills/proj-plan/SKILL.md`（319 行）+ wbs-template + project-context-template | proj-plan brownfield 入口完成：§Brownfield 接管入口节 + §0 入口二选一 + Round A/B brownfield 子步 + WBS 三态列（已完成/进行中/待做）+ project-context 项目类型字段；validator 5/5 退 0。ORD-26 **全部落实** |
| 2026-06-02 | 状态 | EXP-06 | `10-…md` | 维持 pending；嵌入 proj-survey §分支判据为 provisional + GATE-S 兜底；待 intent 难重建真实 repo 压测 |
