# Contributing

感谢关注本仓库。以下是添加或修改 skill 的约定。

## Skill 命名

- 目录名 = `name` frontmatter 字段 = 小写字母、数字、连字符
- 避免泛化名：`helper`、`utils`、`tools`
- 单 skill 主文件 `SKILL.md` 建议 **500 行以内**；长内容放到 `references/`

## 目录约定

| 路径 | 用途 |
|------|------|
| `SKILL.md` | 必需。元数据 + 核心指令 |
| `prompts/` | 可注入的提示词片段 |
| `templates/` | 用户或 Agent 产出的模板 |
| `references/` | 按需阅读的参考文档 |
| `scripts/` | 可执行脚本（注明依赖与用法） |
| `assets/` | 图标、字体等静态资源 |

`SKILL.md` 中引用附属文件时，保持**一层深度**（从 `SKILL.md` 直接链接到 `references/foo.md`）。

## Description 写法

- 第三人称
- 写清 **做什么** + **何时触发**（关键词、场景）
- 示例：`Processes Excel files and generates reports. Use when analyzing .xlsx files or spreadsheets.`

## 提交流程

1. 在 `skills/` 下新增或修改 skill 目录
2. 更新根 `README.md` 的 4 skill 索引表与对应 skill 详细节（如有 skill 增删或描述变化）
3. 运行 `uv run scripts/validate_skills.py`
4. 提交 PR（CI 会自动校验）

## 安全

Skill 不得包含恶意代码、凭据或误导性指令。脚本应行为明确、可审查。
