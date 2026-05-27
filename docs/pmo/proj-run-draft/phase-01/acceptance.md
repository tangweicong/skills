# 验收手册 — phase-01 · proj-run 完整版起草 + EXP-04 试跑

| # | 验收项 | 通过标准 | 结果 |
|---|--------|----------|------|
| 1 | T-01 · dispatch-manifest-template.md | 5 项 validation 全通过 | **☑ pass**（V1~V5 全过，141 行）|
| 2 | T-02 · acceptance-template.md | 4 项 validation 全通过 | **☑ pass**（V1~V4 全过，82 行）|
| 3 | T-03 · cursor-agents-template.md | 4 项 validation 全通过 | **☑ pass**（V1~V4 全过，113 行）|
| 4 | T-04 · message-bus-template.md | 4 项 validation 全通过 | **☑ pass**（V1~V4 全过，62 行）|
| 5 | T-05 · validation-gate-template.md | 4 项 validation 全通过 | **☑ pass**（V1~V4 全过，99 行）|
| 6 | T-06 · proj-run/SKILL.md 完整版 | 覆盖 v0 + ORD-18~22 全 5 章节 + 工作流/失败模式/触发词 + ≤600 行 + 中文双层标题 + validate_skills.py 通过 | **☑ pass**（283 行，13 章节齐 · 标题 `# 执行调度（proj-run）` · validate 4/4 退 0）|
| 7 | T-07 · analyze checklist | 7 硬规则全 pass | **☑ pass · T-08 修复后**（T-07 初跑 6/7 fail rule 5；T-08 修复 artifact-index 后 Opus 父再跑 7/7 pass）|
| 8 | T-08 · 同步 + README + DECISIONS 回写 + review | validate 退 0；DECISIONS EXP-04 状态非 pending；skills/README.md proj-run 行已更新 | **☑ pass** |

## EXP-04 v1.4 度量

### baseline（已锁定）

| 项 | 值 | 出处 |
|---|----|------|
| baseline lines | 1066（302 SKILL + 764 assets）| `wc -l skills/proj-plan/SKILL.md skills/proj-plan/assets/*.md` |
| baseline bytes | 46,350 utf-8 | 同上 |
| baseline output tokens（估算）| ~10,375 | CJK 4855/1.5 + ASCII 28555/4 |
| baseline input tokens（估算 · 6 轮迭代累加）| ~90,000 | output × ~8x |
| baseline cost · 一次性写完 | ~$2.25 | 90K × $15/M + 12K × $75/M |
| baseline cost · **含 3x 迭代因子** | **~$6.75** | 一次性 × 3x（proj-plan 实际经 6 轮迭代）|

### actual（试跑实测 · 节点估算）

> **测量方法说明**：本试跑无精确 token 计量器；估算依据 = 父 agent 读取文件总字符数 ÷ 3.5（CJK+英文混合的 ~tokens/char 比率）+ sub-agent 报告自己的 token 估算。误差范围约 ±20%。

| 节点 | 阶段 | Opus input tokens | Opus output tokens | Composer Fast input | Composer Fast output | 节点 cost |
|------|------|-------------------|--------------------|----------------------|----------------------|-----------|
| N-01 | 读 DECISIONS + 07 轮 + skill 文档 + 8 模板（plan 阶段前置）| ~15,000 | — | — | — | ~$0.225 |
| N-02 | 起草 08 轮 docs + DECISIONS 同步 + 5 处 StrReplace | ~3,000 | ~7,000 | — | — | ~$0.045 + $0.525 = $0.57 |
| N-03 | Round A 4 文档 + GATE-0 准备 | ~2,000 | ~3,500 | — | — | ~$0.03 + $0.26 = $0.29 |
| N-04 | Round B 7 文档 + analyze 内联 + GATE-1+2 | ~5,000 | ~10,000 | — | — | ~$0.075 + $0.75 = $0.825 |
| N-05 | phase-01/plan + acceptance + GATE-3 | ~3,000 | ~7,000 | — | — | ~$0.045 + $0.525 = $0.57 |
| N-06 | T-01~T-05 + T-07 dispatch（6 sub-agents：sub-agent 自报 token + Opus 评审）| ~15,000（dispatch prompt + return summary 读）| ~3,000（dispatch prompt 写）| ~55,000（sub-agent 输入：dispatch prompt + 读参考文件）| ~12,000（sub-agent 输出：模板 + 报告）| Opus: ~$0.225+$0.225=$0.45；Composer: ~$0.165+$0.18=$0.35；小计 ~$0.80 |
| N-07 | T-06 SKILL.md Opus 直写（读 5 templates 自己写 + 8 templates 风格参考）| ~5,000 | ~6,000 | — | — | ~$0.075 + $0.45 = $0.525 |
| N-08 | T-08 同步 DECISIONS + README + acceptance + review + index + 再 analyze（本节）| ~5,000 | ~5,000 | — | — | ~$0.075 + $0.375 = $0.45 |
| **累计** | — | **~53,000** | **~41,500** | **~55,000** | **~12,000** | **~$4.26**（中位估算）|

**估算范围**：保守上界 ~$4.5（input/output 高估 20%）；激进下界 ~$3.4（低估 20%）。

### EXP-04 v1.4 判定

