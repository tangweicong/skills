# 26-可理解性规范-大白话与teach-back

| 字段 | 值 |
|------|-----|
| 轮次 | 26 |
| 主题 | I-4 可理解性规范：大白话输出规范 + GATE 拍板前 teach-back 设计与接线 |
| 日期 | 2026-08-17 |
| 状态 | discussed（GATE 已确认 2026-08-17 → ORD-44 立项 + 3 处 diff 已 apply + U1 观察项确认 · 六论改造主线闭合）|
| 讨论方法 | `proj-experts`（复用 r22 F8 teach-back；新增联邦平实语言查证） |
| 写入格式 | 轻量（决定收敛轮） |
| 承接 | ORD-40（议题 I-4 · 序 4 · 最后议题）；r22 F8/F5 |

> 本轮 = ORD-40 议题 I-4 的决策轮（六论改造主线最后一个议题）：把 r22 已推的「可理解性」收敛为输出规范 + 拍板点 teach-back。产出 = 候选 ORD-44 + 3 处 diff 提案，不新增/修订 INV/ORD/EXP（候选待 GATE）。

## 用户输入（本轮）

> 用户拍板「继续」→ 按 ORD-40 议题序进入 I-4：可理解性规范（大白话输出规范 + GATE 拍板前 teach-back）；产出形态 = ORD 候选 + 输出规范 diff；判据 = 与 INV-01/ORD-12 无冲突。

## 事实与假设

### 轻量框定（查证前问题清单）

**消费上轮「最没把握」条目**（r25 #1：「可选段」是否会因可选而从不被使用）：属 I-3/U1 dogfood 观察项，本轮 I-4 不触及 → 不立查证问题，观察继续。

**外部前提复查（ORD-39）**：本轮不触及任何登记条目（ORD-16/EXP-08b/11/12/13/14 均与输出规范无关）。**复查结论（2026-08-17）**：无条目需复查，留痕如上。

