# 第 5 课: CSV 数据读取与清洗

预计时间: 120 到 180 分钟

## 本课目标

- 使用 `csv.DictReader` 读取带表头的数据。
- 使用 `csv.DictWriter` 写出规范 CSV。
- 把字符串字段转换成整数。
- 对缺失、非法和负数数据进行校验。
- 使用临时文件测试数据流程。

## CSV 与 Excel

CSV 是纯文本表格。每一行是一条记录，逗号分隔字段。第一行通常保存表头:

```csv
date,minutes,note
2026-10-08,45,变量练习
2026-10-09,60,命令行项目
```

## 读取

使用 `DictReader` 后，每一行会变成字典，键来自表头:

```python
import csv
from pathlib import Path

path = Path("sessions.csv")
with path.open("r", encoding="utf-8-sig", newline="") as file:
    rows = list(csv.DictReader(file))
```

Windows 上打开 CSV 时使用 `newline=""`，可以避免空行问题。`utf-8-sig` 能兼容 Excel 可能写入的字节顺序标记。

## 清洗

CSV 读出的所有值都是字符串，所以 `minutes` 需要转换:

```python
minutes_text = row["minutes"].strip()
minutes = int(minutes_text)
```

如果转换失败，应该给出包含行信息的错误:

```python
try:
    minutes = int(minutes_text)
except ValueError as exc:
    raise ValueError(f"row {row_number}: invalid minutes") from exc
```

## 写出

使用 `DictWriter` 明确字段顺序:

```python
with path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["date", "minutes", "note"])
    writer.writeheader()
    writer.writerows(cleaned_rows)
```

## 示范

运行:

```powershell
python -m unittest discover lessons/05-csv-data -v
```

示范测试会在临时目录中生成输入文件，不依赖手工准备数据。

## 练习

进入 `exercises/06-csv-cleaner/`，完成 `csv_cleaner.py`。

## 自检

1. 为什么 CSV 读出的数字仍然是字符串？
2. `DictReader` 和普通 `reader` 的区别是什么？
3. 为什么要报告出错行号，而不是只说“数据无效”？
