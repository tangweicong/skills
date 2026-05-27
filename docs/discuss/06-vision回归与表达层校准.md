# 06-vision回归与表达层校准

> **2026-05-27 命名变更注记（轮次 07 决定）**：skills 集体重命名：`best-minds-grounded` → `proj-experts`、`idea-discuss` → `proj-shape`、`idea-pmo` → `proj-plan`；新增 `proj-run`（执行调度，骨架版）。本文档作为历史快照沿用讨论时的旧名，**正文不动**；引用时按上表换算。完整说明见 `07-sub-agent-model-tier-编排.md`。

| 字段 | 值 |
|------|-----|
| 轮次 | 06 |
| 主题 | vision 回归与表达层校准（不推翻前 5 轮决定） |
| 日期 | 2026-05-27 |
| 状态 | confirmed · synced（DECISIONS.md + skills/idea-pmo 已落实 ORD-10~14 + ORD-04 修订 @ 2026-05-27）|
| 讨论方法 | `best-minds-grounded` |
| 写入格式 | 完整 |
| 承接 | 前 5 轮（INV-01~04、ORD-01~09、EXP-01~03、ORD-10 pending） |

## 用户输入（本轮）

用户原话（摘要）：

> 本意是想用 PMP 流程约束 AI 工作流，AI 当主力执行任何"可项目化"的事情；人作为项目发起人，只提供初始的模糊想法和关键决策，而不用自己管理繁重的项目管理细节文件和过程。
>
> 用户自己有 PMP 证书但作为程序员从未实践 PM，所以懂理论但不懂落地细节。
>
> 引入 SDD 是因为 PMP 注重文档 + SDD 也注重文档 + PMP 过程符合 harness 思想 → 自然结合。
>
> 保留 best-minds-grounded 和 idea-discuss（对应 PMP 商业论证过程）。
>
> "在实际使用过程中，总感觉心理没底，但具体说不上来有什么问题"。

**本轮范围（用户已确认）**：vision-grounded re-anchoring，不推翻前 5 轮已确立决定；新增/修订少数 ORD 让 SKILL.md 在表达层显化原始 vision。

## 事实与假设

### 轻量框定（查证前问题清单）

| # | 待查问题 | 查证结论（摘要） |
|---|----------|------------------|
| Q1 | PMI 公开材料里"sponsor + agent-as-PM"或"AI-assisted PM"是否已有讨论？术语是什么？ | ✓ Sponsor 是 PMI 标准角色（owns business case, go/no-go, value）；PMBOK 8 有 AI Appendix，立场 "AI augment, PM accountable" |
| Q2 | SDD harness 思想的真实出处？ | ✓ Spec Kit `spec-driven.md` 明确 Constitution = "architectural DNA / guardrails / putting walls"；harness 表述有据 |
| Q3 | PMBOK 7 "Tailor based on context" 章节对"小项目最小裁剪"的具体指导？ | ✓ PMI 官方 4 步骤；强调 "deliberate choice, not anything goes"；与 ORD-04 Coach hybrid 完全对齐 |
| Q4 | "AI as project manager" 公开实践？ | ✓ arXiv 2601.16392（2026/1）提 4 autonomy modes；APM 开源框架已实现 Planner/Manager/Workers 三角色——本项目 vision 不是孤例 |

### 已查证事实

