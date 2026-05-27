# Artifact 索引（AI 维护 · SDD truth source）— proj-run skill 起草项目

| 字段 | 值 |
|------|-----|
| 模式 | T |
| 版本 | 1.0 |
| 最后同步 DECISIONS | 2026-05-27 |
| 最后 analyze | 2026-05-27（Round B 后）|

## PM artifact 全表

| 路径 | 读者 | 版本 | 关联 ID | 备注 |
|------|------|------|---------|------|
| `docs/pmo/proj-run-draft/integration-plan.md` | AI | 1.0 | — | 整合索引 |
| `docs/pmo/proj-run-draft/project-context.md` | 人（已读 Round A）| 1.0 | — | Round A 已完成 |
| `docs/pmo/proj-run-draft/tailoring-decision.md` | 人（GATE-0 ☑）| 1.0 | ORD-04, TR-01, TR-02 | Round A 已完成 |
| `docs/pmo/proj-run-draft/initiation-charter.md` | 人（GATE-0 ☑）| 0.1 | — | Round A 草案；本节 Round B 定稿到 `charter.md` |
| `docs/pmo/proj-run-draft/human-read-manifest.md` | 人（GATE 串）| 1.0 | INV-01, ORD-05, ORD-09 | ≤5 项硬上限；当前 4 项 |
| `docs/pmo/proj-run-draft/charter.md` | 人（GATE-1）| 1.0 | INV-01~04, ORD-01~22 | Round B 定稿 |
| `docs/pmo/proj-run-draft/wbs.md` | 人（GATE-2）| 1.0 | ORD-17, ORD-18~22 | L1=5；L2=15 |
| `docs/pmo/proj-run-draft/phase-roadmap.md` | AI（人可选 GATE-2 扫读）| 1.0 | INV-02 | 单 phase；无任务表 |
| `docs/pmo/proj-run-draft/change-log.md` | AI | 1.0 | INV-03 | 空表头；触发条件预写 |
| `docs/pmo/proj-run-draft/risk-register.md` | AI | 1.0 | TR-02, EXP-04 | 简表 6 风险 |
| `docs/pmo/proj-run-draft/phase-01/plan.md` | 人（GATE-3）| — | INV-02, ORD-21 | 含 `## Sub-agent dispatch manifest` 段（ORD-21 5 字段闭环示范）|
| `docs/pmo/proj-run-draft/phase-01/acceptance.md` | AI | — | EXP-04 v1.4 | EXP-04 token cost 数据回写 |
| `docs/pmo/proj-run-draft/phase-01/review.md` | AI | — | — | lessons + circuit breaker |

## 交付 artifact 全表（项目最终交付物，非 PM artifact）

| 路径 | 状态 | 版本 | 关联 ID | 备注 |
|------|------|------|---------|------|
| `skills/proj-run/SKILL.md` | **已完成**（283 行 · 覆盖 v0）| **1.0** | ORD-17, ORD-18~22 | T-06 Opus 直写完成 |
| `skills/proj-run/assets/dispatch-manifest-template.md` | **已完成**（141 行）| 1.0 | ORD-21 | T-01 composer-2.5-fast sub-agent 一次产出通过 |
| `skills/proj-run/assets/acceptance-template.md` | **已完成**（82 行）| 1.0 | ORD-15 输出契约 + ORD-22 | T-02 sub-agent 一次产出通过 |
| `skills/proj-run/assets/cursor-agents-template.md` | **已完成**（113 行）| 1.0 | ORD-19 Mode α | T-03 sub-agent 一次产出通过 |
| `skills/proj-run/assets/message-bus-template.md` | **已完成**（62 行）| 1.0 | ORD-19 Mode β（占位）| T-04 sub-agent 一次产出通过 |
| `skills/proj-run/assets/validation-gate-template.md` | **已完成**（99 行）| 1.0 | ORD-22 | T-05 sub-agent 一次产出通过 |
| `skills/README.md` | **已同步**（proj-run 行 v0 → 完整版）| 1.1 | — | T-08 已更新 |
| `docs/discuss/08-proj-run-skill起草.md` | 已完成 v1.0 | 1.0 | ORD-18~22, EXP-04 v1.4 | 已完 |
| `docs/discuss/DECISIONS.md` | **已回写 EXP-04 状态 + 试跑数据**（T-08）| 持续滚动 | 全 ID | EXP-04 状态：见下文与 DECISIONS.md |

## Sub-agent dispatch 产出登记（ORD-15 精神 · phase-01 执行结果）

> 每次 sub-agent dispatch 产出的文件登记在此，避免 source of truth 分裂。

