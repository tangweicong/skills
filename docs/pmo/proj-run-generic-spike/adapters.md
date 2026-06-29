# Dispatch Adapters（EXP-08 被测物）

> 三个 adapter 实现 `DispatchCapability`（spawn/collect + 属性声明）。Cursor = 既有能力重表达；conversation-fallback = universal 兜底（本 spike 实跑验证）；claude-code = 骨架。

## 1. Cursor adapter（既有 3 Mode 重表达 · 不丢能力）

| 属性 | 值 |
|------|-----|
| context_isolation | true（Mode α/β）|
| model_selectable | **false**（legacy plan · ORD-16；usage-based 通常仅 composer-2.5-fast）|
| cross_session | true（Mode β）|

| 内部策略 | spawn 实现 | collect |
|----------|-----------|---------|
| Mode α | Task tool 调 `.cursor/agents/<role>.md` | sub-agent 返回结果 |
| Mode β | 写 `.apm/bus/tasks/<id>.md` + 通知用户开新 session | 用户 shuttle 回 `.apm/bus/` |
| Mode γ | 父 agent 内联 + 用户 `@composer`/`@opus` 手动切换 | 对话内 |

> 选择策略 = 现有 §Mode 选择决策树（plan 类型 + 是否跨 session）；**已被 EXP-04 实跑验证**（5/5 templates 一次过 validation）。

## 2. Conversation-fallback adapter（universal 兜底 · 本 spike 实跑）

| 属性 | 值 |
|------|-----|
| context_isolation | **false**（父 agent 内联扮演，无独立 context）|
| model_selectable | false |
| cross_session | false |

| spawn 实现 | collect |
|-----------|---------|
| 父 agent 在一个**明确分隔的 scratch 区/文件**内，按 self-contained prompt 扮演 specialist 完成 task | 读该 scratch 文件作为 artifact |

**适用**：任何 runtime（无 sub-agent 能力时的下限）；**代价**：无 context 隔离 → 仅适合小 task（与 §dispatch 决策树一致：context 密集/需父持续回溯的 task 本就该父直写，不该 sub-agent，所以 fallback 的 false 隔离不构成新问题）。

## 3. Claude Code adapter（EXP-08b · CLI 实证硬化 · 实跑阻塞于登录）

| 属性 | 值 | 实证来源（非记忆 · 本机 CLI 验证 2026-06-29）|
|------|-----|------|
| context_isolation | true | `claude -p` headless 子进程 / `--agents` native subagents 各自独立 context |
| model_selectable | **true** | `claude --model <alias\|full>` 存在（"alias 'sonnet'/'opus' 或全名 'claude-sonnet-4-6'"）→ **CLI 层 model 可选**，**与 Cursor ORD-16（subagent model 被 server 忽略）相反** |
| cross_session | true | `--resume`/`--continue`/`--session-id`/`--fork-session` 均在 |

| spawn 实现 | collect |
|-----------|---------|
| `claude -p`（headless worker 子进程）或 `--agents <json>` 定义 native subagent + Task 委派 | worker `Write` 出 artifact 文件 → 父读该文件；`--output-format json` 的 `modelUsage` 字段供 VERIFY 校验实际 model |

**实证清单（本机 `claude` v2.1.81 · 验证而非假设）**：
- `-p/--print` headless · `--output-format json`（返回 `result`/`modelUsage`/`total_cost_usd`）
- `--model <model>` 选模型（`model_selectable=true` 直接证据）
- `--agents <json>` 内联 native subagent 定义（adapter spawn 机制坐实）
- `--max-budget-usd` 成本硬上限 · `--permission-mode acceptEdits` + `--allowedTools "Write"` 受控落盘 · `--add-dir` 授权目录

**阻塞**：CLI **未登录**（`Not logged in · Please run /login`），且无 `ANTHROPIC_API_KEY`/`CLAUDE_CODE_OAUTH_TOKEN` → 真实 dispatch 需用户先 `claude /login`（交互 OAuth，不可代办）。

**Ready-to-run（登录后一条命令即实跑 spawn→collect→VERIFY）**：

```bash
# spawn: Claude Code worker 落一个 3 字段 artifact
claude -p --model haiku --output-format json --max-budget-usd 0.20 \
  --add-dir docs/pmo/proj-run-generic-spike \
  --permission-mode acceptEdits --allowedTools "Write" \
  'Write a file docs/pmo/proj-run-generic-spike/cc-dispatched-artifact.md containing exactly these three lines:
objective: prove claude-code adapter spawn->collect->validate
adapter: claude-code (context_isolation=true, model_selectable=true)
runtime: claude-code' > /tmp/cc-run.json
# collect+VERIFY (core gate · 防 F9): 字段齐 + json 的 model 确为所选(haiku) → model_selectable 实证
f=docs/pmo/proj-run-generic-spike/cc-dispatched-artifact.md
for kw in "objective:" "adapter:" "runtime:"; do c=$(grep -c "$kw" "$f" 2>/dev/null || true); c=${c:-0}; echo "$kw : $([ "$c" -ge 1 ] && echo PASS || echo FAIL)"; done
grep -o '"model[^,]*haiku[^,]*"' /tmp/cc-run.json && echo "model_selectable: PASS (haiku honored)" || echo "model_selectable: CHECK json"
```

## Adapter 对照（core 只依赖接口，不依赖下表细节）

| adapter | isolation | model_selectable | cross_session | 实跑状态 |
|---------|-----------|------------------|---------------|----------|
| cursor | ✓ | ✗ | ✓ | EXP-04 已验证 |
| conversation-fallback | ✗ | ✗ | ✗ | **本 spike 实跑** |
| claude-code | ✓ | ✓ | ? | 骨架 |
