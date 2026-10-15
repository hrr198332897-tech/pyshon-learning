# Python 学习仓库

**下一步先读 [START_HERE.md](START_HERE.md)。当前以基础练习验收为主。**

课程与三个项目属于学习材料和参考实现，不能作为本人已经掌握或独立完成的证明。

这是一个面向 AI 时代的 Python 学习仓库。目标不是快速刷完课程，而是建立稳定的编程能力，并用 GitHub 持续记录练习、项目、复盘和成长轨迹。

项目总览见 [PORTFOLIO.md](PORTFOLIO.md)。

## 目标

- 掌握足以独立解决问题的 Python 基础。
- 能处理文件、API、表格数据和自动化任务。
- 能理解并调用常见 AI 能力，完成可运行的 AI 应用。
- 建立三个可以展示的作品，并养成 Git 与 GitHub 工作习惯。

## 仓库结构

| 目录 | 用途 |
| --- | --- |
| `docs/` | 学习路线、环境说明、GitHub 工作流和资料索引 |
| `lessons/` | 按顺序展开的课程说明和示范代码 |
| `exercises/` | 按阶段完成的小练习 |
| `projects/` | 可独立运行并被展示的项目 |
| `journal/` | 每周学习记录和复盘 |
| `templates/` | 可复用的记录模板 |
| `tools/` | 仓库级检查与辅助脚本 |

## 16 周路线

| 周次 | 主题 | 阶段成果 |
| --- | --- | --- |
| 1-4 | Python 基础 | 一个命令行小工具 |
| 5-8 | 数据、文件与自动化 | 一个数据处理脚本 |
| 9-12 | AI 应用基础 | 一个调用 AI API 的应用 |
| 13-16 | 作品集与发布 | 三个整理完成的项目 |

完整说明见 [ROADMAP.md](ROADMAP.md)。

## 每周节奏

1. 阅读或观看一个明确主题。
2. 手写练习，不直接复制完整答案。
3. 完成一个可运行的小成果。
4. 提交一次 Git commit。
5. 用 `templates/weekly-log.md` 写一份复盘。

建议每周投入 5 到 8 小时。时间不足时可以降低篇幅，但保留“写代码、运行、复盘、提交”四个动作。

## 本地环境

创建项目专用虚拟环境并安装依赖:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

`.venv/` 已被 Git 忽略。

## 统一检查

运行以下命令，会依次检查所有课程和练习目录:

```powershell
python tools/run_checks.py
```

推送到 GitHub 后，同一套检查也会由 GitHub Actions 自动运行。

## 当前状态

- GitHub 仓库已建立并推送；本机 Python/Git 版本请实际运行命令确认。
- 已准备第 0–12 课、练习骨架和三个参考项目。
- 可见基础练习包含变量、加法、拼接和条件判断；独立掌握程度待验收。
- 部分练习通过跳过未实现函数保持维护检查可运行；检查成功不等于学完。
- 单个练习验收：`python tools/run_checks.py --exercise 02-variables-and-input --strict`。
- 16 周路线为参考，当前执行顺序与验收标准以 START_HERE.md 为准。
