"""Practice DataFrame construction, filtering, grouping, and summaries."""

from __future__ import annotations

from typing import Any

try:
    import pandas as pd
except ImportError:
    pd = None


def require_pandas() -> None:
    """Raise a clear error when pandas is unavailable."""
    if pd is None:
        raise RuntimeError("pandas is required for this exercise")


def build_dataframe(rows: list[dict[str, Any]]) -> Any:
    """Build a normalized DataFrame from records."""
    raise NotImplementedError("请完成 build_dataframe 函数")


def filter_minimum(frame: Any, minimum: int) -> Any:
    """Return records meeting the minimum number of minutes."""
    raise NotImplementedError("请完成 filter_minimum 函数")


def minutes_by_label(frame: Any) -> list[dict[str, Any]]:
    """Sum minutes by label using deterministic ordering."""
    raise NotImplementedError("请完成 minutes_by_label 函数")


def summarize(frame: Any) -> dict[str, int | float]:
    """Return aggregate statistics."""
    raise NotImplementedError("请完成 summarize 函数")


def main() -> None:
    print("安装 Pandas 后，用测试驱动完成本练习。")


if __name__ == "__main__":
    main()
