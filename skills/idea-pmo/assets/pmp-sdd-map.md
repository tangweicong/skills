# PMP × SDD 对照（idea-pmo 实现边界）

> 供 Coach / AI 理解：**PMP 定有什么**，**SDD 定 AI 怎么守**。

## 计划三层（回答「WBS 够不够」）

| 层 | PMP | artifact | SDD 角色 |
|----|-----|----------|----------|
| 范围 | 创建 WBS | `wbs.md` | spec：做什么 |
| 进度（粗） | 制定进度计划（wave 远期） | `phase-roadmap.md` | plan：何时/分阶段 |
| 进度（细） | 定义活动 + 估时 | `phase-NN/plan.md` | tasks：可执行项 |
| 整合 | 项目管理计划 | `integration-plan.md` | 索引 truth source |

**WBS  alone 不够**；T 模式最小集 = WBS + roadmap + rolling plan + integration 索引。

## 过程组 × skill 边界

| 过程组 | idea-pmo | 执行方 |
|--------|----------|--------|
| Initiating | Round A + charter | idea-pmo |
| Planning | Round B + rolling phase | idea-pmo |
| Executing | ✗ | 对话 / execute skill |
| Monitor & Control | acceptance, review, change-log, analyze | idea-pmo |
| Closing | review + close checklist | idea-pmo |

## SDD 机制映射

| SDD（Spec Kit） | idea-pmo |
|-----------------|----------|
| constitution | `DECISIONS.md` INV |
| specify / clarify | idea-discuss 轮次 |
| plan | charter + wbs + roadmap + integration-plan |
| tasks | `phase-NN/plan.md` |
| gate | manifest GATE-0/1/2/N |
| analyze | [analyze-checklist.md](analyze-checklist.md) |

## 模式 T vs F（产物）

见 [tailoring-rules.md](tailoring-rules.md)。F = T + risk + stakeholder + communication + quality-plan（按需）。
