"""Worked examples for lesson 12."""

from __future__ import annotations

import logging
from collections import Counter
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class StudySession:
    """A validated, immutable study session."""

    study_date: str
    minutes: int
    label: str

    def __post_init__(self) -> None:
        if not self.study_date.strip():
            raise ValueError("study_date cannot be empty")
        try:
            date.fromisoformat(self.study_date)
        except ValueError as exc:
            raise ValueError("study_date must use YYYY-MM-DD") from exc
        if self.minutes < 0:
            raise ValueError("minutes cannot be negative")
        if not self.label.strip():
            raise ValueError("label cannot be empty")


def total_by_label(sessions: list[StudySession]) -> dict[str, int]:
    """Sum minutes by label in deterministic order."""
    totals = Counter()
    for session in sessions:
        totals[session.label] += session.minutes
    return dict(sorted(totals.items()))


def completed_sessions(
    sessions: list[StudySession],
    minimum: int = 60,
) -> list[StudySession]:
    """Return sessions meeting the minimum duration."""
    if minimum < 0:
        raise ValueError("minimum cannot be negative")
    return [session for session in sessions if session.minutes >= minimum]


def configure_logger(name: str = "study_lesson") -> logging.Logger:
    """Create a simple logger without duplicate handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(logging.StreamHandler())
    return logger


def log_summary(logger: logging.Logger, sessions: list[StudySession]) -> None:
    """Log aggregate session statistics."""
    total = sum(session.minutes for session in sessions)
    logger.info("sessions=%d total_minutes=%d", len(sessions), total)


def main() -> None:
    sessions = [
        StudySession("2026-10-08", 45, "python"),
        StudySession("2026-10-09", 60, "ai"),
    ]
    print(total_by_label(sessions))
    log_summary(configure_logger(), sessions)


if __name__ == "__main__":
    main()
