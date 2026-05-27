# APM Message Bus 模板（Mode β）

> 本文件是 **proj-run** skill 的 **Mode β**（APM message bus · 跨 IDE session 或重场景）**占位模板**。
> **不含 runtime**——仅目录结构 + 触发条件 + 框架引用；本仓库当前不命中 β 场景，供未来真实用户开箱使用。

来源 `proj-run/assets/` · 依据 ORD-16 · ORD-19 · Mode β = `.apm/bus/` 文件级通信。

---

## `.apm/bus/` 目录结构

Worker 在独立 chat session 运行；Manager / Planner 通过 markdown 文件交换 task、结果与状态（用户 shuttle 或 APM-Auto 自动化）。

```
.apm/bus/
├── tasks/         # 待办 task（Manager → Worker）；每条 task 一个 .md
├── results/       # Worker 完成结果（Worker → Manager）；与 task ID 对齐
├── status/        # task 状态同步（pending / in-progress / done / blocked）
└── meta.md        # bus 元信息：APM 版本、phase ID、最后更新时间
```

| 目录 / 文件 | 用途 |
|------------|------|
| `tasks/` | Manager 写入 objective、validation criteria、上下文路径 |
| `results/` | Worker 回填产出路径、validation 输出、简短笔记 |
| `status/` | 跨 session 进度可见；避免重复 dispatch |
| `meta.md` | 项目级 bus 元数据；首次启用 Mode β 时创建 |

---

## 触发条件（何时启用 Mode β）

| 场景 | 说明 | 典型信号 |
|------|------|---------|
| 跨 IDE session | 关掉 IDE 重启、换设备继续同一 phase | 父 context 无法恢复 sub-agent 历史 |
| 单 task 输出过大 | 单 task 产出 >50K tokens，父 context 无法容纳 | sub-agent 返回被截断或父 agent 丢上下文 |
| 多 sub-agent 协作 | Manager 串行/并行派活，Worker 间需交接 | T-02 依赖 T-01 结果且各自独立 session |
| Cursor Task tool 不足 | 内置 sub-agent 无法跨 session 持久化 | 需人工或 APM-Auto shuttle 消息 |

**默认路径**：未命中上表 → 用 **Mode α**（usage-based）或 **Mode γ**（legacy 手动切换）。

---

## APM 框架引用

| 项目 | 说明 |
|------|------|
| **APM** | [Agentic Project Management](https://github.com/sdi2200262/agentic-project-management) — Planner / Manager / Workers 三角色 + Message Bus 文件级跨 session 通信 |
| **APM-Auto**（备用） | [APM-Auto fork](https://github.com/sdi2200262/apm-auto) — 自动化消息 shuttle，替代原版人工 cp/mv |

---

## 占位声明 · 不实现 runtime（ORD-19）

**本模板不实现 runtime**——无 shuttle 脚本、无 APM-Auto 集成、无 bus 监听逻辑。

| 理由 | 说明 |
|------|------|
| 避免过早抽象 | 本仓库当前不命中 β 场景；实现会让 proj-run 复杂度爆炸 |
| 未来迭代 | 真实用户命中 Mode β 时，再开 **09 轮** 迭代实现 runtime + 与 dispatch manifest 对接 |

**开箱用法（占位）**：复制上方目录结构 → 按 manifest task ID 在 `tasks/` 写 task 文件 → Worker session 读 task、写 `results/` + `status/` → Manager session 汇总进 `acceptance.md`。
