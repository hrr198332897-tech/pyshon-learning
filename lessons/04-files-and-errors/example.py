"""Worked examples for lesson 4."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def save_entries(path: Path, entries: list[dict[str, Any]]) -> None:
    """Save study entries as readable UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(entries, ensure_ascii=False, indent=2) + "\n"
    path.write_text(content, encoding="utf-8")


def load_entries(path: Path) -> list[dict[str, Any]]:
    """Load entries, returning an empty list when the file is missing."""
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError("study log is not valid JSON") from exc

    if not isinstance(data, list):
        raise ValueError("study log must contain a JSON list")
    return data


def add_entry(
    entries: list[dict[str, Any]],
    day: int,
    minutes: int,
) -> list[dict[str, Any]]:
    """Return a new entry list with one validated record appended."""
    if day < 1:
        raise ValueError("day must be at least 1")
    if minutes < 0:
        raise ValueError("minutes cannot be negative")
    return [*entries, {"day": day, "minutes": minutes}]


def total_minutes(entries: list[dict[str, Any]]) -> int:
    """Sum all recorded minutes."""
    return sum(entry["minutes"] for entry in entries)


def main() -> None:
    path = Path("data/local/study-log.json")
    entries = load_entries(path)
    entries = add_entry(entries, day=1, minutes=60)
    save_entries(path, entries)
    print(f"累计学习 {total_minutes(entries)} 分钟")


if __name__ == "__main__":
    main()
