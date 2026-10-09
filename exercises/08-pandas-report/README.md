# 练习 08: Pandas 学习报告

## 目标

使用 Pandas 构建、筛选、分组和汇总学习记录。

## 步骤

1. 确保已经执行 `python -m pip install -r requirements.txt`。
2. 打开 `pandas_report.py`。
3. 完成 `build_dataframe()`、`filter_minimum()`、`minutes_by_label()` 和 `summarize()`。
4. 运行测试:

```powershell
python -m unittest discover exercises/08-pandas-report -v
```

## 数据格式

```python
rows = [
    {"label": "python", "minutes": 60},
    {"label": "ai", "minutes": 30},
]
```

## 完成标准

- 四个函数的测试不再跳过。
- `minutes` 列转换为 `int64`。
- 筛选不会修改原 DataFrame。
- 分组结果按标签升序排列。
- 空数据返回全零汇总。
