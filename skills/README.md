# Skills Index

本目录下的每个子文件夹是一个独立的 Agent Skill。

| Skill | Description |
|-------|-------------|
| [best-minds-grounded](./best-minds-grounded/) | Grounded 模拟器思维：先查证再模拟（可指定专家）；外推须标注 |
| [idea-discuss](./idea-discuss/) | 以实现为导向的讨论：`docs/discuss/`（DECISIONS+轮次+EXP）；分析层完整走 best-minds-grounded，写入层按争议/收敛分级重组 |
| [idea-pmo](./idea-pmo/) | 承接 DECISIONS 的 PMO 规划：`docs/pmo/`（PMP 计划分层+SDD analyze/gate+integration-plan+change-log+rolling phase+sub-agent handoff）；配合 idea-discuss |

<!-- 新增 skill 后在此添加一行，并运行: uv run scripts/validate_skills.py -->
