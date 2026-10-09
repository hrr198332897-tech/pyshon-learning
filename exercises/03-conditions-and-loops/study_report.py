"""Practice conditions, loops, continue, break, and enumerate."""

from __future__ import annotations


def classify_study_time(minutes: int) -> str:
    """Return a study intensity label for one day."""
    raise NotImplementedError("请完成 classify_study_time 函数")


def count_active_days(daily_minutes: list[int]) -> int:
    """Count days with more than zero minutes."""
    raise NotImplementedError("请完成 count_active_days 函数")


def first_goal_day(daily_minutes: list[int], target: int = 60) -> int | None:
    """Return the first one-based day reaching the target, or None."""
    raise NotImplementedError("请完成 first_goal_day 函数")


def build_report(daily_minutes: list[int], target: int = 60) -> str:
    """Build the summary sentence shown in the exercise README."""
    raise NotImplementedError("请完成 build_report 函数")


def main() -> None:
    raw = input("输入七天学习分钟数，用逗号分隔: ").strip()
    try:
        daily_minutes = [int(item.strip()) for item in raw.split(",")]
    except ValueError:
        print("每一项都必须是整数，例如 20,65,0,90,30,130,45。")
        return

    try:
        print(build_report(daily_minutes))
    except ValueError as exc:
        print(f"输入错误: {exc}")


if __name__ == "__main__":
    main()
