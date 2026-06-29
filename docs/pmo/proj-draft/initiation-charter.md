# 启动章程草案（Initiation Charter） — `proj` orchestrator skill

| 字段 | 值 |
|------|-----|
| 状态 | Round A 草案 → GATE-0 |
| 授权来源 | 用户 @轮次12「继续」（显式授权进 proj-plan 起草 `proj`）|
| 上游 | DECISIONS.md ORD-29/30/31 + EXP-07 passed |

## 目的（why）

proj-* 现有 5 skill 是**专家流水线**，但缺一个**用户总入口**：用户得知道该调哪个、跨 skill 的先后/GATE 靠人脑维持。`proj` 补这个洞——做流水线之上的薄 **Supervisor + 有界 loop + facade**，让「描述问题 → AI 编排专家 → 规划-执行-验证闭环 → GATE 处交人」一站式发生。

## 范围（what · 已被 ORD 锁定）

**做**：
- 新建 `skills/proj/SKILL.md`：固定专家集调用表 + 有界 loop（STATE→CLASSIFY→PLAN→EXECUTE→VERIFY→GATE?→RE-ROUTE→MEMORY）+ GATE 清单 + autonomy slider + 反模式 + 触发词。
- 显式声明职责边界：**不重做 host model-invocation**（ORD-30）；只做 host 给不了的有状态序列 + gate + loop。
- README 索引扩到 6 skill。

**不做**（非目标）：proj-run 通用化 / 跨 runtime 适配器（ORD-28 · EXP-08 独立后续）；不改 experts/shape/plan/survey 正文。

## 成功标准（验收基线）

1. `skills/proj/SKILL.md` shipped，`validate_skills.py` 退 0。
2. 三决定可见：ORD-29（facade/Supervisor）、ORD-30（收窄·不重做路由）、ORD-31（有界 loop + slider）。
3. README 6 skill 索引一致。
4. acceptance 覆盖 EXP-07 两条 caveat 的设计层自检（冷启动全遍历 + 失败 re-route loop）。

## 关键约束

- INV-04（本 skill 只规划，不执行）/ ORD-30 / ORD-31 / 不写新 INV·ORD / SKILL.md ≤600 行。

## 假设与风险（简）

- 假设：spike 结构（EXP-07 验证）可直接升级为 shipped，无重大返工。
- 风险：`proj` description 过广 → 与其他 skill 触发冲突（host 侧）；缓解留 ORD-28/EXP-08，本项目仅写设计注记。

## GATE-0

- [ ] 用户批准启动 + 范围 + 成功标准
- [ ] 用户在 tailoring-decision 选定 T-lean / T-full
