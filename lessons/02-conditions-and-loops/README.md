# 第 2 课: 条件判断与循环

预计时间: 90 到 120 分钟

## 本课目标

- 使用比较运算符得到 `True` 或 `False`。
- 使用 `if`、`elif` 和 `else` 处理多种情况。
- 使用 `for` 循环遍历列表。
- 使用 `enumerate()` 同时得到序号和值。
- 使用 `continue` 跳过不需要处理的数据。

## 条件判断

比较表达式会产生布尔值:

```python
minutes = 75

print(minutes >= 60)  # True
print(minutes < 30)   # False
```

根据结果选择不同分支:

```python
if minutes >= 120:
    label = "高强度学习"
elif minutes >= 60:
    label = "投入充足"
elif minutes >= 30:
    label = "达到基础目标"
else:
    label = "需要继续积累"
```

Python 会从上往下检查，遇到第一个为真的条件后停止。

## 循环

`for` 循环可以依次处理列表中的每个元素:

```python
daily_minutes = [0, 45, 70, 20]
active_days = 0

for minutes in daily_minutes:
    if minutes == 0:
        continue
    active_days += 1
```

`continue` 表示跳过本轮剩余逻辑，直接进入下一次循环。

需要同时知道日期序号时，使用 `enumerate()`:

```python
for day, minutes in enumerate(daily_minutes, start=1):
    if minutes >= 60:
        print(f"第 {day} 天达标")
        break
```

`break` 会结束整个循环。

## 示范

运行测试:

```powershell
python -m unittest discover lessons/02-conditions-and-loops -v
```

阅读 `example.py`，观察条件顺序、`continue`、`break` 和 `return` 如何配合。

## 练习

进入 `exercises/03-conditions-and-loops/`，完成 `study_report.py`。

## 自检

1. 如果把条件从严格到宽松的顺序写反，会得到什么错误结果？
2. `continue` 和 `break` 分别影响了哪一层逻辑？
3. 为什么未达到目标时，函数应该返回 `None`，而不是随便返回一个日期？