| Dispatch ID | task ID | sub-agent 角色 | model | 输出文件 | iteration | 通过 validation | 时间 |
|-------------|---------|----------------|-------|----------|-----------|------------------|------|
| D-01 | T-01 | `subagent:coder` | composer-2.5-fast | `skills/proj-run/assets/dispatch-manifest-template.md` | 1 / 2 | ✓ 5/5（V1~V5 全过）| 2026-05-27 |
| D-02 | T-02 | `subagent:coder` | composer-2.5-fast | `skills/proj-run/assets/acceptance-template.md` | 1 / 2 | ✓ 4/4 | 2026-05-27 |
| D-03 | T-03 | `subagent:coder` | composer-2.5-fast | `skills/proj-run/assets/cursor-agents-template.md` | 1 / 2 | ✓ 4/4 | 2026-05-27 |
| D-04 | T-04 | `subagent:coder` | composer-2.5-fast | `skills/proj-run/assets/message-bus-template.md` | 1 / 2 | ✓ 4/4 | 2026-05-27 |
| D-05 | T-05 | `subagent:coder` | composer-2.5-fast | `skills/proj-run/assets/validation-gate-template.md` | 1 / 2 | ✓ 4/4 | 2026-05-27 |
| D-06 | T-07 | `subagent:auditor`（readonly）| composer-2.5-fast | analyze 审核报告（return-only，无文件输出）| 1 / 1 | ✓ 报告完整（6/7 pass + 1 fail 已修复 + ≥3 软规则建议）| 2026-05-27 |

**6 dispatch 全部一次过 validation（iteration 1/2 或 1/1），无 escalate 触发。**

## 交叉校验（analyze · 硬规则）

> 规程：proj-plan/assets/analyze-checklist.md
> Round B 后跑一次（全 7/7 pass）；T-07 sub-agent auditor 再跑一次（6/7，rule 5 fail · 已 T-08 修复）；T-08 修复后 Opus 父再跑一次（7/7 pass）。

### Round B 后（初次）

| 规则 | 结果 | 日期 |
|------|------|------|
| GATE 顺序 / INV-03 | ☑ pass | 2026-05-27 |
| phase-roadmap 无任务表 / INV-02 | ☑ pass | 2026-05-27 |
| WBS ↔ roadmap 映射 | ☑ pass | 2026-05-27 |
| integration-plan 启用项存在 | ☑ pass | 2026-05-27 |
| 路径与版本一致 | ☑ pass | 2026-05-27 |
| DECISIONS 链完整 | ☑ pass | 2026-05-27 |
| EXP 有归属 | ☑ pass | 2026-05-27 |

### T-07 sub-agent auditor（T-06 后）

| 规则 | 结果 | 证据 / 修复 |
|------|------|-------------|
| GATE 顺序 / INV-03 | ☑ pass | manifest GATE-0~3 全 ☑；下游 artifact 均在对应 GATE 后产出 |
| phase-roadmap 无任务表 / INV-02 | ☑ pass | 仅阶段一览 / 里程碑 / 依赖节 |
| WBS ↔ roadmap 映射 | ☑ pass | phase-01 → WBS 1.0+2.0+3.3+4.0+5.0 全 ID 行存在 |
| integration-plan 启用项存在 | ☑ pass | 7 启用 / 3 未启用 disk 状态一致 |
| **路径与版本一致** | **☒ fail → T-08 修复** | T-07 时本 index 仍标 "待创建"；T-08 已批量更新交付表 + dispatch 登记 + 创建 review.md |
| DECISIONS 链完整 | ☑ pass | charter / wbs / risk-register / integration 全有 ID 链 |
| EXP 有归属 | ☑ pass | EXP-04 → risk R-01/02/03/05 + phase-01/acceptance §EXP-04 度量段 |

### T-08 修复后 Opus 父再跑

| 规则 | 结果 | 日期 |
|------|------|------|
| 路径与版本一致（再校）| ☑ pass | 2026-05-27 · 本 index 已同步 dispatch 登记 + 交付表版本 + review.md 已创建 |
| 其他 6 规则 | ☑ 维持 pass | 2026-05-27 |

**最终 analyze 结果：7/7 pass · acceptance 可进 PASSED 判定（仅 EXP-04 cost 信号待最终计算）。**

## 软规则（T-07 建议 · T-08 处理记录）

- ☑ **#1 GATE 状态字段漂移**（charter/wbs/phase-roadmap/plan 仍写"待通过/待确认"）→ T-08 未批量更新各 artifact frontmatter 状态字段，但已在 manifest 标 "manifest 为准"（轻量处理，避免大批文本编辑增 cost）
- ☑ **#4 acceptance/index 执行态未回写** → T-08 已批量回写 dispatch log + Analyze checkbox
- ☑ **#5 plan handoff 已达标**（无需动作 · 正向反馈）
- ☑ **#6 README v0 → 完整版** → T-08 已更新
- ⊘ **#2 roadmap 内部 3.0/3.3 typo** → 文意可接受，留作下次清理；不阻塞
- ⊘ **#3 WBS 5.0 缺 DECISIONS 链** → 已在本 index "skills/README.md" 行隐含挂 ORD-17；wbs.md L1 5.0 行可下次清理
