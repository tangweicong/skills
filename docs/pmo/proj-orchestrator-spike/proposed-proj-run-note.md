<!-- STATUS: APPLIED 2026-06-29 — human GATE approved; inserted into skills/proj-run/SKILL.md after §设计 vision (with 规划中 marker); validate_skills.py 5/5 pass. -->
<!-- Original: PROPOSED diff produced by `proj` spike (EXP-07 experiment arm), awaiting human GATE approval. -->
<!-- Target: skills/proj-run/SKILL.md — insert after §设计 vision -->

## 与 `proj` 入口的关系（ORD-29）

用户通常经 **`proj`**（流水线总入口 orchestrator）间接到达本 skill：`proj` 负责跨 skill 状态机 + 有界 loop + GATE 编排（ORD-30/31），本 skill 仍**专管 PMP Executing**（ORD-17/18 不变）。直接调用本 skill 亦可——`proj` 不改变本 skill 的职责边界。
