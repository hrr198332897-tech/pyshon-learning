"""Worked examples for lesson 2."""

from __future__ import annotations


def classify_study_time(minutes: int) -> str:
    """Return a study intensity label."""
    if minutes < 0:
        raise ValueError("minutes cannot be negative")
    if minutes >= 120:
        return "高强度学习"
    if minutes >= 60:
        return "投入充足"
    if minutes >= 30:
        return "达到基础目标"
    return "需要继续积累"


def count_active_days(daily_minutes: list[int]) -> int:
    """Count days with more than zero minutes."""
    active_days = 0
    for minutes in daily_minutes:
        if minutes <= 0:
            continue
        active_days += 1
    return active_days


def first_goal_day(daily_minutes: list[int], target: int = 60) -> int | None:
    """Return the first one-based day that reaches the target."""
    for day, minutes in enumerate(daily_minutes, start=1):
        if minutes >= target:
            return day
    return None


def main() -> None:
    daily_minutes = [20, 65, 0, 90, 30, 130, 45]
    print(count_active_days(daily_minutes))
    print(first_goal_day(daily_minutes))


if __name__ == "__main__":
    main()
