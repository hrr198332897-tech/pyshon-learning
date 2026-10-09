"""Practice variables, input conversion, functions, and f-strings."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a greeting in the form 你好，名字！"""
    raise NotImplementedError("请完成 greet 函数")


def minutes_to_hours(minutes: int) -> float:
    """Convert minutes to hours."""
    raise NotImplementedError("请完成 minutes_to_hours 函数")


def build_summary(name: str, minutes: int) -> str:
    """Return the one-line summary shown in the exercise README."""
    raise NotImplementedError("请完成 build_summary 函数")


def main() -> None:
    name = input("你的名字: ").strip()
    minutes_text = input("本周计划学习多少分钟: ").strip()

    try:
        minutes = int(minutes_text)
    except ValueError:
        print("请输入整数分钟数，例如 150。")
        return

    print(build_summary(name, minutes))


if __name__ == "__main__":
    main()
