# 03-idea-pmo两轮启动与决定收敛

| 字段 | 值 |
|------|-----|
| 轮次 | 03 |
| 主题 | 用户确认收敛；idea-pmo 双轮启动；Coach 人机确认 |
| 日期 | 2026-05-19 |
| 状态 | discussed |
| 分析层 | best-minds-grounded（轻量：对照 PMBOK Initiate/Plan 与 Shape Up betting） |
| 承接 | 轮次 02 §用户回复 |

## 用户输入（本轮）

用户于 `02-ai全量pmp与智能裁剪.md` §用户回复 确认：

| # | 原问题 | 用户回复 |
|---|--------|----------|
| 1 | INV-01′–03′、ORD-05–06 取代轮次 01 草案？ | **同意** |
| 2 | 默认 T / F / AI 推荐？ | **分两轮**：第一轮基本信息 + 建议模式，类似章程授权；**用户确认后再详细规划** |
| 3 | manifest 硬上限 | **5 项** |
| 4 | EXP-03 与 EXP-01 合并？ | **可以** |
| 5 | skill 命名 | **idea-pmo** |
| O1 | 重量转移到 machine corpus？ | **同意** |
| O2 | 高合规是否选 F？ | **同 #2**：AI 建议，用户确认 |
| O3 | Coach 规则表 vs LLM？ | **同 #2**：AI 建议，用户确认 |

## 事实与假设

### best-minds-grounded · 轻量框定

