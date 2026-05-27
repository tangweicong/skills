# Agent Skills：想法 → 收敛 → 规划 → 执行（proj-* 流水线）

个人沉淀的 [Agent Skills](https://agentskills.io) 集合，可在 Cursor、Claude Code 等支持 Skills 的 Agent 中使用。

本仓库包含 **4 个可配合使用的 skill**，对应 PMP 4 大 Process Group，覆盖从模糊想法到执行落地的完整链路：

| Skill | 中文名 | PMP 对应 | 一句话 | 主要产出 |
|-------|--------|---------|--------|----------|
| [proj-experts](./skills/proj-experts/) | 专家研判 | Initiating · Business Case | 先查证，再模拟最懂的人怎么说（含选用理由 + 三档真实性标签）| 对话中的专家视角分析 |
| [proj-shape](./skills/proj-shape/) | 想法收敛 | Initiating · 多轮决议 | 以实现为导向的多轮讨论留痕 + 决定汇总 + 可验证尝试 | `docs/discuss/` |
| [proj-plan](./skills/proj-plan/) | 项目蓝图 | Initiate(charter) + Planning + 规划侧 M&C + Closing | 承接决定，做 PMP 分层规划 + GATE + analyze + dispatch manifest 承诺字段 | `docs/pmo/` |
| [proj-run](./skills/proj-run/) | 执行调度 | Executing | 承接 plan + dispatch manifest，调度 sub-agent + validation gate + escalate | `phase-NN/acceptance.md` + `.cursor/agents/*.md` |

```
模糊想法
    │
    ▼
┌─────────────────┐     ┌──────────────────────┐
│  proj-shape     │────▶│  docs/discuss/       │
│  （想法收敛）    │     │  DECISIONS.md + 轮次  │
└────────┬────────┘     └──────────────────────┘
         │ 分析层默认配合
         ▼
┌─────────────────┐
│  proj-experts   │  查证 + 专家视角 + 三档真实性标签
│  （专家研判）    │  （原话 / 已公开立场 / 模拟推理）
└─────────────────┘
         │ ready-for-implementation
         ▼
┌─────────────────┐     ┌──────────────────────┐
│  proj-plan      │────▶│  docs/pmo/           │
│  （项目蓝图）    │     │  WBS + 阶段 + GATE   │
└────────┬────────┘     │  + dispatch manifest │
         │              └──────────────────────┘
         │ GATE-3 通过 · phase-NN/plan.md（含 manifest）
         ▼
┌─────────────────┐     ┌──────────────────────┐
│  proj-run       │────▶│  acceptance.md       │
│  （执行调度）    │     │  + sub-agent 产出    │
└─────────────────┘     │  + .cursor/agents/   │
                        └──────────────────────┘
```

---

## 安装

将需要的 skill 目录链接或复制到 Agent 的 skills 路径：

```bash
# Cursor 示例（在本仓库根目录执行）
ln -s "$(pwd)/skills/proj-experts" ~/.cursor/skills/proj-experts
ln -s "$(pwd)/skills/proj-shape"   ~/.cursor/skills/proj-shape
ln -s "$(pwd)/skills/proj-plan"    ~/.cursor/skills/proj-plan
ln -s "$(pwd)/skills/proj-run"     ~/.cursor/skills/proj-run
```

也可在对话中 `@` 引用仓库内的 `SKILL.md`，或直接说出触发词（见各 skill 下方）。

---

## proj-experts（专家研判 · Initiating · Business Case）

**做什么**：Grounded 模拟器思维——先查证事实，再模拟「谁最懂这个问题的人」会怎么说；输出按 **三档真实性标签**（【原话】/【已公开立场】/【模拟推理】）分级，**绝不**把模拟推理伪装成原话。

**适用场景**：

- 架构 / 技术选型 / 策略决策，且涉及具体产品、项目或命名概念
- 想听「顶级专家会怎么看」，或指定某人视角（如「以 Karpathy 视角分析」）
- 问题没有工业界 playbook，需要基于专家已记录的原则做发散

**核心流程**：

1. 轻量框定：列出 TA 会先确认的 3–5 个事实问题
2. 定向 WebSearch（官方 docs / repo / issue / RFC）
3. 识别或锁定专家（用户指定优先）
4. 输出：每位 TA 先写 **选用理由**，再用三档标签产出观点

**触发词示例**：最强大脑 · 谁最懂这个 · 以 X 视角 · 模拟 Y · 指定专家 · 没有现成方案 · proj-experts

**单独使用**：可直接用于纯分析问答，不必开启讨论文档。

**详细说明**：[skills/proj-experts/SKILL.md](./skills/proj-experts/SKILL.md)

---

## proj-shape（想法收敛 · Initiating · 多轮决议）

**做什么**：以实现为终点的多轮想法讨论框架。把模糊想法磨清楚，留痕到 `docs/discuss/`，汇总已确定决定到 `DECISIONS.md`；对前沿 / 无现成解法的问题，产出可验证尝试（`EXP-xx`）及继续 / 中止标准。

**不负责**：MVP 细则、里程碑排期、写代码（这些交给 proj-plan 或执行阶段）。

**产出目录**（在项目根目录）：

```text
docs/discuss/
├── DECISIONS.md          # 已确定决定 + EXP 表 + 讨论状态（优先读此文件）
├── 01-初始想法简述.md
├── 02-技术选型争议.md
└── ...
```

**与 proj-experts 的分工**：

| 层 | skill | 产出 |
|----|-------|------|
| 分析层（方法可替换）| proj-experts（默认）/ pre-mortem / socratic-grounded / ... | 查证、专家视角、三档标签（完整执行）|
| 讨论层（框架）| proj-shape | 轮次文档 + DECISIONS 汇总 + 就绪判断 |

每轮讨论默认配合 proj-experts 做分析，由 proj-shape 重组写入文档；用户可显式切换其他讨论方法 skill。

**对 proj-plan 的承诺字段**：当讨论状态变为 `ready-for-implementation` 时，DECISIONS 必须为 proj-plan 准备好 INV/ORD 区分、成功标准、范围边界、EXP 降级路径、来源追溯。

**典型用法**：

```text
用户：我想做一个 XXX，但不确定技术路线，帮我讨论一下
→ Agent 启用 proj-shape，创建 docs/discuss/01-…md，同步更新 DECISIONS.md

用户：讨论够了吗？能不能开始做？
→ 对照「讨论就绪」硬条件，更新 DECISIONS 状态为 ready-for-implementation（须用户确认）
```

**讨论状态**：`exploring` → `deciding` → `ready-for-implementation` / `blocked`

**触发词示例**：想法讨论 · proj-shape · 前沿方案 · 无现成解法 · 可验证尝试 · 讨论够了没 · EXP · DECISIONS · 切换讨论方法

**详细说明**：[skills/proj-shape/SKILL.md](./skills/proj-shape/SKILL.md)

---

## proj-plan（项目蓝图 · Initiate + Planning + 规划侧 M&C + Closing）

**做什么**：承接 `docs/discuss/DECISIONS.md`，用 PMP 计划分层 + SDD gate/analyze 纪律生成 `docs/pmo/` 规划产物。AI 维护完整 artifact 集；人类**只读** `human-read-manifest.md`（≤5 项）。

**前置条件**：`DECISIONS.md` 讨论状态为 `ready-for-implementation`，或用户显式授权开工。

**不负责**：写新 INV/ORD（属 proj-shape）、执行代码、启动 sub-agent（执行归 proj-run；本 skill 只在 `phase-NN/plan.md` 末尾写 `## Sub-agent dispatch manifest` 承诺字段）。

**产出目录**（在项目根目录）：

```text
docs/pmo/
├── human-read-manifest.md   # 人类必读（≤5 项）+ GATE 状态
├── charter.md / wbs.md / phase-roadmap.md
├── integration-plan.md / change-log.md
├── artifact-index.md        # AI · SDD truth source
├── phase-01/plan.md         # 细任务仅在此（含 ## Sub-agent dispatch manifest 段）
└── ...
```

**工作流概要**：

| 阶段 | 内容 | 人类确认 |
|------|------|----------|
| Round A · Initiate | 项目上下文、裁剪决策、启动章程草案 | GATE-0 |
| Round B · Plan | 章程定稿、WBS、阶段路线图、整合计划、变更日志、artifact 索引（+ analyze） | GATE-1 → GATE-2 |
| Rolling · 阶段 | 进入某阶段时写 `phase-NN/plan.md`（含 dispatch manifest） + 验收 | GATE-3 |

**模式**：Coach hybrid 裁剪——**T**（精简）或 **F**（全量子计划），由用户在 GATE-0 确认。

**立场声明**：SKILL.md 含 vision + 借鉴/自创术语标注 + 基准版本声明（PMBOK 6/7/8 + GitHub Spec Kit 机制借鉴 + 学术 Agentic PM）+ Sub-agent dispatch manifest 段（ORD-15 对 proj-run 的承诺字段）。

**与 proj-shape / proj-run 的衔接**：

- 讨论未就绪 → 回 proj-shape
- 阶段验收失败 / EXP failed → 回 proj-shape 修订决定
- 推翻 ORD/INV → change-log + 回 proj-shape
- GATE-3 通过 → 把 `phase-NN/plan.md` 交给 proj-run 执行

**触发词示例**：proj-plan · 项目章程 · WBS · phase-roadmap · integration-plan · change-log · analyze · GATE · tailoring · sub-agent

**详细说明**：[skills/proj-plan/SKILL.md](./skills/proj-plan/SKILL.md)

---

## proj-run（执行调度 · Executing）

**做什么**：承接 proj-plan 的 `phase-NN/plan.md`（必含 `## Sub-agent dispatch manifest` 段），负责 sub-agent 调度、model-tier 选择、validation gate、失败 escalate。对应 **PMP 6 Executing Process Group**；承接 3 项核心过程（Direct & Manage Project Work + Manage Quality + Manage Project Knowledge），其余 7 项刻意外置。

**前置条件**：proj-plan 已交付 plan.md 含 `## Sub-agent dispatch manifest` 段（5 字段闭环：objective / specialist / validation criteria / iteration budget / escalate）；GATE-3 已通过。

**3 Mode 表**（按用户 plan 类型 + 是否跨 session 选择，**不**按 cost）：

| Mode | 触发条件 | 实现方式 |
|------|---------|----------|
| **α**（自动 dispatch）| usage-based plan + 同一 IDE session | `.cursor/agents/<name>.md` + Task tool 直接调用 |
| **β**（message bus）| 跨 IDE session / 单 sub-agent 输出 > 父 context | `.apm/bus/` 文件级通信（占位 · 无 runtime）|
| **γ**（手动模型切换）| legacy request-based plan | 父 agent IDE 默认 + 用户手动 `@opus`/`@composer` 切换 |

**Validation gate 3 类**：structural（文件存在/字段齐/行数上限）/ lint（validate_skills.py / YAML frontmatter）/ behavioral（关键字 grep / 负向断言）。

**Sub-agent dispatch 决策树**：第一判据 = "task 输出是否需要被父持续回溯"；需回溯 → 不该 sub-agent；fire-and-forget → 候选 sub-agent。

**产出**：

```text
docs/pmo/phase-NN/
├── acceptance.md          # validation 结果 + token cost + escalate 标记 + GATE 联动
└── （回写 artifact-index.md）

.cursor/agents/<name>.md   # 仅 Mode α 时
.apm/bus/                  # 仅 Mode β 时（用户人工 shuttle）
```

**Cursor 当前约束**（ORD-16）：sub-agent `model` 字段在 legacy request-based plan 被 server 端忽略（详见 [Cursor Forum #156736](https://forum.cursor.com/t/task-tool-model-parameter-only-accepts-fast-cannot-specify-model-ids-for-subagents/156736)）；usage-based plan 通常也仅可调度 `composer-2.5-fast`（不可 standard）。**Mode 选择会按 plan 类型自动降级到 Mode γ**。

**触发词示例**：proj-run · 执行调度 · sub-agent · dispatch manifest · validation gate · Mode α/β/γ · `.cursor/agents/` · message bus · `.apm/bus/` · model-tier

**详细说明**：[skills/proj-run/SKILL.md](./skills/proj-run/SKILL.md)

---

## 推荐组合用法

### 完整链路（新项目）

1. **讨论**：「帮我讨论一下 XXX 想法」→ `proj-shape`（分析层自动配合 `proj-experts`）
2. **就绪**：多轮后确认 `DECISIONS.md` 为 `ready-for-implementation`
3. **规划**：「按 DECISIONS 做项目规划」→ `proj-plan`（Round A → Round B → 按需进阶段，含 dispatch manifest）
4. **执行**：「按 plan + manifest dispatch sub-agent」→ `proj-run`（按 3 Mode 选择 → validation → escalate → acceptance）

### 只要专家分析

「谁最懂 RAG 评估？请以 Andrej Karpathy 视角分析」→ 单独用 `proj-experts`

### 已有决定，直接规划

若项目已有 `docs/discuss/DECISIONS.md` 且状态就绪 → 直接用 `proj-plan`

### 已有 plan + dispatch manifest，直接执行

若项目已有 `phase-NN/plan.md` 含 `## Sub-agent dispatch manifest` 段 → 直接用 `proj-run`

---

## 设计理念

- **角色分工**：人 = Sponsor + PM 关键决策权（GATE 审批 / abort/retry / 关键 trade-off）；AI = PM 执行 + sub-agent 调度 + artifact 维护；对应 [Agentic PM Supervised-AI mode](https://arxiv.org/html/2601.16392v1)
- **人类只读 manifest（≤5 项）**：避免人类被全量 PM artifact 树淹没；AI 维护完整 artifact 集
- **借鉴 vs 自创术语显式标注**：每个 SKILL.md 都含「立场声明」节，区分 PMBOK 6/7/8 借鉴 / GitHub Spec Kit 机制借鉴 / 本 skill 自创术语（Coach hybrid / 模式 T-F / GATE-N / 3 Mode 表 / 5 字段闭环 manifest 等）
- **决定单一真源 DECISIONS.md**：其它 skill / 用户在落地前只需读 DECISIONS.md，无需通读全部讨论轮次

---

## 开发与贡献

```bash
# 校验所有 skill（YAML frontmatter + 命名 + 长度上限 600 行）
uv run scripts/validate_skills.py

# 从模板新建 skill
cp -r template skills/my-new-skill
```

详见 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [skills/README.md](./skills/README.md)（skill 索引表）。

变更历史见 [CHANGELOG.md](./CHANGELOG.md)。

## License

MIT — 见 [LICENSE](./LICENSE)。
