# Agent 资源与 Sub-agent Handoff

> **PMP**：资源管理 + 沟通管理（AI 时代扩展）。  
> **SDD**：执行者须在 plan 中显式声明；sub-agent 不得绕过 GATE / INV-04。

## 执行者类型

| 类型 | plan.md「执行者」列 | 说明 |
|------|---------------------|------|
| AI（主 agent） | `AI` | 当前对话 agent |
| 人工 | `人工` | 须标注人工预估（ORD-07） |
| Sub-agent | `subagent:{角色}` | 见下表 |

## Sub-agent 角色（示例，按项目裁剪）

| 角色 slug | 职责 | 输入 artifact | 输出 |
|-----------|------|---------------|------|
| `explore` | 只读探查代码库 | plan 任务描述 + artifact-index | 摘要写入 plan 或 review |
| `shell` | 命令/脚本 | plan 任务 + 验收标准 | 命令结果；**不含**未授权 git push |
| `generalPurpose` | 多步实现 | plan 任务 | **仍属 Execute**；idea-pmo 只规划不调用 |

## Handoff 最小字段（sub-agent 任务必填）

在 `phase-NN/plan.md` 任务行下方或「Handoff」节：

```markdown
| 任务 # | subagent 角色 | 输入 | 完成定义 | 结果回写 |
|--------|---------------|------|----------|----------|
| 3 | subagent:explore | 搜 idea-pmo assets | 文件清单 | review §问题 |
```

## 纪律

- idea-pmo **只规划** handoff，**不启动** sub-agent（INV-04）
- sub-agent 产出若推翻 ORD → `change-log` + 回 idea-discuss
- manifest 仍 ≤5；sub-agent 报告**不得**要求人类通读
