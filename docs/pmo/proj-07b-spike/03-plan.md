# 形态1 · 段3 plan（proj 调 proj-plan · 出沙盒 plan）

> 落实 sROD-1 的最小 plan（T-lean）。

## 任务
| ID | 任务 | 执行者 | verify |
|----|------|--------|--------|
| T1 | 在沙盒产出 `pipeline-state` 块（`04-run-artifact.md`）| sub-agent（conversation-fallback adapter）| 见 dispatch manifest |

## Sub-agent dispatch manifest（ORD-21 · 5 字段闭环）
- **objective**: T1 — 产出含 3 必填字段的 `pipeline-state` 机读块
- **specialist**: `subagent:coder`
- **validation criteria**（父一行 shell 可判）:
  - `grep -c "^stage:" 04-run-artifact.md` ≥ 1
  - `grep -c "^status:" 04-run-artifact.md` ≥ 1
  - `grep -c "^pending_exp:" 04-run-artifact.md` ≥ 1
- **iteration budget**: 2
- **escalate**: 超 budget → 回 proj-plan 改 validation 措辞；仍失败 → 回 proj-shape 重审 sROD-1

## GATE（命中 → 默认档 STOP）
- proj-plan GATE-3（用户审 plan + manifest）→ **默认档此处 STOP**。EXP 授权下继续 → 交 proj-run。
