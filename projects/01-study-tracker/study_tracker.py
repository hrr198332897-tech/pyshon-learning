"""A small JSON-backed study tracker command-line application."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any, Sequence


DEFAULT_DATA_PATH = Path("data/local/study-tracker.json")
REQUIRED_ENTRY_KEYS = {"date", "minutes", "note"}


def validate_entry(entry: dict[str, Any]) -> None:
    """Validate one stored entry."""
    if not REQUIRED_ENTRY_KEYS.issubset(entry):
        raise ValueError("entry is missing required keys")
    if not isinstance(entry["date"], str) or not entry["date"].strip():
        raise ValueError("entry date must be a non-empty string")
    if not isinstance(entry["minutes"], int) or entry["minutes"] < 0:
        raise ValueError("entry minutes must be a non-negative integer")
    if not isinstance(entry["note"], str):
        raise ValueError("entry note must be a string")


def load_entries(path: Path) -> list[dict[str, Any]]:
    """Load and validate entries from a JSON file."""
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}") from exc

    if not isinstance(data, list):
        raise ValueError("study tracker data must contain a JSON list")

    entries: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("every study tracker entry must be an object")
        validate_entry(item)
        entries.append(item)
    return entries


def save_entries(path: Path, entries: list[dict[str, Any]]) -> None:
    """Save entries as readable UTF-8 JSON."""
    for entry in entries:
        validate_entry(entry)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(entries, ensure_ascii=False, indent=2) + "\n"
    path.write_text(content, encoding="utf-8")


def add_entry(
    entries: list[dict[str, Any]],
    study_date: str,
    minutes: int,
    note: str = "",
) -> list[dict[str, Any]]:
    """Return a new list containing one validated entry."""
    if not study_date.strip():
        raise ValueError("date cannot be empty")
    if minutes < 0:
        raise ValueError("minutes cannot be negative")

    try:
        date.fromisoformat(study_date)
    except ValueError as exc:
        raise ValueError("date must use YYYY-MM-DD format") from exc

    entry = {"date": study_date, "minutes": minutes, "note": note}
    validate_entry(entry)
    return [*entries, entry]


def build_report(entries: list[dict[str, Any]]) -> dict[str, int | float]:
    """Build aggregate statistics from entries."""
    if not entries:
        return {
            "sessions": 0,
            "total_minutes": 0,
            "average_minutes": 0.0,
            "best_minutes": 0,
        }

    total = sum(entry["minutes"] for entry in entries)
    best = max(entry["minutes"] for entry in entries)
    return {
        "sessions": len(entries),
        "total_minutes": total,
        "average_minutes": round(total / len(entries), 1),
        "best_minutes": best,
    }


def format_report(report: dict[str, int | float]) -> str:
    """Format report values for display."""
    return "\n".join(
        [
            f"学习次数: {report['sessions']}",
            f"总学习: {report['total_minutes']} 分钟",
            f"平均每次: {report['average_minutes']} 分钟",
            f"单次最高: {report['best_minutes']} 分钟",
        ]
    )


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description="Track study sessions in a local JSON file.")
    parser.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA_PATH,
        help=f"data file path (default: {DEFAULT_DATA_PATH})",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="add a study session")
    add_parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="study date in YYYY-MM-DD format",
    )
    add_parser.add_argument("--minutes", type=int, required=True, help="study minutes")
    add_parser.add_argument("--note", default="", help="optional note")

    subparsers.add_parser("report", help="show aggregate statistics")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line application."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        entries = load_entries(args.data)
    except ValueError as exc:
        print(f"数据错误: {exc}")
        return 2

    if args.command == "add":
        try:
            entries = add_entry(entries, args.date, args.minutes, args.note)
            save_entries(args.data, entries)
        except ValueError as exc:
            print(f"输入错误: {exc}")
            return 2
        print(f"已添加 {args.minutes} 分钟，累计 {sum(item['minutes'] for item in entries)} 分钟。")
        return 0

    if args.command == "report":
        print(format_report(build_report(entries)))
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
