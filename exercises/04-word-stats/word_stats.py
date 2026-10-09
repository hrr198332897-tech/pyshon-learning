"""Practice list, dictionary, function, and sorting operations."""

from __future__ import annotations


def count_words(text: str) -> dict[str, int]:
    """Count normalized words in a text."""
    raise NotImplementedError("请完成 count_words 函数")


def top_words(
    vocabulary: dict[str, int],
    limit: int = 3,
) -> list[tuple[str, int]]:
    """Return the most common words with deterministic tie-breaking."""
    raise NotImplementedError("请完成 top_words 函数")


def build_summary(text: str) -> str:
    """Build a summary for the most common word."""
    raise NotImplementedError("请完成 build_summary 函数")


def main() -> None:
    text = input("输入一段英文文本: ").strip()
    counts = count_words(text)
    print(f"词频: {counts}")
    print(f"高频词: {top_words(counts)}")
    print(build_summary(text))


if __name__ == "__main__":
    main()
