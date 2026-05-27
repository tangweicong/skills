# proj-plan 立场对照（PMBOK 借鉴 / SDD 借鉴 / 本 skill 自创）

> 让用户与 agent 能逐条判断"这是 PMI 标准 / 借鉴 SDD 机制 / 本 skill 自创"。
> 本文件配合 SKILL.md §立场声明使用；详细基准与自创术语清单见 SKILL.md。

## 覆盖边界（ORD-10）

proj-plan PMP 覆盖范围 = **Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close**。

**不含**：Execute Process Group（10 过程；[INV-04](../../../docs/discuss/DECISIONS.md)）、成本管理（4 过程）、采购管理（3 过程）、定量风险分析、CPM/甘特、资源平衡、逐任务 RACI、正式 CCB、启动期全量 WBS 词典 L3+。

详见 [docs/discuss/05-idea-pmo-pmp-coverage-rereview.md](../../../docs/discuss/05-idea-pmo-pmp-coverage-rereview.md) 的 49 过程覆盖矩阵（**注**：历史文件名沿用旧 skill 名 idea-pmo，不改）。

需求 / 商业论证由 `proj-experts` + `proj-shape` 承担；执行由 `proj-run` skill 承担（见 ORD-17）。

---

## 一、PMBOK 借鉴

> 基准：PMBOK 6 过程组（覆盖矩阵）+ [PMBOK 7 tailoring 原则](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) + [PMBOK 8 AI 立场](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence)。

### PMP 计划三层（直接对应 PMBOK 6 计划层级）

