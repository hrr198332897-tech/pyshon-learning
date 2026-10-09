# 练习 13: 任务数据类与日志

## 目标

使用数据类表达任务，使用不可变替换完成任务，并输出结构化日志。

## 步骤

1. 打开 `task_dataclass.py`。
2. 完成 `mark_complete()`、`summarize_tasks()` 和 `log_task()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/13-task-dataclass -v
```

## 完成标准

- 函数测试不再跳过。
- 空标题、负分钟数会触发 `ValueError`。
- `mark_complete()` 不修改原任务。
- 汇总包含总数、完成数和待完成数。
- 日志包含任务标题、分钟数和完成状态。
