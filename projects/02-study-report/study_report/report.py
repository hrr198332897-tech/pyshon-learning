"""Build summaries and Markdown reports."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from study_report.data import require_pandas


def summarize_sessions(frame: Any) -> dict[str, Any]:
    """Calculate top-level study statistics."""
    require_pandas()
    sessions = int(len(frame))
    if sessions == 0:
        return {
            "sessions": 0,
            "total_minutes": 0,
            "average_minutes": 0.0,
            "active_days": 0,
            "top_label": None,
            "top_minutes": 0,
        }

    total = int(frame["minutes"].sum())
    label_totals = minutes_by_label(frame)
    top_label = label_totals[0]["label"] if label_totals else None
    top_minutes = int(label_totals[0]["minutes"]) if label_totals else 0

    return {
        "sessions": sessions,
        "total_minutes": total,
        "average_minutes": round(total / sessions, 1),
        "active_days": int(frame["minutes"].gt(0).sum()),
        "top_label": top_label,
        "top_minutes": top_minutes,
    }


def minutes_by_label(frame: Any) -> list[dict[str, Any]]:
    """Return label totals ordered by minutes, then label."""
    require_pandas()
    grouped = frame.groupby("label", as_index=False)["minutes"].sum()
    grouped = grouped.sort_values(["minutes", "label"], ascending=[False, True])
    return grouped.to_dict("records")


def build_markdown_report(frame: Any) -> str:
    """Build a Markdown report from session data."""
    summary = summarize_sessions(frame)
    label_rows = minutes_by_label(frame)

    lines = [
        "# Study Report",
        "",
        f"- Sessions: {summary['sessions']}",
        f"- Total minutes: {summary['total_minutes']}",
        f"- Average minutes: {summary['average_minutes']}",
        f"- Active days: {summary['active_days']}",
    ]

    if summary["top_label"] is None:
        lines.append("- Top label: none")
    else:
        lines.append(
            f"- Top label: {summary['top_label']} ({summary['top_minutes']} minutes)"
        )

    lines.extend(
        [
            "",
            "## Minutes by label",
            "",
            "| Label | Minutes |",
            "| --- | ---: |",
        ]
    )
    for row in label_rows:
        lines.append(f"| {row['label']} | {row['minutes']} |")

    return "\n".join(lines) + "\n"


def write_report(path: Path, content: str) -> None:
    """Write a UTF-8 Markdown report."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
