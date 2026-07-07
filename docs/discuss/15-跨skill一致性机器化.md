# 15-跨 skill 一致性机器化（扩 validate_skills.py 做跨 artifact 校验）

| 字段 | 值 |
|------|-----|
| 轮次 | 15 |
| 主题 | backlog #2（收敛 3）：扩 `scripts/validate_skills.py`，把「DECISIONS↔轮次同步 / skill↔README 索引 / pipeline-state 内部一致」做成可机器断言的 lint，降低人工 parity 维护能量 |
| 日期 | 2026-06-30 |
| 状态 | **已实现**（用户 GATE = C1–C4 全 + 扩 `validate_skills.py`）→ ORD-33；VERIFY 全过 |
| 讨论方法 | `proj-experts`（承接 round 13 收敛 3 + Shannon/Bertalanffy 视角，收敛型轻量轮）|
| 写入格式 | 轻量 |
| 承接 | `13-…md` 收敛 3 + §同步注记 backlog #2；ORD-32（#1 刚加的 `pipeline-state` 块 = 本项校验对象之一）；现有 `scripts/validate_skills.py`（逐 skill frontmatter/布局校验，6/6 退 0，ORD-22 lint gate 引用它）|

## 用户输入（本轮）

> 继续 #2

→ 推进序 #2 = 跨 skill 一致性机器化（round 13 收敛 3 + 收敛 1 的「降低维持有序能量」修向）。本轮 = 讨论收敛检查项设计 → GATE → 实现。

## 事实与假设

### 已查证事实（读现状，不臆造）

