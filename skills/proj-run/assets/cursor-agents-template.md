# Cursor Sub-agent 模板（Mode α）

> 本文件是 **proj-run** skill 的 **Mode α**（自动 dispatch · usage-based plan）专用模板，演示如何编写 `.cursor/agents/<name>.md` 让 Cursor 父 agent 自动 dispatch sub-agent。
>
> **适用**：Cursor **usage-based plan**（扩展 model selection 已 rollout）。**Legacy request-based plan** 用户应转 **Mode γ**（按 `model-tier.yaml` 手动切换 planning / execution），见下方 warning。
>
> **model 来源**：写 `.cursor/agents/*.md` 时，`model:` 填 **resolved `execution`**（见 [`model-tier.yaml`](model-tier.yaml)；项目可在 `docs/pmo/model-tier.yaml` 覆盖）。

来源 `proj-run/assets/` · 依据 ORD-16 · ORD-21 · Mode α = `.cursor/agents/*.md` + Task tool。

---

## YAML frontmatter 模板段

每个 `.cursor/agents/<name>.md` 以 YAML frontmatter 开头，后跟 markdown 正文。复制下方骨架并按需修改：

```yaml
---
# description: 必须。父 agent 何时 delegate 到此 sub-agent 的依据（一句话 + 触发场景）
description: "Brief trigger — when parent should delegate (e.g. draft template files, implement config snippets)"

# tools: 可选。限定 sub-agent 可用工具列表；省略则继承父 agent 全部工具
tools: ["Read", "Write", "StrReplace", "Grep", "Shell"]

# model: 填 resolved model-tier.execution（默认 cursor-grok-4.5-high-fast）
model: cursor-grok-4.5-high-fast

# is_background: 可选 bool。true = 异步后台运行，父 agent 不阻塞等待
is_background: false

# readonly: 可选 bool。true = 只读 auditor/reviewer 角色，禁止写文件
readonly: false
---

<!-- markdown 正文：sub-agent 职责、输入/输出契约、提示词风格 -->
```

---

## 完整 example：`.cursor/agents/template-coder.md`

以下为可复制的完整 sub-agent 定义示例（对应 dispatch manifest 中 `subagent:coder`）：

```markdown
---
description: >-
  Draft or implement artifact files from phase-NN/plan.md dispatch manifest
  (T-NN objective). Use when parent needs a coder specialist — template files,
  config snippets, markdown assets. Do NOT use for read-only audit or codebase
  exploration.
tools: ["Read", "Write", "StrReplace", "Grep", "Shell"]
model: cursor-grok-4.5-high-fast
is_background: false
readonly: false
---

You are a Cursor sub-agent dispatched by the parent agent as **specialist:coder**.

## When to delegate (parent agent)
- Dispatch manifest row has `specialist: subagent:coder`
- Task objective is drafting / implementing a concrete artifact (not review or explore)

## Inputs
- Task ID + objective from `## Sub-agent dispatch manifest` in `phase-NN/plan.md`
- Paths, validation criteria, iteration budget from the same manifest row
- Self-contained context block from parent (do not assume prior chat history)

## Outputs
- Artifact file(s) at path(s) specified in objective
- Return to parent: file path + line count + validation command outputs + brief notes

## Style
- Minimize scope; match repo conventions; run validation before returning
- Do not modify git, other files, or open new decisions (escalate to parent)
```

---

## ⚠ Legacy plan · `model` 字段失效 warning（ORD-16）

> **【已公开立场】** Cursor sub-agent 的 `model` 字段在 **legacy request-based pricing plan 被 server 端忽略**——subagent 会 silently fallback 到父 model；仅 usage-based plan 的 expanded model selection 已 rolling out。
>
> 出处：[Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736)

| 用户 plan | 推荐 mode | 说明 |
|----------|-----------|------|
| Usage-based | **Mode α** | `.cursor/agents/<name>.md` + 父 agent Task tool；`model` 字段生效 |
| Legacy request-based | **Mode γ** | 按 model-tier：执行段用 `execution`、规划/评审用 `planning`；**不依赖** sub-agent `model` 字段 |

---

## 使用流程（Mode α vs Mode γ）

### 1. 用户创建 sub-agent 文件

1. 在仓库根目录创建 `.cursor/agents/`（若不存在）
2. 按 manifest 中 `specialist` slug 命名，如 `template-coder.md`、`plan-auditor.md`
3. 复制上方 frontmatter 模板 + 正文，填入 `description` 与职责说明；`model:` 用 resolved `execution`
4. `description` 是父 agent 自动选择 sub-agent 的**唯一依据**——写清何时 delegate、何时不 delegate

### 2. 父 agent 自动 dispatch（Mode α）

1. 读取 `phase-NN/plan.md` 的 `## Sub-agent dispatch manifest`
2. 按 task 的 `specialist` 匹配 `.cursor/agents/<name>.md` 的 `description`
3. 用 **Task tool** dispatch：`subagent_type` 选对应 specialist，`prompt` 含 objective + validation criteria + 自包含上下文
4. 收 sub-agent 返回 → 跑 manifest 中 validation criteria → 失败则按 iteration budget 重 dispatch 或 escalate

### 3. 与 Mode γ 对照

| | Mode α（本模板） | Mode γ（legacy / 手动） |
|--|-----------------|------------------------|
| sub-agent 定义 | `.cursor/agents/*.md` | 无；父 agent IDE 默认 |
| model 选择 | frontmatter `model` = model-tier.execution | 用户按 model-tier 手动切 planning / execution |
| dispatch 方式 | 父 agent Task tool 自动 | 父 agent 口头指示用户切换模型 |
| 适用 plan | usage-based | legacy request-based |
