# 风险登记 — proj-run skill 起草项目

> **PMP**：识别风险 → 定性分析 → 规划应对。
> **T + TR-02**：填「简表」即可；本项目不升 F。

| 字段 | 值 |
|------|-----|
| 模式 | T（简表 · TR-02 触发）|
| 最后更新 | 2026-05-27 |

## 简表（T / TR-02 必填）

| ID | 风险描述 | 来源 | 概率 | 影响 | 应对（规避/减轻/接受） | 关联 EXP/ORD | 状态 |
|----|----------|------|------|------|------------------------|--------------|------|
| R-01 | EXP-04 cost 节省未达 ≥3x（success）或 <2x（abort）| DECISIONS EXP-04 v1.4 | **中** | **高**（aborted 触发 abort 本项目 + 回 proj-shape 09 轮）| **减轻**：分阶段记 cost；接近 plan 阶段 50% baseline 时预警；sub-agent dispatch 失败立即缩 batch | EXP-04 | 开放 |
| R-02 | Composer Fast sub-agent 反复 validation 失败 > 3 次/template | DECISIONS EXP-04 v1.4 中止信号 | **中** | **高**（触发 abort）| **减轻**：iteration budget = 2；超过 escalate 给我（Opus 父）改写 plan 或回 proj-plan 改 dispatch manifest | EXP-04 | 开放 |
| R-03 | Opus plan 字段对 Composer Fast 不够明确，sub-agent 输出偏离 | DECISIONS EXP-04 v1.4 中止信号 | **中** | **中** | **减轻**：dispatch manifest 5 字段闭环（ORD-21）严格执行；validation criteria 必须 1 行命令可判定 | EXP-04, ORD-21 | 开放 |
| R-04 | proj-run SKILL.md 超 600 行硬上限 | validate_skills.py | **低** | **中**（validate 失败）| **规避**：写时分章节预算（350-420 行目标）；如超 500 行立即拆 assets 引用 | — | 开放 |
| R-05 | GATE 一次通过率 < 80%（< 4/4 = 100% 或 < 4/5 = 80%）| EXP-04 v1.4 成功信号 | **低** | **中**（success 不达，aborted 不触发）| **规避**：每个 GATE 提交前自查 INV-01~04；Round B 前跑 analyze checklist | EXP-04 | 开放 |
| R-06 | 试跑中发现需要新 INV/ORD（边界越权风险）| INV-04 | **低** | **中**（违反"不在 proj-plan 内新建决定"原则）| **规避**：发现需要新决定立即停手记下，回 proj-shape 09 轮处理；不在本项目内创建 | INV-04 | 开放 |

## 与 phase-01 review 联动

- 阶段 `review.md` 须标注本阶段新增/关闭的风险 ID
- EXP-04 中止 → R-01 / R-02 / R-03 标 **已实现**，触发 circuit breaker：abort 本项目 + 回 proj-shape 09 轮
- EXP-04 passed → R-01 关闭；R-02~R-06 视实际情况关闭或留 open 到下个项目（如有）
