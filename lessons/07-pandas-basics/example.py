"""Worked examples for lesson 7."""

from __future__ import annotations

from typing import Any

try:
    import pandas as pd
except ImportError:
    pd = None


def require_pandas() -> None:
    """Raise a clear error when pandas is unavailable."""
    if pd is None:
        raise RuntimeError("pandas is required for this lesson")


def build_dataframe(rows: list[dict[str, Any]]) -> Any:
    """Build a normalized DataFrame from records."""
    require_pandas()
    frame = pd.DataFrame(rows, columns=["label", "minutes"])
    frame["minutes"] = frame["minutes"].astype("int64")
    return frame


def filter_minimum(frame: Any, minimum: int) -> Any:
    """Return records meeting the minimum number of minutes."""
    require_pandas()
    return frame[frame["minutes"] >= minimum].copy()


def minutes_by_label(frame: Any) -> list[dict[str, Any]]:
    """Sum minutes by label using deterministic ordering."""
    require_pandas()
    grouped = (
        frame.groupby("label", as_index=False)["minutes"]
        .sum()
        .sort_values("label")
    )
    return grouped.to_dict("records")


def summarize(frame: Any) -> dict[str, int | float]:
    """Return aggregate statistics."""
    require_pandas()
    sessions = int(len(frame))
    if sessions == 0:
        return {"sessions": 0, "total_minutes": 0, "average_minutes": 0.0}

    total = int(frame["minutes"].sum())
    return {
        "sessions": sessions,
        "total_minutes": total,
        "average_minutes": round(total / sessions, 1),
    }


def main() -> None:
    rows = [
        {"label": "python", "minutes": 60},
        {"label": "ai", "minutes": 30},
        {"label": "python", "minutes": 45},
    ]
    frame = build_dataframe(rows)
    print(summarize(frame))
    print(minutes_by_label(frame))


if __name__ == "__main__":
    main()
