# 02-ai全量pmp与智能裁剪

> **2026-05-27 命名变更注记（轮次 07 决定）**：skills 集体重命名：`best-minds-grounded` → `proj-experts`、`idea-discuss` → `proj-shape`、`idea-pmo` → `proj-plan`；新增 `proj-run`（执行调度，骨架版）。本文档作为历史快照沿用讨论时的旧名，**正文不动**；引用时按上表换算。完整说明见 `07-sub-agent-model-tier-编排.md` + `DECISIONS.md`。

| 字段 | 值 |
|------|-----|
| 轮次 | 02 |
| 主题 | AI 执行全量 PMP vs 智能裁剪；SDD 与 PMP 分工 |
| 日期 | 2026-05-19 |
| 状态 | discussed |
| 分析层 | best-minds-grounded（完整执行） |
| 承接 | 轮次 01（轻量 PMP × Shape Up × SDD）；本轮扩展「重量」问题的 AI 解法 |

## 用户输入（本轮）

用户提出新灵感，并追问若干概念：

1. **全量 PMP + 人读子集** — 是否可执行**完整** PMP 流程，由 AI 完成全部文档；人**不必**读所有文档，只读必需文档 → 既减人工、又保一致性与完备性？
2. **裁剪的官方原因** — PMP 官方为何建议 tailoring？能否通过 **skill 让 AI 自动裁剪**？
3. **SDD vs PMP** — SDD 重点是否在于**以文档约束 AI 行为**，工作流程反而不严格限定？PMP 经时间验证的流程文档化后，是否反而能发挥更大作用？
4. **重量问题的本质** — 仍怕「太重」，但 AI 是否正好解决：**智能裁剪** 或 **全量生成 + 人只读一小部分**，都能节省绝大部分人工？

## 事实与假设

### best-minds-grounded · 轻量框定（查证前问题清单）

| # | TA 会先确认什么 | 指向 |
|---|-----------------|------|
| Q1 | PMBOK 说「要裁剪」的**首要理由**是人力成本，还是**环境不适配**？ | 决定 AI 能否消除裁剪需求 |
| Q2 | 裁剪难点官方怎么说？谁该负责裁剪？ | 决定 skill 是否可承担「DSDM Coach」角色 |
| Q3 | SDD 官方如何定义 spec 与 code 的关系？workflow 是固定还是可组装？ | 检验用户对 SDD 的理解 |
| Q4 | 是否已有「AI 生成 PMBOK 对齐文档」的产品/研究？ | 全量 PMP 由 AI 写是否已有先例 |
| Q5 | 轮次 01 的「轻量 B 方案」与本灵感是否冲突，还是同一光谱两端？ | 讨论收敛 |

### 已查证事实

**PMBOK · 为何 tailoring（官方，多源）**