1. **PMI Sponsor 定义**：sponsor 是 "an individual or group that provides resources and support for a project, program, or portfolio and is accountable for its success"；责任包括 own business case、define success criteria、make go/no-go calls、approve deliverables、ensure value。来源：[PMI Project Sponsorship](https://www.pmi.org/learning/library/importance-of-project-sponsorship-9946)

2. **PMBOK 8 AI Appendix 立场**：AI = decision-support tool, augment not replace；PM remains accountable for decisions（即使 AI-informed）；governance 须处理 AI 特定风险（bias / transparency / data privacy）。来源：[AI in PMBOK 8th Edition](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence)

3. **Spec Kit Constitution 真实定位**："architectural DNA of the system... transforms AI from a code generator into an architectural partner that respects and reinforces system design principles"；"putting walls around the application... stay within these boundaries at all times"。来源：[spec-driven.md @ github/spec-kit](https://github.com/github/spec-kit/blob/main/spec-driven.md)、[CodeStandUp Spec Kit Tutorial 02](https://codestandup.com/posts/2025/github-spec-kit-tutorial-constitution-command/)

4. **PMBOK 7 Tailoring 4 步骤**：Select Initial Development Approach → Tailor for Organization → Tailor for Project → Implement Ongoing Improvement。强调 "just enough process" 和 "deliberate, conscious process of choosing"，**反对** "anything goes"。来源：[PMI Tailoring PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf)

5. **Agentic PM 学术框架**：4 autonomy modes — Guided AI-autonomy、Supervised-AI、Human-AI Collaborative、AI-assisted；根据 task complexity + risk level 选模式；人 PM 演化为 "ethical strategic leader / coach"。来源：[arXiv 2601.16392 - Toward Agentic Software Project Management](https://arxiv.org/html/2601.16392v1)

6. **APM 开源框架**：三角色架构 Planner（spec/plan/rules）/ Manager（coordinate）/ Workers（execute）。来源：[github.com/sdi2200262/agentic-project-management](http://github.com/sdi2200262/agentic-project-management)

7. **前 5 轮历史确认**：INV-01~04、ORD-01~09 均经多轮讨论确立并试跑（EXP-01/02 passed）；EXP-03（模式 F 试跑）pending；ORD-10（PMP 覆盖边界声明）05 轮草案待确认。来源：`01-…md` ~ `05-…md` + `DECISIONS.md`

### 推理（非事实、非待验证）

> 本节按 best-minds-grounded【模拟推理】档；下方"方法专属输出"展开三视角

- **推理 · 模拟推理 · PMBOK 7+8 立场**：用户 vision 在 PMBOK 框架下可重新表达为"人扮演 Sponsor + PM 决策权合体角色；AI 扮演 PM 执行角色 + analyst + artifact 维护"——这跟 PMBOK 8 "AI augment, PM accountable" **不冲突**，只是把 PM 角色拆分了。依据 [PMI Sponsor URL](https://www.pmi.org/learning/library/importance-of-project-sponsorship-9946) + [PMBOK 8 AI URL](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence) 的 sponsor 责任清单 + AI augmentation 原则。

- **推理 · 模拟推理 · Spec Kit 范式**：SDD harness 从 dev 域到 PM 域的迁移是合理的——关键映射是 Constitution↔DECISIONS.md INV、gate↔manifest GATE、analyze↔analyze-checklist。但**不应做命令 1:1 映射**——spec-kit 是 feature-level，idea-pmo 是 project-level，借鉴的是机制不是命令名。依据 [spec-driven.md @ spec-kit](https://github.com/github/spec-kit/blob/main/spec-driven.md) 的 "constitution as architectural DNA" 原则。

- **推理 · 模拟推理 · Agentic PM 学术派**：用户体系在 4 modes 中对应 **"Supervised-AI mode"**（AI 做、人审批）；idea-discuss + idea-pmo + execute 的三 skill 拆分**结构上对应** APM 的 Planner/Manager/Workers 三角色——这是已被学术和开源界探索的方向。依据 [arXiv 2601.16392](https://arxiv.org/html/2601.16392v1) 4 mode 框架。

### 待验证 / 未查证

- 无新待验证项（EXP-03 维持 pending，承接自 05 轮）

### 方法专属输出（best-minds-grounded · 三视角）

#### 视角 A · PMI / PMBOK 7+8 立场

**选用理由**：本题核心争议轴是"AI 主力 PM" vs "PM accountable"；PMI 是 PMP/PMBOK 标准制定方，对该轴有权威立场——且 PMBOK 8 已专门设 AI Appendix。比"泛 PM 专家"更直接对题。

**【原话】**：未引用——PMBOK 8 AI Appendix 全文未在公开 URL 找到逐字版本；按 #7 不强引用。

**【已公开立场】**：

1. **Sponsor 角色定义**：PMI 立场——sponsor "owns the business case, defines success criteria, makes go or no-go calls, approves deliverables, ensures the project delivers intended value"。[源](https://www.pmi.org/learning/library/importance-of-project-sponsorship-9946)

2. **AI 与 PM 责任**（PMBOK 8）：AI 是 decision-support tool，**augment** PM judgment；PM **remains accountable** for all decisions（即使 AI-informed）；治理框架须处理 AI 特定风险（bias、transparency、data privacy）。["AI in PMBOK 8" guide](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence)

3. **Tailoring 不是 anything goes**：PMBOK 7 强调 tailoring 是 "deliberate, conscious process of choosing the right processes and tools for the job, not abandoning process altogether"。[PMI Tailoring PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf)

**【模拟推理】**：

依据上述立场推导，**PMI 派会建议**：

- 用户 vision "AI 主力 PM + 人 sponsor" 应**重新表达**为：
  - 人 = **Sponsor + PM 决策角色合体**（business case、go/no-go、approve、关键决策、GATE 审批）
  - AI = **PM 执行角色**（charter 扩写、WBS 维护、phase plan 生成、analyze 运行；artifact 维护）
- 这种表达**没有违背** PMBOK 8 "PM accountable" 原则——因为"人"承担了 PM 的 accountable 部分
- ORD-04 Coach hybrid + 模式 T/F 对接 PMBOK 7 tailoring 4 步骤（**完全合规**）；只需在 SKILL.md 显式声明这个对接

**关切 → 路径**（按 best-minds-grounded #10 建设性优于否定）：

- **关切**：表达层若写"AI 主力 PM"易被误读为"AI 取代 PM"，违背 PMBOK 8 立场
- **达成原目标的路径**：
  1. SKILL.md vision 段写"人保留 Sponsor + PM 关键决策；AI 承担 PM 执行 + artifact 维护"
  2. 明确"AI 不做关键决策"——所有 GATE 是人审批
  3. 加 PMBOK 8 AI Appendix URL 出处

#### 视角 B · SDD / Spec Kit 作者范式

**选用理由**：本题核心争议轴是"用 SDD 约束 AI 的 harness 思想"；Spec Kit 作者团队是 SDD 范式的主要倡导者，对该轴有第一手设计意图。比"泛 AI 工具评论者"更直接对题。

**【原话】**：

> "raw AI generation without structure produces chaos. SDD provides that structure through specifications and subsequent implementation plans that are precise, complete, and unambiguous enough to generate working systems. The specification becomes the primary artifact. Code becomes its expression."
>
> — [spec-driven.md, github/spec-kit](https://github.com/github/spec-kit/blob/main/spec-driven.md)

> "The constitution... acts as the **architectural DNA** of the system... transforms AI from a code generator into an architectural partner that respects and reinforces system design principles."
>
> — 同上

**【已公开立场】**：

1. SDD 核心：spec is primary artifact, code/implementation is expression
2. Constitution 角色：non-negotiable principles that **trump all other instructions**（CodeStandUp tutorial: "anything in the constitution should trump all other instructions, because those are your non negotiable principles"）
3. gate/analyze 机制：Spec Kit 工作流原生支持 `type: gate`（人工审批）+ `/speckit.analyze`（cross-artifact consistency & coverage）

**【模拟推理】**：

依据上述立场推导，**SDD 范式作者会指出**：

- Spec Kit 是 **feature-level 代码生成**工具（每次跑一个 feature），不是 project-level 治理框架——把它当 PMP 工具用是范畴错误
- 但 SDD 的**机制层面**（spec-as-truth、constitution-as-guardrail、gate、analyze）是范式无关的——迁移到 PM 域是合理探索
- **正确的借鉴方式**：
  - DECISIONS.md INV ↔ Constitution（不可推翻原则）
  - manifest GATE-N ↔ Spec Kit `type: gate`（人工审批节点）
  - analyze-checklist ↔ `/speckit.analyze`（cross-artifact 一致性校验）
  - artifact-index ↔ spec-anchored truth source
- **错误的借鉴方式**：命令名 1:1 映射（specify→discuss、plan→charter、tasks→phase-plan）——这是 `pmp-sdd-map.md` 当前的写法，跟 05 轮"借鉴机制"的精神矛盾

**关切 → 路径**：

- **关切**：`pmp-sdd-map.md` 当前用 SDD 命令名做 1:1 映射会误导用户/agent，以为"idea-pmo = Spec Kit on PM"
- **达成原目标的路径**：
  1. 修订 `pmp-sdd-map.md`：拆成「PMBOK 借鉴」「SDD 借鉴（机制层）」「本 skill 自创」三段
  2. SDD 借鉴段明确"借鉴的是 constitution-as-guardrail、gate、analyze 三个机制；**不映射命令名**"
  3. 加 [spec-driven.md URL](https://github.com/github/spec-kit/blob/main/spec-driven.md) 作为出处

#### 视角 C · Agentic PM 学术 / APM 开源范式

**选用理由**：本题核心争议轴是"AI 当主力 PM 是否可行 / 已有先例"；arXiv 2601.16392 是 2026/1 的最新学术 vision paper，APM 是已运行的开源框架——比"通用 AI 评论者"更直接对题，且能回答用户的"我是不是意淫"焦虑。

**【已公开立场】**：

1. **arXiv 2601.16392** 提出 4 autonomy modes：
   - Guided AI-autonomy mode（AI 主，人监督）
   - **Supervised-AI mode（AI 决策，人审批）**
   - Human-AI Collaborative mode（协同）
   - AI-assisted mode（人主，AI 辅助）
   
   根据 task complexity + risk level 选模式；人 PM 演化为 "ethical strategic leader or coach"。

2. **APM 开源框架** 三角色架构：
   - **Planner** — structured project discovery + 分解为 Spec/Plan/Rules
   - **Manager** — 协调执行、分配 Task、维护项目状态
   - **Workers** — 执行特定 Task（自包含 Task Prompt + validate + report back）

**【模拟推理】**：

依据上述立场推导，**Agentic PM 学派会指出**：

- 用户 vision **不是孤例**——它对应 4 modes 中的 **Supervised-AI mode**（用户提供 vision + 关键决策，AI 执行 + 报告）
- 本项目的 three-skill 拆分**结构上对应** APM 的三角色：
  | 本项目 | APM 角色 | 对应 |
  |--------|----------|------|
  | best-minds-grounded + idea-discuss | Planner | 商业论证 + spec/plan/rules 生成 |
  | idea-pmo | Manager | 协调、维护状态、artifact 维护 |
  | execute（未来 skill 或对话） | Workers | 执行具体任务 |
- 这个结构**有学术和开源界的支持**，应在 SKILL.md 显式声明对接，让读者（包括未来的你、agent）知道这不是孤立设计

**关切 → 路径**：

- **关切**：autonomy mode 没明示，agent 在边缘 case 不知道该问还是该做
- **达成原目标的路径**：
  1. SKILL.md vision 段显式声明 **"AI in Supervised-AI mode"**
  2. 加 [arXiv 2601.16392 URL](https://arxiv.org/html/2601.16392v1) 作为参考
  3. 边缘 case 默认行为：**不确定 → 升给人审批**（符合 Supervised mode 的"AI 决策、人审批"）

#### 收敛（【模拟推理】，非任一专家原话）

三视角合并出一份**建议的 vision 声明**，供 SKILL.md 头部段落使用：

> **idea-pmo 的设计 vision**
>
> idea-pmo 借鉴 **SDD harness 范式**（spec-as-truth、constitution-as-guardrail、gate、analyze；机制层借鉴自 [GitHub Spec Kit](https://github.com/github/spec-kit)），将 **PMP 项目管理流程**（PMBOK 6 过程组 + PMBOK 7 [tailoring 原则](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) + PMBOK 8 AI 立场）落地为 **agent 可执行的工作流**。
>
> **角色分工对应 Agentic PM 框架中的 [Supervised-AI mode](https://arxiv.org/html/2601.16392v1)**：
>
> - **人 = Sponsor + PM 关键决策权**：模糊想法、go/no-go、success criteria、关键 trade-off、GATE 审批；只读 `human-read-manifest.md`（≤5 项）
> - **AI = PM 执行 + analyst + artifact 维护**：扩写 charter、维护 WBS、生成 phase plan、跑 analyze；**不做关键决策**
>
> 与 PMBOK 8 AI Appendix 立场对齐：AI augment, human accountable for decisions.
>
> 边缘 case 默认行为：不确定 → 升给人审批（symmetric with Supervised mode）。

## 讨论

### 1. "心理没底"的真实根源（修正版）

按上述三视角查证后，重新定位前 5 轮设计的真实状态：

| 维度 | 状态 | 评估 |
|------|------|------|
| 已确立的 INV-01~04、ORD-01~09 | 经 5 轮 + 试跑 | **设计本身扎实** |
| 自创术语（Coach hybrid、T/F、GATE-N） | 有 discuss 出处，合法自创 | 不是 AI 凭空编造 |
| SKILL.md 是否显化 vision | **未显化** | **真正不安源 #1** |
| SKILL.md 是否声明借鉴/自创立场 | **未声明** | **真正不安源 #2** |
| SDD 映射立场 | 05 轮已修正为"借鉴机制"，但 `pmp-sdd-map.md` 仍是命令映射 | **真正不安源 #3** |
| PMBOK 版本基准 | 未在 SKILL.md 声明 | **真正不安源 #4** |
| 真实出处 URL | 几乎缺失 | **真正不安源 #5** |
| EXP-03 模式 F 试跑 | pending | 真实债务（05 轮已识别） |

**核心诊断**：你"心理没底"不是因为设计错了，而是**设计的"为什么"和"基于谁"没有在 SKILL.md 显化**——你读自己的 skill 时找不到锚点。

### 2. 本轮新增/修订 ORD 草案

| 草案 ID | 提议 | 落实位置 | 类型 |
|---------|------|----------|------|
| **ORD-10**（承接 05 轮）| PMP 覆盖边界声明 = Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close；不含 Execute、成本、采购 | SKILL.md 头部 + pmp-sdd-map.md | 确认前轮草案 |
| **ORD-11**（新）| SKILL.md 必含 vision 声明段（见上方收敛草案）；显式声明人/AI 角色 + Supervised-AI mode | SKILL.md 头部首段（在「不可违背」之前） | 新增 |
| **ORD-12**（新）| SKILL.md 必含「借鉴 / 自创」立场声明节；自创术语明示 + discuss 出处链接 | SKILL.md 新增节 | 新增 |
| **ORD-13**（新）| 修订 `pmp-sdd-map.md`：拆为「PMBOK 借鉴 / SDD 借鉴（机制层）/ 本 skill 自创」三段；去掉命令 1:1 映射；加 URL | `assets/pmp-sdd-map.md` | 修订 |
| **ORD-14**（新）| 声明基准 = PMBOK 6 过程组 + PMBOK 7 tailoring 原则 + PMBOK 8 AI 立场；每条加 URL | SKILL.md 立场声明节 | 新增 |

### 3. 跟 best-minds-grounded + idea-discuss 的协调

用户原提："这两个对应 PMP 商业论证过程"——**确认成立**：

- **PMP Initiating Process Group** 包括 Business Case（需求分析、备选方案、可行性论证）+ Charter（正式授权）
- **best-minds-grounded**：专家视角分析、备选方案、可行性外推 → 对接 Business Case 的"备选方案分析"
- **idea-discuss**：多轮收敛 + INV/ORD/EXP + 讨论就绪判断 → 对接 Business Case 的"决策收敛"+ 进入 Charter 前的"ready"判断
- 输出 `ready-for-implementation` 状态的 DECISIONS.md → 即 Business Case 完成、可进入 Charter（idea-pmo Round A）

这个三段式分工**结构上对应**：
- APM Planner = best-minds + discuss
- APM Manager = idea-pmo
- APM Workers = execute（未来或对话）

这在 06 轮文档里要显式说明，作为对 ORD-11 的支撑论据。

### 4. 不在本轮做什么

- **不动**前 5 轮 INV/ORD/EXP 的核心内容
- **不跑** EXP-03（模式 F 试跑）——仍 pending
- **不动** 21 个 templates——等 EXP-03 跑完再评估哪些真没用
- **不改** best-minds-grounded、idea-discuss SKILL.md——本轮焦点是 idea-pmo

### 5. 落地（在本轮决定之后）

idea-pmo SKILL.md 修订工作量预估：
- 新增 vision 声明段（ORD-11）：约 15-25 行
- 新增"借鉴/自创"立场声明节（ORD-12）：约 20-30 行
- 修订 `pmp-sdd-map.md`（ORD-13）：替换约 40 行
- ORD-10/14 集成进上述节：穿插约 5 行 URL

总计约 80-100 行净增量；不动 SKILL.md 现有 INV-01~04 / ORD-01~09 / 工作流 / GATE / Coach 部分。**本轮决定通过后，落实在轮次 07 或直接修订 skill 时执行**（用户选择）。

## 可验证尝试与继续/中止

本轮无新 EXP；承接 EXP-03：

| 项 | 内容 |
|----|------|
| EXP-03 | 维持 pending；执行计划不变（虚构 TR-04 project → Round B 模式 F → 只读 manifest 验收）；本轮决定通过后**仍**为唯一未闭合开放项 |

## 本轮决定

> **同步状态**：ORD-10~14 + ORD-04 修订**已于 2026-05-27 同步至 `DECISIONS.md` 并落实到 `skills/idea-pmo/SKILL.md` + `assets/pmp-sdd-map.md`**（用户确认 Q1=全部、Q2=立即修订、Q3=sub-agent 协议暂缓）。下文条目原文不动，作为 06 轮决议存档。


### 已确定 — 原则性不变量（新增/修订）

（无 INV 变更）

### 已确定 — 普通决定（新增/修订）

> 以下 ORD-10~14 已通过用户确认（Q1=全部）并入 `DECISIONS.md`@2026-05-27。

- [x] **ORD-10**（承接 05 轮）：idea-pmo PMP 覆盖范围 = **Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close**；**不含** Execute、成本、采购；需求输入由 idea-discuss 承担。T + TR 命中即视为过程闭合；F 须 EXP-03 试跑后标定。  
  **来源**：`05-…md` §6 待确认；本轮确认；[PMI Tailoring PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf)  
  → 同步至 DECISIONS.md `ORD-10`

- [x] **ORD-11**（新）：SKILL.md 必含 vision 声明段——显式声明人/AI 角色分工 + Supervised-AI mode；vision 段为收敛草案（见 §方法专属输出 · 收敛）。  
  **来源**：`06-…md` §方法专属输出 · 收敛；用户 @本轮原话；推理 · 模拟推理 · Agentic PM 学派；依据 [arXiv 2601.16392](https://arxiv.org/html/2601.16392v1) + [PMI Sponsor](https://www.pmi.org/learning/library/importance-of-project-sponsorship-9946)  
  → 同步至 DECISIONS.md `ORD-11`

- [x] **ORD-12**（新）：SKILL.md 必含「借鉴 / 自创」立场声明节；自创术语（Coach hybrid、模式 T/F、GATE-N）显式标注"本 skill 自创"+ 链接对应 discuss 出处。  
  **来源**：`06-…md` §讨论 1；推理 · 模拟推理 · PMI 派的关切→路径；依据 best-minds-grounded #7 真实性三档标签原则  
  → 同步至 DECISIONS.md `ORD-12`

- [x] **ORD-13**（新）：修订 `assets/pmp-sdd-map.md`——拆为「PMBOK 借鉴 / SDD 借鉴（机制层）/ 本 skill 自创」三段；**去除 SDD 命令 1:1 映射**（specify/plan/tasks）；保留机制借鉴（constitution↔INV、gate↔GATE-N、analyze↔analyze-checklist）；每段加真实 URL。  
  **来源**：`05-…md` §外推 · SDD（已识别但未落实）；本轮 §方法专属输出 · 视角 B；推理 · 模拟推理 · Spec Kit 范式；依据 [spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md)  
  → 同步至 DECISIONS.md `ORD-13`

- [x] **ORD-14**（新）：SKILL.md 立场声明节包含基准版本声明——**PMBOK 6 过程组**（idea-pmo 覆盖矩阵的基准）+ **PMBOK 7 tailoring 原则**（Coach hybrid 的依据）+ **PMBOK 8 AI 立场**（人/AI 责任分工的依据）；每条加 URL。  
  **来源**：`06-…md` §方法专属输出 · 视角 A；推理 · 模拟推理 · PMI 派；依据 [PMI Tailoring PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) + [AI in PMBOK 8](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence)  
  → 同步至 DECISIONS.md `ORD-14`

### 对既有决定的修订

| 操作 | ID | 说明 | DECISIONS 变更日志 |
|------|-----|------|-------------------|
| 修订 | ORD-04 | 「Coach hybrid + GATE-0」**保留**；但显式标注"本 skill 自创术语（见 ORD-12）；对接 PMBOK 7 tailoring 4 步骤" | 本轮 |

### 待确认（下轮继续）

1. 是否一并修订 21 个 templates 的真实出处链接（README 节）？— 暂缓，等 EXP-03 结束
2. 是否新增"sub-agent 启动协议"（temp.md 的 TODO）？— 不在本轮，单独开 07 轮

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-10 | 新增（承接 05 轮草案）| ✓ 已同步（2026-05-27） |
| ORD-11 | 新增 | ✓ 已同步（2026-05-27） |
| ORD-12 | 新增 | ✓ 已同步（2026-05-27） |
| ORD-13 | 新增 | ✓ 已同步（2026-05-27） |
| ORD-14 | 新增 | ✓ 已同步（2026-05-27） |
| ORD-04 | 修订（加标注） | ✓ 已同步（2026-05-27 · 加注脚） |
| EXP-03 | 维持 pending | ✓ |

讨论状态同步：维持 **`ready-for-implementation`**（本轮新增 ORD 是表达层校准，不影响过程闭合判定）

同步完成时间：**2026-05-27**（用户 Q1=全部确认；DECISIONS.md + `skills/idea-pmo/SKILL.md` + `assets/pmp-sdd-map.md` 已落实）。

## 开放问题（本轮答复）

1. ORD-10~14 是否一并确认入表？还是逐条审核？ → **Q1=全部**（已落实）
2. 本轮决定通过后，是否立即修订 `skills/idea-pmo/SKILL.md` 和 `pmp-sdd-map.md`？ → **Q2=a 立即修订**（已落实）
3. sub-agent 启动协议（temp.md TODO）何时开启 07 轮？ → **Q3=c 暂缓**（不开 07 轮）

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-27 | vision-grounded re-anchoring；ORD-10~14 草案；不推翻前 5 轮 |
| 1.1 | 2026-05-27 | 用户 Q1=全部 / Q2=a 立即修订 / Q3=c 暂缓；DECISIONS.md + skills/idea-pmo 已落实；本文档状态 → confirmed · synced |
