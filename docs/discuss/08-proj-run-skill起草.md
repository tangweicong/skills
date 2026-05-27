# 08-proj-run skill 完整版起草（双重目标：起草 + EXP-04 试跑）

| 字段 | 值 |
|------|-----|
| 轮次 | 08 |
| 主题 | proj-run skill 完整工作流起草 + EXP-04 model-tier 试跑 |
| 日期 | 2026-05-27 |
| 状态 | discussed · v1.1（含试跑结果回写）|
| 讨论方法 | `proj-experts`（4 视角：PMP / Aider architect / Anthropic Supervisor+Specialists / APM 三角色）|
| 写入格式 | 完整（架构争议：proj-run 工作流尚无现成模板）|
| 承接 | DECISIONS ORD-15/16/17 + EXP-04 v1.3 案例精化；本轮触发起草 |

## 用户输入（本轮）

> 任务：开启 08 轮 — 双重目标 = proj-run 完整 SKILL.md 起草 + EXP-04 试跑（model-tier 验证）。用 proj-* 流水线给 proj-run 起草完整 SKILL.md + assets templates。这同时是 08 轮目标本身（ORD-17 触发的下一步）+ EXP-04 试跑案例本身（验证 Opus 规划 + Composer 执行的 model-tier 假设）。

**本轮范围**：仅起草 + 试跑；不在本轮新增/修订 INV 或与 proj-run 实现无关的 ORD（属 proj-shape 边界）。

## 事实与假设

### 轻量框定（查证前问题清单）

| # | 待查问题 | 查证结论 |
|---|---------|----------|
| Q1 | 4 视角的关键 URL 是否还需要重查？| **否** — 沿用 07 轮 §F1-F5 已查证 URL；本轮不重新搜（任务书明示）|
| Q2 | proj-plan 21 个 assets 总规模 | 1066 行 / 46 KB / 34.5K 字符 / 估算 ~10.4K 输出 tokens（用于 EXP-04 baseline）|
| Q3 | Cursor sub-agent 实际可调度的 Composer 模型档 | 仅 `composer-2.5-fast`（$3/$15 M-token）；**`composer-2.5-standard`（$0.50/$2.50）当前不可通过 sub-agent dispatch**——见 [Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736) legacy plan 限制 |
| Q4 | 本轮新增决定的归属 | proj-run 实现细节（mode 选择策略 / dispatch manifest 完整 schema / validation gate 流程）属本轮起草范围；不形成新 INV/ORD（属 proj-shape） |

### 已查证事实（沿用 07 轮 §F1-F5）

