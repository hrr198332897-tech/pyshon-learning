"""Worked examples for lesson 5."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


FIELDNAMES = ("date", "minutes", "note")


def load_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV rows as dictionaries."""
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def clean_rows(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    """Convert and validate CSV rows."""
    cleaned: list[dict[str, Any]] = []
    for row_number, row in enumerate(rows, start=2):
        study_date = row.get("date", "").strip()
        minutes_text = row.get("minutes", "").strip()
        note = row.get("note", "").strip()

        if not study_date:
            raise ValueError(f"row {row_number}: date cannot be empty")

        try:
            minutes = int(minutes_text)
        except ValueError as exc:
            raise ValueError(f"row {row_number}: minutes must be an integer") from exc

        if minutes < 0:
            raise ValueError(f"row {row_number}: minutes cannot be negative")

        cleaned.append({"date": study_date, "minutes": minutes, "note": note})
    return cleaned


def summarize(rows: list[dict[str, Any]]) -> dict[str, int | float]:
    """Return basic statistics for cleaned rows."""
    if not rows:
        return {"sessions": 0, "total_minutes": 0, "average_minutes": 0.0}

    total = sum(row["minutes"] for row in rows)
    return {
        "sessions": len(rows),
        "total_minutes": total,
        "average_minutes": round(total / len(rows), 1),
    }


def write_cleaned(path: Path, rows: list[dict[str, Any]]) -> None:
    """Write cleaned rows to a normalized CSV file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    source = Path("data/local/sessions.csv")
    destination = Path("data/local/sessions-cleaned.csv")
    rows = clean_rows(load_rows(source))
    write_cleaned(destination, rows)
    print(summarize(rows))


if __name__ == "__main__":
    main()
