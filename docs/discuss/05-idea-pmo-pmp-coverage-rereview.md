# 05-idea-pmo-pmp-coverage-rereview

> **2026-05-27 命名变更注记（轮次 07 决定）**：skills 集体重命名：`best-minds-grounded` → `proj-experts`、`idea-discuss` → `proj-shape`、`idea-pmo` → `proj-plan`；新增 `proj-run`（执行调度，骨架版）。本文档作为历史快照沿用讨论时的旧名（含文件名 idea-pmo），**正文不动**；引用时按上表换算。完整说明见 `07-sub-agent-model-tier-编排.md` + `DECISIONS.md`。

| 字段 | 值 |
|------|-----|
| 轮次 | 05 |
| 主题 | idea-pmo 补全后再评审：PMP 49 过程覆盖（明确排除项除外） |
| 日期 | 2026-05-21 |
| 状态 | discussed |
| 分析层 | best-minds-grounded（轻量） |
| 写入格式 | 轻量 |
| 承接 | `04-…md` 缺口清单；`skills/idea-pmo/` @2026-05-21 补全 |

## 用户输入（本轮）

用户请求：**再评审** 当前 `skills/idea-pmo/` 是否已覆盖**所有 PMP 流程**；**明确不需要的不算**。

## 事实与假设

### 轻量框定

| # | 待查问题 | 结论 |
|---|----------|------|
| Q1 | 04 轮 P0/P1 缺口是否已闭合？ | phase-roadmap / integration-plan / change-log / analyze / F 模板 / sub-agent handoff **均已入 skill**；试跑 `docs/pmo/` 已补 phase-roadmap 等 |
| Q2 | 「不需要」的边界仍以何为准？ | `INV-04`（Execute）+ 01 轮「刻意差异」表 + tailoring-rules |
| Q3 | 49 过程如何计「覆盖」？ | artifact + 工作流 + TR 条件命中 + **跨 skill**（idea-discuss 承担部分 Planning 输入） |
| Q4 | 模式 F 是否已验证？ | **否** — 仍仅 T 试跑；模板在，运行路径未 EXP |

### 已查证事实

**idea-pmo 当前资产**（`skills/idea-pmo/`）：SKILL.md + **21** 个 assets（含 phase-roadmap、integration-plan、change-log、analyze、risk/stakeholder/communication/quality、pmp-sdd-map、agent-handoff）。

**跨 skill 分工（计入覆盖时须一并算）**

| PMP 输入/过程 | 承担方 |
|---------------|--------|
| 收集需求、商业论证、INV/ORD/EXP | **idea-discuss** · DECISIONS |
| 执行、采购实施、风险应对实施、团队管理 | **执行**（对话 / 未来 execute skill）· INV-04 |
| 启动、规划、（规划侧）监控、（规划侧）收尾 | **idea-pmo** |

**01 轮已确立的「刻意不含」**（本轮不计为缺口）

- Execute 过程组（10）
- 成本管理（规划 3 + 控制 1）
- 采购管理（规划 1 + 执行 2）
- CPM / 甘特 / 资源平衡 / 逐任务 RACI / 正式 CCB
- 启动时全量 WBS 词典 L3+（rolling 进 phase plan）

### 外推

