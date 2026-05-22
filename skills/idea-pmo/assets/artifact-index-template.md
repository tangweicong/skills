# Artifact 索引（AI 维护 · SDD truth source）

| 字段 | 值 |
|------|-----|
| 模式 | T / F |
| 版本 | 1.0 |
| 最后同步 DECISIONS | YYYY-MM-DD |
| 最后 analyze | YYYY-MM-DD |

| 路径 | 读者 | 版本 | 关联 ID | 备注 |
|------|------|------|---------|------|
| docs/pmo/integration-plan.md | AI | 1.0 | | 整合索引 |
| docs/pmo/charter.md | 人 GATE-1 | 1.0 | | |
| docs/pmo/wbs.md | 人 GATE-2 | 1.0 | | |
| docs/pmo/phase-roadmap.md | AI | 1.0 | INV-02 | 无任务表 |
| docs/pmo/change-log.md | AI | 1.0 | | |
| docs/pmo/risk-register.md | AI | | TR-02 | 可选 |
| docs/pmo/phase-01/plan.md | 人 GATE-3 | | INV-02 | rolling |
| … | | | | 模式 F 扩展 |

## 交叉校验（analyze · 硬规则）

> 规程：skill 内 [analyze-checklist.md](analyze-checklist.md)

| 规则 | 最后结果 | 日期 |
|------|----------|------|
| GATE 顺序 / INV-03 | ☐ pass ☐ fail | |
| phase-roadmap 无任务表 / INV-02 | ☐ | |
| WBS ↔ roadmap 映射 | ☐ | |
| integration-plan 启用项存在 | ☐ | |
| 路径与版本一致 | ☐ | |
| DECISIONS 链完整 | ☐ | |
| EXP 有归属 | ☐ | |

**analyze 失败 → 不得标记 GATE 通过或进入下阶段。**
