---
name: proj-plan
description: >-
  PMP-style planning (PMBOK 6 process groups + PMBOK 7 tailoring + PMBOK 8 AI
  stance) from docs/discuss/DECISIONS.md: docs/pmo/ with Coach hybrid tailoring,
  Round A/B initiate+plan, human-read-manifest (≤5), mode T/F, integration-plan
  + phase-roadmap (coarse) + rolling phase plans, change-log, SDD analyze gate
  (mechanism-borrowed from GitHub Spec Kit), sub-agent handoff. Role split =
  Supervised-AI mode: human = Sponsor + PM key decisions; AI = PM execution +
  artifact maintenance. Pairs with proj-experts + proj-shape (Business
  Case stage).
compatibility: >-
  Requires docs/discuss/DECISIONS.md (ready-for-implementation) OR a proj-survey
  brownfield handoff (docs/survey/*-handoff.md). Writes under project-root
  docs/pmo/. Updates EXP-xx in DECISIONS. Does not execute builds.
---

<!--
input: docs/discuss/DECISIONS.md
output: docs/pmo/（Round A/B + rolling phase-NN/）
pos: 落地规划 skill；proj-shape 之后、执行之前

修改本文件后，请同步更新根 README.md 的 4 skill 索引表与 proj-plan 详细节（skills/README.md 已于 1.2.0 合并至根 README）。
-->

# 项目蓝图（proj-plan）

承接 **`docs/discuss/DECISIONS.md`**，用 **PMP 计划分层 + SDD gate/analyze 纪律** 生成规划产物：AI 维护完整 artifact 集（可裁剪或全量），人类**只读** `human-read-manifest.md`（≤5 项）。

**规划归本 skill；讨论与执行不归本 skill**（讨论 → `proj-experts` + `proj-shape`；编码/交付 → 对话或其它 skill）。

## 设计 vision

proj-plan 借鉴 **SDD harness 范式**（spec-as-truth、constitution-as-guardrail、gate、analyze；机制层借鉴自 [GitHub Spec Kit](https://github.com/github/spec-kit/blob/main/spec-driven.md)），将 **PMP 项目管理流程**（[PMBOK 7 tailoring 原则](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) + [PMBOK 8 AI 立场](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence)）落地为 **agent 可执行的工作流**。

**角色分工对应 [Agentic PM 框架的 Supervised-AI mode](https://arxiv.org/html/2601.16392v1)**：

| 角色 | 谁担任 | 职责 |
|------|--------|------|
| **Sponsor + PM 关键决策权** | **人** | 模糊想法、go/no-go、[success criteria / business case](https://www.pmi.org/learning/library/importance-of-project-sponsorship-9946)、关键 trade-off、GATE 审批；**只读** `human-read-manifest.md`（≤5 项） |
| **PM 执行 + analyst + artifact 维护** | **AI** | 扩写 charter、维护 WBS、生成 phase plan、跑 analyze；**不做关键决策** |

与 [PMBOK 8 AI Appendix](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence) 立场对齐：**AI augment, human accountable for decisions**。边缘 case 默认行为：**不确定 → 升给人审批**（symmetric with Supervised mode）。

**与 proj-experts + proj-shape 的衔接**（对应 PMP Business Case → Charter 转换）：

| 阶段 | PMP 对应 | 本体系 skill |
|------|---------|-------------|
| 商业论证（专家分析 / 备选方案 / 多轮决策收敛）| Initiating · Business Case | `proj-experts` + `proj-shape` → 输出 `DECISIONS.md` `ready-for-implementation` |
| 项目化落地规划 | Initiate（charter）+ Plan（rolling）+ 规划侧 M&C + 阶段 Close | **`proj-plan`（本 skill）** |
| 执行 | Execute | 对话 / 未来 execute skill（INV-04 故意外置） |

体系结构对应 [APM 开源框架](http://github.com/sdi2200262/agentic-project-management) 的 Planner（best-minds + discuss）/ Manager（pmo）/ Workers（execute）三角色。

## 规划原则 · JIT（恰好足够 / 在对的时间规划）

> **行为原则**（ORD-27；与模式 T/F 正交）。「JIT」是本 skill 借用的**类比**（取自 JIT 编译）；行业出处 = PMBOK **rolling wave planning** / **progressive elaboration**（[PMBOK 6 §6.2.2.3](https://www.oreilly.com/library/view/q-as/9781628254624/a_chapter06.xhtml)、[progressive elaboration](https://www.projectmanagement.com/wikis/295452/progressive-elaboration)）+ Lean **Last Responsible Moment**（[Poppendieck](https://blog.codinghorror.com/the-last-responsible-moment/)）。

**原则**：每个规划细节**推迟到「再不展开就会因缺信息而被迫默认决策」的那一刻**才展开（LRM 判据 = 不决策的代价 > 等待的收益）；不做超前的细节规划。

**边界（防滥用 · 必读）**：

| | 对象 | 处理 |
|---|------|------|
| **适用**（可推迟）| 细节展开深度、可逆决策（phase plan 任务表、WBS L3+ 分解） | 推迟到 LRM |
| **非适用**（故意提前）| 范围骨架（WBS L1–L2）、阶段骨架（phase-roadmap）、授权（charter）、不可逆决策 | 早定——LRM 明示「late commitment 不得退化为 no commitment」 |

**推迟 ≠ 省略 artifact**：JIT 约束的是*展开时机与深度*，不是*是否产出该 artifact*（否则撞 §失败模式「仅 WBS 无 phase-roadmap → 不完整」）。

### 在飞工作量控制（ORD-52 · 执行侧）

> **证据强度声明（必读）**：本条依据 [Kanban Guide](https://kanbanguides.org/english/) 的规范要求 + 用户自述症状，**无本项目实测数据**（讨论侧有实测：图谱线停滞 15 轮）。按 ORD-51 的教训——**无机器检查的界较弱**——本条为**纪律级**，刻意不进 validator（proj-plan 服务任意项目，本仓库 validator 够不着其 `docs/pmo/`）。若日后出现执行侧实测数据，再考虑升级。

- **WIP 单位** = 同时处于「进行中」的 phase 数（brownfield 另含 WBS 三态里的 `进行中` 项）。
- **控制方式**：rolling wave 本就隐含「一次展开一个 phase」；本条把它**显式化为一个数字**并写进 `wbs.md` / `phase-roadmap.md` 表头——**写在使用点上**（ORD-51 实测：可数的数字写在使用点的约束 51 天零违反，定性措辞写在别处的涨了 4.21 倍）。**默认 1**，项目可自定。
- **例外条款（= 中断协议 · 一次性写入，非每轮成本）**：允许插入新工作，但被中断的 phase / WBS 项**必须显式置为「暂停」并在 `change-log.md` 记一行**（何时中断、被什么中断、恢复条件）。**禁止静默搁置。**
- **不做的事**：不新增 artifact、不新增人读文件（INV-01 的 ≤5 不动）、不设审批流。

本原则**解释**既有结构：INV-02（细任务仅在 phase plan）、phase-roadmap「无任务表」、WBS 仅 L1–L2、"L3+ rolling 进 phase plan" 均为 rolling wave 的实现。与裁剪轴正交——**模式 T/F 管「做哪些 artifact」（广度轴）；JIT 管「每个 artifact 何时展开到多深」（时间/深度轴）**。

## 立场声明（借鉴 / 自创）

> 让用户与 agent 能逐条判断"这是行业标准 / 借鉴 / 本 skill 自创"。**未在此声明的术语不应被当作 PMI / SDD 行业标准。**

### 基准版本（借鉴的真实标准）

| 来源 | 用于 | 出处 |
|------|------|------|
| **PMBOK 6**（5 Process Groups + 10 Knowledge Areas, 49 processes） | 过程覆盖矩阵基准（见 `docs/discuss/05-idea-pmo-pmp-coverage-rereview.md`；历史文件名沿用旧 skill 名 idea-pmo，不改） | PMBOK Guide 6th Edition (PMI, 2017) |
| **PMBOK 7** Tailoring 原则（4 步骤） | Coach hybrid 裁剪流程的依据 | [PMI Tailoring PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) |
| **PMBOK 8** AI Appendix | 人 / AI 责任分工原则 | [AI in PMBOK 8 Guide](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence) |
| **GitHub Spec Kit**（SDD） | 借鉴 constitution-as-guardrail / gate / analyze **三个机制**（**非命令名映射**） | [spec-driven.md @ spec-kit](https://github.com/github/spec-kit/blob/main/spec-driven.md)；详见 [pmp-sdd-map.md](assets/pmp-sdd-map.md) |
| **Agentic PM 学术框架** | 角色分工对应 Supervised-AI mode；体系对应 APM Planner/Manager/Workers | [arXiv 2601.16392](https://arxiv.org/html/2601.16392v1)、[APM 开源框架](http://github.com/sdi2200262/agentic-project-management) |

### 本 skill 自创术语（**不是** PMI / SDD 标准）

| 术语 | 含义 | discuss 出处 |
|------|------|------|
| **Coach hybrid** | Coach 模式 tailoring 流程（对接 PMBOK 7 tailoring 4 步骤但简化为 T/F 二选一 + 用户 GATE-0） | `docs/discuss/02-ai全量pmp与智能裁剪.md` §O2、O3；DECISIONS.md ORD-04 |
| **模式 T / F** | T = Tailored Minimum；F = Full（对接 PMBOK 7 "just enough process"）| `docs/discuss/02-…md`；DECISIONS.md ORD-04 / ORD-06 |
| **GATE-0 / 1 / 2 / N** | manifest 上的人工审批节点编号（借鉴 Cooper stage-gate + Spec Kit `type: gate`；编号体系本 skill 自创） | `docs/discuss/02-…md`；DECISIONS.md INV-03 |
| **human-read-manifest（≤5）** | 限定人类必读 artifact ≤5 的清单（对接 PMBOK 8 "AI augment" 立场的具体执行机制） | `docs/discuss/02-…md`、`03-…md`；DECISIONS.md INV-01 / ORD-05 / ORD-09 |
| **Round A / B** | 双轮启动（Initiate / Plan）（对接 PMBOK Initiating + Planning Process Group 的本 skill 自创双轮结构）| `docs/discuss/02-…md`；DECISIONS.md ORD-03 |

### 故意刻意不做（边界声明 · ORD-10）

proj-plan PMP **覆盖边界** = Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close；**不含**：

- **Execute Process Group**（10 过程；INV-04 故意外置——由对话 / 未来 execute skill 承担）
- **成本管理**（4 过程；01 轮刻意省略）
- **采购管理**（3 过程；01 轮刻意省略）
- **定量风险分析、CPM/甘特、资源平衡、逐任务 RACI、正式 CCB**（01 轮刻意省略）
- **全量 WBS 词典 L3+**（rolling 进 phase plan 而非启动期）

详见 [pmp-sdd-map.md](assets/pmp-sdd-map.md) + `docs/discuss/05-idea-pmo-pmp-coverage-rereview.md`（历史文件名沿用旧 skill 名，不改）。

## PMP 计划 ≠ 仅 WBS

| 层 | 回答 | artifact | 何时写 |
|----|------|----------|--------|
| 范围 | 做什么 | `wbs.md` + charter | Round B · GATE-2 |
| 进度（粗） | 分几段、依赖、里程碑 | `phase-roadmap.md` | Round B · GATE-2（**无任务表**） |
| 整合 | 子计划索引 | `integration-plan.md` | Round B · GATE-2 后 |
| 进度（细） | 活动、执行者、依赖 | `phase-NN/plan.md` | 进阶段 · GATE-3 |
| 变更 | 整体变更控制 | `change-log.md` | T 默认；Round B 起 |

详见 [assets/pmp-sdd-map.md](assets/pmp-sdd-map.md)。

## 与商业论证层 + 执行层的职责边界

> 高层衔接已在 §设计 vision 给出；本节为具体职责边界。

| | `proj-experts` + `proj-shape`（商业论证层）| **proj-plan（本 skill · 规划层）** | `proj-run`（执行层） |
|---|---------------------------------------------|--------------------------------------|---------------------|
| PMP 对应 | Initiating · Business Case | Initiating · Charter + Planning + 规划侧 M&C + Closing | Executing |
| 问题 | 谁最懂？事实是什么？试什么？决定是什么？ | 怎么授权？怎么分解？怎么分阶段计划？ | 谁/什么模型/怎么 dispatch？validation 怎么跑？|
| 产出 | `docs/discuss/`（轮次 + `DECISIONS.md`）| `docs/pmo/`（charter / WBS / phase plans / ...）| `phase-NN/acceptance.md` + `.cursor/agents/*.md`（可选）|
| 边界 | 不写 PM artifact | **不写**新 INV / ORD；**不写**代码 / 执行（INV-04）| 不写新 INV / ORD；不写计划；不规划 model 选择策略 |

## Brownfield 接管入口（ORD-26）

> 接管历史项目时，**上游不是 DECISIONS 而是 `proj-survey` 的规划交接** `docs/survey/*-handoff.md`（intent 可信重建 → 可 plan 分支的产物）。本节是 proj-plan 的第二入口。

| 来源 | 进 proj-plan 的去向 |
|------|---------------------|
| handoff §**既成约束（已完成）** | 写入 `charter.md`「背景/现状」+ WBS 标 **`已完成`**（三态），**不重新规划** |
| handoff §**未完成工作** | WBS 标 **`待做`/`进行中`**（三态）→ phase-roadmap 划分 |
| handoff §成功标准 / 范围边界 | charter 验收基线（替代 DECISIONS 的成功标准）|
| handoff §已知风险 / 待验证 | risk-register（F）/ 登记为待跑 EXP |

**WBS 三态（ORD-26 · 仅 brownfield）**：每个 WBS 项标 `已完成 / 进行中 / 待做`；**`已完成` 项是既成约束**，phase-roadmap 与 phase plan **不得**把它当新工作（否则违反"接管"语义）。greenfield 项目无此列。

**自动 + GATE**：proj-survey baseline 自动生成、人在 GATE-S 已审批分支；proj-plan 这里**直接消费 handoff**，正常走 Round A → GATE-0（不重复 survey 的盘点）。handoff 缺失成功标准/范围边界等关键字段 → 回 proj-survey 或与人补齐，**不**自行臆造。

## 案例库 / 跨项目学习闭环（ORD-36）

> proj-* 的**慢/外层双环学习反馈**：项目经验 → 案例 → 被未来项目消费 → 必要时回头修订 `INV/ORD/skill`。捕获 + 消费由本 skill **既有职责扩展**承载（不新增 skill）：**阶段 Close 捕获 / Round A 消费**。集中库在 proj-* skills 仓库 `docs/cases/`（[库说明](../../docs/cases/README.md) · [模板](assets/case-template.md)）。

| 端 | 落点 | 动作 |
|----|------|------|
| **捕获**（Close）| 末阶段 `review.md` §经验教训之后 | **AI 从本项目 `DECISIONS.md` + `change-log.md` + `review.md` 派生案例草稿 + 人审** → 写入 `docs/cases/NN-{项目}.md`（用 case-template）|
| **消费**（Initiate）| Round A 读 `DECISIONS` 时 | 查阅案例库**相似类型**案例 → 带入 charter / 风险 / ORD；**回填被消费案例 §消费记录**（闭环证据）|

**纪律**（防 write-only · 头号失败模式）：① 案例 §消费记录 为空 = 未闭环；② 每案例必填 §治理变量检视（Argyris 双环：至少检视一条 INV/ORD/skill 该不该改，否则是只改 checklist 的假学习）。**自动化边界**：仅做「AI 派生草稿 + 人审」；全自动总结 / CBR 相似度检索引擎暂不做（YAGNI · 待案例累积 + 闭环证成）。

## Sub-agent dispatch manifest（对 proj-run 的承诺字段 · ORD-15）

> 本 skill 的 `phase-NN/plan.md` 模板**新增可选段** `## Sub-agent dispatch manifest`，作为对下游 `proj-run` skill 的承诺字段（类比 proj-shape → proj-plan 的 `DECISIONS.md` 承诺）。
>
> **本 skill 仅负责"列清单"**（artifact-level 契约），**不负责** model 选择、Cursor `.cursor/agents/*.md` 生成、validation 执行（属 proj-run 域，违反 INV-04）。

### Manifest 段最小字段

| 字段 | 必备程度 | proj-run 用途 |
|------|---------|---------------|
| 适合 sub-agent 的 task ID 列表 | 必填 | 决定调度范围 |
| 每条 task 的 **specialist 类型**（如 `reviewer` / `coder` / `auditor` / `explorer`）| 必填 | 决定 sub-agent 角色 + cursor `.cursor/agents/<name>.md` 模板选择 |
| 每条 task 的 **validation criteria**（如 lint 命令 / test 命令 / 输出格式校验）| 必填 | validation gate 判据 |
| iteration budget（最大重试次数）| 必填 | 防止 validation 反复失败的兜底 |
| **不**指定具体 model 名 | — | 留给 proj-run 按用户 plan 类型 + cost-quality 取舍决定 |

> **完整模板见 EXP-04 试跑后定**（v0 阶段 manifest 段可选，不强制；EXP-04 passed 后升级为强制段）。

### artifact-index 扩展

`artifact-index.md` schema **扩展段**，登记 sub-agent 产出的 artifact，避免 source of truth 分裂（INV-03 精神）。具体 schema 同样待 EXP-04 试跑后定。

## 项目目录结构

```text
docs/pmo/
├── project-context.md
├── tailoring-decision.md
├── initiation-charter.md
├── human-read-manifest.md       # 人类必读（≤5）+ GATE
├── charter.md                   # Round B · GATE-1
├── wbs.md                       # Round B · GATE-2
├── phase-roadmap.md             # Round B · GATE-2（粗进度，无任务表）
├── integration-plan.md          # Round B · 整合索引（PMP 项目管理计划入口）
├── change-log.md                # T 默认 · 整体变更控制
├── artifact-index.md            # AI · SDD truth source
├── risk-register.md             # TR-02 / F
├── stakeholder-register.md      # TR-03 / F
├── communication-plan.md        # TR-03 / F
├── quality-plan.md              # F 按需
├── phase-01/
│   ├── plan.md                  # rolling · GATE-3
│   ├── acceptance.md
│   └── review.md
└── README.md
```

## 不可违背

| ID | 要点 |
|----|------|
| INV-01 | 人只读 manifest（≤5） |
| INV-02 | 细任务**仅**在 `phase-NN/plan.md`；`phase-roadmap.md` **不得**含任务表 |
| INV-03 | manifest GATE 未过 → **禁止**下游 artifact |
| INV-04 | **不含执行**（含不启动 sub-agent） |
| ORD-09 | Round A 人类必读**固定 2 项** |

## SDD 纪律（机制层借鉴自 [Spec Kit](https://github.com/github/spec-kit/blob/main/spec-driven.md)）

> **借鉴 Spec Kit 的机制**（constitution-as-guardrail、gate、analyze），**不映射命令名**（详见 [pmp-sdd-map.md](assets/pmp-sdd-map.md) §SDD 借鉴）。

| 本 skill 机制 | 对应 Spec Kit 概念 | 实现 |
|--------------|-------------------|------|
| Source of truth | constitution (`memory/constitution.md`) | `DECISIONS` + `artifact-index` + `integration-plan` |
| Gate | `type: gate`（[workflow 人工审批节点](https://github.github.com/spec-kit/reference/workflows.html)）| manifest GATE-0 / 1 / 2 / N |
| Analyze | `/speckit.analyze`（cross-artifact 一致性 & 覆盖校验）| [assets/analyze-checklist.md](assets/analyze-checklist.md) — Round B 后、每阶段 acceptance 前 |
| 禁止越权 | constitution 不可推翻、gate 必经 | GATE 未过不得生成下游；analyze 失败不得标 GATE 通过 |

## Coach hybrid（裁剪）

> **本 skill 自创术语**（DECISIONS.md ORD-04；非 PMI 标准）；对接 [PMBOK 7 tailoring 4 步骤](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf)（Select Approach → Tailor for Org → Tailor for Project → Inspect & Adapt）。Coach hybrid = 简化为「T / F 二选一 + 用户 GATE-0 确认」的 tailoring 决策流程；遵守 PMBOK 7「deliberate choice, not anything goes」原则。

1. 读 [assets/tailoring-rules.md](assets/tailoring-rules.md) + `DECISIONS` + `project-context.md`。
2. 写 `tailoring-decision.md`：建议模式 T/F、产物清单、规则 ID。
3. **GATE-0**：用户确认；agent **不得**单方面定模式。

> **拍板前 teach-back（ORD-44）**：GATE-0/1/2/3 交人确认前，AI 用 1–3 句复述「当前要拍什么 + 拍下去的后果」，人核对无误后再拍板；复述有偏先纠正。只在拍板点使用，全程使用 = 啰嗦。

| 模式 | Round B 生成 |
|------|--------------|
| **T** | charter, wbs, phase-roadmap, **integration-plan**, **change-log**, artifact-index |
| **F** | 上列 + risk, stakeholder, communication, quality-plan（按需） |

## 工作流

### 0. 前置

- **入口二选一**：(a) `DECISIONS.md` 为 `ready-for-implementation` 或用户显式授权；(b) **brownfield**：`proj-survey` handoff `docs/survey/*-handoff.md`（见 §Brownfield 接管入口）。
- 确保 `docs/pmo/` 存在。

### Round A · Initiate

1. `project-context.md` → `tailoring-decision.md` → `initiation-charter.md`
   - **brownfield**：`project-context.md` 标项目类型=接管 + 引 handoff；charter「背景/现状」纳入 handoff §既成约束
   - **案例库消费（ORD-36）**：查阅 `docs/cases/` 相似类型案例，把可复用建议带入 charter / 风险；回填被消费案例 §消费记录
2. `human-read-manifest.md`：**[Round-A] 固定 2 项** + 预留 GATE 槽位（≤5）
3. **GATE-0** 用户确认

### Round B · Plan

1. 定稿 `charter.md` → manifest **GATE-1**
2. 用户确认 GATE-1 → 并行写：
   - `wbs.md`（L1–L2，**无**阶段顺序表；**brownfield 须标三态** `已完成/进行中/待做`，已完成项为既成约束不重新规划 · ORD-26）
   - `phase-roadmap.md`（阶段、里程碑、WBS 映射、依赖；**无任务表**）
3. 用户确认 GATE-2 → 写：
   - `integration-plan.md`（子计划索引）
   - `change-log.md`（空表头即可）
   - 按 TD：`risk-register` / `stakeholder` / `communication` / `quality-plan`（F 或 TR 命中）
   - `artifact-index.md`
4. 运行 **analyze**（[analyze-checklist.md](assets/analyze-checklist.md)）→ 更新 artifact-index 校验节
5. **仍不写** `phase-NN/plan`，直至进阶段

### Rolling · 阶段规划

1. 写 `plan.md` + `acceptance.md` → **GATE-3** 用户确认
2. 执行（**非本 skill**）→ acceptance 前 **analyze**
3. `review.md`：含 **circuit breaker**、lessons learned、末阶段收尾检查
   - **末阶段案例捕获（ORD-36）**：AI 从本项目 `DECISIONS`+`change-log`+`review.md` 派生跨项目案例草稿（[case-template](assets/case-template.md)）+ 人审 → 写入 `docs/cases/`
4. acceptance **不通过** → **禁止**下阶段 plan；EXP failed → 回 proj-shape
5. 回写 `DECISIONS` EXP；变更记 `change-log`

### Circuit breaker（硬规则）

| 事件 | 动作 |
|------|------|
| acceptance 不通过 | 不得创建下一 `phase-NN/plan` |
| analyze 失败 | 不得标记 GATE 通过 |
| 推翻 ORD/INV | change-log + **proj-shape** |

### Agent / Sub-agent（规划侧）

- plan 任务表支持 `AI` / `人工` / `subagent:{角色}`
- Handoff 字段见 [assets/agent-handoff.md](assets/agent-handoff.md)
- **本 skill 只写 handoff，不启动 sub-agent**（INV-04）

### 时间预估（ORD-07）

| 执行者 | plan.md |
|--------|---------|
| AI / subagent | 不写人工时长 |
| 人工 | 标注预估 |

## human-read-manifest

| 规则 | 说明 |
|------|------|
| 硬上限 | 5 项 |
| Round A | 固定 2 项（ORD-09） |
| Round B | + GATE-1、GATE-2 → 满 5 |
| 进阶段 | GATE-3 可滚动替换槽位；integration/change-log **不要求人读** |

## 失败模式

- 跳过 Round A / GATE-0
- 仅 WBS 无 phase-roadmap / integration-plan → 计划不完整
- phase-roadmap 含任务表 → 违反 INV-02
- 跳过 analyze 即标 GATE 通过
- acceptance 未过仍开下阶段
- 要求人读 artifact-index 或全量树
- 在本 skill 内执行或启动 sub-agent

## 模板索引

| 文档 | 模板 |
|------|------|
| PMP × SDD 对照 | [assets/pmp-sdd-map.md](assets/pmp-sdd-map.md) |
| 裁剪规则 | [assets/tailoring-rules.md](assets/tailoring-rules.md) |
| Analyze | [assets/analyze-checklist.md](assets/analyze-checklist.md) |
| Agent handoff | [assets/agent-handoff.md](assets/agent-handoff.md) |
| 项目上下文 | [assets/project-context-template.md](assets/project-context-template.md) |
| 裁剪决策 | [assets/tailoring-decision-template.md](assets/tailoring-decision-template.md) |
| 启动章程草案 | [assets/initiation-charter-template.md](assets/initiation-charter-template.md) |
| 人类必读清单 | [assets/human-read-manifest-template.md](assets/human-read-manifest-template.md) |
| 项目章程定稿 | [assets/charter-template.md](assets/charter-template.md) |
| WBS | [assets/wbs-template.md](assets/wbs-template.md) |
| 阶段路线图 | [assets/phase-roadmap-template.md](assets/phase-roadmap-template.md) |
| 整合计划索引 | [assets/integration-plan-template.md](assets/integration-plan-template.md) |
| 变更日志 | [assets/change-log-template.md](assets/change-log-template.md) |
| 风险登记 | [assets/risk-register-template.md](assets/risk-register-template.md) |
| 干系人登记 | [assets/stakeholder-register-template.md](assets/stakeholder-register-template.md) |
| 沟通计划 | [assets/communication-plan-template.md](assets/communication-plan-template.md) |
| 质量计划 | [assets/quality-plan-template.md](assets/quality-plan-template.md) |
| 产物索引 | [assets/artifact-index-template.md](assets/artifact-index-template.md) |
| 阶段 plan | [assets/plan-template.md](assets/plan-template.md) |
| 验收 | [assets/acceptance-template.md](assets/acceptance-template.md) |
| 评审 | [assets/review-template.md](assets/review-template.md) |
| 跨项目案例（ORD-36 · 案例库 `docs/cases/`）| [assets/case-template.md](assets/case-template.md) |

## 触发词

proj-plan · 项目章程 · WBS · phase-roadmap · integration-plan · change-log · analyze · GATE · tailoring · sub-agent

## 不触发本 skill

- 尚无 DECISIONS / 讨论未就绪 → proj-shape
- 只要一次性改代码 → 直接执行
