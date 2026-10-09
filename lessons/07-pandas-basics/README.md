# 第 7 课: Pandas 数据分析

预计时间: 150 到 210 分钟

## 本课目标

- 把字典列表转换为 Pandas `DataFrame`。
- 检查列类型和基本统计信息。
- 使用条件筛选数据。
- 使用 `groupby()` 按标签汇总。
- 使用 `sort_values()` 得到稳定排序。

## 安装依赖

在项目虚拟环境中安装:

```powershell
python -m pip install -r requirements.txt
```

## DataFrame

`DataFrame` 类似一个可以编程操作的表格:

```python
import pandas as pd

frame = pd.DataFrame(
    [
        {"label": "python", "minutes": 60},
        {"label": "ai", "minutes": 30},
    ]
)
```

指定列类型:

```python
frame["minutes"] = frame["minutes"].astype("int64")
```

## 筛选

布尔条件会生成一列 `True` 和 `False`:

```python
selected = frame[frame["minutes"] >= 60].copy()
```

## 分组汇总

```python
summary = (
    frame.groupby("label", as_index=False)["minutes"]
    .sum()
    .sort_values("label")
)
```

结果可以转换为普通字典列表:

```python
records = summary.to_dict("records")
```

## 示范

如果环境没有 Pandas，测试会跳过；安装依赖后会开始实际验证:

```powershell
python -m unittest discover lessons/07-pandas-basics -v
```

## 练习

进入 `exercises/08-pandas-report/`，完成 `pandas_report.py`。

## 自检

1. Pandas 的布尔筛选与普通 Python 的 `if` 有什么不同？
2. 为什么筛选后常使用 `.copy()`？
3. `groupby()` 解决了哪类重复计算问题？
