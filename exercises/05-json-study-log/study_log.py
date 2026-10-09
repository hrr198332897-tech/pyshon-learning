"""Practice file I/O, JSON, validation, and exceptions."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def save_entries(path: Path, entries: list[dict[str, Any]]) -> None:
    """Save entries as readable UTF-8 JSON."""
    raise NotImplementedError("请完成 save_entries 函数")


def load_entries(path: Path) -> list[dict[str, Any]]:
    """Load entries, returning an empty list when the file is missing."""
    raise NotImplementedError("请完成 load_entries 函数")


def add_entry(
    entries: list[dict[str, Any]],
    day: int,
    minutes: int,
) -> list[dict[str, Any]]:
    """Return a new list with one validated record appended."""
    raise NotImplementedError("请完成 add_entry 函数")


def total_minutes(entries: list[dict[str, Any]]) -> int:
    """Sum all recorded minutes."""
    raise NotImplementedError("请完成 total_minutes 函数")


def main() -> None:
    path = Path("data/local/study-log.json")
    entries = load_entries(path)

    try:
        day = int(input("学习日序号: "))
        minutes = int(input("学习分钟数: "))
        entries = add_entry(entries, day=day, minutes=minutes)
    except ValueError as exc:
        print(f"输入错误: {exc}")
        return

    save_entries(path, entries)
    print(f"累计学习 {total_minutes(entries)} 分钟")


if __name__ == "__main__":
    main()