| 信号 | 阈值 | 实际 | 结果 |
|------|------|------|------|
| 成功 · cost ≤ 1/3 baseline | actual ≤ $2.25（≥3x 节省）| **~$4.26**（中位估算）| **☒ fail** |
| 成功 · GATE 一次通过率 ≥ 80% | ≥ 4/4 = 100% | GATE-0 ☑ + GATE-1 ☑ + GATE-2 ☑ + GATE-3 ☑ = **4/4 = 100%** | **☑ pass** |
| 成功 · analyze 通过 | T-07 7 硬规则全 pass | **6/7（T-07）→ 7/7（T-08 修复后）** | **☑ pass** |
| 成功 · validate_skills.py 通过 | shell exit 0 | exit 0（4 skills validated） | **☑ pass** |
| 中止 · cost 节省 < 2x | actual > $3.375 | **~$4.26 > $3.375**（节省 ~1.58x < 2x）| **☑ 触发**（abort 信号命中）|
| 中止 · Composer validation 反复失败 > 3 次/template | — | 0 次失败（5 templates 全 1/2 iteration 一次过）| ☐ 未触发 |
| 中止 · Opus plan 无法被 Composer 解读 | — | 6/6 dispatch 全部 sub-agent 一次产出符合 dispatch prompt 要求 | ☐ 未触发 |
| 中止 · Cursor sub-agent 关键 feature 阻塞 | — | Task tool + composer-2.5-fast model dispatch 均可用 | ☐ 未触发 |

**最终判定**：**ABORTED**（cost 中止信号触发：估算 actual ~$4.26 > $3.375 = $6.75 × 1/2；节省 ~1.58x < 2x 中止阈值）

**ABORTED 不等于失败**：4 个成功信号中 3 个全过（GATE 100%、analyze 7/7、validate 退 0）；仅 cost 信号未达阈值。试跑暴露的核心洞察是 **valuable data**：

| 洞察 | 数据支持 |
|------|---------|
| **Opus plan 阶段成本占主导** | N-01~N-05（plan 阶段）累计 ~$2.48；占 baseline 的 ~37%；占 actual 的 ~58% |
| **Composer Fast 执行层 cost 极低** | sub-agent dispatch 总 cost ~$0.35（5 template + 1 audit）；占 actual ~8% |
| **Opus 评审 + 直写主导成本** | Opus 全程（plan + 评审 + T-06 直写 + T-08 同步）~$3.91；占 actual ~92% |
| **算术天花板**：actual 中 plan + Opus 直写 ~$3.5 是固定成本，与 sub-agent 数量无关；要实现 ≥3x 节省，project 总规模需 ≥ $10.5（即 plan 成本占比 < 22%）；当前小项目无此条件 |
| **model-tier 真正生效**：需 plan 成本占比 < 20% 的大项目（多 phase / 大 execute 量）；本试跑案例规模不足 |
| **正面验证**：Composer Fast sub-agent 对结构化模板任务**质量充分**（5/5 templates 一次过 validation；0 escalate）|

## Sub-agent dispatch log

| Dispatch # | task | model | iteration | validation 通过项 | failed 项 | escalate? | 时间 |
|-----------|------|-------|-----------|------------------|-----------|-----------|------|
| 1 | T-01 dispatch-manifest-template | composer-2.5-fast | 1/2 | V1~V5 全 5 | — | ☐ 无 | 2026-05-27 |
| 2 | T-02 acceptance-template | composer-2.5-fast | 1/2 | V1~V4 全 4 | — | ☐ 无 | 2026-05-27 |
| 3 | T-03 cursor-agents-template | composer-2.5-fast | 1/2 | V1~V4 全 4 | — | ☐ 无 | 2026-05-27 |
| 4 | T-04 message-bus-template | composer-2.5-fast | 1/2 | V1~V4 全 4 | — | ☐ 无 | 2026-05-27 |
| 5 | T-05 validation-gate-template | composer-2.5-fast | 1/2 | V1~V4 全 4 | — | ☐ 无 | 2026-05-27 |
| 6 | T-07 analyze auditor（readonly）| composer-2.5-fast | 1/1 | 报告含 7 硬规则 + 软规则建议 + token 估算 | — | ☐ 无（rule 5 fail 是审核结果，不是 auditor 失败）| 2026-05-27 |

## Analyze（SDD · T-07 跑完 + T-08 修复后再跑）

- [x] 本阶段 plan 任务与 wbs/roadmap 映射一致（T-07 rule 3 pass）
- [x] 无 GATE 越权 artifact（T-07 rule 1 pass）
- [x] proj-run/SKILL.md + 5 templates 全存在且 validation 通过（实测验证）
- [x] DECISIONS EXP-04 状态已回写（T-08 完成）
- [x] artifact-index.md 已同步 sub-agent 产出登记（T-08 修复 rule 5 fail）

## 结论

- [ ] **通过** — 可进入 review；EXP-04 状态 = PASSED → 触发后续 ORD-15 升级
- [x] **不通过（cost 信号）** — **circuit breaker · EXP-04 cost 中止**：abort EXP-04；EXP-04 状态 = **ABORTED with valuable insights**；不触发 ORD-15 升级（保持 manifest 段 v0 可选）
- [ ] **部分通过** — 主交付完成但 EXP-04 介于成功/中止；EXP-04 状态 = PARTIAL

**注**：主交付（proj-run 完整版 SKILL.md + 5 templates + PM artifact）全部完成且通过 validation；本 phase 的项目级交付 ✓。**仅 EXP-04 cost 信号未达**——按 v1.4 阈值客观判定为 ABORTED；不阻塞 proj-run 完整版发布；不触发 ORD-15 升级。

**验收人 / 日期**：用户审批中 / 2026-05-27
