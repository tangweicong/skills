# 评审总结 — phase-01 · proj-run 完整版起草 + EXP-04 试跑

| 字段 | 值 |
|------|-----|
| 阶段 | phase-01（单 phase 项目）|
| acceptance | **部分通过**：项目级交付全部通过 ✓；EXP-04 cost 信号未达 → ABORTED with valuable insights |
| circuit breaker | 见下 |

## 计划完成度

| 项 | 状态 | 说明 |
|----|------|------|
| WBS 1.0 · proj-run/SKILL.md 完整版 | ✓ 完成 | 283 行 · 13 章节 · 覆盖 ORD-18~22 + 工作流 + 失败模式 + 触发词 |
| WBS 2.0 · 5 templates | ✓ 完成 | 全部 sub-agent 一次产出 + validation 通过（0 escalate）|
| WBS 3.0 · PM artifact 全集 | ✓ 完成 | Round A + Round B + phase-01 · GATE-0/1/2/3 全 ☑（一次通过率 100%）|
| WBS 4.0 · EXP-04 试跑度量与回写 | ✓ 完成（结果 ABORTED）| token cost + GATE + analyze + validate 数据全回写 acceptance + DECISIONS |
| WBS 5.0 · skills/README.md 同步 | ✓ 完成 | proj-run 行从 v0 → 完整版 |

## Circuit breaker（Shape Up × M&C）

| 条件 | 动作 |
|------|------|
| **项目级 acceptance 通过**（5 个 WBS + 4 GATE + analyze + validate）| ✓ 触发 — 允许项目关闭；不开 phase-02；更新 roadmap 标 phase-01 closed |
| **EXP-04 cost 信号未达**（actual ~$4.26 > $3.375）| ✓ 触发 — EXP-04 状态 = ABORTED；**不**触发 ORD-15 升级（保持 proj-plan plan-template manifest 段 v0 可选）|
| EXP-04 其他 3 成功信号通过 | acceptance 标"部分通过"；不触发回 proj-shape 09 轮（仅 cost 信号未达不构成需"分析失败模式"——失败模式已在试跑中 observed 并写入 proj-run/SKILL.md §F1）|

## 问题

| 问题 | 处理 |
|------|------|
| T-07 audit 发现 artifact-index rule 5 fail（路径与版本不一致：磁盘有 templates 但 index 标"待创建"）| T-08 已批量修复 + Opus 父再跑 analyze 7/7 pass |
| Opus shell 复核 V3 时 grep -c 返回非零退出码导致 set -e 中断后续命令 | observed 写入 proj-run/SKILL.md §F9 失败模式 |
| 试跑无精确 token 计量器；估算误差 ±20% | 在 acceptance §EXP-04 度量段明示 "估算方法 + 误差范围"；下次试跑可考虑结合 Cursor IDE 内置 token 计量（如有）|

## EXP 验证

| ID | 结果 | 同步 DECISIONS |
|----|------|----------------|
| EXP-04 v1.4 | **ABORTED with valuable insights** · cost 节省 ~1.58x（< 2x 中止阈值；估算 actual ~$4.26 / baseline $6.75）；4 成功信号中 3 个全过（GATE 100% + analyze 7/7 + validate 退 0），仅 cost 信号未达 | T-08 已同步 |

**核心洞察**（写入 DECISIONS EXP-04 状态行注脚）：
1. Opus plan 阶段 cost ~$2.48 占 baseline 37%；占 actual 58%（plan 阶段为固定成本主导）
2. Composer Fast 执行层 cost ~$0.35 仅占 actual 8%（model-tier 节省的有效部分）
3. Opus 评审 + T-06 SKILL.md 直写 + T-08 同步等 Opus 工作量占 actual 92%
4. 算术天花板：要实现 ≥3x 节省，project 总规模需 ≥ $10.5 让 plan + 评审 + 直写成本占比 < 33%；本试跑规模不足
5. 正面验证：Composer Fast 对结构化模板任务质量充分（5/5 一次过 validation；0 escalate；ORD-21 5 字段闭环 + ORD-22 三类 gate 设计有效）

