# 第 12 课: 类型标注、数据类与日志

预计时间: 150 到 210 分钟

## 本课目标

- 使用类型标注说明函数输入和输出。
- 使用 `dataclass` 定义结构化数据。
- 使用 `frozen=True` 创建不可变对象。
- 在 `__post_init__()` 中集中校验。
- 使用 `logging` 替代随意的 `print()`。

## 数据类

字典适合保存松散数据，数据类适合表达稳定结构:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class StudySession:
    study_date: str
    minutes: int
    label: str
```

`frozen=True` 表示对象创建后不能修改。需要修改时使用 `dataclasses.replace()` 创建新对象。

## 集中校验

```python
def __post_init__(self) -> None:
    if self.minutes < 0:
        raise ValueError("minutes cannot be negative")
```

这样所有创建路径都会经过同一套验证。

## 日志

日志比 `print()` 更适合项目:

```python
import logging

logger = logging.getLogger("study")
logger.info("sessions=%d total_minutes=%d", count, total)
```

日志记录级别、时间、模块和结构化上下文，后续可以输出到文件或监控系统。

## 示范

运行:

```powershell
python -m unittest discover lessons/12-dataclasses-logging -v
```

## 练习

进入 `exercises/13-task-dataclass/`，完成 `task_dataclass.py`。

## 自检

1. 数据类比普通字典多了哪些约束？
2. 为什么修改不可变对象时要创建新对象？
3. 日志比 `print()` 更适合哪些场景？
