# Sandbox pipeline state (MEMORY · 形态1 冷启动随阶段更新)

> proj 的 MEMORY 步每段回写这里（沙盒，不动 live DECISIONS.md）。

| 时刻 | stage | 讨论状态 | 决定 | 待验证 | 下一步 |
|------|-------|---------|------|--------|--------|
| t0 STATE | — | （沙盒空）新想法 | — | — | CLASSIFY |
| t1 CLASSIFY | — | exploring | — | — | 新想法无既有决定 → 从 **experts** 入（不跳段）|
| t2 experts done | experts | exploring | — | — | → shape（GATE: 无，experts 无状态）|
| t3 shape done | shape | deciding→ready | sROD-1（采纳最小块）| — | **GATE: 升 ready-for-implementation → 默认档 STOP** |
| t4 plan done | plan | ready | sROD-1 | — | **GATE-3 → 默认档 STOP** |
| t5 run VERIFY#1 | run | ready | sROD-1 | sEXP fail | **RE-ROUTE**（见形态2）|
| t6 run VERIFY#2 | run | ready | sROD-1 | sEXP pass | **GATE: 改 shipped 前 STOP**（仅出 proposed）|
