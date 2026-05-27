# 执行验收 — phase-{NN}（proj-run → proj-plan）

> proj-run 执行完本 phase 后回填 `docs/pmo/phase-{NN}/acceptance.md`；触发 proj-plan 的 `review.md` 与 GATE-3 判定。sub-agent 产出文件登记追加到 `artifact-index.md`（ORD-15 · 不在本文件）。

| 字段 | 值 |
|------|-----|
| phase | phase-{NN} |
| 关联 plan.md | `docs/pmo/phase-{NN}/plan.md` |
| 状态 | _进行中 / 通过 / 失败_ |

---

## 1 · validation 结果（ORD-22 · 三类 gate）

> 判据来源 = plan.md `## Sub-agent dispatch manifest` 段 `validation criteria`。每条：**判据命令 + pass/fail + 证据 1 行**。

### structural（结构 · 文件 / 字段 / 行数）

| # | 判据命令 | 结果 | 证据（1 行）|
|---|----------|------|-------------|
| S-1 | `test -f {产出路径}` | ☐ pass / ☐ fail | |
| S-2 | `wc -l {文件} ≤ {N}` | ☐ pass / ☐ fail | |
| S-3 | 必填字段 / 段关键字存在（如 manifest 5 字段）| ☐ pass / ☐ fail | |

### lint（静态 · schema / 工具）

| # | 判据命令 | 结果 | 证据（1 行）|
|---|----------|------|-------------|
| L-1 | `python validate_skills.py`（若改 skill）| ☐ pass / ☐ fail / ☐ n/a | |
| L-2 | markdown 结构 / YAML frontmatter 合规 | ☐ pass / ☐ fail | |
| L-3 | _manifest 指定 lint 项_ | ☐ pass / ☐ fail | |

### behavioral（行为 · grep / 负向断言）

| # | 判据命令 | 结果 | 证据（1 行）|
|---|----------|------|-------------|
| B-1 | `rg -c "{关键字}" {文件} ≥ N` | ☐ pass / ☐ fail | |
| B-2 | 负向：`rg -c "model:" {文件} = 0`（模板禁绑 model）| ☐ pass / ☐ fail | |
| B-3 | _manifest 指定 behavioral 项_ | ☐ pass / ☐ fail | |

**validation 汇总**：☐ 全 pass · ☐ 有 fail（见 §3 escalate）

---

## 2 · token cost（sub-agent dispatch · ORD-15）

| dispatch ID | task | model | input tokens | output tokens | 单价 | cost |
|-------------|------|-------|--------------|---------------|------|------|
| T-01 | _示例：起草 template_ | _由 proj-run 填_ | | | _由 proj-run 填_ | |
| **累计** | — | — | **_Σ_** | **_Σ_** | — | **_Σ cost_** |

> model 由 proj-run 按 Mode α/β/γ 决定；manifest 不指定具体 model 名，本表回填实际 tier。

---

## 3 · escalate 标记

| dispatch ID | task | 失败原因 | iteration 用尽 | 回退去向 |
|-------------|------|----------|----------------|----------|
| — | _无 escalate 时保留此行_ | | _budget 值_ | _回父 / 回 proj-plan / 回 proj-shape_ |

> validation 反复失败 → escalate 行必填 + 通知 GATE-N。全 phase sub-agent 累计失败 > 3 → circuit breaker（abort phase）。

---

## 4 · GATE 联动

| 条件 | 动作 |
|------|------|
| acceptance **通过**（validation 全 pass + 无未解 escalate）| 解锁 **GATE-N** → proj-plan 跑 `review.md` + 允许下阶段 plan |
| acceptance **失败** | **circuit breaker**：不得创建下一 phase plan；change-log + 回退本 phase 或 proj-shape |
| acceptance **PARTIAL** | 进 review 记 gap；**GATE-N** 人工判定缩 scope / 继续 / 回退 |

---

## 结论

- [ ] **通过** — 可进入 proj-plan `review.md`；允许下阶段规划
- [ ] **不通过** — **circuit breaker**：不得进入下阶段
- [ ] **部分通过（PARTIAL）** — 主交付完成但 validation / token cost / escalate 有 gap；GATE-N 人工判定

**验收人 / 日期**：__________________________
