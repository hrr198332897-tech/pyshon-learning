# 项目 2: 学习数据报告生成器

这个项目把 CSV 数据读取、Pandas 汇总和 Markdown 报告生成组合成一个模块化命令行应用。

## 功能

- 从 CSV 读取学习记录。
- 检查缺失列、空标签、非法分钟数和负数。
- 计算总时长、平均时长、有效学习天数和主要学习方向。
- 按标签汇总分钟数。
- 生成 Markdown 表格报告并保存到文件。

## 输入格式

```csv
date,minutes,label,note
2026-10-06,45,python,variables
2026-10-07,30,ai,concepts
```

示例文件位于 `examples/sessions.csv`。

## 运行

进入项目目录:

```powershell
Set-Location projects/02-study-report
python -m study_report --input examples/sessions.csv
```

保存报告:

```powershell
python -m study_report --input examples/sessions.csv --output report.md
```

## 代码结构

| 文件 | 职责 |
| --- | --- |
| `study_report/data.py` | CSV 读取和数据校验 |
| `study_report/report.py` | 汇总统计和 Markdown 生成 |
| `study_report/cli.py` | 命令行参数与错误处理 |
| `study_report/__main__.py` | `python -m study_report` 入口 |

## 测试

```powershell
Set-Location projects/02-study-report
python -m unittest discover -v
```

## 继续改造

1. 增加按周筛选。
2. 输出 HTML 或图表。
3. 从 API 获取数据后复用同一报告模块。
4. 增加日期连续性分析。
