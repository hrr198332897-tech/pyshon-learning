"""Worked examples for lesson 1."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a short greeting."""
    return f"你好，{name}！"


def minutes_to_hours(minutes: int) -> float:
    """Convert minutes to hours."""
    return minutes / 60


def build_summary(name: str, minutes: int) -> str:
    """Build a one-line study plan summary."""
    hours = minutes_to_hours(minutes)
    return f"{greet(name)} 你这周计划学习 {minutes} 分钟，也就是 {hours:.1f} 小时。"


def main() -> None:
    name = input("你的名字: ").strip()
    minutes = int(input("本周计划学习多少分钟: "))
    print(build_summary(name, minutes))


if __name__ == "__main__":
    main()
