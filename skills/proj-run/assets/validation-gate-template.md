# Validation Gate 模板（ORD-22）

> 本模板定义 proj-run 的 **3 类 validation gate**（**structural** / **lint** / **behavioral** · ORD-22）。sub-agent dispatch 完成后，父 agent 按判据逐条执行；与 dispatch manifest **§validation criteria** 字段配套使用——plan 作者从本标准库挑选 + 组合，写入 manifest 各 task 行。

| 字段 | 值 |
|------|-----|
| 来源 | proj-run/assets/validation-gate-template.md |
| 依据 | ORD-22（3 类 validation gate）· ORD-21（dispatch manifest 5 字段） |
| 用途 | plan 作者写 validation criteria 时的标准段库；proj-run 父 agent 跑 gate 时的判据分类 |

---

## §structural gate

**定义**：产出在磁盘与结构层面的硬约束——文件存在、必填字段/节出现、行数/条数上限。

**用途**：最快失败；不读语义，只验证 artifact「骨架齐」。

| # | 判据类型 | 示例命令（父 agent 一行 shell 可判） |
|---|---------|--------------------------------------|
| S1 | 文件存在 | `test -f skills/proj-run/assets/dispatch-manifest-template.md && echo pass` |
| S2 | 行数上限 | `L=$(wc -l < skills/proj-run/SKILL.md); [ "$L" -le 120 ] && echo pass` |
| S3 | 字段/关键字齐 | `grep -cE "objective|specialist|validation criteria|iteration budget|escalate" skills/proj-run/assets/dispatch-manifest-template.md`; 期望 ≥ 5 |
| S4 | 节标题齐 | `grep -c "^## " docs/pmo/phase-01/plan.md`; 期望 ≥ N（plan 作者定 N） |

---

## §lint gate

**定义**：仓库级或格式级校验——skill 合规、Markdown 结构、YAML frontmatter 可解析。

**用途**：catch 结构性违规（缺 frontmatter、skill 名冲突）再进入 behavioral。

| # | 判据类型 | 示例命令 |
|---|---------|---------|
| L1 | skill 合规 | `uv run scripts/validate_skills.py proj-run`（退 0 = pass） |
| L2 | YAML frontmatter | `python -c "import yaml; yaml.safe_load(open('skills/proj-run/SKILL.md').read().split('---')[1])"` |
| L3 | Markdown 链接 | `grep -cE '\]\([^)]+\)' skills/proj-run/SKILL.md` ≥ 1（引用非空） |

---

## §behavioral gate

**定义**：内容语义与策略约束——关键字必须出现、禁用模式不得出现；可正向 / 负向 / 多条件组合。

**用途**：验证「写得对」而非仅「写得齐」；负向断言防 ORD-15 等策略违规。

| # | 断言方向 | 示例命令 |
|---|---------|---------|
| B1 | **正向** | `grep -c "validation gate" skills/proj-run/SKILL.md` ≥ 1 |
| B2 | **负向** | `grep -c "model:" skills/proj-run/assets/dispatch-manifest-template.md` = 0（manifest 禁具体 model 名） |
| B3 | **组合** | S1 pass **且** B2 pass：`test -f $FILE && [ $(grep -c "gpt-4" $FILE) -eq 0 ]` |
| B4 | **多文件** | `rg -l "ORD-22" skills/proj-run/` 命中 ≥ 2 个文件 |

---

## §失败 escalate 流程

sub-agent 产出返回后，父 agent **逐条跑 manifest §validation criteria**（每条可归入 structural / lint / behavioral 之一）。

```
validation 全 pass → 登记 artifact-index → 下一 task / 写 acceptance.md
        │
        ▼ fail（任一条）
检查 iteration budget（manifest 字段，典型 2）
        │
        ├─ budget 未用尽 → 父 agent 输出：失败判据 + 证据 + 修订要点 → 重 dispatch（iteration +1）
        │
        └─ budget 用尽 → 触发 escalate（manifest §escalate 字段）
                ├─ 回父 agent 接手（最常见：父 agent 直接改 artifact）
                ├─ 回 proj-plan 改 plan / dispatch manifest（validation 标准不合理、缺字段）
                └─ 回 proj-shape 开新轮（需新 INV/ORD/EXP，execute 层不得自改决定）
```

**phase 级补充**（见 dispatch-manifest-template §iteration & escalate 总策略）：全 phase sub-agent 累计失败 > 3 → circuit breaker → abort phase + 回 proj-shape。

---

## §与 dispatch manifest 联动

| 本模板 gate | manifest 字段 | 写法要点 |
|-------------|---------------|---------|
| structural | **validation criteria** 第 (1)–(N) 条 | `test -f` / `wc -l` / `grep -c` 字段齐 |
| lint | 同上，标注 lint | `validate_skills.py` / YAML parse |
| behavioral | 同上，标注正向/负向 | `grep -c "必含"` ≥ 1；`grep -c "禁用"` = 0 |

**iteration budget** 与 **escalate** 写在 manifest 各 task 行（非本模板重复定义）；本模板只规定「哪些 validation 类型有效」。

### 端到端示例

plan.md manifest 中 T-05 task：

| 字段 | 值 |
|------|-----|
| **validation criteria** | (1) structural: `test -f skills/proj-run/assets/validation-gate-template.md`；(2) structural: `wc -l` ≤ 120；(3) behavioral 正向: `grep -cE "structural\|lint\|behavioral"` ≥ 3；(4) behavioral 负向: 正文无具体 model 名 |
| **iteration budget** | 2 |
| **escalate** | budget 用尽 → 父 agent 接手；若 gate 类型需新 ORD → 回 proj-shape |

父 agent dispatch T-05 → 收稿 → 跑 4 条 → 任一条 fail 且 iteration < budget → 给修订要点重 dispatch；第 2 次仍 fail → 按 escalate 回父 agent 接手。