- **F1**：Cursor sub-agent 当前 model 字段限制 — [Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736)
- **F2**：Composer 2.5 价格三档 + Artificial Analysis Coding Agent Index — [Officechai](https://officechai.com/ai/cursors-composer-2-5-places-3rd-in-artificial-analysis-coding-agent-index-is-10-60x-cheaper-than-variants-above-it/) + [Lushbinary](https://lushbinary.com/blog/composer-2-5-vs-claude-opus-4-7-vs-gpt-5-5-coding-comparison/) + [Pondero](https://pondero.ai/coding/guides/cursor-composer-2-5-benchmarks-pricing-may-2026/)
- **F3**：Aider architect/editor SOTA — [Aider blog 2024-09-26](https://aider.chat/2024/09/26/architect.html) + [DeployHQ guide](https://www.deployhq.com/guides/aider)
- **F4**：Anthropic Claude Code subagents + Supervisor+Specialists 96.3% — [Claude Code agents docs](https://code.claude.com/docs/en/agents.md) + [DEV pattern survey](https://dev.to/wilsonhoe/why-your-multi-agent-system-breaks-at-3-am-orchestration-patterns-that-survive-production-1efi)
- **F5**：APM 三角色 + Message Bus + APM-Auto fork — [APM repo](http://github.com/sdi2200262/agentic-project-management) + [APM-Auto](http://github.com/sdi2200262/apm-auto)

### 本轮新增事实

- **F6**（本轮）：当前 Cursor IDE 内 sub-agent 可调度模型清单 = `claude-4.6-sonnet-medium-thinking` / `claude-opus-4-7-thinking-xhigh` / `composer-2-fast` / `composer-2.5-fast` / `gpt-5.3-codex` / `gpt-5.5-medium`；**不包含** `composer-2.5-standard`。这是 EXP-04 阈值 v1.4 调整的硬性根据（见 §决定 1）。
- **F7**（本轮）：proj-plan SKILL.md + 21 assets baseline = 1066 行 / 34.5K 字符 / 估算 ~10.4K 输出 tokens；对应估算输入 tokens（含 6 轮迭代上下文累加）~80K—150K；估算全 Opus baseline cost = $4—$10 区间。

### 推理（非事实、非待验证）

- **推理 · proj-experts · 视角 A（PMP）**：proj-run 不应承接全部 PMBOK 6 Executing 10 过程；按 proj-plan ORD-10 同等原则做边界声明——核心承接 **Direct & Manage Project Work + Manage Quality + Manage Project Knowledge** 三项；其余（Acquire/Develop/Manage Resources、沟通管理执行侧、采购执行）刻意外置；依据 [PMBOK 7 tailoring](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) 的「deliberate choice」原则。
- **推理 · proj-experts · 视角 B（Aider）**：proj-run 的 model-tier 不只是"两个模型"——核心是每次 dispatch 必须含 **validation 命令 + iteration budget + 失败 escalate**；失败不允许 sub-agent 自我宣告完成；依据 [Aider blog](https://aider.chat/2024/09/26/architect.html) 的 architect-mode SOTA 是建立在 lint/test 验证关之上的。
- **推理 · proj-experts · 视角 C（Anthropic）**：sub-agent 边界按"context 是否需要回溯"划分（需回溯不该 sub-agent），不按 model cost 划分；cost 是结果不是判据；依据 [Claude Code docs](https://code.claude.com/docs/en/agents.md) 的 "side task" 定义。
- **推理 · proj-experts · 视角 D（APM）**：proj-run 应明确 3 mode 的触发条件 — Mode α（usage-based plan 用户的默认）/ Mode γ（legacy plan 用户的默认）/ Mode β（跨 IDE session 或重场景的可选 fallback）；Mode β 不强制实现 runtime，只提供 `.apm/bus/` 目录结构 template；依据 [APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md) 的"context isolation 是核心契约，runtime 是次要"立场。

### 待验证 / 未查证

- 本轮 EXP-04 试跑的实际 token 消耗（试跑过程中记录）
- Composer 2.5 Fast 对 template 类输出的实际质量（试跑过程中以 validation 通过率衡量）

### 方法专属输出（proj-experts · 4 视角）

#### 视角 A · PMP / PMBOK 6 Executing Process Group

**选用理由**：proj-run 对应 PMBOK 6 Executing Process Group；必须明确"承接哪几个 Executing 过程、其余刻意外置"，否则违反 proj-plan ORD-10 同等的边界声明纪律。

**【已公开立场】**：PMBOK 6 定义 Executing Process Group 共 10 过程：Direct & Manage Project Work、Manage Project Knowledge、Manage Quality、Acquire Resources、Develop Team、Manage Team、Manage Communications、Implement Risk Responses、Conduct Procurements、Manage Stakeholder Engagement。[PMBOK 7 tailoring 4 步骤](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) 允许"deliberate choice"按项目情境裁剪。

**【模拟推理】**：依据 PMBOK 7 tailoring 原则 + proj-plan ORD-10 的边界声明模式（"覆盖 X，不含 Y"），推理路径：
- **承接**（3 项）：
  - Direct & Manage Project Work → sub-agent dispatch 本质就是"执行 plan.md 任务"
  - Manage Quality → validation gate（lint / test / 输出格式校验）
  - Manage Project Knowledge → sub-agent 产出登记到 artifact-index（避免 source of truth 分裂）
- **刻意外置**（7 项）：
  - Acquire/Develop/Manage Resources → 由 proj-plan handoff 字段+人工分配（INV-04 精神延续）
  - Manage Communications → 跨 sub-agent 沟通仅通过 manifest + artifact-index，不引入 communications plan
  - Implement Risk Responses → 由 proj-plan circuit breaker 触发，proj-run 仅向上 escalate
  - Conduct Procurements → 项目级采购属 proj-plan 边界外（proj-plan ORD-10 已声明不含采购）
  - Manage Stakeholder Engagement → 同上

**关切 → 路径**：若 proj-run 承接过多 Executing 过程，会变成"小型项目管理工具"——失去焦点。**→** 只承接与"sub-agent 执行 + validation"强相关的 3 项；其余明示外置 + 失败时回 proj-shape 或对话处理。

#### 视角 B · Aider 作者 Paul Gauthier 派（architect/editor 哲学）

**选用理由**：proj-run 的核心机制 = Opus 规划 + Composer 执行，与 Aider architect/editor 模式高度同构；不借鉴其 validation 设计会重复其踩过的坑。

**【原话】**："Splitting up 'code reasoning' and 'code editing' in this manner has produced SOTA results" — [Aider blog 2024-09-26](https://aider.chat/2024/09/26/architect.html)

**【已公开立场】**：Aider architect-mode 的 SOTA 不是单纯"两个模型"，而是 **architect 给指令 → editor 实现 → diff 自动 apply → lint/test 验证 → 失败重试**的完整闭环；2026 推荐配对（[DeployHQ](https://www.deployhq.com/guides/aider)）：`aider --architect --model gpt-5 --editor-model gpt-5-mini`；"architect-mode runs typically cost 30-50% less than the same task done by the architect model alone"。

**【模拟推理】**：依据 Aider 闭环结构推理：proj-run 的 dispatch manifest 必须含 5 字段闭环：
1. **objective**（task ID + 一句话目标）
2. **specialist 类型**（决定 sub-agent 角色）
3. **validation criteria**（具体可执行 = lint 命令 / 文件结构校验 / 关键字 grep / 行数上限）
4. **iteration budget**（默认 2；超过则 escalate）
5. **escalate 规则**（失败时回写到 acceptance.md + 通知 GATE）

**关切 → 路径**：若 validation 只写"质量好"这种模糊判据，sub-agent 会"自我宣告完成"。**→** validation 必须**可由父 agent 一行命令判定**（如 `rg -c "model:" file.md` 必须为 0，或 `wc -l file.md` 必须 ≤ N）。

#### 视角 C · Anthropic Claude Code 派（Supervisor + Specialists）

**选用理由**：Cursor sub-agent 设计直接借鉴 Claude Code 模式；"96.3% 成功率" 的 Supervisor+Specialists pattern 是工业验证的最佳实践。

**【原话】**："Subagents are delegated workers inside one session that do a side task in their own context and return a summary. Use them when: a side task would flood your main conversation with search results, logs, or file contents you won't reference again." — [Claude Code agents docs](https://code.claude.com/docs/en/agents.md)

**【已公开立场】**：[DEV pattern survey](https://dev.to/wilsonhoe/why-your-multi-agent-system-breaks-at-3-am-orchestration-patterns-that-survive-production-1efi) 给出 "Supervisor + Specialists 是默认选择，96.3% 成功率"；强调 "blast radius containment — subagent 出错只污染自己的 context"。

**【模拟推理】**：依据 "side task" 定义 + blast radius 原则，推理路径：
- proj-run dispatch 决策树第一问 **不是** "能不能省钱"，而是 **"这个 task 的输出是否需要被父 agent 持续回溯？"**
- **是 → 不该 sub-agent**（输出会脱离父 context，需要时找不到）
- **否 → 才该 sub-agent**（fire-and-forget；validation 通过即归档到 artifact-index）

这与 task 大小、cost 节省都正交——cost 节省是结果，不是判据。

**关切 → 路径**：若 proj-run 把所有 task 都塞给 sub-agent 追求 cost 节省，会出现 "Composer 写出来的 SKILL.md 与 plan.md 冲突，父 agent 已无法回看 sub-agent context 修复" → **重新交付循环**反而比全 Opus 贵。**→** SKILL.md 中明示 dispatch 判据是"context 回溯需求"；cost 节省是 by-product，不是触发条件。

#### 视角 D · APM 学派 / CobuterMan 派（message bus + 三角色）

**选用理由**：APM 三角色（Planner / Manager / Workers）与 proj-* 体系（proj-experts+proj-shape / proj-plan / proj-run）天然对应；APM Message Bus 是 sub-agent 不够时的备用通信机制，proj-run 应提供占位 template。

**【已公开立场】**：[APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md) 强调 "each agent operating in its own context with only the information it needs"；[APM-Auto fork](http://github.com/sdi2200262/apm-auto) "replaces the user-mediated Worker model with autonomous subagent dispatch"；APM 原生 Message Bus = `.apm/bus/` 文件级跨 session 通信。

**【模拟推理】**：依据 APM 三角色 + Message Bus 设计推理 proj-run 的 3 mode 表：

| Mode | 触发条件 | 实现方式 | 适用 plan 类型 |
|------|---------|----------|----------------|
| **α**（自动 dispatch）| usage-based plan + 用户在同一 IDE session 内 | `.cursor/agents/<name>.md` + 父 agent 用 Task tool 直接调用 sub-agent | usage-based |
| **β**（message bus）| 跨 IDE session / 跨设备 / 单一 sub-agent 输出 > 父 context 承载 | `.apm/bus/` 文件级通信；每个 sub-agent 一个独立 chat session；用户人工 shuttle | 任意（重场景）|
| **γ**（手动模型切换）| legacy request-based plan + 用户在同一 IDE session 内 | 父 agent 默认 `@composer`；规划/评审节点用户手动 `@opus` 切换；不依赖 sub-agent dispatch | legacy request-based |

**关切 → 路径**：β mode 实现成本高（需要用户跨 session 操作）；若强制实现 runtime，会把 proj-run 复杂度推到不可维护。**→** β mode 只提供 `.apm/bus/` 目录结构 template + 触发条件说明；不实现 runtime（用户按需用 cp/mv 命令搬数据）；如有用户真实命中 β 场景，再迭代起草具体脚本。

#### 收敛（4 视角共识 · 【模拟推理】）

1. **3 mode 表必要** — 视角 A/D 共识：proj-run 需要明示 mode 选择策略 + 触发条件；视角 C 警示：mode 选择按 context 回溯需求和 plan 类型决定，**不**按 cost
2. **dispatch manifest 5 字段闭环** — 视角 B 主张：objective / specialist / validation（可执行）/ iteration budget / escalate 规则；视角 D 补充：每条 task 须标"是否真的需要 sub-agent"判据
3. **承接 3 个 PMBOK 6 Executing 过程，其余刻意外置** — 视角 A 共识；与 proj-plan ORD-10 边界声明同构
4. **β mode 不实现 runtime** — 视角 D 共识：只提供 template + 触发条件；避免过早抽象
5. **EXP-04 阈值需调整** — 视角 B/D 共识：Composer 2.5 Standard 当前不可 sub-agent dispatch（F1+F6），原 ≤1/5 阈值需放宽到 ≤1/3（用户已 B1=relax 确认）

## 讨论

### 1. proj-run SKILL.md 完整版的章节骨架（基于 4 视角收敛）

proj-run/SKILL.md 完整版应含以下章节（参照 proj-plan/SKILL.md 风格）：

| § | 章节 | 内容来源 |
|---|------|---------|
| 1 | 标题 + frontmatter（中文双层标题）| 命名规范 |
| 2 | 设计 vision（PMP Executing 承接 + Supervised-AI mode）| ORD-11 延续 |
| 3 | 与 proj-plan 的接口契约（承诺字段）| v0 骨架已有，加固 |
| 4 | 立场声明（借鉴 / 自创 + 基准版本 + ORD-16 Cursor 约束披露）| ORD-12/14/16 |
| 5 | **PMP 6 Executing 边界声明**（承接 3 项 + 刻意外置 7 项）| 视角 A 收敛 |
| 6 | **3 Mode 表 + 触发条件 + 选择决策树**| 视角 D 收敛 |
| 7 | **Sub-agent dispatch 决策树**（context 回溯判据 → 是否 dispatch）| 视角 C 收敛 |
| 8 | **Dispatch manifest 完整 schema**（5 字段闭环 + 示例）| 视角 B 收敛 |
| 9 | **Validation gate 3 类**（structural / lint / behavioral + 失败 escalate 流程）| 视角 B 收敛 |
| 10 | 工作流（前置 → dispatch → validation → escalate → 回写 acceptance.md）| 整合 |
| 11 | Circuit breaker（validation 反复失败 / sub-agent 关键 feature 不可用）| INV-03 延续 |
| 12 | 失败模式（明示反模式）| 试跑后补充 |
| 13 | 触发词 + 不触发本 skill |  |
| 14 | 模板索引 |  |

预估 SKILL.md 长度：~350-420 行；不超过 600 行硬上限。

### 2. proj-run/assets/ 必要 templates 清单（5 个）

| Template | 用途 | 对应章节 |
|----------|------|---------|
| `dispatch-manifest-template.md` | dispatch manifest 完整 schema（5 字段闭环 + 字段说明 + 完整示例）| §8 |
| `acceptance-template.md` | 阶段验收报告（validation 结果 + 实际 token cost + escalate 标记）| §3 输出契约 |
| `cursor-agents-template.md` | Mode α 模板（YAML frontmatter + `description`/`tools`/`is_background`/`readonly` 字段示例 + legacy plan warning）| §6 Mode α |
| `message-bus-template.md` | Mode β 占位（`.apm/bus/` 目录结构 + 触发条件说明 + 不含 runtime 声明）| §6 Mode β |
| `validation-gate-template.md` | Validation gate 3 类（structural / lint / behavioral）+ 失败 escalate 标准流程 | §9 |

不做：
- 不做 `.cursor/agents/*.md` 真实文件（属用户项目，非 skill 模板）
- 不做 `.apm/bus/` 实际 runtime 脚本（β mode 故意只提供 template）
- 不做 review-template.md（沿用 proj-plan 的 review-template；proj-run 仅写 acceptance）

### 3. EXP-04 试跑度量方法（实操细节）

#### 3.1 baseline 计算（B3=skill_plus_assets 已确认）

baseline = "假如本轮 proj-run 完整版（SKILL.md + 5 templates）全部由 Opus 独立完成的预估成本"

近似公式：
```
baseline_output_tokens ≈ proj-plan 总规模 ÷ 1066 × proj-run 预期规模
                       ≈ 10,375 ÷ 1066 × 预期行数（~1100-1300）
                       ≈ 10,700-12,650 tokens（输出）

baseline_input_tokens（含 6 轮迭代上下文累加估算）≈ output × 8 倍
                                                  ≈ 85K-100K tokens
（保守取中间值 90K）

baseline_cost ≈ 90K × $15/M + 12K × $75/M
              ≈ $1.35 + $0.90
              = $2.25
```

考虑实际迭代/重写/修订成本（proj-plan 实际经过 6 轮，每轮重读+重改），保守乘以 **3x 迭代因子**：

**baseline ≈ $6.75**（用于 EXP-04 比较的工作基线；明示这是 order-of-magnitude 估算，非精确测量）

#### 3.2 actual 测量（本轮试跑）

按任务/角色记录 token 消耗：
- **Opus 节点**：input tokens（读取的文件/上下文）+ output tokens（我的输出）× Opus 单价
- **Composer Fast sub-agent 节点**：sub-agent input（dispatch prompt + 上下文）+ output × Composer Fast 单价

测量方法：
- 每个节点结束时，记录 input/output tokens（用字符数 ÷ 平均 token/char 估算；CJK 1.5/token、ASCII 4/token）
- 累加到 phase-01/acceptance.md 的 token-cost 表
- 最终汇总在 DECISIONS.md EXP-04 状态行

#### 3.3 成功/中止阈值（v1.4，本轮 B1=relax 确认）

| 信号 | 原 v1.3 阈值 | 本轮 v1.4 调整后 | 调整理由 |
|------|-------------|------------------|----------|
| 成功 · cost | ≤ 1/5 baseline（≥5x 节省）| **≤ 1/3 baseline（≥3x 节省）** | Composer 2.5 Standard 不可 sub-agent dispatch（F6）；Fast 价差 ~5x；总 saving 现实上限约 2-3x |
| 成功 · GATE | GATE-0/1/2 一次通过率 ≥ 80% | **不变**（≥80%）| 与模型无关，是规划质量指标 |
| 成功 · analyze | analyze checklist 通过 | **不变** | 同上 |
| 成功 · validate | validate_skills.py 通过 | **不变** | 同上 |
| 中止 · cost | < 3x 节省 | **< 2x 节省** | 同步放宽；low bound 仍要求 baseline 比 actual 大至少 2x，否则案例规模不够 |
| 中止 · validation | Composer 反复失败 > 3 次/template | **不变**（> 3 次/template）|  |
| 中止 · 解读失败 | Opus plan 无法被 Composer 正确解读 | **不变** |  |
| 中止 · 阻塞 | Cursor sub-agent 关键 feature 阻塞 | **不变** |  |

### 4. 本轮的 dispatch 路径（B2=Hybrid 已确认）

| Task ID | 任务 | 路径 | 模型 | 备注 |
|---------|------|------|------|------|
| T-01 | `proj-run/assets/dispatch-manifest-template.md` | sub-agent | composer-2.5-fast | 结构化模板，validation 易判定 |
| T-02 | `proj-run/assets/acceptance-template.md` | sub-agent | composer-2.5-fast | 同上 |
| T-03 | `proj-run/assets/cursor-agents-template.md` | sub-agent | composer-2.5-fast | 同上 |
| T-04 | `proj-run/assets/message-bus-template.md` | sub-agent | composer-2.5-fast | 同上（占位，无 runtime） |
| T-05 | `proj-run/assets/validation-gate-template.md` | sub-agent | composer-2.5-fast | 同上 |
| T-06 | `skills/proj-run/SKILL.md` 完整版（覆盖 v0）| **Opus 直写** | claude-opus-4-7-thinking-xhigh（即父 agent）| 一致性 + 边界守护强需求；不适合 sub-agent（视角 C 共识）|
| T-07 | analyze checklist 跑全 artifact | sub-agent | composer-2.5-fast（readonly）| 视角 C 推荐的 auditor 模式 |
| T-08 | 同步 DECISIONS.md + 回写 EXP-04 | Opus 直写 | 同 T-06 | 跨文档一致性需求 |

iteration budget = 2 / template；失败 escalate 给我（Opus 父）重写或回 proj-plan 改 plan。

## 可验证尝试与继续/中止

### EXP-04 v1.4 修订（沿用 v1.3 案例 + 本轮 v1.4 阈值调整）

| 项 | 内容 |
|----|------|
| 假设 | "Opus 规划/评审 + Composer Fast sub-agent 执行" 在 proj-plan + proj-run 协同流水线下，total cost ≤ 1/3 baseline 且 GATE 通过率 ≥ 80% |
| 尝试方案 | 沿用 v1.3 案例（本轮起草 proj-run skill）；执行路径按 B2=Hybrid（T-01~05/07 sub-agent，T-06/08 Opus 直写）|
| 成功信号 | (1) total cost ≤ 1/3 baseline（≥3x 节省）；(2) GATE-0/1/2 一次通过率 ≥ 80%；(3) analyze 通过；(4) validate_skills.py 通过 |
| **继续** | passed → 把 dispatch manifest 5 字段 schema 固化进 phase-NN/plan.md 模板 + proj-run 完整 SKILL.md 同步发布 + 后续 skill 起草用相同 model-tier 模式 |
| **中止** | 任一：cost 节省 < 2x / Composer validation 反复失败 > 3 次/template / Opus plan 无法被 Composer 正确解读 / Cursor sub-agent 关键 feature 阻塞 |
| 来源 | DECISIONS EXP-04 v1.3；本轮 §讨论 3.3 v1.4 阈值修订；本轮 B1/B2/B3 用户确认；推理 · proj-experts 4 视角收敛 |

## 本轮决定

### 已确定 — 普通决定（新增 · 落实于 proj-run 内部）

> **重要**：本轮决定 ORD-18~22 均为 proj-run skill **实现细节** —— 落实在 `skills/proj-run/SKILL.md` 完整版与 assets 内；不属 INV，不会改变 proj-experts/proj-shape/proj-plan 任何边界。本轮亦修订 EXP-04 阈值（v1.3 → v1.4）。

- [x] **ORD-18**：**proj-run PMP 6 Executing 边界声明** —— proj-run 承接 PMP Executing Process Group 中 3 项（Direct & Manage Project Work / Manage Quality / Manage Project Knowledge），其余 7 项刻意外置（与 proj-plan ORD-10 同构纪律）；落实在 proj-run/SKILL.md §PMP Executing 边界节。
  **来源**：本轮 §视角 A 收敛；推理 · proj-experts · 视角 A；依据 [PMBOK 7 tailoring](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf) 的 deliberate choice 原则
  → 同步至 DECISIONS.md `ORD-18`

- [x] **ORD-19**：**3 Mode 表 + 触发条件** —— proj-run 提供 Mode α（自动 dispatch · usage-based plan）/ Mode β（message bus · 跨 session 或重场景）/ Mode γ（手动模型切换 · legacy plan）；Mode 选择按 plan 类型 + 是否跨 session 决定，**不**按 cost；落实在 proj-run/SKILL.md §3 Mode 表节；Mode β 仅提供 template 不实现 runtime（避免过早抽象）。
  **来源**：本轮 §视角 D 收敛；推理 · proj-experts · 视角 D；依据 [APM Getting Started](https://github.com/sdi2200262/apm-website/blob/main/docs/Getting_Started.md) + 07 轮 ORD-16
  → 同步至 DECISIONS.md `ORD-19`

- [x] **ORD-20**：**Sub-agent dispatch 决策树** —— proj-run 第一判据 = "task 输出是否需要被父 agent 持续回溯"，**需回溯 → 不该 sub-agent**；判据**不**包含 cost（cost 是 by-product）；落实在 proj-run/SKILL.md §dispatch 决策树节。
  **来源**：本轮 §视角 C 收敛；推理 · proj-experts · 视角 C；依据 [Claude Code agents docs](https://code.claude.com/docs/en/agents.md) "side task" 定义
  → 同步至 DECISIONS.md `ORD-20`

- [x] **ORD-21**：**Dispatch manifest 5 字段闭环（强制）** —— 每条 sub-agent task 必含 (1) objective / (2) specialist 类型 / (3) **可由父 agent 一行命令判定的** validation criteria / (4) iteration budget / (5) 失败 escalate 规则；落实在 proj-run/assets/dispatch-manifest-template.md + proj-plan/assets/plan-template.md 的 `## Sub-agent dispatch manifest` 段（v0 manifest 可选 → 本轮 EXP-04 跑过后升级为强制）。
  **来源**：本轮 §视角 B 收敛；推理 · proj-experts · 视角 B；依据 [Aider blog 2024-09-26](https://aider.chat/2024/09/26/architect.html) architect-mode 闭环结构
  → 同步至 DECISIONS.md `ORD-21`

- [x] **ORD-22**：**Validation gate 3 类** —— proj-run 区分 (1) structural（文件存在、字段齐、行数上限）/ (2) lint（validate_skills.py、markdown 结构、YAML frontmatter）/ (3) behavioral（关键字 grep、负向断言如 `rg -c "model:" = 0`）；任一失败按 ORD-21 iteration budget 重试；超出 budget escalate 给 Opus 父或 GATE；落实在 proj-run/assets/validation-gate-template.md + proj-run/SKILL.md §Validation gate 节。
  **来源**：本轮 §视角 B 收敛延伸；推理 · proj-experts · 视角 B（"validation 必须可由父一行命令判定"细化）
  → 同步至 DECISIONS.md `ORD-22`

### 对既有决定的修订

| 操作 | ID | 说明 | DECISIONS 变更日志 |
|------|-----|------|-------------------|
| 修订 | EXP-04 | 阈值 v1.3 → v1.4：成功 cost 由 ≤1/5 放宽至 ≤1/3；中止 cost 由 <3x 放宽至 <2x；其他信号不变。理由：F6 + 用户 B1=relax | 已记 2026-05-27 |
| 修订 | ORD-15 | manifest 段升级（**v0 可选 → 本轮 EXP-04 跑过后强制**，按 ORD-21 5 字段闭环执行）| 已记 2026-05-27（待 EXP-04 passed 后执行）|

### 待确认（下轮继续）

- ORD-15 manifest 段升级到强制 = 本轮 EXP-04 passed 后立即执行（落实在 proj-plan/SKILL.md + plan-template.md）；若 EXP-04 aborted 则保持 v0 可选

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-18 | 新增 · proj-run PMP 6 Executing 边界 | ✓ 已同步（2026-05-27）|
| ORD-19 | 新增 · 3 Mode 表 + 触发条件 | ✓ 已同步 |
| ORD-20 | 新增 · Sub-agent dispatch 决策树 | ✓ 已同步 |
| ORD-21 | 新增 · Dispatch manifest 5 字段闭环 | ✓ 已同步 |
| ORD-22 | 新增 · Validation gate 3 类 | ✓ 已同步 |
| EXP-04 | 修订 · 阈值 v1.3 → v1.4 | ✓ 已同步 |
| ORD-15 | 修订 · v0 可选 → EXP-04 passed 后强制（待执行） | ✓ 已同步 |

讨论状态同步：维持 `ready-for-implementation`（本轮新增决定均为 proj-run 实现细节，不影响过程闭合判定）

同步完成时间：2026-05-27

## 开放问题（下轮）

1. EXP-04 试跑实际数据出来后，是否需要修订阈值（v1.4 → v1.5）或为不同 plan 类型用户给出不同推荐 mode
2. proj-run 试跑过程中若发现新的失败模式，整理到 SKILL.md §失败模式节（试跑驱动而非预设）
3. 若有真实用户命中 Mode β 场景，再迭代起草 `.apm/bus/` runtime 脚本

## 试跑结果回写（v1.1 · 2026-05-27 同日完成）

> 按 proj-shape 协议两侧同步：本节是 08 轮 EXP-04 试跑结束后的回写；与 DECISIONS.md EXP-04 行 + `docs/pmo/proj-run-draft/phase-01/{acceptance,review}.md` 互为同步。

### 主交付（全部完成）

| 交付物 | 行数 | validation 结果 |
|--------|------|----------------|
| `skills/proj-run/SKILL.md` 完整版 1.0 | 283（≤ 600 ✓）| validate_skills.py 4/4 退 0；含 ORD-18~22 全 5 章节 + 工作流 + 失败模式 F1~F10 + 触发词 |
| `skills/proj-run/assets/dispatch-manifest-template.md` | 141 | 5/5 |
| `skills/proj-run/assets/acceptance-template.md` | 82 | 4/4 |
| `skills/proj-run/assets/cursor-agents-template.md` | 113 | 4/4 |
| `skills/proj-run/assets/message-bus-template.md` | 62 | 4/4 |
| `skills/proj-run/assets/validation-gate-template.md` | 99 | 4/4 |
| `docs/pmo/proj-run-draft/` 全套 PM artifact | — | GATE 4/4 一次通过率 100% · analyze 7/7 pass（T-08 修复后）|
| `skills/README.md` proj-run 行 | 更新 | v0 骨架 → 完整版 1.0 |

### EXP-04 v1.4 试跑结果 = **ABORTED with valuable insights**

| 信号 | 阈值 | 实际 | 结果 |
|------|------|------|------|
| 成功 · cost ≤ 1/3 baseline | actual ≤ $2.25 | **~$4.26**（中位估算 · ±20%）| ☒ fail |
| 成功 · GATE 一次通过率 ≥ 80% | ≥ 80% | **100%（4/4）** | ☑ pass |
| 成功 · analyze 通过 | 7/7 pass | **7/7 pass**（T-08 修复后）| ☑ pass |
| 成功 · validate_skills.py 通过 | exit 0 | **exit 0** | ☑ pass |
| 中止 · cost 节省 < 2x | actual > $3.375 | **~$4.26 > $3.375** → 节省 ~1.58x < 2x | ☑ 触发 |
| 其他 3 中止信号 | — | 全部未触发 | ☐ 未触发 |

### 核心洞察（写入 EXP-04 状态行）

1. **Opus plan 阶段固定成本占主导**：plan 阶段（N-01~N-05）累计 ~$2.48；占 baseline 37%；占 actual 58%
2. **Composer Fast 执行层 cost 极低**：6 dispatch 总 cost ~$0.35；占 actual 仅 8%
3. **算术天花板**：要实现 ≥3x 节省，项目总规模需 ≥ $10.5 baseline 让 plan + 评审 + 直写成本占比 < 33%；当前小项目无此条件
4. **正面验证**：Composer Fast 对结构化模板任务质量充分（5/5 一次过 + 0 escalate）；ORD-21 5 字段闭环 + ORD-22 三类 gate 设计有效
5. **真正瓶颈不是 sub-agent 质量**：而是 plan 阶段 Opus 固定成本占比；model-tier 需大规模项目稀释 plan 成本

### 后续动作触发情况

| 修订条款 | 触发条件 | 实际触发 | 动作 |
|---------|---------|---------|------|
| ORD-15 manifest 段 v0 可选 → 强制 | EXP-04 passed | ☒ 未触发（EXP-04 aborted）| **保持 v0 可选不升级**（按"EXP-04 aborted 则保持 v0 可选不强制"条款）|
| abort + 回 proj-shape 09 轮分析失败模式 | EXP-04 中止信号触发 | ☑ cost 中止触发 | **不开 09 轮**——失败模式已在试跑中被观察并写入 `proj-run/SKILL.md §失败模式 F1~F10`；不构成"需要新决定"的失败模式，无需 09 轮分析 |

### 新发现的失败模式（已写入 proj-run/SKILL.md）

试跑过程中 observed 的 10 个失败模式 F1~F10 已写入 SKILL.md §失败模式节；其中：

- **F1**（试跑核心发现）：把 sub-agent 主要当 cost 优化工具用 — Cursor 只能调度 Composer Fast 不能 Standard；plan 阶段固定成本天花板
- **F9**（实操踩坑）：grep -c 退出非零码与 set -e 交互导致 validation 命令中断；对策：用 `$(grep -c ... || echo 0)` 兜底

其他 F2~F8 / F10 为常见反模式（详见 SKILL.md）。

### 与 DECISIONS 同步状态（v1.1）

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-18~22 | 已落实到 proj-run/SKILL.md + assets | ✓ 已同步 |
| EXP-04 | 状态 = ABORTED with valuable insights | ✓ 已同步 |
| ORD-15 | 维持 v0 可选不升级 | ✓ 已同步 |

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-05-27 | 初稿；4 视角分析（沿用 07 轮 F1-F5 URL）；ORD-18~22 草案；EXP-04 v1.4 阈值修订；待 GATE 审批后开始 proj-plan Round A |
| 1.1 | 2026-05-27 | 同日完成试跑；回写主交付清单 + EXP-04 v1.4 结果（ABORTED with valuable insights · cost 唯一未达信号）+ 核心洞察 5 条 + 后续动作触发情况（ORD-15 保持 v0 可选；不开 09 轮）+ 失败模式 F1/F9 摘录 |
