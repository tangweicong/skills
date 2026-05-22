# PMO Analyze（SDD 交叉校验）

> 类比 Spec Kit `/analyze`：在 **GATE 通过后**、**阶段结束前** 执行；失败则 **不得** 标记 GATE 通过或进入下阶段。

## 何时运行

| 时机 | 必须 |
|------|------|
| Round B：GATE-2 后、写完全部 Round B artifact | ✓ |
| 每阶段：acceptance 前 | ✓ |
| change-log 有「已批准」条目后 | ✓ |

## 硬规则（失败 = blocked）

- [ ] **GATE 顺序**：manifest 中未通过 GATE 的下游 artifact **不存在**（INV-03）
- [ ] **INV-02**：`phase-roadmap.md` **无**任务表（无 `#`/`| 任务 |` 级细项）
- [ ] **WBS ↔ roadmap**：roadmap 每阶段映射 WBS ID 在 `wbs.md` 存在
- [ ] **integration-plan**：子计划索引中「已启用」项在磁盘有文件
- [ ] **artifact-index**：表中每条路径文件存在；版本与文件头一致
- [ ] **DECISIONS 链**：charter/wbs 关键结论可追溯到 INV/ORD/EXP ID
- [ ] **EXP**：每条 open/pending EXP 在 risk-register 或 phase plan/review 有归属
- [ ] **change-log**：已批准变更已反映到目标 artifact 版本

## 软规则（警告，可记 review）

- [ ] phase-roadmap 里程碑与 wbs 完成定义不矛盾
- [ ] 模式 F 启用项（risk/stakeholder/communication）非空模板
- [ ] plan 中 sub-agent 任务有 handoff 说明

## 输出

在 `artifact-index.md` 「交叉校验」节更新日期 + 勾选；失败项写入 `phase-NN/review.md` 或阻塞 GATE。
