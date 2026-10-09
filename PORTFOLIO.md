# 作品集

## 1. 学习记录命令行工具

目录: `projects/01-study-tracker/`

展示能力:

- 命令行参数设计。
- JSON 数据保存与校验。
- 错误处理。
- 函数测试和命令行端到端测试。

运行:

```powershell
python projects/01-study-tracker/study_tracker.py --data data/local/demo.json add --date 2026-10-09 --minutes 60 --note "lesson 1"
python projects/01-study-tracker/study_tracker.py --data data/local/demo.json report
```

## 2. 学习数据报告生成器

目录: `projects/02-study-report/`

展示能力:

- Pandas 数据清洗和分组汇总。
- CSV 输入校验。
- 模块化项目结构。
- Markdown 报告生成。

运行:

```powershell
Set-Location projects/02-study-report
python -m study_report --input examples/sessions.csv
```

## 3. 本地知识搜索

目录: `projects/03-knowledge-search/`

展示能力:

- 文档扫描、分块和来源追踪。
- 中英文 TF-IDF 检索。
- 余弦相似度和稳定排序。
- 无匹配保护。
- 可插拔模型生成器接口。

运行:

```powershell
Set-Location projects/03-knowledge-search
python -m knowledge_search --query "RAG 是什么" --show-context
```

## 验证

从仓库根目录运行:

```powershell
.\.venv\Scripts\python.exe tools/run_checks.py
```

当前结果: 87 项测试通过，48 项练习测试等待完成。