## 风险（联动 risk-register）

| ID | 本阶段变化 |
|----|------------|
| R-01（EXP-04 cost 节省未达 ≥3x）| **已实现** → ABORTED；abort 仅止于 EXP-04 不止于项目；其他成功信号通过故主交付继续 |
| R-02（Composer Fast 反复失败 > 3 次/template）| **未实现** → 关闭 |
| R-03（Opus plan 字段对 Composer Fast 不够明确）| **未实现** → 关闭；ORD-21 5 字段闭环验证有效 |
| R-04（SKILL.md 超 600 行）| **未实现** → 关闭（283 行）|
| R-05（GATE 一次通过率 < 80%）| **未实现** → 关闭（100% 通过率）|
| R-06（试跑中需要新 INV/ORD）| **未实现** → 关闭（试跑发现的失败模式属 proj-run 实现细节，已写入 SKILL.md §失败模式，不构成新决定）|

## 经验教训

| 类别 | 内容 |
|------|------|
| **做得好的** | (1) 4 视角分析（PMP/Aider/Anthropic/APM）沿用 07 轮 F1-F5 URL 不重搜，节省查证 cost；(2) ORD-21 5 字段闭环 + ORD-22 三类 gate 设计经实测验证有效（5/5 一次过 + 6/6 dispatch 0 escalate）；(3) Hybrid 路径（关键文件 Opus 直写 + 结构化模板 sub-agent）路径选择正确（避免 T-06 跨章节一致性失守）；(4) GATE-1+2 合并 + 节点暂停审批节奏既保留人控又避免微观审批 |
| **待改进** | (1) Round B artifact-index 应预留"待回写"占位但不写"待创建"字面值——避免被 analyze 判 fail；(2) Opus 父复核 shell 命令需考虑 grep -c 退出码与 set -e 交互（observed F9）；(3) 试跑 EXP-04 前先估算 baseline + plan 阶段固定成本占比，提前判定项目规模是否够大支撑 ≥3x 节省（避免"几乎注定 ABORTED"的试跑）；(4) charter/wbs/phase-roadmap/plan 的状态字段在 GATE 通过后批量更新（软规则 #1）|
| **下项目建议** | (1) model-tier 真正有效的项目规模 ≥ $10.5 baseline；小项目（< $5）不强求 model-tier 反而 Opus 直写更经济；(2) sub-agent dispatch 优势在 **context 隔离**（视角 C）而非 cost——dispatch 大量结构化输出且 fire-and-forget 的 task；(3) 后续若要再试 model-tier，选择更大规模项目（如开源前发布 v1.0 / 多 skill 联动重构）；(4) 试跑无精确 token 计量是结构性问题——可考虑接入 Cursor IDE token 计量 API（如有）或外置代理；(5) **proj-run 完整版**本身已就绪发布，不依赖 EXP-04 passed |

## 收尾检查（末阶段必填）

- [x] 全部 WBS 条目已验收（5 个 L1 全 ✓）
- [x] EXP 状态已同步 DECISIONS（EXP-04 = ABORTED with valuable insights · T-08 完成）
- [x] artifact-index analyze 通过（T-08 修复后 7/7 pass）
- [x] change-log 无 dangling 变更（EXP-04 ABORTED 已按 change-log 预设触发条件处理：不触发 ORD-15 升级；记 valuable insights）

## 下阶段

- **项目结束**（单 phase 设计）→ 不开 phase-02
- proj-run 完整版（SKILL.md + 5 assets）已就绪发布
- EXP-04 留作"小规模项目 model-tier 不经济"的反例数据；后续如需再验证 model-tier，须选 ≥ $10.5 baseline 规模的项目
- 后续动作建议：若用户决定关闭 EXP-04 不再试，可在 09 轮 proj-shape（如有）正式标 EXP-04 状态 = closed（保留 valuable insights 注脚）
