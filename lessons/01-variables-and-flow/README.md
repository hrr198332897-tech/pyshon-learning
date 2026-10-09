# 第 1 课: 变量、输入与函数

预计时间: 60 到 90 分钟

## 本课目标

- 使用变量保存文字、整数和小数。
- 使用 `input()` 接收用户输入。
- 使用 `int()` 或 `float()` 转换输入类型。
- 使用函数组织重复逻辑。
- 使用 f-string 生成清晰输出。

## 核心概念

变量是给数据起的名字:

```python
name = "小明"
minutes = 90
ratio = 1.5
```

Python 会根据值自动判断类型。`name` 是字符串，`minutes` 是整数，`ratio` 是小数。

`input()` 得到的永远是字符串。需要计算时，要先转换:

```python
minutes_text = input("学习了多少分钟？")
minutes = int(minutes_text)
```

函数用于把一段逻辑命名并复用:

```python
def minutes_to_hours(minutes: int) -> float:
    return minutes / 60
```

`return` 把计算结果交还给调用函数的地方。

f-string 可以把变量放进文字:

```python
hours = minutes_to_hours(90)
print(f"90 分钟等于 {hours:.1f} 小时")
```

`:.1f` 表示保留一位小数。

## 示范

运行:

```powershell
python lessons/01-variables-and-flow/example.py
```

阅读 `example.py` 中的四个函数，然后运行测试:

```powershell
python -m unittest discover lessons/01-variables-and-flow -v
```

## 练习

进入 `exercises/02-variables-and-input/`，按照 README 完成 `study_tracker.py`。

## 自检

完成练习后，尝试不查看资料回答:

1. 为什么 `input()` 的结果不能直接参与数学计算？
2. `return` 和 `print()` 有什么区别？
3. f-string 中的 `{hours:.1f}` 做了什么？
