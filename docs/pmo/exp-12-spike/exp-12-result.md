# EXP-12 结果（步1 · model pin 实测）

| 字段 | 值 |
|------|-----|
| EXP | EXP-12（model-tier 经济性复测 @Cursor 3.3+） |
| 步骤 | 步1（pin 实测）· 完成；步2（经济性复测）· 待合适规模 phase |
| 日期 | 2026-07-07 |
| 环境 | Cursor IDE（本机 · 用户当前 plan）；父 agent model = Fable 5 |
| 判定 | **步1 PASS** → 触发 ORD-16 修订（用户 @轮次21 GATE 定序 after_exp） |

## 实验设计

三路差分：对同一最小任务（写 3 行身份文件）分别派发 3 个 sub-agent（Task tool · generalPurpose）：

| # | model 参数 | 预期自报 | 实际自报 |
|---|-----------|----------|----------|
| A | `composer-2.5-fast` | Composer 系 | **Composer** ✓ |
| B | `gpt-5.5-medium` | GPT 系 | **GPT-5.5** ✓ |
| C | （缺省 = inherit） | 父模型 Fable 5 | **Fable 5** ✓ |

自报机制 = sub-agent 读取自身 system prompt 的「powered by」措辞并写入 artifact（system prompt 由 runtime 注入，不受模型幻觉影响的合理代理观测）。

## Validation（一行命令 · ORD-22 三类）

- structural：`test -f docs/pmo/exp-12-spike/pin-test-{fast,gpt,inherit}.md` → 3/3 PASS
- behavioral 正向：`grep -ci 'model_reported: Composer' pin-test-fast.md` = 1；`grep -ci 'model_reported: GPT' pin-test-gpt.md` = 1；`grep -ci 'model_reported: Fable' pin-test-inherit.md` = 1 → 3/3 PASS
- behavioral 负向：`grep -ci 'Fable' pin-test-fast.md` = 0；`grep -ci 'Fable' pin-test-gpt.md` = 0 → 2/2 PASS（pinned agent 未 silent fallback 到父模型）

## 结论

1. **本机/本 plan 下 sub-agent model pin 被尊重**——Task tool `model` 参数接受具体 slug 并实际生效（跨两个 vendor 档位 + inherit 对照差分）。这直接推翻旧 ORD-16 核心约束（「model 字段被 server 端忽略 / enum 仅 fast」· [Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736) 时代）；与 Cursor 3.3+ 文档一致（[Cursor Docs Subagents](https://cursor.com/docs/subagents)）。
2. 论坛 3.3.30 个案 bug（pin 被忽略 · [Forum #160012](https://forum.cursor.com/t/subagents-are-not-useful-if-we-cant-select-their-model/160012)）在本机**未复现**。
3. round 21 开放问题 1（A2「pin 在本机是否被尊重」）**闭合：被尊重**。

## Caveat

- 观测是 system prompt 自报，非计费面 modelUsage 记录；但三路差分 + 负断言使 silent fallback 假设不成立，证据等级足以支撑 ORD-16 能力面修订。
- 未测 `.cursor/agents/*.md` frontmatter pin 路径（本环境经 Task tool `model` 参数达成同一目的，且该参数正是旧 ORD-16 所指对象，证据更直接）。
- legacy plan 无 Max Mode 强制 Composer 的半条约束未在本机验证（本机非该 plan 形态），保留为文档级条件注记。

## 步2（经济性复测）状态

**当下不可跑**：需要 baseline ≥ EXP-04（≈$6.75，约等于「起草一整个 SKILL.md + 成套 assets」规模）的真实 phase；本仓库当前无此规模的 pending 工作。候选载体（按到来顺序取先者）：EXP-11 落地 phase（若含成套文档产出）/ 小说项目的某个大 phase / 下一个新 skill 起草。届时按 EXP-04 同法记录 cost + GATE 通过率，重算盈亏平衡阈值。

EXP-12 总状态：**partial**（步1 passed · 步2 pending 待载体）。
