"""Practice CSV loading, conversion, validation, and writing."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any


FIELDNAMES = ("date", "minutes", "note")


def load_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV rows as dictionaries."""
    raise NotImplementedError("请完成 load_rows 函数")


def clean_rows(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    """Convert and validate CSV rows."""
    raise NotImplementedError("请完成 clean_rows 函数")


def summarize(rows: list[dict[str, Any]]) -> dict[str, int | float]:
    """Return basic statistics for cleaned rows."""
    raise NotImplementedError("请完成 summarize 函数")


def write_cleaned(path: Path, rows: list[dict[str, Any]]) -> None:
    """Write cleaned rows to a normalized CSV file."""
    raise NotImplementedError("请完成 write_cleaned 函数")


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print("用法: python csv_cleaner.py 输入文件 输出文件")
        return 2

    source = Path(args[0])
    destination = Path(args[1])

    try:
        rows = clean_rows(load_rows(source))
        write_cleaned(destination, rows)
    except (FileNotFoundError, ValueError) as exc:
        print(f"处理失败: {exc}")
        return 1

    print(summarize(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
