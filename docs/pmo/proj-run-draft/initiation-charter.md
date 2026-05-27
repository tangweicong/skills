# 启动章程（草案） — proj-run skill 起草项目

> Round A 产物；GATE-0 审阅。定稿见 `charter.md`（Round B）。

| 字段 | 值 |
|------|-----|
| 基于 DECISIONS | 2026-05-27（含 08 轮 ORD-18~22 + EXP-04 v1.4）|
| 版本 | 草案 0.1 |

## 一句话

把 `proj-run` skill 从 v0 骨架升级到完整可用版本（覆盖工作流 + 3 mode 实现 + dispatch manifest 完整 schema + validation gate + 失败模式 + 触发词），并同步在试跑过程中验证 EXP-04 假设（Opus 规划 + Composer Fast 执行的 model-tier 可在 ≥3x cost 节省下保持 GATE 一次通过率 ≥80%）。

## 背景与目标

**背景**：07 轮已确立 ORD-17（建立独立 proj-run skill 承接 PMP Executing Process Group）与 EXP-04（验证 model-tier 在 proj-* 流水线下的经济可持续性）；08 轮承接其触发的"完整工作流起草 + 试跑同步进行"双重目标。proj-run/SKILL.md v0 骨架已落实接口契约 + ORD-16 Cursor 约束披露；本项目要写的是其余 80% 内容（PMP 6 Executing 边界 / 3 Mode 表 / dispatch 决策树 / manifest schema / validation gate / 工作流 / circuit breaker / 失败模式）。

**目标**：
1. 交付 `skills/proj-run/SKILL.md` 完整版（覆盖 ORD-18~22 全部 5 项决定）+ `skills/proj-run/assets/` 5 templates，通过 validate_skills.py
2. 完成 EXP-04 试跑并按 v1.4 阈值（≥3x cost 节省 + ≥80% GATE 一次通过率 + analyze + validate）回写状态到 DECISIONS.md
3. EXP-04 passed 时，触发后续动作：升级 proj-plan/assets/plan-template.md 的 manifest 段从 v0 可选到强制（ORD-15 修订条款）

## 成功标准

链 EXP-04 v1.4 + 任务书完成 checkbox：

| # | 标准 | 验证方式 |
|---|------|---------|
| 1 | proj-run/SKILL.md 完整版（覆盖 ORD-18~22 + 工作流 / 失败模式 / 触发词）| 章节齐 + ≤600 行 + validate_skills.py |
| 2 | proj-run/assets/ 5 templates 齐 | 文件存在 + structural validation |
| 3 | EXP-04 cost 节省 ≥3x | 实际 token cost ÷ baseline ≤ 1/3（baseline ≈ $6.75）|
| 4 | GATE-0/1/2/3 一次通过率 ≥80% | GATE 通过表（4 GATE 至少 3 个一次过即 75% → 至少 4/4 才达 80%；试跑中如实记录）|
| 5 | analyze checklist 通过 | proj-plan/assets/analyze-checklist.md 全 7 项通过 |
| 6 | validate_skills.py 通过 | shell exit 0 |

## 范围与边界

### 在范围内

- proj-run/SKILL.md 完整版起草（覆盖 ORD-18~22）
- proj-run/assets/ 5 templates（dispatch-manifest / acceptance / cursor-agents / message-bus / validation-gate）
- 本项目 docs/pmo/proj-run-draft/ 全套 PM artifact（Round A + B + phase-01）
- EXP-04 试跑数据采集与回写

### 显式非目标

- **不**实现 Mode α 真实 `.cursor/agents/*.md` 文件（只写 template）
- **不**实现 Mode β 真实 runtime（只写 template + 触发条件）
- **不**修改 proj-plan/SKILL.md 或 plan-template.md（ORD-15 manifest 段升级到强制属 EXP-04 passed 后的后续动作，不在本项目内执行）
- **不**修改 proj-experts / proj-shape（本轮不涉边界）
- **不**改 docs/pmo/（EXP-01 历史遗产；本项目独立 namespace docs/pmo/proj-run-draft/）
- **不**在本轮新建 phase-02（rolling：先做 phase-01，发现规模需要再开）

## 决策权限

| 谁 | 权限 |
|----|------|
| 用户（Sponsor + PM 关键决策权 · ORD-11）| GATE-0/1/2/3 审批 / validation 反复失败时 abort/retry 决策 / 关键 trade-off（如阈值修订、新发现的决定方向）|
| AI（Opus 父 agent · 本对话）| PM 执行 + 全部 artifact 维护 + sub-agent 调度 + 评审 sub-agent 输出 + analyze / validate / 同步 DECISIONS |
| Sub-agent（composer-2.5-fast · 试跑期间）| 单一 template 起草任务；不得越权改其它文件、不得改 DECISIONS、不得跳 validation |

**新决定方向**：发现需要新 INV/ORD/EXP → 回 proj-shape 走下一轮（不在 proj-plan / proj-run 内创建）

## 主要风险与 EXP 闸门

| EXP | 角色 |
|-----|------|
| **EXP-04 v1.4** | 本项目的双重目标之一；试跑数据 + 最终状态写回 DECISIONS。中止信号触发任一 → abort 本项目并回 proj-shape 开 09 轮分析失败模式 |

风险细节见 `risk-register.md`（Round B）。

## 授权请求（GATE-0）

确认本草案 + `tailoring-decision.md` 后，授权进入 Round B 详细规划。

Round B 将生成（按模式 T + TR-02 简表）：charter / wbs / phase-roadmap / integration-plan / change-log / artifact-index / risk-register（简表），并运行 analyze checklist 后进 GATE-1 + GATE-2。
