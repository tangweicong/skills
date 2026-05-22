---
name: idea-pmo
description: >-
  PMP-style planning from docs/discuss/DECISIONS.md: docs/pmo/ with Coach hybrid
  tailoring, Round A/B initiate+plan, human-read-manifest (≤5), mode T/F,
  integration-plan + phase-roadmap (coarse) + rolling phase plans, change-log,
  SDD analyze gate, sub-agent handoff. AI maintains full artifact corpus; humans
  read manifest. Pairs with idea-discuss.
compatibility: >-
  Requires docs/discuss/DECISIONS.md (ready-for-implementation). Writes under
  project-root docs/pmo/. Updates EXP-xx in DECISIONS. Does not execute builds.
---

<!--
input: docs/discuss/DECISIONS.md
output: docs/pmo/（Round A/B + rolling phase-NN/）
pos: 落地规划 skill；idea-discuss 之后、执行之前

修改本文件后，请同步更新 skills/README.md。
-->

# Idea PMO（项目化落地规划）

承接 **`docs/discuss/DECISIONS.md`**，用 **PMP 计划分层 + SDD gate/analyze 纪律** 生成规划产物：AI 维护完整 artifact 集（可裁剪或全量），人类**只读** `human-read-manifest.md`（≤5 项）。

**规划归本 skill；讨论与执行不归本 skill**（讨论 → idea-discuss；编码/交付 → 对话或其它 skill）。

## PMP 计划 ≠ 仅 WBS

| 层 | 回答 | artifact | 何时写 |
|----|------|----------|--------|
| 范围 | 做什么 | `wbs.md` + charter | Round B · GATE-2 |
| 进度（粗） | 分几段、依赖、里程碑 | `phase-roadmap.md` | Round B · GATE-2（**无任务表**） |
| 整合 | 子计划索引 | `integration-plan.md` | Round B · GATE-2 后 |
| 进度（细） | 活动、执行者、依赖 | `phase-NN/plan.md` | 进阶段 · GATE-3 |
| 变更 | 整体变更控制 | `change-log.md` | T 默认；Round B 起 |

详见 [assets/pmp-sdd-map.md](assets/pmp-sdd-map.md)。

## 与 idea-discuss 的分工

| | idea-discuss | idea-pmo（本 skill） |
|---|--------------|----------------------|
| 问题 | 试什么？决定是什么？ | 怎么授权？怎么分解？怎么分阶段计划？ |
| 产出 | `docs/discuss/` | `docs/pmo/` |
| 边界 | 不写 PM artifact | 不写新 INV/ORD；不写代码/执行 |

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

## SDD 纪律

| 机制 | 实现 |
|------|------|
| Source of truth | `DECISIONS` + `artifact-index` + `integration-plan` |
| Gate | manifest GATE-0/1/2/N |
| Analyze | [assets/analyze-checklist.md](assets/analyze-checklist.md) — Round B 后、每阶段 acceptance 前 |
| 禁止越权 | GATE 未过不得生成下游；analyze 失败不得标 GATE 通过 |

## Coach hybrid（裁剪）

1. 读 [assets/tailoring-rules.md](assets/tailoring-rules.md) + `DECISIONS` + `project-context.md`。
2. 写 `tailoring-decision.md`：建议模式 T/F、产物清单、规则 ID。
3. **GATE-0**：用户确认；agent **不得**单方面定模式。

| 模式 | Round B 生成 |
|------|--------------|
| **T** | charter, wbs, phase-roadmap, **integration-plan**, **change-log**, artifact-index |
| **F** | 上列 + risk, stakeholder, communication, quality-plan（按需） |

## 工作流

### 0. 前置

- `DECISIONS.md` 为 `ready-for-implementation` 或用户显式授权。
- 确保 `docs/pmo/` 存在。

### Round A · Initiate

1. `project-context.md` → `tailoring-decision.md` → `initiation-charter.md`
2. `human-read-manifest.md`：**[Round-A] 固定 2 项** + 预留 GATE 槽位（≤5）
3. **GATE-0** 用户确认

### Round B · Plan

1. 定稿 `charter.md` → manifest **GATE-1**
2. 用户确认 GATE-1 → 并行写：
   - `wbs.md`（L1–L2，**无**阶段顺序表）
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
4. acceptance **不通过** → **禁止**下阶段 plan；EXP failed → 回 idea-discuss
5. 回写 `DECISIONS` EXP；变更记 `change-log`

### Circuit breaker（硬规则）

| 事件 | 动作 |
|------|------|
| acceptance 不通过 | 不得创建下一 `phase-NN/plan` |
| analyze 失败 | 不得标记 GATE 通过 |
| 推翻 ORD/INV | change-log + **idea-discuss** |

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

## 触发词

idea-pmo · 项目章程 · WBS · phase-roadmap · integration-plan · change-log · analyze · GATE · tailoring · sub-agent

## 不触发本 skill

- 尚无 DECISIONS / 讨论未就绪 → idea-discuss
- 只要一次性改代码 → 直接执行
