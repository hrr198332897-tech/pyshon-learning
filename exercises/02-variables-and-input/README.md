# 练习 02: 学习时间记录器

## 目标

实现三个小函数，并组合成一个可以询问姓名和学习时间的命令行脚本。

## 步骤

1. 打开 `study_tracker.py`。
2. 完成 `greet()`、`minutes_to_hours()` 和 `build_summary()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/02-variables-and-input -v
```

4. 运行脚本:

```powershell
python exercises/02-variables-and-input/study_tracker.py
```

## 预期行为

输入:

```text
你的名字: 小明
本周计划学习多少分钟: 150
```

输出:

```text
你好，小明！ 你这周计划学习 150 分钟，也就是 2.5 小时。
```

## 完成标准

- 三个函数的测试全部通过或不再跳过。
- 输入无效分钟数时，脚本不会直接崩溃。
- 能把函数与循环、条件配合的改进想法写进周记录。