- **F1 · 现有 validator 范围**：`scripts/validate_skills.py` 当前只做**逐 skill** 校验——frontmatter（name/description 规则）+ 目录名匹配 + SKILL.md 行数上限；**无任何跨 artifact 检查**。入口 `main()` 遍历 `skills/*`，无 DECISIONS/README/轮次的交叉校验。来源：`scripts/validate_skills.py` 全文。
- **F2 · ORD-22 已把它定为 lint gate**：proj-run Validation gate 3 类中 lint 类典型命令 = `uv run scripts/validate_skills.py`；即本脚本已是项目**唯一 lint 入口**。来源：`skills/proj-run/SKILL.md` §Validation gate。
- **F3 · 项目自身的「可机判」纪律**：proj-run F3 = 「validation criteria 写成『质量好/结构完整』等模糊判据 → sub-agent 自我宣告完成」；对策 = validation 必须可由一行 shell/grep 判定。**任何新增检查必须可机器决定、低误报**，否则反噬信任。来源：`proj-run/SKILL.md` §失败模式 F3 + F9（`grep -c` 兜底）。
- **F4 · 现成的人工 parity 负担**：proj-shape「同步检查清单」要求人工核对「当轮每条已确定在 DECISIONS 有对应 ID / DECISIONS 每条有效 ID 来源指向正确轮次 / 无单边存在」——这正是 round 13 收敛 3 指的「人工 parity = 易错信道」。来源：`skills/proj-shape/SKILL.md` §同步检查清单。
- **F5 · README 索引格式**：README 用表格 + 链接 `[name](./skills/<name>/)` 引用 6 skill；可机判「skills/* ↔ README 提及」双向。来源：`README.md` 行 9–14。

### 推理（承接 round 13，标注三元组）

- **推理 · 模拟推理 · Shannon（round 13 收敛 3）**：人工 parity 校验是易错信道；把「DECISIONS↔轮次 / skill↔README / pipeline-state」一致性下沉为机器断言 = 给冗余信道加自动纠错码，降低维持有序的人力能量。依据 `13-…md` §收敛 3 + §视角 B。
- **推理 · proj-experts · 边界（防过度工程）**：依据 proj-run F3 + 用户 rule #2「简单优先」，**只自动化可机器决定、零/低误报的检查**；语义级一致（决定条文等价、三分离标注对错、推理三元组齐全）**故意不自动化**——强行 lint 会高误报，反噬信任（撞 F3）。这类留给人/GATE/proj-shape 纪律。

### 待验证 / 未查证

- **U1**：C4（轮次同步状态 → DECISIONS）对**历史轮次**会不会误报已废止 ID（如 EXP-03 N/A）？→ 设计上「DECISIONS 已知 ID 集」**含变更日志**（废止 ID 仍在日志）→ 不误报。实现时验证。

## 方法专属输出（proj-experts）

收敛轮（轻量）：experts 分析已在 round 13（Shannon/Bertalanffy/收敛 3）完成；推理已在上节标三元组。省略独立多视角节。

## 讨论

### 提议的检查项（全部可机器决定 · 低误报）

| ID | 检查 | 判定方式（一行可机判）| 对应收敛/痛点 | 误报风险 |
|----|------|----------------------|---------------|----------|
| **C1** | `DECISIONS.md` 有 `pipeline-state` 块且 `stage`/`status`/`pending_exp` 三字段齐；`stage` ∈ {exploring,deciding,ready-for-implementation,blocked} | 解析顶部 yaml fenced 块 | 锁 ORD-32 结构（#1 依赖）| 零 |
| **C2** | `pipeline-state.pending_exp` 每个 EXP id (a) 在 §待验证尝试表有行；(b) 该行**未**标 passed / ABORTED（即确为「开放」）| 正则 EXP 表行 + 状态列关键字 | DECISIONS 内部一致（机读块↔EXP 表不漂移）| 低（状态关键字稳定）|
| **C3** | `skills/*`（除 template）每个目录名在 README 出现；README 引用的 `./skills/<name>/` 每个都有真实目录 | 集合双向差 | skill↔README 索引（收敛 3）| 零 |
| **C4** | 每个 `docs/discuss/NN-*.md` 的「## DECISIONS 同步状态」表里出现的 INV/ORD/EXP id，必须在 `DECISIONS.md` **某处**出现（决定表 / EXP 表 / 变更日志）| 正则同步表 id + 全文 id 集 | 轮次→DECISIONS 同步（收敛 3 / F4）| 低（含变更日志 → 不误报废止 ID · U1）|

### 故意不自动化（守边界 · 防 F3 高误报）

- 决定**条文语义等价**（轮次「已确定」与 DECISIONS 条文是否一字不差地一致）——语义判定，易误报。
- **三分离 / 三档标签**标注是否正确、**推理三元组**（方法/角色/URL）是否齐全——需语义理解。
- 这些**保留为人/GATE/proj-shape 同步检查清单**职责（F4 仍由人兜底，但 C1–C4 把最机械、最易漏的那部分接走）。

### 落点：扩 `validate_skills.py` 还是新脚本？

- **倾向扩 `validate_skills.py`**（加一个 `validate_cross_artifact()`，main 末尾调用）：ORD-22 已把它定为唯一 lint gate（F2），单入口 = 项目各处 VERIFY 命令不用改；跨 artifact 错误前缀 `cross-artifact:` 与逐 skill 错误区分。
- 备选（新脚本 `validate_consistency.py`）：职责更纯，但多一个入口、ORD-22 引用需更新、VERIFY 命令要改两处——更碎，违简约。

### 与 #1 / #3 的关系

- C1/C2 正是把 #1（ORD-32）刚加的 `pipeline-state` 块**上锁**——印证 round 13 排序「#1 定义结构 → #2 校验结构」。
- 不依赖 #3。

## 可验证尝试与继续/中止

本轮无新 EXP。VERIFY（实现后已执行 · 双向）：

- **(a) 正向全过**：`uv run scripts/validate_skills.py` → `ok: 6 skill(s) validated + cross-artifact (C1–C4)` 退 0。
- **(b) 故意制造不一致须 fail**（防「永远 pass 的假门」）：
  - C2：`pending_exp` 注入 `EXP-99`（无行）+ `EXP-01`（已 passed）→ 退 1，两条都指名 ✓（已回滚）。
  - C1：无 `yaml` 块 → `_extract_first_yaml_block` 返回 None；缺 `pending_exp` + `stage: bogus` → 字段缺失 + 越枚举均被检出 ✓。
  - C4：合成 `## DECISIONS 同步状态` 段含 `ORD-77`（DECISIONS 无）→ 列为未知 ✓；段外 id 正确忽略 ✓。
  - C3：实现时**真抓到** README 的 `cp -r template skills/my-new-skill`（示例非真 skill）→ 据此把匹配收紧为「带尾斜杠 `skills/<name>/`」（索引式引用），消除误报、保留双向力 ✓。

## 实现纪要

- 落点：`scripts/validate_skills.py` 加 `validate_cross_artifact()`（+ 3 个纯函数 helper），`main()` 仅在**全量运行**（无 targets）时调用；逐 skill 校验逻辑不动。错误前缀 `cross-artifact[Cn]:` 与逐 skill 错误区分。
- **故意不自动化**（守边界）：决定条文语义等价 / 三分离标注对错 / 推理三元组齐全 —— 保留人/GATE/proj-shape 职责（见上「故意不自动化」节）。
- **C3 误报修正**（实现中真实发生）：初版正则 `skills/(name)` 把代码块示例 `skills/my-new-skill` 误判为悬空引用；收紧为 `skills/(name)/`（需尾斜杠）——6 个真 skill 在索引表均以 `./skills/<name>/` 出现，示例无尾斜杠正确被忽略。印证「只自动化低误报检查」的边界纪律。

## 本轮决定

### 已确定 — 普通决定（新增/修订）

- **ORD-33（新增）**：扩 `scripts/validate_skills.py` 做**跨 artifact 一致性 lint**（4 项 · 全量运行时执行）——**C1** `pipeline-state` 块结构（三字段齐 + stage 枚举 · 锁 ORD-32）/ **C2** `pending_exp` ↔ §待验证尝试表一致（id 有行且未 passed/ABORTED）/ **C3** `skills/*` ↔ README 索引双向（尾斜杠引用）/ **C4** 各轮次「DECISIONS 同步状态」段 id ⊆ DECISIONS 全文 id 集（含变更日志 → 不误报废止）。语义级一致**故意不自动化**（防 proj-run F3 高误报）。落实 round 13 收敛 3。
  **来源**：`13-…md` 收敛 3 + §同步注记 backlog #2；ORD-32（C1/C2 校验对象）；推理 · Shannon（冗余信道纠错码）+ 边界（proj-run F3）；用户 @本轮 GATE（scope=C1–C4 全 · place=扩 validate_skills.py）
  → 已同步 DECISIONS.md `ORD-33` + 变更日志；VERIFY 双向全过。

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-33 | 新增 | ✓ |

讨论状态同步：维持 `deciding`（backlog #2 = ORD-33 已落实；#3 待推进）。

同步完成时间：2026-06-30

## 开放问题（本轮 GATE · 已回答）

1. **范围**：~~C1–C4 全 / 核心 C1–C3~~ → 用户选 **C1–C4 全**。
2. **落点**：~~扩 `validate_skills.py` / 新脚本~~ → 用户选 **扩 `validate_skills.py`**。

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-06-30 | draft：backlog #2 讨论；4 项可机判检查 C1–C4 + 故意不自动化的语义级边界；落点二选一；候选 ORD-33 待 GATE |
| 1.1 | 2026-06-30 | 用户 GATE = C1–C4 全 + 扩 validate_skills.py；实现 + 双向 VERIFY 全过（含 C3 误报实测→收紧正则）；升 ORD-33 |
