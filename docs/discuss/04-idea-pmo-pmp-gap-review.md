# 04-idea-pmo-pmp-gap-review

| 字段 | 值 |
|------|-----|
| 轮次 | 04 |
| 主题 | idea-pmo 实现评审：相对 PMP 流程的覆盖与缺口 |
| 日期 | 2026-05-21 |
| 状态 | discussed |
| 分析层 | best-minds-grounded（完整执行） |
| 写入格式 | 完整 |
| 承接 | `03-…md` 试跑完成；用户 @temp.md todo + 本评审请求 |

## 用户输入（本轮）

用户请求：**评审当前 `idea-pmo/SKILL.md` 实现，看缺少了哪些 PMP 流程**。

附带上下文（`docs/discuss/temp.md` todo，未关闭）：

- idea-pmo 只有 wbs，没有阶段计划 → *注：03 轮后已设计 `phase-roadmap` + rolling `phase-NN/plan`，但试跑产物有缺口（见 §实现缺陷）*
- idea-pmo 增加 sub-agent 的定义和流程

## 事实与假设

### best-minds-grounded · 轻量框定（查证前问题清单）

| # | 待查问题 | 查证结论（摘要） |
|---|----------|------------------|
| Q1 | PMBOK 6 的过程组 / 知识领域 / 49 过程是否仍是 idea-pmo「PMP 映射」的合理对照系？ | PMBOK 7 改为 12 原则 + 8 绩效域；**49 过程 + 10 知识领域仍属 PMP 考试与工业对照常用框架**。[PM Study Circle](https://pmstudycircle.com/process-group-and-knowledge-area-in-the-pmbok-guide/) |
| Q2 | PMBOK 官方对「裁剪」是否允许省略大量 Planning 过程？ | 允许；关键是 **holistic tailoring**，非 cherry-pick。[Tailor based on context](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/) |
| Q3 | 当前 idea-pmo SKILL + assets + 试跑 `docs/pmo/` 实际覆盖了哪些产物？ | 见 §实现快照 |
| Q4 | 模式 F「全量 PM 树」在 skill 中是否已有可执行模板？ | **否**——`tailoring-rules.md` 列了风险/干系人/沟通/变更/质量等，**assets 无对应模板** |
| Q5 | 试跑是否验证过模式 F？ | **否**——TR-01 → 模式 T；F 仅文档级声明 |

### 已查证事实

**idea-pmo 当前实现快照**（`~/.claude/skills/idea-pmo/` + 本仓库 `skills/idea-pmo/` 同步；试跑 `docs/pmo/` @2026-05-19）

| 层级 | 已有 | 缺失 / 不一致 |
|------|------|----------------|
| SKILL 工作流 | Round A/B、GATE-0/1/2、Rolling phase、Coach hybrid、模式 T/F | 无 Execute/Close 专章；无 sub-agent 流程 |
| assets 模板（11 个） | project-context、TD、initiation-charter、manifest、charter、wbs、plan、acceptance、review、artifact-index、tailoring-rules | **`phase-roadmap-template.md` 被 SKILL 引用但不存在** |
| 试跑 docs/pmo | 除 `phase-roadmap.md` 外 Round A/B + phase-01 齐全 | **`phase-roadmap.md` 在 artifact-index 登记但文件未生成** |
| tailoring-rules 模式 F | 文字列出全量产物 | 无 risk/stakeholder/communication/change/quality 模板 |
| 过程组（tailoring-rules §过程组启用） | Initiate ✓、Plan ✓（rolling）、Execute ✗、Monitor 部分、Close 部分 | 与 SKILL 一致 |

**PMBOK 6 五过程组 × 覆盖定性**（相对 **49 过程** 的 skill 实现，非考试逐条对照）

| 过程组 | 过程数 | idea-pmo 覆盖 | 说明 |
|--------|--------|---------------|------|
| Initiating | 2 | **部分** | 章程 ✓；干系人识别仅 F 且无模板 |
| Planning | 24 | **部分（刻意轻量）** | 范围/WBS/rolling 计划 ✓；进度粗路线图 ✓；成本/采购/资源计划 ✗；风险/质量/沟通计划 △（F 宣称） |
| Executing | 10 | **刻意不含** | INV-04；归执行 skill / 对话 |
| Monitoring & Controlling | 12 | **弱** | phase `review` + acceptance；无变更 log、无控进度/成本/风险过程 |
| Closing | 1 | **弱** | `review.md` 末阶段；无 lessons learned / 正式收尾 checklist 模板 |

**10 知识领域 × 模式 T（默认）**

| 知识领域 | T 模式 | 主要 artifact / 行为 |
|----------|--------|----------------------|
| 整合 | △ | charter + artifact-index；**无合一的项目管理计划（PMP 整合文档）** |
| 范围 | ✓ | WBS L1–L2、phase acceptance |
| 进度 | △ | phase-roadmap（粗）+ rolling plan；**无活动排序/关键路径** |
| 成本 | ✗ | 无 |
| 质量 | △ | acceptance.md；无质量计划 |
| 资源 | △ | plan 中 AI/人工；无资源管理计划 |
| 沟通 | ✗ | 无（F 才列沟通计划） |
| 风险 | △ | TR-02 建议简登记；**无模板、无识别/分析/应对流程** |
| 采购 | ✗ | 无 |
| 干系人 | ✗ | 无（F 才列干系人登记） |

### 专家视角讨论（best-minds-grounded）

#### 视角 A · PMBOK 裁剪派（PMI 原则体系）

**会说的（有出处）**：tailoring 允许省略不适配的过程；upfront 宜最小、随进展 enrich。[When to tailor](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s4-when-to-tailor/)

**外推（非 PMI 原话）**：依据 tailoring + rolling wave 原则，idea-pmo 对 **个人/AI 辅助小项目** 省略成本/采购/正式 CCB **符合 PMP 精神**；缺口应分 **「刻意裁剪」** 与 **「宣称有但未实现」**——后者（模式 F 产物树、phase-roadmap 模板）违反 holistic tailoring 的 **一致性**。

#### 视角 B · Ryan Singer（Shape Up）

**会说的（有出处）**：shaping 不写 task 清单；building cycle 才展开；circuit breaker 未 ship 则回 shaping。[Principles of Shaping](https://basecamp.com/shapeup/1.1-chapter-02)

**外推（非 Ryan 原话）**：依据 shaping/building 分离，**Execute 过程组不含** 是正确边界；缺口不在 Execute，而在 **Monitor**——`review.md` 相当于 retrospective，但缺 **显式 circuit breaker 规则**（未过 acceptance 是否禁止下一阶段）写入 SKILL 硬规则。

#### 视角 C · Spec Kit / SDD

**会说的（有出处）**：gate 控制 artifact 顺序；analyze 做交叉校验。[Workflows](https://github.github.com/spec-kit/reference/workflows.html)

**外推（非 Spec Kit 作者原话）**：依据 gate + analyze，`artifact-index` 的「交叉校验」在试跑为 checkbox，**无强制 analyze 命令或失败处理**；模式 F 未试跑 = **完备性路径未验证**。

#### 收敛（综合，非任一专家原话）

| 缺口类型 | 代表项 | 是否 PMP「缺流程」 | 建议 |
|----------|--------|-------------------|------|
| **A · 刻意不含** | Execute 全组、成本/采购、CPM | 是，但 **by design** | 在 SKILL 增「刻意不覆盖对照表」，避免误读为遗漏 |
| **B · 宣称未实现** | 模式 F 模板、phase-roadmap 模板/试跑文件 | 是，且 **实现 bug** | 优先补模板 + 试跑 F 或下调 F 宣称 |
| **C · 弱覆盖可 enrich** | 变更控制、风险、收尾、lessons learned | PMP 有、T 可裁剪 | 用 TR 规则 + rolling enrich，非启动全写 |
| **D · AI 时代新增** | sub-agent 编排 | PMP 无直接对应 | 映射到 **资源/沟通/整合** 绩效域，单独立 ORD |

## 讨论

### 1. 实现缺陷（非 PMP 理论缺口，但影响「已有流程」可信度）

| # | 问题 | 影响 |
|---|------|------|
| D1 | `assets/phase-roadmap-template.md` **不存在**，SKILL 仍引用 | Round B 步骤无法按 skill 复现 |
| D2 | 试跑 `docs/pmo/phase-roadmap.md` **未生成**，artifact-index 却标 GATE-2 ✓ | INV-02 / ORD-06 交叉校验失真 |
| D3 | 模式 **F 从未试跑** | TR-04 / F 全量树为 **纸面流程** |
| D4 | `review-template.md` 无 **lessons learned** 字段 | Closing 过程弱 |
| D5 | 用户 todo：**sub-agent 无定义** | 多 agent 执行时无 PM 归属 |

> temp.md「只有 wbs 没有阶段计划」：**设计已补**（phase-roadmap + rolling plan），**试跑未闭合**（D1/D2）。

### 2. PMP 49 过程 — 按过程组明细缺口

图例：**✓** 有 artifact/硬规则 · **△** 部分/仅 F/仅文字 · **✗** 无 · **⊘** 刻意不含（INV-04 等）

#### Initiating（2）

| 过程 | 状态 | idea-pmo 对应 |
|------|------|---------------|
| 制定项目章程 | ✓ | initiation-charter → charter |
| 识别干系人 | △ | F：干系人登记（无模板）；T：隐含在 project-context |

#### Planning（24）— 仅列与 skill 相关的代表过程

| 过程 | 状态 | 对应 / 缺口 |
|------|------|-------------|
| 制定项目管理计划 | △ | 碎片：charter + wbs + TD + roadmap；**无整合 PMP 单文档** |
| 规划范围管理 | ✗ | — |
| 收集需求 | ⊘ | idea-discuss / DECISIONS |
| 定义范围 | ✓ | charter 范围与非目标 |
| 创建 WBS | ✓ | wbs.md L1–L2 |
| 定义活动 | △ | rolling plan.md |
| 排列活动顺序 | ✗ | — |
| 估算活动持续时间 | △ | 仅人工步骤（ORD-07） |
| 制定进度计划 | △ | phase-roadmap（粗）；**模板/试跑缺失** |
| 规划/估算/制定预算（成本组） | ✗ | — |
| 规划质量管理 | △ | F 文字；acceptance 替代部分 |
| 规划资源管理 | ✗ | — |
| 估算活动资源 | △ | AI/人工标签 |
| 规划沟通管理 | △ | F 文字 |
| 规划风险管理 / 识别风险 / 分析 / 规划应对 | △ | TR-02 + F 文字；**无流程与模板** |
| 规划采购管理 | ✗ | — |
| 规划干系人参与 | △ | F 文字 |

#### Executing（10）

| 状态 | 说明 |
|------|------|
| **⊘ 全组** | INV-04；skill 止于 review + EXP 回写 |

#### Monitoring & Controlling（12）

| 过程 | 状态 | 对应 / 缺口 |
|------|------|-------------|
| 监控项目工作 | △ | phase review |
| 实施整体变更控制 | △ | 推翻 ORD → idea-discuss；**无 pmo 变更 log** |
| 确认范围 / 控制范围 | △ | acceptance.md |
| 控制进度 | ✗ | — |
| 控制成本 | ✗ | — |
| 控制质量 | △ | acceptance |
| 控制资源 | ✗ | — |
| 监督沟通 | ✗ | — |
| 监督风险 | ✗ | — |
| 控制采购 | ✗ | — |
| 监督干系人参与 | ✗ | — |

#### Closing（1）

| 过程 | 状态 | 对应 / 缺口 |
|------|------|-------------|
| 结束项目或阶段 | △ | review.md；**无收尾 checklist、无 lessons learned 模板** |

### 3. 与前期讨论（01–03 轮）的一致性

01 轮「与 full PMP 的刻意差异」表已预告省略：预算、全量词典、RACI、CCB、甘特。**本轮评审结论：skill 实现与该表大体一致**，额外发现：

1. **phase-roadmap** 在 03 轮后进入设计，但 **assets/试跑未跟上**（实现债）。
2. **模式 F** 在 02 轮是核心灵感之一，**至今无 EXP 验证**（EXP-01 合并试跑仅 T）。
3. **sub-agent** 为 AI 工作流新增需求，**不在 PMBOK 6 过程列表中**，宜映射为「资源管理 + 沟通 + 整合」扩展，而非硬套 49 过程。

### 4. 缺口优先级（讨论建议，非决定）

| 优先级 | 项 | 类型 | 理由 |
|--------|-----|------|------|
| P0 | 补 `phase-roadmap-template.md` + 试跑文件 | B 实现 | SKILL 已引用；INV-02 依赖 |
| P0 | 明确 rolling **circuit breaker**（acceptance 不过 → 不进下阶段） | C 弱覆盖 | Shape Up + M&C 最小闭环 |
| P1 | 模式 F 最小模板集（risk、stakeholder、change-log）或 **缩减 F 宣称** | B | 避免虚假完备 |
| P1 | `change-log.md` + DECISIONS 变更联动 | C | 整体变更控制最小实现 |
| P1 | sub-agent 流程（角色、handoff、manifest 读者） | D | 用户 todo |
| P2 | lessons learned 字段 / 收尾 checklist | C | Closing  enrich |
| P2 | `/pmo.analyze` 式交叉校验（artifact-index 硬规则） | C | SDD 层 |
| P3 | 成本/采购/CPM | A 刻意 | 除非 TR 新规则命中 |

### 5. PMBOK 7 视角（补充，非 skill 当前框架）

PMBOK 7 用 **8 绩效域** 替代 10 知识领域。idea-pmo 若要对齐 7 版，缺口感更强的域：

- **Measurement**（度量）：无 KPI/EVM
- **Uncertainty**（不确定性）：风险过程弱
- **Team**（团队）：sub-agent 可部分覆盖

**讨论倾向**：skill 描述写「PMP 思维」即可；**不必**改为 7 版绩效域术语，除非用户明确要求。

## 可验证尝试与继续/中止

### EXP-03（草案 — 模式 F 与 PMP 缺口补全）

| 项 | 内容 |
|----|------|
| 假设 | 补齐 P0（phase-roadmap + F 最小三模板）后，idea-pmo 在「PMP 完备性」上可自洽，且 manifest≤5 仍成立 |
| 尝试方案 | ① 补 `phase-roadmap-template.md` 并重生成试跑 `phase-roadmap.md`；② 选 **合规向虚构 project-context** 走 TR-04 → 模式 F，仅生成 risk + stakeholder + change-log 三模板；③ 对照 §2 过程表填覆盖问卷 |
| 成功信号 | F 试跑 GATE 可走通；artifact-index 与文件一致；用户认为「缺的 PMP 流程」清单可接受或已登记 enrich 路径 |
| **继续** | 将 P0/P1 写入 ORD；更新 tailoring-rules |
| **中止** | F 仍过重 → 缩减 F 为「T + 可选三附件」；不再称「全量 PM 树」 |
| 来源 | `04-idea-pmo-pmp-gap-review.md` §EXP-03 |

### EXP-04（草案 — sub-agent PM 流程）

| 项 | 内容 |
|----|------|
| 假设 | 在 idea-pmo 中定义 sub-agent 角色/handoff 后，多 agent 执行可不破坏 INV-01/03/04 |
| 尝试方案 | spike：在 SKILL 增「Agent 资源管理」节 + plan.md 任务表增加 `agent` 列；试跑 1 个需 sub-agent 的 phase |
| 成功信号 | 任务归属清晰；manifest 仍 ≤5；无越权 Execute |
| **继续** | ORD 固化 agent 列与 handoff 模板 |
| **中止** | 与 INV-04 冲突 → sub-agent 归独立 execute skill |
| 来源 | 用户 @temp.md todo；`04-…md` §4 P1 |

## 本轮决定

### 已确定 — 原则性不变量（新增/修订）

（无 — 本轮为评审；INV 不变）

### 已确定 — 普通决定（新增/修订）

（无 — 待用户确认优先级与 EXP）

### 待确认（下轮继续）

1. **P0 实现债**：是否立即补 phase-roadmap 模板 + 试跑文件？
2. **模式 F**：补模板 vs 缩减宣称？
3. **EXP-03 / EXP-04** 是否纳入 DECISIONS 待验证表？
4. **sub-agent**：放在 idea-pmo 还是独立 execute skill？
5. **变更 log**：pmo 层最小变更控制是否纳入 T 模式默认产物？

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| — | 本轮无新 INV/ORD | ✓ |
| EXP-03 | 草案（未入汇总） | — |
| EXP-04 | 草案（未入汇总） | — |

讨论状态同步：维持 **`ready-for-implementation`**（缺口评审不推翻试跑结论）；**实现债与 F 未验证** 记为开放项

同步完成时间：2026-05-21

## 开放问题（下轮）

1. 上表 P0–P3 你的优先级排序？
2. temp.md「阶段计划」是否指 **phase-roadmap（粗）** 还是 **rolling plan**？（设计两者都有）
3. 是否需要一张 **「idea-pmo × PMBOK 49 过程」** 常驻对照表放进 skill assets？

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-21 | PMP 缺口评审初稿 |
