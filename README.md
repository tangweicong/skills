# Agent Skills：想法 → 规划 → 执行

个人沉淀的 [Agent Skills](https://agentskills.io) 集合，可在 Cursor、Claude Code 等支持 Skills 的 Agent 中使用。

本仓库包含 **三个可配合使用的 skill**，覆盖从模糊想法到落地规划前的完整链路：

| Skill | 一句话 | 主要产出 |
|-------|--------|----------|
| [best-minds-grounded](./skills/best-minds-grounded/) | 先查证，再模拟最懂的人怎么说（含选用理由） | 对话中的专家视角分析 |
| [idea-discuss](./skills/idea-discuss/) | 以实现为导向的多轮讨论留痕 | `docs/discuss/` |
| [idea-pmo](./skills/idea-pmo/) | 承接决定，做 PMP 分层规划 + GATE | `docs/pmo/` |

```
模糊想法
    │
    ▼
┌─────────────────┐     ┌──────────────────────┐
│  idea-discuss   │────▶│  docs/discuss/       │
│  （讨论留痕）    │     │  DECISIONS.md + 轮次  │
└────────┬────────┘     └──────────────────────┘
         │ 分析层配合
         ▼
┌─────────────────┐
│ best-minds-     │  查证 + 专家视角 + 标注外推
│ grounded        │
└─────────────────┘
         │
         │ ready-for-implementation
         ▼
┌─────────────────┐     ┌──────────────────────┐
│  idea-pmo       │────▶│  docs/pmo/           │
│  （项目化规划）  │     │  WBS / 阶段 / GATE   │
└─────────────────┘
         │
         ▼
    执行（对话或其它 skill）
```

---

## 安装

将需要的 skill 目录链接或复制到 Agent 的 skills 路径：

```bash
# Cursor 示例（在本仓库根目录执行）
ln -s "$(pwd)/skills/best-minds-grounded" ~/.cursor/skills/best-minds-grounded
ln -s "$(pwd)/skills/idea-discuss"         ~/.cursor/skills/idea-discuss
ln -s "$(pwd)/skills/idea-pmo"             ~/.cursor/skills/idea-pmo
```

也可在对话中 `@` 引用仓库内的 `SKILL.md`，或直接说出触发词（见各 skill 下方）。

---

## best-minds-grounded

**做什么**：Grounded 模拟器思维——先查证事实，再模拟「谁最懂这个问题的人」会怎么说；无现成方案时允许建设性外推，但必须显式标注「外推 ≠ 原话」。

**适用场景**：

- 架构 / 技术选型 / 策略决策，且涉及具体产品、项目或命名概念
- 想听「顶级专家会怎么看」，或指定某人视角（如「以 Karpathy 视角分析」）
- 问题没有工业界 playbook，需要基于专家已记录的原则做发散

**核心流程**：

1. 轻量框定：列出 TA 会先确认的 3–5 个事实问题
2. 定向 WebSearch（官方 docs / repo / issue / RFC）
3. 识别或锁定专家（用户指定优先）
4. 输出：每位 TA 先写 **选用理由**，再有出处的「会说的」+ 标注清晰的「外推」

**触发词示例**：最强大脑 · 谁最懂这个 · 以 X 视角 · 模拟 Y · 指定专家 · 没有现成方案 · best-minds-grounded

**单独使用**：可直接用于纯分析问答，不必开启讨论文档。

**详细说明**：[skills/best-minds-grounded/SKILL.md](./skills/best-minds-grounded/SKILL.md)

---

## idea-discuss

**做什么**：以实现为终点的多轮想法讨论框架。把模糊想法磨清楚，留痕到 `docs/discuss/`，汇总已确定决定到 `DECISIONS.md`；对前沿 / 无现成解法的问题，产出可验证尝试（`EXP-xx`）及继续 / 中止标准。

**不负责**：MVP 细则、里程碑排期、写代码（这些交给 idea-pmo 或执行阶段）。

**产出目录**（在项目根目录）：

```text
docs/discuss/
├── DECISIONS.md          # 已确定决定 + EXP 表 + 讨论状态（优先读此文件）
├── 01-初始想法简述.md
├── 02-技术选型争议.md
└── ...
```

**与 best-minds-grounded 的分工**：

| 层 | skill | 产出 |
|----|-------|------|
| 分析层 | best-minds-grounded | 查证、专家视角、外推（完整执行） |
| 讨论层 | idea-discuss | 轮次文档 + DECISIONS 汇总、就绪判断 |

每轮讨论建议配合 best-minds-grounded 做分析，由 idea-discuss 重组写入文档（非原样粘贴）。

**典型用法**：

```text
用户：我想做一个 XXX，但不确定技术路线，帮我讨论一下
→ Agent 启用 idea-discuss，创建 docs/discuss/01-…md，同步更新 DECISIONS.md

用户：讨论够了吗？能不能开始做？
→ 对照「讨论就绪」硬条件，更新 DECISIONS 状态为 ready-for-implementation（须用户确认）
```

**讨论状态**：`exploring` → `deciding` → `ready-for-implementation` / `blocked`

**触发词示例**：想法讨论 · 前沿方案 · 无现成解法 · 可验证尝试 · 讨论够了没 · EXP · DECISIONS

**详细说明**：[skills/idea-discuss/SKILL.md](./skills/idea-discuss/SKILL.md)

---

## idea-pmo

**做什么**：承接 `docs/discuss/DECISIONS.md`，用 PMP 计划分层 + SDD gate/analyze 纪律生成 `docs/pmo/` 规划产物。AI 维护完整 artifact 集；人类**只读** `human-read-manifest.md`（≤5 项）。

**前置条件**：`DECISIONS.md` 讨论状态为 `ready-for-implementation`，或用户显式授权开工。

**不负责**：写新 INV/ORD、执行代码、启动 sub-agent（只写 handoff 字段）。

**产出目录**（在项目根目录）：

```text
docs/pmo/
├── human-read-manifest.md   # 人类必读（≤5 项）+ GATE 状态
├── charter.md / wbs.md / phase-roadmap.md
├── integration-plan.md / change-log.md
├── phase-01/plan.md         # 细任务仅在此（rolling 阶段规划）
└── ...
```

**工作流概要**：

| 阶段 | 内容 | 人类确认 |
|------|------|----------|
| Round A · Initiate | 项目上下文、裁剪决策、启动章程草案 | GATE-0 |
| Round B · Plan | 章程定稿、WBS、阶段路线图、整合计划 | GATE-1 → GATE-2 |
| Rolling | 进入某阶段时写 `phase-NN/plan.md` + 验收 | GATE-3 |

**模式**：Coach hybrid 裁剪——**T**（精简）或 **F**（全量子计划），由用户在 GATE-0 确认。

**与 idea-discuss 的衔接**：

- 讨论未就绪 → 回到 idea-discuss
- 阶段验收失败 / EXP failed → 回 idea-discuss 修订决定
- 推翻 ORD/INV → change-log + 回 idea-discuss

**触发词示例**：idea-pmo · 项目章程 · WBS · phase-roadmap · GATE · tailoring · analyze

**详细说明**：[skills/idea-pmo/SKILL.md](./skills/idea-pmo/SKILL.md)

---

## 推荐组合用法

### 完整链路（新项目）

1. **讨论**：「帮我讨论一下 XXX 想法」→ `idea-discuss`（分析层自动配合 `best-minds-grounded`）
2. **就绪**：多轮后确认 `DECISIONS.md` 为 `ready-for-implementation`
3. **规划**：「按 DECISIONS 做项目规划」→ `idea-pmo`（Round A → Round B → 按需进阶段）
4. **执行**：按 `phase-NN/plan.md` 在对话或其它 skill 中落地

### 只要专家分析

「谁最懂 RAG 评估？请以 Andrej Karpathy 视角分析」→ 单独用 `best-minds-grounded`

### 已有决定，直接规划

若项目已有 `docs/discuss/DECISIONS.md` 且状态就绪 → 直接用 `idea-pmo`

---

## 开发与贡献

```bash
# 校验所有 skill
uv run scripts/validate_skills.py

# 从模板新建 skill
cp -r template skills/my-new-skill
```

详见 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [skills/README.md](./skills/README.md)（skill 索引）。

## License

MIT — 见 [LICENSE](./LICENSE)。