| # | 对照问题 | 查证结论 |
|---|----------|----------|
| Q1 | 用户「两轮启动」是否合业界实践？ | PMBOK：**Initiate（章程/授权）与 Plan（详细规划）分过程组**；upfront 宜最小。[When to tailor](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s4-when-to-tailor/) |
| Q2 | 「AI 建议 + 人确认」模式？ | Shape Up：**betting table** 审 shaped pitch 后一次性授权 building；非 PM 单方面定 scope。[The Betting Table](https://basecamp.com/shapeup/2.2-chapter-08) |
| Q3 | DSDM Coach 与 hybrid 裁剪？ | PMBOK：裁剪宜 holistic，PM 未必会裁；Coach 专责设计体系——skill 可 **规则库 + LLM 建议 + GATE 确认** 实现 hybrid。[The difficulty of tailoring](https://pmbok.guide/s2-understanding-and-interpreting/s1-pmbok-principles/s07-tailor-based-on-context/s3-the-difficulty-of-tailoring/) |

### 已查证事实

- 用户已**显式确认**轮次 01–02 合并后的 INV/ORD 方向（`02-…md` §用户回复 @2026-05-19）。
- 轮次 02 已论证：**模式 T/F 均为 tailoring 结果**；manifest 是重量控制的核心机制。
- `skills/idea-implement/` 仍存在于仓库，待 **idea-pmo** 重写后废止或迁移（尚未执行）。

### 外推（非原话）

- **外推 A**（依据 Initiate/Plan 分离 + 用户两轮诉求）：**Round A = Initiate 包**（TD 草案 + 模式建议 + initiation charter + manifest 草案）；**Round B = Plan 包**（charter 定稿、WBS、模式 F 全量树等）——不是两次完整 PMP，而是 **一次 idea-pmo 调用内的两个 GATE**。
- **外推 B**（依据 Coach hybrid）：固定规则表保证 **一致性**；LLM 负责 **读 DECISIONS 上下文给建议**；**GATE-0 人确认** 保证 **不误裁/不误选 F**——三者缺一不可。

### 待验证 / 未查证

- 双轮启动下 Round A 人类阅读能否稳定 **≤5 分钟** —— 并入 **EXP-01**（已与 EXP-03 合并试跑）。
- `docs/pmo/` vs `docs/implement/` 目录命名 —— 本轮 **ORD-01** 定为 `docs/pmo/`，待落地时创建。

## 讨论

### 1. 决定收敛（轮次 01 + 02 → 正式 ID）

用户「同意」取代草案，以下写入 **DECISIONS.md**（本轮同步）。

**原则性不变量**

| ID | 决定 |
|----|------|
| INV-01 | 人类**只读** `human-read-manifest.md` 所列文档（**≤5 项**）；**禁止**要求人读全量 PM artifact 树 |
| INV-02 | 细任务与逐步验收**仅**出现在 `phase-NN/plan.md`（rolling）；启动与 Plan 轮**不得**生成 phase 级 task-list |
| INV-03 | 无论模式 T/F，**manifest 所列 GATE 未通过**，不得生成下游 artifact |
| INV-04 | **idea-pmo** 不含**执行**（编码、物理交付、一次性对话式 patch）；止于阶段 `review` 与 EXP 状态回写 |

**普通决定**

| ID | 决定 |
|----|------|
| ORD-01 | 落地 skill 名 **`idea-pmo`**；产物根目录 **`docs/pmo/`**；废止 `idea-implement` 命名（迁移重写） |
| ORD-02 | `charter.md` 替代 `architecture.md`；`wbs.md` 替代 `phase-plan.md` |
| ORD-03 | **双轮启动**（见 §2）；第一步非直接写全量 charter，而是 **Round A 启动包** |
| ORD-04 | **Coach hybrid**：内置 tailoring 规则库 + AI 读 DECISIONS 给 **模式 T/F 与产物建议** → **GATE-0 用户确认** 后生效；agent 不得单方面选定模式 |
| ORD-05 | `human-read-manifest.md` **硬上限 5 项**（含 GATE 检查点） |
| ORD-06 | 模式 F 须 `artifact-index.md`；模式 T 须至少 `artifact-index` 简表（路径 + 关联 DECISIONS ID） |
| ORD-07 | AI 工作步骤不给人工时长预估；人工步骤仅在 `phase-NN/plan.md` 标注预估时间 |
| ORD-08 | **EXP-01 与 EXP-03 合并试跑**（本仓库重写 idea-pmo 为试跑项目）；试跑前可并行起草 skill |

### 2. idea-pmo 双轮启动（用户 #2 的形式化）

```text
DECISIONS（idea-discuss · ready）
         │
         ▼
┌────────────────────────────────────────────────────────────┐
│  Round A · Initiate（启动授权）                             │
│  AI（Coach hybrid）产出：                                     │
│    · project-context.md      — 向用户收集/确认的基本信息      │
│    · tailoring-decision.md   — 建议模式 T/F、产物清单、依据   │
│    · initiation-charter.md   — 章程草案（综合 DECISIONS）     │
│    · human-read-manifest.md  — 草案（全流程 ≤5 项预览）       │
│  人类此轮必读：manifest 中标记 [Round-A] 的 1–2 项            │
│         │                                                   │
│         ▼ GATE-0：用户确认 TD + 模式 + initiation charter   │
└─────────┼──────────────────────────────────────────────────┘
          │ 授权「进入详细规划」
          ▼
┌────────────────────────────────────────────────────────────┐
│  Round B · Plan（详细规划）                                 │
│  按已确认 TD 生成：                                           │
│    · charter.md（定稿）                                       │
│    · wbs.md（L1–L2；模式 T）或 + 全量 PM 树（模式 F）          │
│    · artifact-index.md                                      │
│    · manifest 更新：追加 GATE-1（charter）、GATE-2（wbs）等   │
│  仍不写 phase-NN/plan，直至对应工作包 GATE 通过              │
└─────────┼──────────────────────────────────────────────────┘
          ▼
   Rolling · phase-NN/plan + acceptance + review
          ▼
   执行（非 idea-pmo）
```

**与 PMBOK / Shape Up 的对照**

| 用户说法 | 映射 |
|----------|------|
| 第一轮像章程授权 | Round A + **GATE-0** ≈ Initiate + betting table 审 pitch |
| 确认后再详细规划 | Round B ≈ Plan 过程组；rolling wave 仍适用 |
| AI 建议模式 | Coach hybrid + TD；高合规时 AI **建议 F**，用户可 override 为 T |
| 人读子集 | Round A 只 expos  manifest 的 **[Round-A] 子集**；全流程仍 ≤5 |

**Round A 人类阅读预算（讨论约定）**

| manifest 项 | 内容 | 预估 |
|-------------|------|------|
| [Round-A] 1 | `initiation-charter.md` | ~3 min |
| [Round-A] 2 | `tailoring-decision.md`（模式 + 产物摘要） | ~2 min |

GATE-0 合并确认后进入 Round B；Round B 新增项计入 5 项上限内。

### 3. Coach hybrid 工作流（回应 O2、O3）

```text
规则库（skill 内 reference）
    ↓ 约束输出 schema
DECISIONS + project-context
    ↓ LLM 读上下文
tailoring-decision 建议（T/F + 产物列表 + 理由）
    ↓
GATE-0 用户确认 / 修订
    ↓
定稿 TD → Round B 生成
```

- **非**纯规则表：规则无法覆盖所有领域元数据。
- **非**纯 LLM：无规则易 cherry-pick（PMBOK 警告的 Frankenstein）。
- **失败降级**：用户否决 AI 建议 → 可强制 T；或回 **idea-discuss** 补 DECISIONS。

### 4. 讨论就绪评估

| # | 硬条件 | 满足 |
|---|--------|------|
| 1 | 成功标准已写入 INV/ORD | ☑ |
| 2 | 无阻塞性待确认 | ☑（模式选择 → GATE-0；合规 → AI 建议+人确认） |
| 3 | EXP + 降级路径 | ☑ EXP-01 合并试跑；中止→默认 T |
| 4 | INV 未摇摆 | ☑ 用户 @轮次02 确认 |

**结论**：决策集已闭合；**建议**标 `ready-for-implementation` 以启动 **idea-pmo skill 重写 + EXP-01 合并试跑**——须用户下条消息**显式确认「可以开工」**（skill 规则：agent 不得单方面设定 ready）。

### 5. 开放项（非阻塞）

| 项 | 建议 |
|----|------|
| `idea-implement` 目录 | 重写为 `idea-pmo` 后删除或留 redirect 说明 |
| EXP-02（GATE 硬编码） | 并入 idea-pmo skill 实现，与 EXP-01 试跑一并验证 |
| idea-discuss 硬约束 best-minds | 仍开放；可单独立项 |

## 可验证尝试与继续/中止

### EXP-01（修订：合并原 EXP-03）

| 项 | 内容 |
|----|------|
| 假设 | idea-pmo **双轮启动 + Coach hybrid + manifest≤5** 在试跑项目中可行；且（子假设）模式 F 相对 T 的完备性/重量 tradeoff 可接受 |
| 尝试方案 | **试跑项目 = 本仓库重写 idea-pmo**；走 Round A→GATE-0→Round B；并行生成 T 与 F 对照（或 TD 推荐 + 用户选一）；人只读 manifest [Round-A] + GATE 项；问卷 5 点 |
| 成功信号 | Round A 阅读 ≤5min；GATE-0 可决策；Round B 产物与 TD 一致；用户愿用双轮流程 |
| **继续** | 发布 idea-pmo skill；默认 Coach hybrid |
| **中止** | Round A 仍过重 → 缩 manifest [Round-A] 为 1 项；F 不可信 → 默认 T + F 仅合规显式启用 |
| 来源 | `03-idea-pmo两轮启动与决定收敛.md` §EXP-01；合并自 `02-…md` EXP-03 |

（EXP-03 合并入 EXP-01，不再单独跟踪）

## 本轮决定

### 已确定 — 原则性不变量

- [x] **INV-01** — 人类只读 manifest（≤5 项）；禁止要求读全量 artifact 树  
  **来源**：`02-ai全量pmp与智能裁剪.md` §用户回复 1、3；`03-…md` §决定收敛；用户 @轮次02 确认  
  → 已同步 DECISIONS.md

- [x] **INV-02** — 细任务仅出现在 rolling `phase-NN/plan`  
  **来源**：`01-implement-skill流程与pmp映射.md` §待确认 INV-01；`02-…md` §INV-02′；用户 @轮次02 同意取代  
  → 已同步 DECISIONS.md

- [x] **INV-03** — GATE 未过不得生成下游 artifact  
  **来源**：`02-…md` §INV-03′；用户 @轮次02 同意  
  → 已同步 DECISIONS.md

- [x] **INV-04** — idea-pmo 不含执行  
  **来源**：`01-…md` §待确认 INV-02；用户 @轮次02 同意取代  
  → 已同步 DECISIONS.md

### 已确定 — 普通决定

- [x] **ORD-01** — skill 名 `idea-pmo`；目录 `docs/pmo/`  
  **来源**：`02-…md` §用户回复 5；`03-…md` §讨论  
  → 已同步 DECISIONS.md

- [x] **ORD-02** — charter + wbs 命名  
  **来源**：`01-…md` §ORD-01；用户 @轮次02 同意  
  → 已同步 DECISIONS.md

- [x] **ORD-03** — 双轮启动 Round A/B  
  **来源**：`02-…md` §用户回复 2；`03-…md` §2  
  → 已同步 DECISIONS.md

- [x] **ORD-04** — Coach hybrid + GATE-0  
  **来源**：`02-…md` §用户回复 O2、O3  
  → 已同步 DECISIONS.md

- [x] **ORD-05** — manifest ≤5  
  **来源**：`02-…md` §用户回复 3  
  → 已同步 DECISIONS.md

- [x] **ORD-06** — artifact-index 要求  
  **来源**：`02-…md` §ORD-06；用户 @轮次02 同意  
  → 已同步 DECISIONS.md

- [x] **ORD-07** — AI/人工时长规则  
  **来源**：`01-…md` §ORD-04；用户 @轮次02 同意  
  → 已同步 DECISIONS.md

- [x] **ORD-08** — EXP-01 与 EXP-03 合并试跑  
  **来源**：`02-…md` §用户回复 4  
  → 已同步 DECISIONS.md

### 待确认（下轮 / 开工前）

- ~~是否显式确认 **ready-for-implementation**~~ → 用户 @2026-05-19「可以开工」✓
- ~~Round A manifest 固定 2 项~~ → **ORD-09** ✓

## 用户确认（2026-05-19）

- 「可以开工」→ `ready-for-implementation`；EXP-01 running
- 「Round A 固定 2 项」→ ORD-09

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| INV-01–04 | 新增 | ✓ |
| ORD-01–08 | 新增 | ✓ |
| EXP-01 | 修订（合并 EXP-03） | ✓ |
| EXP-03 | 合并废止 | ✓ |

| ORD-09 | 新增 | ✓ |

讨论状态同步：`deciding` → **`ready-for-implementation`**（用户 @2026-05-19 可以开工）

同步完成时间：2026-05-19（开工实施）

## 开放问题（下轮）

1. 回复「可以开工」或等价语 → 标 ready，执行 idea-pmo 重写 + EXP-01。
2. Round A 是否再减为 **1 项** manifest（仅 initiation-charter，TD 作为附录）？

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-19 | 用户回复收敛 + 双轮启动设计 |
