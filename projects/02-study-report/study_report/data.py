"""Load and validate study session data."""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import pandas as pd
except ImportError:
    pd = None


REQUIRED_COLUMNS = {"date", "minutes", "label", "note"}


def require_pandas() -> None:
    """Raise a clear error when pandas is unavailable."""
    if pd is None:
        raise RuntimeError("pandas is required for study_report")


def load_sessions(path: Path) -> Any:
    """Load and validate a study session CSV file."""
    require_pandas()
    if not path.exists():
        raise FileNotFoundError(f"input file does not exist: {path}")

    try:
        frame = pd.read_csv(path)
    except pd.errors.EmptyDataError as exc:
        raise ValueError("input CSV is empty") from exc

    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"missing columns: {', '.join(sorted(missing))}")

    frame = frame.copy()
    for column in ("date", "label", "note"):
        frame[column] = frame[column].fillna("").astype(str).str.strip()

    if frame["date"].eq("").any():
        raise ValueError("date cannot be empty")
    if frame["label"].eq("").any():
        raise ValueError("label cannot be empty")

    try:
        frame["minutes"] = pd.to_numeric(frame["minutes"], errors="raise").astype("int64")
    except (TypeError, ValueError) as exc:
        raise ValueError("minutes must contain integers") from exc

    if frame["minutes"].lt(0).any():
        raise ValueError("minutes cannot be negative")

    return frame[["date", "minutes", "label", "note"]]
