# EXP-08 结果：proj-run dispatch 层 runtime 无关化

> 假设：proj-run 3 Mode dispatch 可抽象成 runtime 无关接口 + 适配器，**不丢能力、也不比直接写更复杂**。

## 判定：PASSED → 继续（genericize proj-run · ORD-28）

## 成功信号核对

| 成功信号 | 结果 | 证据 |
|----------|------|------|
| 同一 plan.md/manifest 在 ≥2 runtime 下都能驱动 dispatch+validation | ✅ | **Cursor adapter**（EXP-04 实跑，5/5 templates 一次过）+ **conversation-fallback adapter**（本 spike 实跑：spawn→collect→validate 全 PASS，含 5 字段闭环 + cursor-token=0 负断言）|
| 核心流程无 runtime 专属硬编码 | ✅ | core（决策树/manifest/gate/budget/escalate）原样复用；fallback 产出经**同一** validation gate（ORD-22）通过；负断言 cursor-specific tokens=0 |

## 复杂度评估（abort 条件核对）

abort 条件 = 「Cursor 专属能力大量泄漏 / 接口更绕」。实际：

- **抽象面极小**：只有「spawn worker + collect artifact」被抽接口；core 7 个组件中 5 个本就 runtime 无关，**不动**。
- **3 Mode 不消失，只降位**：α/β/γ 从顶层概念降为 Cursor adapter 的内部策略 → 能力 0 丢失（逐条核对见 interface 文档「不丢能力核对」表）。
- **ORD-16 约束更显式**：从散落注意事项变成 adapter 的 `model_selectable=false` 属性声明。
- 净增 = 1 层间接（接口 + adapter 选择），换来 core 去 Cursor 耦合。**薄抽象，未触发 abort。**

## Caveats（不阻断，记录追踪）

1. **Claude Code adapter 仅骨架**：本环境无 Claude Code，`model_selectable=true` 路径未实跑。属性表已声明，待真实环境补验（可作 EXP-08b，非阻断）。
2. **conversation-fallback 无 context 隔离**：仅适合小 task；但与现有 dispatch 决策树一致（context 密集 task 本就该父直写），不构成新风险。

## 继续动作（待 GATE 批准后改 shipped proj-run）

genericize proj-run/SKILL.md：core 与 dispatch adapter 分离 —— §Mode 表重构为「DispatchCapability 接口 + Cursor adapter（现 3 Mode）+ conversation-fallback 兜底 + Claude Code 骨架」；ORD-16 表述为 adapter 属性。core（决策树/manifest/gate/budget/escalate）措辞去 Cursor 化但逻辑不变。
