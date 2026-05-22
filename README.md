# Agent Skills Collection

个人沉淀的 [Agent Skills](https://agentskills.io) 集合，可在 Cursor、Claude Code、Claude.ai 等支持 Skills 的 Agent 中使用。

## 目录结构

```
.
├── skills/              # 所有 skill（每个子目录一个 skill）
│   ├── README.md        # skill 索引
│   └── <skill-name>/
│       ├── SKILL.md     # 必需：元数据 + 指令
│       ├── prompts/     # 可选：提示词片段
│       ├── templates/   # 可选：模板文件
│       ├── references/  # 可选：参考文档
│       ├── scripts/     # 可选：可执行脚本
│       └── assets/      # 可选：静态资源
├── template/            # 新建 skill 的模板
├── scripts/           # 仓库级工具（校验等）
└── .github/workflows/ # CI（校验 skill 格式）
```

每个 skill 是自包含目录，**必须**包含带 YAML frontmatter 的 `SKILL.md`：

```yaml
---
name: my-skill-name          # 小写、连字符，与目录名一致
description: 做什么、何时触发（第三人称，含触发词）
---
```

## 安装使用

### Cursor

将本仓库 clone 到本地后，把单个 skill 目录链接或复制到个人 skills 目录：

```bash
# 示例：安装某个 skill（将 my-skill 换成实际目录名）
ln -s "$(pwd)/skills/my-skill" ~/.cursor/skills/my-skill
```

或在对话中通过 `@` 引用仓库内的 `SKILL.md`。

### Claude Code

```bash
# 将仓库注册为 plugin marketplace（开源发布后）
/plugin marketplace add <your-github-user>/skills
```

### 通用

把 `skills/<name>/` 整个目录上传到你使用的 Agent 的 skills 配置路径即可。

## 已有 Skills

见 [skills/README.md](./skills/README.md)（随仓库增长在此维护索引）。

## 新建 Skill

```bash
# 1. 从模板复制
cp -r template skills/my-new-skill

# 2. 编辑 skills/my-new-skill/SKILL.md（name、description、正文）

# 3. 校验
uv run scripts/validate_skills.py

# 4. 更新 skills/README.md 索引
```

详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 开发

```bash
# 校验所有 skill
uv run scripts/validate_skills.py

# 校验单个 skill
uv run scripts/validate_skills.py my-skill
```

## License

MIT — 见 [LICENSE](./LICENSE)。
