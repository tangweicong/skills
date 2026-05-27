# Skills Index

本目录下的每个子文件夹是一个独立的 Agent Skill。

> **2026-05-27 集体重命名**：`best-minds-grounded` → `proj-experts`（专家研判）、`idea-discuss` → `proj-shape`（想法收敛）、`idea-pmo` → `proj-plan`（项目蓝图）；新增 `proj-run`（执行调度，骨架版本）。详见 `docs/discuss/07-sub-agent-model-tier-编排.md` + `DECISIONS.md` ORD-15~17。

## 项目流水线（4 个 proj-* skill 对应 PMP 4 大 Process Group）

| # | Skill | 中文名 | PMP 对应 | Description |
|---|-------|-------|----------|-------------|
| 1 | [proj-experts](./proj-experts/) | **专家研判** | Initiating · Business Case · 商业论证 | Grounded 模拟器思维：先查证再模拟（可指定专家）；真实性三档标签（原话/立场/模拟推理）；建设性优于否定；无方案给推理路径+候选方向+待验证假设 |
| 2 | [proj-shape](./proj-shape/) | **想法收敛** | Initiating · 多轮决议 | 以实现为导向的多轮讨论框架：`docs/discuss/`（DECISIONS+轮次+EXP+就绪判断）；事实/推理/待验证三分离（方法无关）；分析层默认 proj-experts，可替换为其他讨论方法 skill；对下游 proj-plan 提供承诺字段 |
| 3 | [proj-plan](./proj-plan/) | **项目蓝图** | Initiate（charter）+ Planning + 规划侧 M&C + Closing | 承接 DECISIONS 的项目化规划：`docs/pmo/`（PMP 计划分层+SDD analyze/gate+integration-plan+change-log+rolling phase+sub-agent handoff manifest）；vision = 人 Sponsor+PM 决策 / AI PM 执行+artifact 维护（Supervised-AI mode）；显式标注借鉴（PMBOK 6/7/8 + Spec Kit 机制层）vs 本 skill 自创（Coach hybrid / 模式 T-F / GATE-N / manifest≤5）；配合 proj-experts + proj-shape（商业论证阶段）|
| 4 | [proj-run](./proj-run/) | **执行调度** | Executing | **完整版 1.0**（08 轮起草 · 283 行）：承接 proj-plan 的 phase-NN/plan.md + `## Sub-agent dispatch manifest`（ORD-21 5 字段闭环）；PMP 6 Executing 承接 3 项（Direct & Manage / Quality / Knowledge），其余 7 项刻意外置（ORD-18）；3 Mode 表 α/β/γ 按 plan 类型 + 跨 session 需求选择（ORD-19）；Sub-agent dispatch 决策树按 context 回溯需求判定（ORD-20，不按 cost）；Validation gate 3 类 structural/lint/behavioral（ORD-22）；含 5 assets templates + Cursor 约束披露（ORD-16）+ 失败模式（含 EXP-04 试跑观察）|

<!-- 新增 skill 后在此添加一行，并运行: uv run scripts/validate_skills.py -->