| 原因类别 | 内容 | 出处 |
|----------|------|------|
| **环境不适配** | 组织规模、文化、背景不同；照搬他司 PM 体系会失败（中型公司导入大厂 PM 系统案例） | [Tailor based on context](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/) |
| **成本并非仅「写文档」** | 未裁剪的方法论对组织「too expensive」——指**运转成本**（仪式、合规、不匹配），非仅页数；裁剪后应**省成本、提声誉** | [When it's too expensive](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s1-when-it-is-too-expensive/) |
| **管理产物 ≠ 文档** | PRINCE2 例：checkpoint report 可以是**电话**而非书面；关键是**按间隔传递约定信息**——tailoring 是选**形式与深度**，不是删过程 | 同上 |
| **裁剪须整体一致** | 简单 cherry-pick 各方法论片段会像「科学怪人」；裁剪是在**建新系统**，需 holistic view | [The difficulty of tailoring](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s3-the-difficulty-of-tailoring/) |
| **PM 未必会裁剪** | 优秀 PM 不一定具备**设计 PM 体系**的能力；DSDM 因此设 **DSDM Coach** 专责裁剪等 | 同上 |
| **两步裁剪** | 组织级 partial tailoring + 项目级 final tailoring | [The tailoring process](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s2-the-tailoring-process/) |
| **upfront 宜最小** |  upfront 裁剪过多易做出过重 formal 系统；宜**先极简、随进展 enrich** | [When to tailor](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s4-when-to-tailor/) |
| **未裁剪的代价** | 现成方法论不裁剪 → 不适合具体项目、浪费、士气下降；裁剪实践与更好项目结果相关 | [PMI: Benefits of Tailoring](https://www.pmi.org/learning/library/tailoring-benefits-project-management-methodology-11133) |

**SDD · Spec Kit 官方立场**

- **规范驱动**：spec 是 primary artifact，code 是 spec/plan 的**生成物**；「Specifications as the Lingua Franca」。[spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- **Workflow 可组装**：SDD 可用 AI + 工具**组装**实践；Spec Kit 用 **commands**（specify/plan/tasks/implement）与 **workflow YAML** 链式组合，含可选 gate。[spec-driven.md §Streamlining SDD with Commands](https://github.com/github/spec-kit/blob/main/spec-driven.md)；[Workflows](https://github.github.com/spec-kit/reference/workflows.html)
- **不必一次 complete**：「Code generation begins as soon as specifications … are **stable enough**, but they do not have to be complete.」——与 rolling 思想相容。
- **Continuous refinement**：一致性校验是**持续**过程，非一次性 gate（虽 Spec Kit 仍提供 gate 命令）。

**AI 生成 PM 文档（行业先例，非官方标准）**

- 商业工具（如 Artifactly GuidedDraft、Vero AIBOL）宣称从输入生成 charter、RACI、风险登记等 **PMBOK 对齐**文档。[Artifactly](https://artifactly.ai/features/guided-draft)；[Vero AIBOL](https://veropm.app/aibol-ai-engine.html)
- 学术研究：meta-prompting + 语义检索生成 **standards-based PM 文档**，强调减幻觉与结构一致。[Springer 2025 chapter](https://link.springer.com/chapter/10.1007/978-3-032-23241-0_12)
- **待验证**：上述工具对**非 IT / 个人小项目**的质量与「人读子集」实践 —— 无独立第三方评测，置信度中。

**轮次 01 结论（本仓库上下文）**

- 推荐方案 B：charter + L1/L2 WBS + GATE + rolling phase plan；控制**人类必读 ≤~2 页**。
- INV/ORD 仍为草案，未用户确认。

### 专家视角讨论（best-minds-grounded）

#### 视角 A · PMBOK 裁剪派

**会说的（有出处）**：tailoring 的首要动机**不是**「人写文档太累」，而是 **PM 系统须匹配项目与组织环境**；即便文档零成本，**错误的过程/产物集**仍会导致决策失误、仪式负担、士气问题。裁剪选的是**哪些过程、以何深度、何形式**（文档/电话/检查表）。

**外推（非 PMI 原话）**：AI 消除的是 **「生成与维护文档的边际成本」**，**不消除**「何种 PM 过程对本项目合适」的判断。因此：**全量 PMP artifact 由 AI 生成** 在技术上可行，但 **不等于** 应对所有项目跑满全部过程组——仍须 **tailoring 决策**（哪怕决策结果是「本项目跑全量」）。

#### 视角 B · DSDM Coach 角色（PMBOK 引述 DSDM）

**会说的（有出处）**：裁剪太难，不应默认每位 PM 都会；DSDM 设 **Coach** 专责构建一致的方法论实例。

**外推（非 DSDM 原话）**：**Skill 可扮演 Coach**——输入 `DECISIONS` + 项目元数据（领域、规模、风险、监管），输出：
- `tailoring-decision.md`（启用哪些过程/产物、深度、形式）
- `human-read-manifest.md`（人必读清单 + GATE 顺序）
- 机器读全集（AI 执行用）

这比「agent 每次临场决定写哪些文件」更一致，也回应 cherry-pick 问题。

#### 视角 C · SDD / Spec Kit

**会说的（有出处）**：SDD 核心是 **spec 作为 truth source 约束生成**；workflow 由 commands/workflows **组装**，非唯一法定流程；gate 是**可选质量机制**。

**对你问题的回应（综合官方表述）**：

| 你的理解 | 修正/补充 |
|----------|-----------|
| SDD 主要是文档约束 AI | **大体对**——「Executable Specifications」+ constitution 约束 plan/implement |
| SDD 不限定具体 workflow | **对**——commands 可裁剪；quick path: specify→plan→tasks→implement |
| PMP 流程文档化后对 AI 更有用 | **部分对**——PMP 提供 **过程完备性检查表**（ nothing obvious missing）；SDD 提供 **生成链与一致性校验**。二者可叠：PMP 定「要有什么」，SDD 定「如何让 AI 按文档执行」 |

**外推（非 Spec Kit 作者原话）**：对你「任何领域」目标，**PMP artifact 集比 SDD 命名更领域中立**；SDD 的 **gate + spec-as-truth** 机制应作为 **AI 行为约束层** 套在 PMP 过程之上，而非二选一。

## 讨论

### 1. 你的灵感：「AI 全量 PMP，人只读必需文档」

**在讨论层判断：可行，且与 PMBOK 官方并不冲突——若把「必需」明确定义为 tailoring 的输出之一。**

```text
                    ┌─────────────────────────────┐
                    │  DECISIONS（idea-discuss）   │
                    └──────────────┬──────────────┘
                                   ▼
                    ┌─────────────────────────────┐
                    │  AI Tailoring（skill/Coach） │
                    │  输出：tailoring-decision    │
                    │  · 模式：full | tailored    │
                    │  · 过程/产物清单             │
                    │  · human-read-manifest      │
                    └──────────────┬──────────────┘
                                   ▼
              ┌────────────────────┴────────────────────┐
              │                                         │
    ┌─────────▼─────────┐                   ┌───────────▼──────────┐
    │ 模式 T：裁剪生成    │                   │ 模式 F：全量生成        │
    │ 只生成 TD 选中产物  │                   │ 生成完整 PMP artifact  │
    │                   │                   │ 树（AI 维护）           │
    └─────────┬─────────┘                   └───────────┬──────────┘
              │                                         │
              └────────────────────┬────────────────────┘
                                   ▼
                    ┌─────────────────────────────┐
                    │  人类只读 manifest 中条目    │
                    │  + GATE 审 charter/WBS/…    │
                    │  其余：AI 读写（一致性/完备） │
                    └─────────────────────────────┘
```

**模式 T（智能裁剪）** 与 **模式 F（全量 + 人读子集）** 不是互斥策略，而是 **tailoring-decision 的两种结果**：

| | 模式 T | 模式 F |
|---|--------|--------|
| AI 生成量 | 少 | 多 |
| 人类阅读 | 少 | manifest 仍少（如 2–5 项） |
| 完备性 | 依赖裁剪质量 | 依赖全量树 + 交叉引用 |
| 适用 | 小项目、低监管 | 高不确定、高合规、多 stakeholder |
| 风险 | 漏产物 | 幻觉/陈旧文档、虚假完备感 |

**关键点**：两种模式都仍需 **human-read-manifest**——这正是 GATE 的 formalization。

### 2. PMBOK 为何建议裁剪？AI 改变了什么、没改变什么？

| 裁剪原因（官方） | AI 能否缓解 | 讨论结论 |
|------------------|-------------|----------|
| 环境/规模不匹配 | 部分 | 生成免费≠过程合适；须 **显式 tailoring 决策** |
| 人工撰写/维护成本 | **是** | 你的灵感直击此处 |
| 人工阅读/决策带宽 | **部分** | manifest + GATE 可限人读；**关键决策仍须人** |
| 仪式过重损害士气 | 部分 | AI 可去掉「填模板」痛苦；若 GATE 过多仍重 |
| cherry-pick 不一致 | **skill 可缓解** | Coach skill + 模板树 + 交叉引用校验 |
| PM 不会裁剪 | **skill 可缓解** | 预设 tailoring 规则 + DECISIONS 输入 |
| upfront 过重 | **是** | 先 manifest+core；rolling enrich 全量树 |

**结论**：AI **不能取消 tailoring 原则**；AI **改变 tailoring 的经济学**——从「人写不了那么多」变成「人读不了那么多 → 机器维护全量、人审 manifest」。

### 3. Skill 能否实现 AI 自动裁剪？

**讨论层：能，且应作为落地 skill 的一级能力**（比轮次 01 的固定 B 方案更 General）。

建议 **tailoring 输入**：

- `DECISIONS`（INV/ORD/EXP、领域、风险）
- 项目元数据：规模、监管、 stakeholder 数、是否物理世界、是否多阶段

建议 **tailoring 输出**（写入 `docs/implement/`）：

| 文件 | 读者 | 内容 |
|------|------|------|
| `tailoring-decision.md` | 人+AI | 启用过程组/产物、深度、模式 T/F、依据 |
| `human-read-manifest.md` | **人** | 必读顺序、GATE、预估阅读时间 |
| `artifact-index.md` | AI | 全量产物路径、依赖、版本、交叉引用 |
| 各 PM artifact |  mostly AI | charter、WBS、风险登记…按 TD 生成 |

**裁剪规则示例（讨论草案，非决定）**：

- 个人 AI 辅助、无监管 → 模式 T：charter + WBS L2 + rolling phase plan
- 多人、有 EXP 高风险 → 模式 T + 风险登记 + 变更 log
- 合规/对外交付 → 模式 F：全量生成，manifest 仍 ≤5 项 GATE 文档

### 4. SDD vs PMP：竞争还是分层？

**讨论结论：分层叠加，不是取代。**

```text
  ┌─────────────────────────────────────────────┐
  │  PMP 层：过程 + artifact 完备性（what to have）│
  │  · 启动/规划/执行/监控/收尾                   │
  │  · WBS、风险、变更、干系人…                    │
  └────────────────────┬────────────────────────┘
                       │ 产物即「规范」
  ┌────────────────────▼────────────────────────┐
  │  SDD 层：文档约束 AI（how AI must behave）    │
  │  · spec/charter = source of truth            │
  │  · gate、analyze、constitution Compliance     │
  │  · 机器可读索引 + 禁止跳过 manifest GATE       │
  └─────────────────────────────────────────────┘
```

- **SDD** 强在：让 AI **按文档执行、持续校验一致性**。
- **PMP** 强在：**跨领域**、时间验证的「别漏项」检查框架。
- **idea-discuss** ≈ SDD 的 specify/clarify + 部分 constitution。
- **落地 skill** 宜：**PMP Coach（tailoring + 产物树）+ SDD gate（manifest + 禁止越权生成）**。

你对 SDD「workflow 不限定」的理解 **基本正确**；对 PMP「文档化后发挥更大作用」在 **AI 时代更强**——因 **写文档成本≈0**，瓶颈移到 **审 manifest + 关键 GATE**。

### 5. 与轮次 01 的关系（收敛，非推翻）

| 轮次 01 | 轮次 02 扩展 |
|---------|--------------|
| 固定方案 B（charter + WBS + GATE） | B 是 **模式 T 的默认实例** |
| 人类必读 ≤2 页 | 泛化为 **human-read-manifest**（小项目仍 ~2 页） |
| 反对启动写 task-list | **不变**——属 SDD gate，与 T/F 无关 |
| 轻量 PMP | **轻量人读 + 可重 machine corpus** |

**INV 草案修订（待确认，取代轮次 01 部分草案）**：

- **INV-01′**：落地 skill 必须产出 **tailoring-decision + human-read-manifest**；人类只需读 manifest 所列；**禁止**要求人读全量 artifact 树。
- **INV-02′**（承接 01）：细任务仅出现在 rolling phase plan；**不变**。
- **INV-03′（新）**：无论模式 T/F，**GATE 未过不得生成下游 artifact**（SDD 纪律）。

**ORD 草案增补**：

- **ORD-05**：落地 skill 第一步为 **AI tailoring**（非直接写 charter）；输出 TD + manifest，经用户确认后再生成产物树。
- **ORD-06**：模式 F 下，全量 artifact **须**有 `artifact-index.md` 供 AI 交叉引用；人仍只读 manifest。

### 6. 风险与障碍（必须带路）

| 风险 | 路径 |
|------|------|
| **虚假完备感**（全量文档看似齐全实则幻觉） | EXP-03：`/speckit.analyze` 式 **artifact 交叉校验**；关键数值须链 DECISIONS ID |
| **文档漂移**（DECISIONS 改了，全量树未更） | artifact-index 版本 + 变更触发 regen |
| **manifest 膨胀**（GATE 越来越多） | manifest 硬上限（如 ≤5 项）；其余合并进单一 GATE checklist |
| **裁剪过度**（模式 T 漏关键产物） | TD 须引用 tailoring 规则 ID；失败则回 **模式 F** 或补产物 |

## 可验证尝试与继续/中止

### EXP-03（新增）

| 项 | 内容 |
|----|------|
| 假设 | 同一项目下，**模式 F（全量 AI 生成 + manifest 人读 ≤5 项）** 在完备性上优于模式 T，且人感重量 ≤ 模式 T |
| 尝试方案 | 选 skills 仓库改 skill 或用户小项目：**并行**生成 (T) 轮次 01 式 charter+wbs 与 (F) 全量 PM 树 + manifest；用户只读 manifest 指定项，填 5 点问卷（完备感/重量/信任） |
| 成功信号 | 人读时间 ≤10min；F 的完备感 ≥ T 且重量感相当；用户愿选 F 或「T+F 混合」 |
| **继续** | 落地 skill 默认 **先 TD 再选 T/F**；实现 artifact-index + 交叉校验 |
| **中止** | F 显著更不信任或更累 → 默认模式 T；全量仅合规场景启用 |
| 来源 | `02-ai全量pmp与智能裁剪.md` §EXP-03 |

### EXP-01 / EXP-02（修订关系）

- **EXP-01**：仍有效，作为 **模式 T 基准线**；与 EXP-03 可同项目串联（先 T 再 F 对比）。
- **EXP-02**：仍有效；manifest 的 GATE 即 EXP-02 的具体化。

## 本轮决定

### 已确定 — 原则性不变量（新增/修订）

（无 — 以下 INV-01′–03′ 待用户确认）

### 已确定 — 普通决定（新增/修订）

（无 — 以下 ORD-05–06 待用户确认）

### 待确认（下轮继续）

1. **INV-01′–03′**、**ORD-05–06** 是否取代轮次 01 的 INV/ORD 草案？
2. 默认倾向：**模式 T**、**模式 F**，还是 **先 TD 由 AI 推荐**？
3. **human-read-manifest** 硬上限：5 项？3 项？
4. EXP-03 是否与 EXP-01 合并试跑？
5. 落地 skill 命名：`idea-implement` 保留 vs 改 `idea-plan` / `idea-pmo`？

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| EXP-03 | 新增 | ✓ |
| EXP-01 | 关系说明：作为模式 T 基准 | ✓（无条文变更） |
| EXP-02 | 关系说明：manifest GATE 具体化 | ✓（无条文变更） |

讨论状态同步：`deciding` → **`deciding`**（议题扩展；新增 T/F 光谱与 TD 机制；INV/ORD 草案迭代，仍未 ready）

同步完成时间：2026-05-19

## 开放问题（下轮）

1. 你是否认同：**AI 不取消 tailoring，但可把「重量」从人转移到 machine corpus**？
2. 高合规场景是否会主动选模式 F？
3. skill 的 Coach 角色：固定规则表 vs LLM 临场 tailoring，哪个更可信？

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-19 | 初稿 |
| 1.1 | 2026-05-19 | 用户 §用户回复；决定收敛见轮次 03 |

## 同步注记（2026-05-19）

- 用户 @§用户回复 确认 INV/ORD 方向、manifest≤5、idea-pmo 命名、EXP 合并、双轮启动、Coach hybrid
- 正式 INV-01–04、ORD-01–08 见 `DECISIONS.md` 与 `03-idea-pmo两轮启动与决定收敛.md`


## 用户回复

### 待确认
1. 同意
2. 是否可以分成两轮，第一轮确定一些基本信息以及建议采取的模式，类似项目章程授权，用户确认后开始详细规划
3. 5项吧
4. 可以
5. idea-pmo吧

### 开放问题
1. 同意
2. 建待确认问题回复2，分多轮，AI给出建议，用户确认
3. 能否也和上一条一样，AI给出建议，用户确认