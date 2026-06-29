# 形态1 · 段1 experts（proj 调 proj-experts · 无状态按需）

> 问题：`proj` CLASSIFY 该靠散文推断，还是加机读 `pipeline-state` 块？

## 视角 A · 简约优先（Anthropic「先求最简」）
散文已能让 LLM 推断入口阶段（EXP-07 实测 CLASSIFY 正确跳过已决 shape）。加结构块=新增必须同步维护的真相源，违反 INV-03（避免 source of truth 分裂）除非散文确实不够。**倾向：不加，除非有实测失败。**

## 视角 B · 鲁棒性 / verifier 友好（Osmani loop engineering）
机读块让 CLASSIFY 与 VERIFY 可由一行 grep 判定「现在哪一阶段」，降低 LLM 推断漂移；且块可被 proj 的 VERIFY 步直接校验。**倾向：加一个最小块（仅 stage + status 两字段），不复制散文内容，只做索引。**

## 收敛输入（交 shape）
两视角在「最小、不复制散文、仅索引」上可调和：加**最小 `pipeline-state` 块**（stage+status+pending_exp 三字段），不重复散文细节 → 既给 verifier 抓手又不分裂真相源。
