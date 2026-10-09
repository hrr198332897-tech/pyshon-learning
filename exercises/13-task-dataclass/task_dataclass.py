"""Practice dataclasses, immutable replacement, summaries, and logging."""

from __future__ import annotations

import logging
from dataclasses import dataclass


@dataclass(frozen=True)
class StudyTask:
    """A validated, immutable study task."""

    title: str
    minutes: int
    completed: bool = False

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("title cannot be empty")
        if self.minutes < 0:
            raise ValueError("minutes cannot be negative")


def mark_complete(task: StudyTask) -> StudyTask:
    """Return a completed copy of the task."""
    raise NotImplementedError("请完成 mark_complete 函数")


def summarize_tasks(tasks: list[StudyTask]) -> dict[str, int]:
    """Return total, completed, pending, and total minutes."""
    raise NotImplementedError("请完成 summarize_tasks 函数")


def log_task(logger: logging.Logger, task: StudyTask) -> None:
    """Log one task without using string concatenation."""
    raise NotImplementedError("请完成 log_task 函数")


def main() -> None:
    print("用测试驱动完成数据类和日志函数。")


if __name__ == "__main__":
    main()
