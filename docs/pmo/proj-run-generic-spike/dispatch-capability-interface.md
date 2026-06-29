# Dispatch Capability 接口（EXP-08 被测物）

> SPIKE，未应用到 shipped proj-run。验证 ORD-28：proj-run 的 dispatch 层能否抽象成 runtime 无关接口 + 适配器，**不丢能力、也不比直接写更复杂**。

## 关键观察（决定抽象面大小）

proj-run 现有内容**绝大多数已 runtime 无关**，只有「怎么真正生出一个 worker」是 Cursor 专属：

| proj-run 组件 | runtime 相关? | 归属 |
|---------------|--------------|------|
| Sub-agent dispatch 决策树（ORD-20）| ❌ 无关 | **core** |
| Dispatch manifest 5 字段闭环（ORD-21）| ❌ 无关 | **core** |
| Validation gate 3 类（ORD-22）| ❌ 无关 | **core** |
| iteration budget / escalate / circuit breaker | ❌ 无关 | **core** |
| 工作流（dispatch→validate→iterate→归档）| ❌ 无关 | **core** |
| **3 Mode 表 α/β/γ** | ✅ **Cursor 专属** | **adapter** |
| `.cursor/agents/*.md` / Task tool / `@composer` 切换 | ✅ Cursor 专属 | adapter |
| ORD-16 Cursor sub-agent model 字段约束 | ✅ Cursor 专属 | adapter |

**结论**：抽象面 = **只把「spawn worker + 取回 artifact」这一个机制**抽成接口；core 几乎不动。这是个**薄抽象**（抽象成本低 → 倾向不触发 abort 条件「比直接写更复杂」）。

## 接口契约（runtime 无关）

proj-run core 对每条 manifest task 只需要两个动作 + 一组属性：

```text
DispatchCapability:
  spawn(specialist_role, self_contained_prompt, refs) -> handle
      启动一个 worker 执行该 task（self-contained：含 objective+context+ref 路径+validation 自检命令 · APM 原则）
  collect(handle) -> artifact_path
      取回 worker 产出（落到 artifact-index 登记的路径）

  属性要求（adapter 须声明满足哪些）：
    - context_isolation: 是否真隔离父 context（sub-agent 的核心价值；fallback 可为 false）
    - model_selectable: 是否可指定 worker model（Cursor legacy=false；见 ORD-16）
    - cross_session: 是否支持跨 session（决定能否承载 >父 context 的大产出）
```

core 拿到 artifact 后，**自己**跑 validation gate（ORD-22）、按 iteration budget 重试、超 budget 走 escalate——**这些不经过 adapter**，故 runtime 无关。

## Adapter 选择（取代「3 Mode 表」的上位概念）

「3 Mode α/β/γ」**降为 Cursor adapter 的内部策略**；跨 runtime 的选择变成「先选 adapter，再由 adapter 选其内部策略」：

```text
1. 检测 runtime → 选 adapter（cursor / claude-code / conversation-fallback）
2. adapter 内部按其能力选策略：
   - cursor adapter:        Mode α（Task tool+.cursor/agents）/ β（.apm/bus）/ γ（手动切换）
   - claude-code adapter:   native subagents（Task）/ 跨 session
   - conversation-fallback: 父 agent 内联扮演（无隔离；universal 兜底）
3. core 用接口 spawn/collect，不感知 adapter 细节
```

**降级链**：首选 adapter 不可用 → conversation-fallback（永远可用，但 context_isolation=false）。这把 ORD-16「Cursor 约束 → 降 Mode γ」泛化成「能力不足 → 降级到更弱属性的 adapter/策略」。

## 不丢能力核对

| 现有能力 | 抽象后落点 | 丢失? |
|----------|-----------|-------|
| Mode α 自动 dispatch | cursor adapter 策略 | 否 |
| Mode β message bus | cursor adapter 策略 | 否 |
| Mode γ 手动切换 | cursor adapter 策略 | 否 |
| ORD-16 model 约束披露 | cursor adapter `model_selectable=false` 属性 | 否（更显式）|
| 决策树/manifest/gate/budget/escalate | core 原样 | 否 |
