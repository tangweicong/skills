---
name: proj-run
description: >-
  PMP Executing skill 承接 proj-plan 的 phase-NN/plan.md（必含 Sub-agent
  dispatch manifest · ORD-21 5 字段闭环），负责 sub-agent 调度、model-tier
  选择（3 Mode：α 自动 dispatch / β APM message bus 占位 / γ 手动模型切换）、
  validation gate（structural/lint/behavioral · ORD-22）、失败 escalate 回
  phase-NN/acceptance.md。承接 PMP 6 Executing 中 Direct & Manage Project Work
  + Manage Quality + Manage Project Knowledge 3 项（ORD-18），其余 7 项刻意外置。
  与 proj-plan 接口契约 = phase-NN/plan.md（artifact-level 文件契约）。
compatibility: >-
  Reads docs/pmo/phase-NN/plan.md (from proj-plan). Writes docs/pmo/phase-NN/
  acceptance.md back. Optionally generates .cursor/agents/*.md (Mode α) or
  .apm/bus/ structure (Mode β placeholder). Cursor sub-agent model field has
  legacy plan limitation; see ORD-16 disclosure inside.
---

<!--
input:  docs/pmo/phase-NN/plan.md（由 proj-plan 产出；必含 ## Sub-agent dispatch manifest 段 · ORD-21 5 字段闭环）
output: docs/pmo/phase-NN/acceptance.md（含 validation 结果 + token cost + escalate 标记）
        + .cursor/agents/*.md（Mode α 时；usage-based plan）
        + .apm/bus/ 目录（Mode β 时；占位无 runtime）
        + docs/pmo/artifact-index.md 追加（sub-agent 产出登记）
pos:    PMP Executing Process Group；与 proj-plan 串联在 PMP Planning 之后

修改本文件后，请同步更新根 README.md 的 4 skill 索引表与 proj-run 详细节（skills/README.md 已于 1.2.0 合并至根 README）。
-->

# 执行调度（proj-run）

承接 proj-plan 的 **`docs/pmo/phase-NN/plan.md`**（必含 `## Sub-agent dispatch manifest` 段 · ORD-21 5 字段闭环），负责 **PMP Executing Process Group** 的 sub-agent 调度、model-tier 选择、validation gate、失败 escalate。

**执行归本 skill；规划与商业论证不归本 skill**（规划 → `proj-plan`；商业论证 → `proj-experts` + `proj-shape`）。

## 设计 vision

proj-run 是 **PMP Executing Process Group** 的承载者，与 `proj-experts`（商业论证）→ `proj-shape`（决议收敛）→ `proj-plan`（Initiating + Planning + 规划侧 M&C + 阶段 Close）构成完整 proj-* 流水线（对应 PMP 4 大 Process Group）。

**角色分工对应 [Agentic PM 框架 Supervised-AI mode](https://arxiv.org/html/2601.16392v1)**：

| 角色 | 谁担任 | 职责 |
|------|--------|------|
| **Sponsor + PM 关键决策权** | **人** | execute 过程中的 GATE 审批 / validation 反复失败时 abort/retry 决策 / 关键 trade-off |
| **PM 执行 + sub-agent 调度** | **AI**（父 agent） | 按 model-tier 策略调度 sub-agent / 评审 sub-agent 输出 / 跑 validation / 维护 acceptance.md + artifact-index.md |
| **Specialist 执行** | **Sub-agent**（角色由 dispatch manifest 指定）| 单一 task 起草 / 评审 / 审计；fire-and-forget；不得越权改其它文件 |

与 [PMBOK 8 AI Appendix](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence) 立场对齐：**AI augment, human accountable for critical decisions**（特别是 validation 反复失败时的 escalate）。

**继承 proj-plan 的 JIT 规划原则（ORD-27）**：proj-run 只执行**当前阶段**那份「恰好足够」的 rolling-wave plan，**不**把未来阶段的细节提前拉进来执行。执行侧的「恰好足够」已落在两处既有机制，无需新增：**§Sub-agent dispatch 决策树**（不为了用而用——只在该 dispatch 时 dispatch）+ **iteration budget**（不过度迭代）。

## 立场声明（借鉴 / 自创）

> 让用户与 agent 能逐条判断"这是行业标准 / 借鉴 / 本 skill 自创"。**未在此声明的术语不应被当作 PMI 行业标准。**

### 基准版本（借鉴的真实标准）

| 来源 | 用于 | 出处 |
|------|------|------|
| **PMBOK 6** Executing Process Group（10 过程）| 覆盖范围基准；承接 3 项 + 刻意外置 7 项（ORD-18） | PMBOK Guide 6th Edition (PMI, 2017) |
| **PMBOK 7** Tailoring 原则 | "deliberate choice" 边界裁剪 | [PMI Tailoring PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) |
| **PMBOK 8** AI Appendix | 人 / AI 责任分工原则（延续 proj-plan ORD-11）| [AI in PMBOK 8](https://mypreppilot.com/pmp/learn/pmbok-8th-edition-ai-artificial-intelligence) |
| **Aider architect/editor 模式** | model-tier 编排原理（强推理模型规划 + 便宜模型执行）；5 字段闭环 dispatch manifest 设计灵感（ORD-21）| [Aider blog 2024-09-26](https://aider.chat/2024/09/26/architect.html) |
| **Anthropic Claude Code subagents** | Supervisor + Specialists 模式（96.3% 成功率）；blast radius containment 原则；sub-agent dispatch 决策树（ORD-20）| [Claude Code agents docs](https://code.claude.com/docs/en/agents.md) |
| **Cursor `.cursor/agents/*.md`** | Mode α 实际 dispatch 实现方式 | [Cursor Subagents 完整指南](https://medium.com/@codeandbird/cursor-subagents-complete-guide-5853e8d39176) |
| **APM 框架** | Mode β Message Bus 跨 sub-agent 通信备选（占位 · 无 runtime）| [APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md) + [APM-Auto fork](http://github.com/sdi2200262/apm-auto) |

### 本 skill 自创术语（**不是** PMI 标准）

| 术语 | 含义 | discuss 出处 |
|------|------|------|
| **3 Mode 表（α / β / γ）** | proj-run 的 3 个执行模式（按用户 plan 类型 + 跨 session 需求选择） | `docs/discuss/07-…md` §F1；DECISIONS.md ORD-19 |
| **Dispatch manifest 5 字段闭环** | manifest 段每条 task 必含 objective / specialist / validation criteria / iteration budget / escalate 5 字段 | `docs/discuss/08-…md` §视角 B；DECISIONS.md ORD-21 |
| **Validation gate 3 类** | structural / lint / behavioral 3 类 validation 分类 | `docs/discuss/08-…md` §视角 B 延伸；DECISIONS.md ORD-22 |
| **Sub-agent dispatch 决策树** | "task 输出是否需要被父 agent 持续回溯"作为第一判据；不按 cost | `docs/discuss/08-…md` §视角 C；DECISIONS.md ORD-20 |
| **PMP 6 Executing 边界声明** | 承接 3 项 + 刻意外置 7 项的边界（与 proj-plan ORD-10 同构纪律）| `docs/discuss/08-…md` §视角 A；DECISIONS.md ORD-18 |

### ORD-16 · Cursor sub-agent 当前约束披露（重要）

> 用户/agent 必须知晓的当前实现限制：

【已公开立场】Cursor sub-agent 的 `model` 字段在 **legacy request-based pricing plan 被 server 端忽略**——subagent 会 silently fallback 到父 model；仅 usage-based plan 的 expanded model selection 已 rolling out。详见 [Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736)。

**进一步约束（EXP-04 试跑发现）**：即使在 usage-based plan 下，Cursor Task tool 可调度的 sub-agent model 列表通常**只含 Composer Fast 不含 Composer Standard**——后者价差 30x，前者价差仅约 5x。这影响 model-tier 经济性测算（详见 §失败模式 F1）。

3 Mode 选择策略见下一节。

## PMP 6 Executing 边界声明（ORD-18 · 与 proj-plan ORD-10 同构）

> 按 [PMBOK 7 tailoring](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) 的 "deliberate choice" 原则做 just-enough process。

**承接**（3 项；与 sub-agent dispatch + validation 强相关）：

| PMBOK 6 Executing 过程 | proj-run 落实方式 |
|----------------------|-------------------|
| **Direct & Manage Project Work** | sub-agent dispatch（按 dispatch manifest 执行 plan.md 任务）|
| **Manage Quality** | validation gate（3 类：structural / lint / behavioral · ORD-22）|
| **Manage Project Knowledge** | sub-agent 产出登记到 artifact-index.md（避免 source of truth 分裂；INV-03 精神）|

**刻意外置**（7 项；由对话 / proj-plan handoff / 人工分配承接）：

| PMBOK 6 Executing 过程 | 外置原因 | 替代承接 |
|----------------------|---------|----------|
| Acquire Resources | 个人/小团队场景无资源采购 | proj-plan handoff 字段 + 人工 |
| Develop Team | 同上 | 人工 |
| Manage Team | 同上 | 人工 |
| Manage Communications | sub-agent 间沟通仅通过 manifest + artifact-index | proj-plan integration-plan |
| Implement Risk Responses | 由 proj-plan circuit breaker 触发 | proj-plan |
| Conduct Procurements | 项目级采购属 proj-plan ORD-10 已声明不含 | proj-plan / 对话 |
| Manage Stakeholder Engagement | 同 Manage Communications | proj-plan |

## 3 Mode 表（ORD-19 · 自创术语）

> Mode 选择按 **plan 类型 + 是否跨 session** 决定，**不**按 cost（视角 C 关切：cost 是 by-product 不是判据）。

| Mode | 触发条件 | 实现方式 | 适用 plan 类型 | 模板引用 |
|------|---------|----------|----------------|---------|
| **α**（自动 dispatch）| usage-based plan + 同一 IDE session 内 | `.cursor/agents/<name>.md` + 父 agent 用 Task tool 直接调用 sub-agent | usage-based | [`assets/cursor-agents-template.md`](assets/cursor-agents-template.md) |
| **β**（message bus）| 跨 IDE session / 跨设备 / 单一 sub-agent 输出 > 父 context 承载 / 多 sub-agent 并行协作 | `.apm/bus/` 文件级通信；每个 sub-agent 一个独立 chat session；用户 cp/mv shuttle 消息（APM 原版）或 APM-Auto fork 自动化 | 任意 | [`assets/message-bus-template.md`](assets/message-bus-template.md)（**占位 · 无 runtime**）|
| **γ**（手动模型切换）| legacy request-based plan + 同一 IDE session | 父 agent 默认 `@composer`；规划/评审节点用户手动 `@opus` 切换；**不**依赖 sub-agent dispatch | legacy request-based | — |

### Mode 选择决策树

```text
1. 用户当前 plan 是 usage-based 还是 legacy？
   ├─ usage-based →
   │   ├─ 单一 sub-agent 输出预期 > 父 context（>50K tokens）?
   │   │   ├─ 是 → Mode β（message bus；占位 + 用户人工 shuttle）
   │   │   └─ 否 → Mode α（自动 dispatch；推荐）
   │   └─ 需跨 IDE session 工作?
   │       ├─ 是 → Mode β
   │       └─ 否 → Mode α
   └─ legacy → Mode γ（手动切换；sub-agent 自动 dispatch 受限）
2. 任何 plan 类型下，多 sub-agent 并行协作场景 → 升 Mode β
```

**实操默认**（EXP-04 试跑验证）：legacy plan 用户走 Mode γ；usage-based 用户走 Mode α；β 仅在前述特定触发条件时启用。

## Sub-agent dispatch 决策树（ORD-20 · 自创术语）

> 决定一个 task **是否该交给 sub-agent**（不是"该交给哪个 model"——那是 model-tier 问题，由 3 Mode 决定）。

**第一判据 = task 输出是否需要被父 agent 持续回溯**（依据 [Claude Code agents docs](https://code.claude.com/docs/en/agents.md) "side task" 定义）：

| 判据 | 是 | 否 |
|------|----|----|
| task 输出是否需要被父 agent 持续回溯（多次引用 / 跨章节一致性 / 持续修订）| **✗ 不该 sub-agent**（父 agent 直写）| ✓ 候选 sub-agent |
| task 是否 fire-and-forget（一次完成归档，父引用结果即可）| ✓ 候选 sub-agent | ✗ 不该 sub-agent |
| task 内部是否 context 密集（多文件/多章节相互依赖）| ✗ 不该 sub-agent | ✓ 候选 sub-agent |

**判据**：**3 条都倾向 ✓ → sub-agent**；**任一 ✗ → 父 agent 直写**。

### 反模式（明确不该 sub-agent）

- **SKILL.md / 主文档跨章节一致性写作** → 父 agent 直写（章节引用密集；validation 难一行命令判定整体一致性）
- **跨多文件同步更新**（如 DECISIONS.md + 多个 artifact 一起改）→ 父 agent 直写
- **决策性内容**（如选择哪个 ORD 修订）→ 父 agent + 人审

**cost 是 by-product 不是判据**：如果用 cost 决定 dispatch（"贵的活给便宜 model"），会出现"Composer 写出来的 SKILL.md 与 plan.md 冲突，父 agent 已无法回看 sub-agent context 修复"→ 重新交付循环反而比父直写贵。

## Dispatch manifest（ORD-21 5 字段闭环 · 强制）

> 完整 schema + 字段说明 + 完整示例 + 使用规则见 [`assets/dispatch-manifest-template.md`](assets/dispatch-manifest-template.md)。

**5 字段闭环**（缺任一项 → proj-run 回退 proj-plan 补齐，不自行补全）：

| 字段 | 含义 |
|------|------|
| **objective** | task ID + 一句话目标 |
| **specialist** | sub-agent 角色 slug（`subagent:coder` / `subagent:reviewer` / `subagent:auditor` / `subagent:explorer`）|
| **validation criteria** | **可由父 agent 一行 shell/grep 命令判定**的判据列表（如 `test -f` / `grep -c "…" ≥ N` / `wc -l ≤ N`）|
| **iteration budget** | 重试次数上限（典型 2；auditor 1）|
| **escalate** | 超出 budget 时的回退路径（回父 / 回 proj-plan / 回 proj-shape）|

**与 ORD-15 的关系**：proj-plan 的 plan-template.md 中 `## Sub-agent dispatch manifest` 段是承诺字段（v0 可选；EXP-04 passed 后升级为强制按本 5 字段闭环）。proj-plan 只规划 specialist 类型与 validation；**model 选择由 proj-run 按 3 Mode 表决定，manifest 内禁止指定具体 model 名**。

## Validation gate（ORD-22 三类 · 强制）

> 完整定义 + 示例命令 + 失败 escalate 流程见 [`assets/validation-gate-template.md`](assets/validation-gate-template.md)。

| Gate 类 | 含义 | 典型命令示例 |
|--------|------|--------------|
| **structural** | 文件存在 / 字段齐 / 行数上限 | `test -f path`、`wc -l file ≤ N`、`grep -c "字段" file ≥ N` |
| **lint** | validate_skills.py / markdown 结构 / YAML frontmatter | `uv run scripts/validate_skills.py`、YAML parse |
| **behavioral** | 关键字 grep（正向断言）/ 负向断言（确认无违规出现）| `grep -c "需求关键字" file ≥ 1`、`grep -c "禁用关键字" file = 0` |

**失败处理流程**（与 ORD-21 iteration budget 联动）：

```text
sub-agent 产出 → 父跑 validation
  ├─ 全部 pass → 归档到 artifact-index + 进下一 task
  └─ 任一 fail → 检查 iteration budget
       ├─ 仍有 budget → 父给失败原因 + 修订要点 → 重 dispatch sub-agent
       └─ budget 用尽 → 按 dispatch manifest §escalate 字段执行：
            ├─ 回父 agent 接手改写（最常见）
            ├─ 回 proj-plan 改 plan / dispatch manifest（如 validation 标准不合理）
            └─ 回 proj-shape 开新轮（如发现需新 INV/ORD/EXP）
```

## 工作流

### 0. 前置

- proj-plan 已交付 `docs/pmo/phase-NN/plan.md`（含 `## Sub-agent dispatch manifest` 段 · 5 字段闭环）
- GATE-3 已通过（用户审过 plan + dispatch manifest）
- 父 agent 已确定 3 Mode（α/β/γ）— 通过 §3 Mode 选择决策树

### 1. Dispatch 准备

- 读 plan.md `## 任务` 表 + `## Sub-agent dispatch manifest` 段
- 对每条 sub-agent task 跑 §Sub-agent dispatch 决策树确认确实该 sub-agent（防止"为了用而用"）
- 准备 dispatch prompt：必须 self-contained（APM 原则：含 objective、context、reference 文件路径、validation 自检命令）

### 2. Dispatch 与 validation 循环

按 plan.md `## 活动依赖` 节顺序（典型串行；视场景可并行）逐 task 执行：

1. **Dispatch**：按 3 Mode 调用 sub-agent
   - Mode α：父用 Task tool 调 `.cursor/agents/<name>.md` 配置的 sub-agent
   - Mode β：父写 task 到 `.apm/bus/tasks/<task-id>.md`；通知用户开新 chat session 接手
   - Mode γ：父 agent IDE 默认；用户 `@composer` 切换；任务对话内完成
2. **Validation**：sub-agent 产出后，父跑 §Validation gate 3 类
3. **Iteration**：失败 → 按 ORD-21 iteration budget 重试；用尽 → escalate
4. **归档**：通过 → 登记到 `docs/pmo/artifact-index.md` sub-agent 产出段 + 更新 `acceptance.md` §Sub-agent dispatch log 与 §token cost 段

### 3. acceptance.md 回写

按 [`assets/acceptance-template.md`](assets/acceptance-template.md) 维护：

- §validation 结果（structural / lint / behavioral 三类分类）
- §token cost（每个 dispatch 的 input/output token 估算 + 累计 cost）
- §escalate 标记（若有触发 escalate 的 task）
- §GATE 联动（acceptance 通过 → GATE-N 解锁 / 失败 → circuit breaker）

### 4. Phase 收尾

- acceptance 全 checkbox 通过 → 触发 proj-plan `review.md` 流程
- 全部 sub-agent 产出登记到 artifact-index.md（含路径 / 时间 / iteration 次数 / 通过 validation 项）
- 试跑 / 验证类 phase（含 EXP-xx）：把试跑数据回写到 `docs/discuss/DECISIONS.md` EXP-xx 状态行

## Circuit breaker（硬规则）

> 借鉴 proj-plan §Circuit breaker；本 skill 的失败模式直接触发以下硬规则。

| 事件 | 动作 |
|------|------|
| 单 task validation 失败 > iteration budget | 按 dispatch manifest §escalate 字段执行 |
| 全 phase sub-agent 累计失败 > 3 次 | abort 本 phase + 通知 GATE + 回 proj-plan 改 plan / 回 proj-shape 开新轮分析 |
| sub-agent 输出严重偏离 dispatch prompt（即"Opus plan 无法被 Composer 解读"）| 立即 abort + 回 proj-plan 改 dispatch manifest §validation criteria 更明确 |
| Cursor sub-agent 关键 feature 阻塞（如 Task tool 不可用 / model 字段全失效）| 切换 Mode γ 手动；记 change-log；通知 GATE |
| sub-agent 产出推翻 INV/ORD/EXP（如发现需新决定）| 立即 abort task + 回 proj-shape；**不在 execute 层改决定**（INV-04 精神延续）|
| acceptance 不通过 | proj-plan **不得**创建下一 `phase-NN/plan` |

## 失败模式（明示反模式 · 含 EXP-04 试跑发现）

- **F1**（EXP-04 试跑发现）：把 sub-agent 主要当 cost 优化工具用 — Cursor 当前 sub-agent 通常只能调度 Composer Fast（5x 价差）不能调度 Composer Standard（30x 价差）；plan 阶段父 agent 用 Opus 的固定成本在小项目中可能占 baseline >1/3，吃掉 model-tier 算术天花板。**对策**：把 sub-agent 用法定位为 context 隔离（视角 C），cost 节省是 by-product；小项目不强求 model-tier；大项目（多 phase / 大 execute）才能稀释 plan 成本
- **F2**：把所有 task 都塞给 sub-agent 追求 cost 节省 — 违反 §Sub-agent dispatch 决策树；会出现"sub-agent 输出与父 plan 冲突，父无法回看 sub-agent context 修复"→ 重新交付循环反而比父直写贵
- **F3**：validation criteria 写成"质量好""结构完整"等模糊判据 — sub-agent 会"自我宣告完成"；**对策**：validation 必须可由父 agent 一行 shell/grep 命令判定（ORD-22 三类标准）
- **F4**：iteration budget 设过大（如 5+）— sub-agent 反复失败时浪费 cost；典型 budget = 2（coder）/ 1（auditor）；失败超 budget 立即 escalate
- **F5**：跳过 §Sub-agent dispatch 决策树直接 dispatch — 会把"该父直写"的 task（如 SKILL.md / 跨多文件同步）误派给 sub-agent；**对策**：每 dispatch 前 3 判据自检
- **F6**：依赖 `model:` 字段在 legacy plan 自动 dispatch — silently fallback 到父 model；**对策**：检测 plan 类型；legacy → Mode γ；usage-based → Mode α
- **F7**：用 sub-agent 写新决定（INV/ORD/EXP）— 违反 INV-04 精神（execute 层不写新决定）；**对策**：sub-agent 发现需新决定立即 abort + 回 proj-shape
- **F8**：sub-agent 产出未登记到 artifact-index.md — source of truth 分裂；后续 phase 找不到产出归属；**对策**：每次 validation 通过后立即追加登记
- **F9**：grep validation 命令在父 agent shell 中因 `grep -c` 返回非零退出而被 `set -e` 中断 — 实际 0 命中是"pass"但 shell 看成 fail；**对策**：validation 命令统一用 `$(grep -c "pattern" file 2>/dev/null || echo 0)` 兜底
- **F10**：dispatch prompt 不 self-contained — sub-agent 不知道你不知道的上下文；按 APM 原则，prompt 必须含 objective + 完整 context + reference 文件路径 + validation 自检命令

## 触发词

proj-run · 执行调度 · sub-agent · 子代理 · subagent dispatch · model-tier · 模型分层 · Opus 规划 · Composer 执行 · phase 执行 · dispatch manifest · validation gate · Mode α · Mode β · Mode γ · cursor agents · `.cursor/agents/` · message bus · `.apm/bus/` · APM · iteration budget · escalate · runway

## 不触发本 skill

- proj-plan 尚未输出 phase-NN/plan.md / 缺少 `## Sub-agent dispatch manifest` 段 → 回 proj-plan 先补齐
- DECISIONS / proj-shape 阶段还在进行 → 回 proj-shape
- 用户只要一次性写代码 / 改 1 文件 → 直接执行，不必走本 skill 流程
- 单 task 输出需要被父持续回溯（决策树 ✗）→ 父 agent 直写

## 模板索引

| 文档 | 模板 |
|------|------|
| Dispatch manifest（5 字段闭环 · ORD-21）| [`assets/dispatch-manifest-template.md`](assets/dispatch-manifest-template.md) |
| Acceptance（validation 结果 + token cost + escalate · ORD-15 输出契约）| [`assets/acceptance-template.md`](assets/acceptance-template.md) |
| Cursor agents（Mode α · YAML frontmatter + legacy warning · ORD-19）| [`assets/cursor-agents-template.md`](assets/cursor-agents-template.md) |
| Message bus（Mode β 占位 · `.apm/bus/` · ORD-19）| [`assets/message-bus-template.md`](assets/message-bus-template.md) |
| Validation gate（3 类 · structural / lint / behavioral · ORD-22）| [`assets/validation-gate-template.md`](assets/validation-gate-template.md) |
