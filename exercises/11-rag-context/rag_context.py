"""Practice document chunking and grounded prompt construction."""

from __future__ import annotations


def chunk_text(
    text: str,
    max_chars: int = 120,
    overlap: int = 20,
) -> list[str]:
    """Split text into overlapping character windows."""
    raise NotImplementedError("请完成 chunk_text 函数")


def normalize_chunks(chunks: list[str]) -> list[str]:
    """Strip chunks and remove empty entries."""
    raise NotImplementedError("请完成 normalize_chunks 函数")


def build_prompt(question: str, contexts: list[str]) -> str:
    """Build a grounded answer prompt with numbered context."""
    raise NotImplementedError("请完成 build_prompt 函数")


def main() -> None:
    print("完成函数后，用测试验证分块和提示结构。")


if __name__ == "__main__":
    main()