- **外推 · PMBOK 裁剪派**（非 PMI 原话）：依据 [Tailor based on context](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/) 的 holistic tailoring，「覆盖所有流程」应理解为 **在 tailoring 边界内每个启用的知识领域有对应产物或委托**，而非 49 过程各一条独立文档。
- **外推 · SDD**（非 Spec Kit 原话）：依据 [Workflows gate/analyze](https://github.github.com/spec-kit/reference/workflows.html)，idea-pmo 用 GATE + analyze 覆盖了 PMP 中部分 **Monitor & Control** 的「证据链」要求，而非逐过程 named template。

## 讨论

### 1. 总览结论

**在「idea-pmo + idea-discuss + 执行分离」体系内，对默认模式 T 及 TR 命中场景：所需 PMP 过程均已覆盖或已合理委托/裁剪。**

| 统计 | 数量 | 说明 |
|------|------|------|
| PMBOK 6 过程合计 | 49 | 对照基准 |
| **明确排除**（不计缺口） | **18** | Execute×10 + 成本×4 + 采购×3 + Execute 内嵌的 Manage/Implement 重复计约 1→ 见下表 |
| **idea-discuss 委托** | **2–3** | 收集需求、商业论证、可行性 |
| **idea-pmo 覆盖（含合并/rolling）** | **20–22** | 见 §2 |
| **弱覆盖（可接受 minimal）** | **5–6** | 见 §3 |
| **仍缺 / 未验证** | **2** | 模式 F 试跑；定量风险（可选） |

**一句话**：不是 49 个过程 49 份文档；**该覆盖的已覆盖**，剩下主要是 **Execute/成本/采购**（故意不要）和 **F 路径未跑通**。

### 2. 五过程组覆盖矩阵

图例：**✓** 有 artifact/流程 · **⊘** 明确排除 · **↗** 委托 discuss/执行 · **△** 合并/TR 条件/最小实现

#### Initiating（2/2 在边界内 ✓）

| 过程 | 状态 | idea-pmo / 体系 |
|------|------|-----------------|
| 制定项目章程 | ✓ | initiation-charter → charter |
| 识别干系人 | △ | project-context；TR-03 → stakeholder-register |

#### Planning（24 过程中：边界内约 15 ✓，3 ↗，6 ⊘）

| 过程 | 状态 | 映射 |
|------|------|------|
| 制定项目管理计划 | ✓ | integration-plan.md |
| 规划范围/进度/风险/质量/资源/沟通/干系人 **管理** | △ | 无独立「规划XX管理」文档；合并在 integration-plan + TD |
| 收集需求 | ↗ | DECISIONS / idea-discuss |
| 定义范围 | ✓ | charter |
| 创建 WBS | ✓ | wbs.md |
| 定义活动 | ✓ | phase-NN/plan.md |
| 排列活动顺序 | △ | plan 内依赖节（最小） |
| 估算活动持续时间 | △ | 人工步骤 ORD-07 |
| 制定进度计划 | ✓ | phase-roadmap + rolling plan |
| 估算成本 / 制定预算 / 规划成本管理 | ⊘ | 01 轮刻意省略 |
| 规划质量管理 | △ | acceptance；F → quality-plan |
| 规划资源管理 / 估算活动资源 | △ | plan 执行者 + agent-handoff |
| 规划沟通管理 | △ | TR-03 / F → communication-plan |
| 识别风险 / 定性分析 / 规划应对 | △ | TR-02 / F → risk-register |
|  Perform **定量**风险分析 | △ | F 可选；T 默认无（可接受） |
| 规划采购管理 | ⊘ | 刻意省略 |

#### Executing（10/10 ⊘）

| 状态 | 依据 |
|------|------|
| **全部排除** | INV-04；含指导与管理项目工作、管理质量/知识/团队、实施风险/采购应对等 |

#### Monitoring & Controlling（12 过程中：边界内约 6 ✓，4 △，2 ⊘）

| 过程 | 状态 | 映射 |
|------|------|------|
| 监控项目工作 | ✓ | review.md |
| 实施整体变更控制 | ✓ | change-log.md + 推翻 ORD → discuss |
| 确认范围 / 控制质量 | ✓ | acceptance + analyze |
| 控制范围 | △ | change-log + acceptance（无独立 scope creep 表） |
| 控制进度 / 控制成本 | △ / ⊘ | review 文字；成本 ⊘ |
| 监督风险 | △ | review ↔ risk-register |
| 监督沟通 / 监督干系人 | △ | 无周期 status report 模板（T 可接受；F 可选 enrich） |
| 控制采购 | ⊘ | |

#### Closing（1/1 △→✓ 对 planning skill 足够）

| 过程 | 状态 | 映射 |
|------|------|------|
| 结束项目或阶段 | ✓ | review：lessons learned + 末阶段收尾检查 |

### 3. 十知识领域 — 边界内是否闭合

| 知识领域 | T 默认 | TR/F 扩展 | 边界内结论 |
|----------|--------|-----------|------------|
| 整合 | ✓ integration-plan | | ✓ |
| 范围 | ✓ wbs + charter + acceptance | | ✓ |
| 进度 | ✓ roadmap + plan | | ✓ |
| 成本 | ⊘ | | 故意不要 |
| 质量 | ✓ acceptance + analyze | quality-plan | ✓ |
| 资源 | △ plan + handoff | | ✓（AI 时代 minimal） |
| 沟通 | △ charter/manifest | communication-plan | ✓ |
| 风险 | △ review | TR-02 risk-register | ✓ |
| 采购 | ⊘ | | 故意不要 |
| 干系人 | △ context | TR-03 register | ✓ |

### 4. 相对 04 轮的改进确认

| 04 缺口 | 05 状态 |
|---------|---------|
| phase-roadmap 模板/试跑 | ✓ 已补 |
| integration-plan | ✓ 已补 |
| change-log | ✓ T 默认 |
| analyze（SDD） | ✓ 硬规则 |
| circuit breaker | ✓ SKILL + review/acceptance 模板 |
| F 模板集 | ✓ 有模板 |
| sub-agent | ✓ agent-handoff + plan 列 |
| 模式 F 试跑 | ✗ 仍缺 |
| 定量风险 | △ 仍无（T 可不要） |

### 5. 仍开放（非「缺 PMP 流程」，是验证/enrich）

| 项 | 类型 | 建议 |
|----|------|------|
| **EXP-03** 模式 F 试跑 | 验证 | TR-04 虚构项目走 Round B |
| 周期 **status report** 模板 | 可选 enrich | 仅 TR-04/F；非 T 必需 |
| **WBS 词典** 独立文件 | 可选 | 01 轮已选 rolling 嵌入 plan |
| 定量风险分析 | 可选 | 合规场景 F 扩展 |

### 6. 评审裁决（讨论层）

**问题：「是否覆盖了所有 PMP 流程（明确不需要的不算）？」**

**答：是 — 在已声明的 tailoring 边界内。**

- **idea-pmo 单独**：覆盖 Initiate、Plan（rolling）、M&C 的**规划与证据链**、Close 的**阶段级**活动；不覆盖 Execute、成本、采购。
- **加 idea-discuss**：需求与决策输入闭合。
- **加执行层**：Execute 过程由 INV-04 故意外置。

未闭合项 = **模式 F 未试跑**（EXP-03），不是「缺流程定义」。

## 可验证尝试与继续/中止

### EXP-03（正式纳入，自 04 轮草案升级）

| 项 | 内容 |
|----|------|
| 假设 | 补全后的 skill 在 **模式 F** 下仍可 manifest≤5 且 analyze 通过 |
| 尝试方案 | 虚构 TR-04 project-context → Round A/B 模式 F → 只读 manifest 验收 |
| 成功信号 | risk/stakeholder/communication/quality 生成；analyze 全 pass；用户信任 F |
| **继续** | 关闭「F 未验证」开放项 |
| **中止** | F 过重 → 降格为「T + 可选三附件」并修订 tailoring-rules 文案 |
| 来源 | `04-…md` §EXP-03；`05-…md` §5 |

## 本轮决定

### 已确定 — 原则性不变量 / 普通决定

（无 — 以下为**待用户确认**的 ORD 草案）

### 待确认

**ORD-10 草案**（PMP 覆盖边界声明）：

> idea-pmo 的 PMP 覆盖范围 = **Initiate + Plan（rolling）+ 规划侧 M&C + 阶段 Close**；**不含** Execute、成本、采购；需求输入由 idea-discuss 承担。T + TR 命中即视为过程闭合；F 须 EXP-03 试跑后标定。

### 待确认（下轮）

1. 是否采纳 **ORD-10** 写入 DECISIONS？
2. 是否启动 **EXP-03**（模式 F 试跑）？
3. status report 模板是否纳入 F（可选）？

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| — | 无新 INV/ORD（ORD-10 待确认） | ✓ |
| EXP-03 | 草案升级，待用户确认入表 | — |

讨论状态同步：维持 **`ready-for-implementation`**

同步完成时间：2026-05-21

## 开放问题

1. ORD-10 确认后，是否在 `pmp-sdd-map.md` 增加 **49 过程对照简表** 常驻（便于日后审计）？

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-21 | 补全后再评审 |
