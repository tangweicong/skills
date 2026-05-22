# WBS（工作分解结构）

| 字段 | 值 |
|------|-----|
| 模式 | T |
| GATE-2 | 2026-05-19 通过 |

## WBS 树

| ID | 名称 | 完成定义（一句话） | 关联 |
|----|------|-------------------|------|
| 1.0 | idea-pmo skill 发布 | skill 可发现、validate 通过、模板齐全 | ORD-01, EXP-01 |
| 1.1 | skill 包与模板 | `skills/idea-pmo/SKILL.md` + assets | |
| 1.2 | 仓库引用更新 | README、idea-discuss；废止 idea-implement | ORD-01 |
| 2.0 | EXP 验证 | EXP-01/02 状态更新 | ORD-08 |
| 2.1 | Round A/B 留痕 | 本目录 docs/pmo 完整 | EXP-01 |
| 2.2 | phase-01 rolling | plan + acceptance + review | INV-02, EXP-02 |

## 依赖

- 1.x 先于 2.1 试跑留痕验收
- 2.2 依赖 GATE-2 通过
