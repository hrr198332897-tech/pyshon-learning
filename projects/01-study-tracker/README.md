# 项目 1: 学习记录命令行工具

这是一个完整可运行的第一阶段参考项目。它把变量、函数、字典、循环、JSON 文件和异常处理组合成一个真正的命令行工具。

## 功能

- 添加一条学习记录。
- 把记录保存为 JSON。
- 查看总时长、学习次数、平均时长和单次最高时长。
- 对无效日期、负数和损坏的数据文件给出清晰错误。

## 运行

添加记录:

```powershell
python projects/01-study-tracker/study_tracker.py --data data/local/demo.json add --date 2026-10-09 --minutes 60 --note "lesson 1"
```

查看报告:

```powershell
python projects/01-study-tracker/study_tracker.py --data data/local/demo.json report
```

查看帮助:

```powershell
python projects/01-study-tracker/study_tracker.py --help
python projects/01-study-tracker/study_tracker.py add --help
```

## 测试

```powershell
python -m unittest discover projects/01-study-tracker -v
```

测试既覆盖底层函数，也真实启动命令行程序完成一次添加和报告流程。

## 继续改造

1. 增加删除记录命令。
2. 按日期筛选报告。
3. 把单文件代码拆分为模块。
4. 增加 `--week` 参数，只统计指定周的数据。
