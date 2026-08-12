# Sub-agent Dispatch Manifest 模板

> 本文件是 **proj-run** skill 的 dispatch manifest 模板，落实 **ORD-21** 5 字段闭环。用户在 `phase-NN/plan.md` 末尾复制 `## Sub-agent dispatch manifest` 段时使用。**EXP-04 passed** 后将固化进 `proj-plan/assets/plan-template.md`。

| 字段 | 值 |
|------|-----|
| 来源 | proj-run/assets/dispatch-manifest-template.md |
| 依据 | ORD-15（承诺字段）· ORD-21（5 字段闭环） |
| 用途 | 嵌入 `docs/pmo/phase-NN/plan.md` 末尾，供 proj-run 调度 sub-agent |

---

## 字段说明 schema（ORD-21 · 强制）

每条 sub-agent task **必含**以下 5 字段；缺任一项时 proj-run **回退 proj-plan 补齐**，不自行补全。

| 字段 | 含义 | 强制 |
|------|------|------|
| **objective** | task ID + 一句话目标（做什么、产出什么 artifact） | ✓ |
| **specialist** | sub-agent 角色 slug（如 `subagent:coder` / `subagent:reviewer` / `subagent:auditor` / `subagent:explorer`） | ✓ |
| **validation criteria** | **可由父 agent 一行 shell/grep 命令判定**的判据列表（如 `test -f` / `rg -c "…" ≥ N` / `wc -l ≤ N`） | ✓ |
| **iteration budget** | validation 失败后的重试次数上限（典型值 **2**；auditor 等只读任务可为 **1**） | ✓ |
| **escalate** | 超出 budget 时的回退路径（回父 agent / 回 proj-plan 改 plan / 回 proj-shape 开新轮） | ✓ |

**model 字段**：**本模板不指定**具体 model 名（ORD-15）。由 proj-run 按 `docs/pmo/model-tier.yaml`（若有）→ skill [`model-tier.yaml`](model-tier.yaml) 默认，再结合 Mode α/β/γ 落点。

### Specialist 角色参考

| slug | 职责 | 典型场景 |
|------|------|---------|
| `subagent:coder` | 起草 / 实现 artifact | template 文件、配置片段 |
| `subagent:reviewer` | 只读评审 + 改进建议 | plan 一致性、边界守护 |
| `subagent:auditor` | 只读跑 checklist / 规则审计 | analyze-checklist、schema 合规 |
| `subagent:explorer` | 只读探查代码库 | 文件清单、依赖梳理 |

完整角色定义见 proj-plan [agent-handoff.md](../../proj-plan/assets/agent-handoff.md)。

---

## 完整 dispatch 示例

以下 2 个 task 展示 5 字段闭环写法；复制到 `phase-NN/plan.md` 时替换 task ID、路径与判据即可。

### 示例 1 · T-01 · 起草 template（coder）

| 字段 | 值 |
|------|-----|
| **objective** | T-01：起草 `skills/proj-run/assets/dispatch-manifest-template.md`（含 schema 表 + ≥2 示例 task + 使用规则） |
| **specialist** | `subagent:coder` |
| **validation criteria** | (1) `test -f skills/proj-run/assets/dispatch-manifest-template.md` 退 0；(2) `wc -l skills/proj-run/assets/dispatch-manifest-template.md` ≤ 200；(3) `rg -c "objective\|specialist\|validation criteria\|iteration budget\|escalate" skills/proj-run/assets/dispatch-manifest-template.md` ≥ 5；(4) 负向 behavioral：正文无具体 model 名（父 agent 跑 ORD-22 V5 自检，命中 0） |
| **iteration budget** | 2 |
| **escalate** | 第 1 次失败 → 父 agent 给修订要点后重 dispatch；第 2 次失败 → 父 agent 直接接手改写；若 schema 需新决定 → 标 change-log + 回 proj-shape |

---

### 示例 2 · T-07 · analyze checklist（auditor）

