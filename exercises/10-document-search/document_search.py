"""Practice TF-IDF indexing and document retrieval."""

from __future__ import annotations

from typing import Any


def build_index(documents: list[str]) -> tuple[Any, Any]:
    """Build a TF-IDF vectorizer and document matrix."""
    raise NotImplementedError("请完成 build_index 函数")


def search_documents(
    query: str,
    documents: list[str],
    top_k: int = 3,
) -> list[dict[str, Any]]:
    """Return the most similar documents with source indexes and scores."""
    raise NotImplementedError("请完成 search_documents 函数")


def build_context(
    query: str,
    documents: list[str],
    top_k: int = 3,
) -> str:
    """Build numbered context from the most relevant documents."""
    raise NotImplementedError("请完成 build_context 函数")


def main() -> None:
    print("安装 scikit-learn 后，用测试驱动完成本练习。")


if __name__ == "__main__":
    main()