| 层 | PMP 概念 | artifact | 何时写 |
|----|----------|----------|--------|
| 范围 | [创建 WBS](https://www.pmi.org/pmbok-guide-standards/foundational/pmbok)（Knowledge Area · 范围管理） | `wbs.md` + `charter.md` | Round B · GATE-2 |
| 进度（粗） | 制定进度计划（rolling wave 远期） | `phase-roadmap.md` | Round B · GATE-2（**INV-02 无任务表**） |
| 进度（细） | 定义活动 + 估时（rolling wave 近期） | `phase-NN/plan.md` | 进阶段 · GATE-3 |
| 整合 | 项目管理计划（Integration Management） | `integration-plan.md` | Round B · GATE-2 后 |
| 变更 | 实施整体变更控制（M&C · Integration） | `change-log.md` | T 默认；Round B 起 |

**WBS alone 不够**；T 模式最小集 = WBS + roadmap + rolling plan + integration 索引。

### Process Group × skill 边界（PMBOK 6 五过程组）

| Process Group | proj-plan | 执行方 |
|---------------|----------|--------|
| Initiating | Round A + charter | proj-plan |
| Planning | Round B + rolling phase | proj-plan |
| Executing | ✗ | 对话 / execute skill（INV-04） |
| Monitor & Control | acceptance / review / change-log / analyze | proj-plan |
| Closing | review + close checklist | proj-plan |

### 角色对应（PMBOK 8 + Agentic PM 框架）

| 角色 | 谁担任 | 对应 PMI 概念 |
|------|--------|---------------|
| Sponsor + PM 关键决策权 | **人** | [Project Sponsor](https://www.pmi.org/learning/library/importance-of-project-sponsorship-9946) + PM accountable decisions |
| PM 执行 + analyst | **AI** | PMBOK 8 AI Appendix · AI augment（[出处](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence)）；[arXiv 2601.16392 · Supervised-AI mode](https://arxiv.org/html/2601.16392v1) |

### Tailoring（PMBOK 7 原则）

proj-plan 的 Coach hybrid + 模式 T/F 对接 PMBOK 7 tailoring 4 步骤：

| PMBOK 7 步骤 | proj-plan 实现 |
|--------------|---------------|
| 1. Select Initial Development Approach | tailoring-decision.md · 模式 T / F（**简化为二选一**——本 skill 自创） |
| 2. Tailor for Organization | tailoring-rules.md 中 TR-04（合规/审计/合同交付 → F） |
| 3. Tailor for Project | TR-01 ~ TR-06 命中规则（项目规模 / EXP / stakeholder / 物理世界 / blocked 等） |
| 4. Implement Ongoing Improvement | 每阶段 review.md · lessons learned + analyze gate |

**遵守原则**："just enough process to maximize value"；"deliberate, conscious process of choosing the right processes and tools for the job, not abandoning process altogether"（[PMBOK 7 tailoring](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf)）。

---

## 二、SDD 借鉴（机制层 · 非命令名映射）

> 借鉴 [GitHub Spec Kit](https://github.com/github/spec-kit/blob/main/spec-driven.md) 的**机制**，**不映射其命令名**（specify / plan / tasks / implement）。
>
> **重要**：Spec Kit 是 feature-level 代码生成工具，proj-plan 是 project-level 治理框架——**范畴不同，只借鉴范式层的机制**。

### 借鉴的三个机制

| Spec Kit 机制 | 真实定位 | proj-plan 借鉴落地 |
|---------------|----------|---------------------|
| **Constitution-as-guardrail**（`memory/constitution.md`） | "architectural DNA of the system... non-negotiable principles that trump all other instructions"（[spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md)） | `DECISIONS.md` 中的 **INV-xx**（不变量）+ `artifact-index.md` + `integration-plan.md` 共同构成 source of truth |
| **Gate**（[`type: gate`](https://github.github.com/spec-kit/reference/workflows.html) 工作流人工审批节点） | 工作流暂停 → 人审 approve/reject → 继续 / abort | **manifest GATE-0 / 1 / 2 / N**（编号体系本 skill 自创）；GATE 未过禁止下游 artifact（INV-03） |
| **Analyze**（`/speckit.analyze`） | "Cross-artifact consistency & coverage analysis" — 跑在 tasks 后、implement 前 | [`assets/analyze-checklist.md`](analyze-checklist.md) — Round B 后、每阶段 acceptance 前；含 GATE 顺序、WBS↔roadmap、artifact-index 校验、DECISIONS 链等 |

### **不**做的（避免范畴错误）

| 反模式 | 为什么不做 |
|--------|-----------|
| `specify → proj-shape` 命令映射 | Spec Kit specify 产出 spec.md（单 feature 的 what/why），proj-shape 是 project-level 多轮讨论框架——范畴不同 |
| `plan → charter+wbs+roadmap` 命令映射 | Spec Kit plan 是技术栈 + 架构（单 feature），不是 PMP 项目管理计划 |
| `tasks → phase-NN/plan` 命令映射 | Spec Kit tasks 是依赖排序的可执行项（单 feature），phase plan 是 PMP 阶段任务 |
| `constitution → DECISIONS INV` 强等价 | 重叠但不等价——constitution 是开发原则（编码风格、TDD 等），INV 是项目级不可变约束。proj-plan 用 INV **借鉴** constitution 的"不可推翻 + trump 其它"性质，不假装它们是同一个东西 |

---

## 三、本 skill 自创（**不是** PMI / SDD 标准）

> 完整清单与 discuss 出处见 SKILL.md §立场声明 · 本 skill 自创术语。

| 术语 | 借鉴自 / 自创动机 | 出处 |
|------|------------------|------|
| **Coach hybrid** | 简化 PMBOK 7 tailoring 4 步骤为 T/F 二选一 + 用户 GATE-0 | DECISIONS.md ORD-04；`docs/discuss/02-…md` |
| **模式 T / F** | T = Tailored Minimum；F = Full（对接"just enough process"）| DECISIONS.md ORD-04 / ORD-06 |
| **GATE-0 / 1 / 2 / N** | 借鉴 Cooper stage-gate + Spec Kit `type: gate`；**编号体系**本 skill 自创 | DECISIONS.md INV-03；`docs/discuss/02-…md` |
| **human-read-manifest（≤5）** | 对接 PMBOK 8 "AI augment" 立场的具体执行机制；自创"5 项上限"硬规则 | DECISIONS.md INV-01 / ORD-05 / ORD-09 |
| **Round A / B** | 对接 PMBOK Initiating + Planning Process Group 的本 skill 自创双轮结构 | DECISIONS.md ORD-03 |

---

## 四、模式 T vs F

详见 [tailoring-rules.md](tailoring-rules.md)。  

**F = T + risk + stakeholder + communication + quality-plan（按需）**。

模式 F 试跑（EXP-03）截至 `docs/discuss/DECISIONS.md` 最后更新时**仍 pending**——F 路径尚未验证。
