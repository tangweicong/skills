# 启动章程（草案）

| 字段 | 值 |
|------|-----|
| 基于 DECISIONS | 2026-05-19 |
| 版本 | 草案 1.0 |

## 一句话

发布 **idea-pmo** skill，以双轮启动 + manifest 人读子集验证 EXP-01，替代 **idea-implement**。

## 背景与目标

三轮 discuss 收敛（`01`–`03`）：落地层采用 PMP 思维 + SDD gate；AI 维护 artifact 集，人类只读 manifest（≤5）。成功 = skill 可用 + 本仓库 `docs/pmo/` 试跑通过 Round A/B。

## 成功标准

- `skills/idea-pmo/SKILL.md` 与模板齐备
- `docs/pmo/` 完成 Round A + Round B（charter、wbs、artifact-index）
- `idea-implement` 废止；README / idea-discuss 引用更新
- EXP-01 可进入 phase-01 验证 rolling plan

## 范围与边界

### 在范围内

- idea-pmo skill 包、docs/pmo 试跑、DECISIONS/讨论文档同步

### 显式非目标

- 不在本章程内写 phase-01 细任务（进阶段时再 plan，INV-02）
- 不在 idea-pmo skill 内执行代码业务（INV-04）
- 模式 F 全量 PM 树（本项目 T）

## 决策权限

- GATE / 推翻 INV → 用户
- 新 ORD → idea-discuss

## 主要风险与 EXP 闸门

| EXP | 角色 |
|-----|------|
| EXP-01 | 验证双轮 + manifest；失败 → 缩 Round A 或默认 T |
| EXP-02 | GATE 硬规则随 skill 一并验证 |

## 授权请求（GATE-0）

已获用户 2026-05-19「可以开工」→ 授权 Round B。