| # | 待查问题 | 查证结论（摘要）|
|---|----------|------------------|
| Q1 | 「大白话规范」有无制度级先例？ | **有**：美国《Plain Writing Act of 2010》（联邦法律）+ plainlanguage.gov 原则（audience first、短句、主动语态、术语即解释）——政府/法律文本都强制平实化 [digital.gov 原则](https://digital.gov/guides/plain-language/principles) / [govinfo 法案全文](https://www.govinfo.gov/content/pkg/BILLS-111hr946pcs/xml/BILLS-111hr946pcs.xml) |
| Q2 | teach-back 先例？ | 复用 r22 F8：AHRQ teach-back——对方用自己的话复述、传达者核对，医疗健康素养标准工具 [AHRQ](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/teachback.html) |
| Q3 | 人拍板点清单（内部）？ | 三处：proj GATE 停点（总入口）/ proj-plan GATE-0/1/2/3 / proj-shape 就绪评估（含盲点双问） |

### 已查证事实

- **F1 · Plain Writing Act 2010（制度先例）**：联邦法强制政府公文平实化；原则 = audience first、短句、主动语态、术语即解释、结论先行 [digital.gov](https://digital.gov/guides/plain-language/principles) / [govinfo](https://www.govinfo.gov/content/pkg/BILLS-111hr946pcs/xml/BILLS-111hr946pcs.xml)。
- **F2 · teach-back（复用 r22 F8）**：AHRQ 标准工具——让患者用自己的话复述理解，由传达者核对纠偏 [AHRQ](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/teachback.html)。
- **F3 · 三处拍板点现状（内部）**：proj §GATE 清单（默认停点）、proj-plan GATE-0/1/2/3（人审节点）、proj-shape §3b 就绪评估（盲点双问已在此）。

### 推理（非事实、非待验证）

- **推理 · 联邦平实语言（Plain Writing Act）**：大白话 ≠ 降智——法律文本都能平实化且不损法效；AI 输出的**准确性**（三档标签/三分离/出处）与**可读性**是两个正交轴，平实化只动后者；依据 [plainlanguage.gov 原则](https://digital.gov/guides/plain-language/principles) 的「术语即解释 + 结论先行」。
- **推理 · AHRQ（teach-back）**：拍板错误的两大来源 = ① 人没读懂要拍什么 ② 人读懂了但 AI 理解偏了（解码错位）；teach-back 一次同时测两者——复述内容人核对 = 测①，复述偏差被纠正 = 测②；依据 [AHRQ teach-back](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/teachback.html) 的确认理解闭环。
- **推理 · 模拟推理 · Shannon（信息论）**：GATE 拍板 = 高 stakes 低容错的解码终点，此处加 ACK（teach-back）= 信道末端纠错；但**全程 ACK = 冗余过载**（人信道本就低带宽）→ 只放拍板点；依据 r22 推理节信息论条 + [Shannon 1948 信道容量]精神。

### 待验证 / 未查证

- **U1**：teach-back 在真实 GATE 中是否**真的改善拍板质量**（还是只加一道手续）——列 I-1 dogfood 并行观察项（与 ORD-41/42/43 同批）。
- **U2**：本轮单人设计（verifier=maker）→ 候选不自决，待用户 GATE。

### 方法专属输出

本轮省略（轻量级）：teach-back 事实已在 r22 查证（F8），新增仅联邦平实语言一项。

## 讨论

### 1. 定位：输出界面的低解码成本规范（信息论 ACK 的落点）

r22 已把「AI 默认人全懂」与「人读不动」定位为**输出界面**问题；本议题 = 给这个界面立两条规范：(a) 大白话（编码端降码本复杂度）；(b) GATE 拍板前 teach-back（解码端加 ACK）。均零新流程、纯呈现层。

### 2. 设计（候选 ORD-44）

**A · 大白话输出规范**（面向人的一切输出）：

1. **结论先行**：第一句给结论。
2. **默认人非专家**：专业名词首现即一句大白话解释（如「序参量 = 少数决定全局的慢变量」）。
3. **复杂决策附「一句话结论 + 理由」**：拍板前给「要拍什么 / 拍下去会怎样 / 为什么」三合一句话版。
4. **准确性不降级**：三档标签 / 三分离 / 出处照常（大白话≠降智）。

**B · GATE 拍板前 teach-back**（高 stakes 决策点）：

5. 交人拍板前，AI 用 **1–3 句**复述「当前要拍什么 + 拍下去的后果」。
6. 人核对复述无误后再拍板；复述有偏 → AI 先纠正复述。
7. **只在 GATE 拍板点使用**（全程使用 = 啰嗦，禁）。

### 3. 边界

- 与 **INV-01**（human-read-manifest ≤5）同向互补（都为人信道降载，一个限条目数、一个限解码难度）；
- 与 **ORD-12**（借鉴/自创立场声明）不冲突；
- **不改任何决定流程**——teach-back 是呈现层，决策权仍全在人（Supervised-AI · ORD-11/31 不变）。

### 4. 落点（3 处 diff · 待 GATE）

| 文件 | 改动 | 覆盖拍板点 |
|------|------|-----------|
| `skills/proj/SKILL.md` | 质疑义务节后新增「§可理解性输出规范（ORD-44）」小节（A+B 全文） | proj GATE 停点 |
| `skills/proj-plan/SKILL.md` | GATE-0 行后加一行注记（GATE-0/1/2/3 通用） | proj-plan GATE-0/1/2/3 |
| `skills/proj-shape/SKILL.md` | §3b 就绪评估加一行（拟标 ready 交人确认前 teach-back） | proj-shape 就绪 GATE |

### 5. 选项对比

| 选项 | 内容 | 判定 |
|------|------|------|
| A（选） | 三处接线（proj 小节 + plan/shape 各一行） | 拍板点全覆盖 + 改动最小 |
| B | 仅 proj 一节 | GATE-0/1/2/3 与就绪 GATE 无模板级防遗忘（EXP-14 证明「纪律持续在场」靠落点） |
| C | 仅 DECISIONS 条文 | 同上，且无输出端即时提醒 |

## 可验证尝试与继续/中止

本轮无新 EXP（纯呈现层 + 可逆 + 低风险；U1 由 I-1 dogfood 并行观察承担）。

## 本轮决定

> 决策轮：候选 ORD-44 + 3 处 diff 待用户 GATE；**不提前写入 DECISIONS**。

### 已确定 — 原则性不变量（新增/修订）

- 无。

### 已确定 — 普通决定（新增/修订）

- 无（候选 ORD-44 见下）。

### 对既有决定的修订

- 无。INV-01/ORD-12 条文不动（本设计与其同向互补）。

### 待确认（用户 GATE 清单）

1. **候选 ORD-44 条文**（§讨论 2：大白话规范 4 条 + teach-back 3 条）：认可？
2. **3 处 diff apply**（§讨论 4 表）：认可？
3. **U1（teach-back 真实增量）**列 I-1 dogfood 并行观察项：认可？

## DECISIONS 同步状态

| ID | 操作 | 与 DECISIONS 一致 |
|----|------|-------------------|
| ORD-44 | 新增（用户 GATE 后） | ✓ |

讨论状态同步：维持 `deciding`（I-4 已落实 ORD-44；**六论改造主线 4 议题全部闭合**；余 dogfood 并行观察项 + EXP-12 步2 载体候选；6 skill 仍 shipped/stable）。

同步完成时间：2026-08-17（GATE 后更新）

## 开放问题（下轮）

1. **本轮 AI 最没把握的点**：teach-back 在真实 GATE 中**是否真改善拍板质量还是沦为啰嗦手续**——挂靠候选 ORD-44 第 5–7 条；若为假（dogfood 观察中复述无增量或你觉得烦）→ 撤销 teach-back 半条，仅保留大白话规范 4 条。
2. 用户拍板 GATE 清单 3 项。
3. **主线闭合后事项**：I-1 dogfood 并行观察项汇总（ORD-41 U1/U2 + ORD-42 长会话 + ORD-43 U1 + ORD-44 U1 + EXP-12 步2 载体）+ 六论学习线（你自述还在学六论——可在真实项目讨论中按需引入对应透镜，不单开纯理论轮）。

## 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-08-17 | 初稿（I-4 决策轮 · 大白话规范 + teach-back 设计 + 候选 ORD-44 + 3 处 diff 提案；不新增/修订 INV/ORD/EXP） |
| 1.1 | 2026-08-17 | GATE 确认更新：ORD-44 立项 + 3 处 diff apply + U1 观察项确认；见 §同步注记 |

## 同步注记（2026-08-17 · 用户 GATE）

用户（Sponsor）GATE = 原话「同意」（GATE 清单 3 项全通过）：

1. **候选 ORD-44 → 已立项并落实**：大白话输出规范 4 条 + GATE 拍板前 teach-back 3 条。
2. **3 处 diff 已 apply**：`skills/proj/SKILL.md`（§可理解性输出规范节）+ `skills/proj-plan/SKILL.md`（GATE-0 后 teach-back 注记 · GATE-0/1/2/3 通用）+ `skills/proj-shape/SKILL.md`（§3b 就绪评估 teach-back 行）。
3. **U1（teach-back 真实增量）→ 已列 I-1 dogfood 并行观察项**。

**主线闭合**：六论改造 4 议题（I-1 挣得记账 / I-2 质疑条款 / I-3 维度表 / I-4 可理解性）全部落地。余项 = dogfood 并行观察（ORD-41 U1/U2 · ORD-42 长会话 · ORD-43 U1 · ORD-44 U1）+ EXP-12 步2 载体候选（I-1 落地首个真实 phase，取先到者）+ 六论学习线（真实项目讨论中按需引入透镜）。