| 字段 | 值 |
|------|-----|
| **objective** | T-07：对 `skills/proj-run/SKILL.md` + `assets/` 模板跑 proj-plan `analyze-checklist.md` 全 7 硬规则，输出 pass/fail 结果表 |
| **specialist** | `subagent:auditor`（readonly） |
| **validation criteria** | (1) 返回表含 7 硬规则全部行；(2) 每条 fail 附证据 1 行（文件 + 违规点）；(3) ≥3 条软规则建议；(4) `git diff --name-only` 无修改（readonly 强制） |
| **iteration budget** | 1 |
| **escalate** | 失败 1 次 → 父 agent 直接跑 checklist 替代（不再 retry sub-agent）；规则歧义 → 回 proj-plan 澄清 checklist |

---

## 使用规则

### 嵌入位置

在 `docs/pmo/phase-NN/plan.md` **末尾**追加：

```markdown
## Sub-agent dispatch manifest（ORD-15 + ORD-21 · 强制）

> 本段是对 proj-run 的承诺字段。不指定具体 model——model 由 proj-run 决定（ORD-15）。

### Manifest schema 字段说明
（复制上方「字段说明 schema」表格）

### Dispatch 详表
（为每个 `subagent:{角色}` 任务行展开 5 字段表格，见上方示例）
```

### 与 plan 主任务表的关系

| 层级 | 位置 | 内容粒度 |
|------|------|---------|
| 主任务表 | `## 任务` | 一行摘要：# / 任务 / 执行者 / 前置 / 状态 |
| Handoff 节 | `## Handoff` | 最小交接：输入 · 完成定义 · 结果回写（见 agent-handoff.md） |
| **Dispatch manifest** | 段末 | **sub-agent 任务行的展开**：5 字段闭环 + 可执行 validation + budget + escalate |

**对应关系**：主任务表中执行者为 `subagent:{角色}` 的行，在 manifest 段各有一条 5 字段详表；task ID（如 T-01）在 objective 与主表 `#` 列对齐。

### 不指定 model 名的原因（ORD-15）

| 原因 | 说明 |
|------|------|
| 版本会过时 | 具体 model 名随 provider 迭代；manifest 是跨阶段承诺，不宜绑定版本 |
| plan 类型差异 | legacy / usage-based plan 对 sub-agent model 字段支持不同（见 proj-run ORD-16） |
| 职责分离 | proj-plan **只规划** specialist 类型与 validation；proj-run **负责** model-tier + Mode α/β/γ 选择与 dispatch |

manifest 正文**禁止**出现具体 model 名；需要说明 model 时写「model 由 proj-run 决定，本模板不指定」即可。

### iteration & escalate 总策略（phase 级）

- 单 task 失败 ≤ budget：父 agent 给修订要点 → 重 dispatch
- 单 task 失败 > budget：按该 task 的 escalate 规则执行（父 agent 接手 / 回 proj-plan / 回 proj-shape）
- 全 phase sub-agent 累计失败 > 3 次：触发 circuit breaker → abort phase + 回 proj-shape 分析失败模式
- 任何 task 发现需新 INV/ORD：立即停手 + 回 proj-shape（不在 execute 层改决定）

---

## 复制用段首（phase-NN/plan.md 粘贴起点）

```markdown
## Sub-agent dispatch manifest（ORD-15 + ORD-21 5 字段闭环 · 强制）

> 本段是 proj-run 调度依据。含 specialist 类型 + validation criteria + iteration budget；**不指定具体 model**（ORD-15）。

| 字段 | 含义 | 强制 |
|------|------|------|
| objective | task ID + 一句话目标 | ✓ |
| specialist | sub-agent 角色 slug | ✓ |
| validation criteria | 一行 shell/grep 可判定的判据 | ✓ |
| iteration budget | 失败重试次数上限 | ✓ |
| escalate | 超出 budget 的回退路径 | ✓ |

### Dispatch 详表

#### {T-NN} · {任务简称}

| 字段 | 值 |
|------|-----|
| **objective** | |
| **specialist** | |
| **validation criteria** | |
| **iteration budget** | |
| **escalate** | |
```
