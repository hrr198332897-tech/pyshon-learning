# 练习 06: 学习记录 CSV 清洗器

## 目标

读取包含 `date`、`minutes` 和 `note` 三列的 CSV，完成类型转换与校验，再输出规范文件。

## 步骤

1. 打开 `csv_cleaner.py`。
2. 完成 `load_rows()`、`clean_rows()`、`summarize()` 和 `write_cleaned()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/06-csv-cleaner -v
```

4. 准备一个输入文件后运行脚本:

```powershell
python exercises/06-csv-cleaner/csv_cleaner.py data/local/input.csv data/local/cleaned.csv
```

## 输入示例

```csv
date,minutes,note
2026-10-08,45,变量练习
2026-10-09,60,命令行项目
```

## 完成标准

- 四个函数的测试不再跳过。
- 非数字或负数的 `minutes` 会触发 `ValueError`。
- 空日期会触发 `ValueError`。
- 输出文件字段顺序固定为 `date,minutes,note`。
- 错误信息包含对应 CSV 行号。
