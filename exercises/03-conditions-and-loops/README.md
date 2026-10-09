# 练习 03: 一周学习报告

## 目标

使用条件判断和循环分析七天的学习分钟数。

## 步骤

1. 打开 `study_report.py`。
2. 完成 `classify_study_time()`、`count_active_days()`、`first_goal_day()` 和 `build_report()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/03-conditions-and-loops -v
```

4. 运行脚本并输入七天数据:

```powershell
python exercises/03-conditions-and-loops/study_report.py
```

## 预期行为

输入:

```text
输入七天学习分钟数，用逗号分隔: 20,65,0,90,30,130,45
```

输出:

```text
本周有 6 天完成学习，首次达标日是第 2 天。
```

没有日期达到目标时:

```text
本周没有达到目标的学习日。
```

## 完成标准

- 四个函数的测试不再跳过。
- 天数和首次达标日都从 `1` 开始计算。
- 负数分钟数会触发 `ValueError`。
- 能解释为什么先检查高强度条件不会影响结果。
