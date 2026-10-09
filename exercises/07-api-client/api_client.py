"""Practice HTTP requests, JSON parsing, and response validation."""

from __future__ import annotations

from typing import Any


def fetch_json(url: str, timeout: float = 5.0) -> Any:
    """Fetch and decode a JSON response."""
    raise NotImplementedError("请完成 fetch_json 函数")


def extract_records(payload: Any) -> list[dict[str, Any]]:
    """Validate and normalize API records."""
    raise NotImplementedError("请完成 extract_records 函数")


def summarize_records(records: list[dict[str, Any]]) -> dict[str, int | float]:
    """Return aggregate statistics for normalized records."""
    raise NotImplementedError("请完成 summarize_records 函数")


def main() -> None:
    print("请先在测试中实现函数，再替换这里为真实 API 地址。")


if __name__ == "__main__":
    main()
