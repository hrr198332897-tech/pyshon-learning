"""Worked examples for lesson 9."""

from __future__ import annotations

from typing import Any

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    TfidfVectorizer = None
    cosine_similarity = None


def require_sklearn() -> None:
    """Raise a clear error when scikit-learn is unavailable."""
    if TfidfVectorizer is None or cosine_similarity is None:
        raise RuntimeError("scikit-learn is required for this lesson")


def build_index(documents: list[str]) -> tuple[Any, Any]:
    """Build a TF-IDF vectorizer and document matrix."""
    require_sklearn()
    if not documents:
        raise ValueError("documents cannot be empty")
    if any(not document.strip() for document in documents):
        raise ValueError("documents cannot contain blank entries")

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(documents)
    return vectorizer, matrix


def search_documents(
    query: str,
    documents: list[str],
    top_k: int = 3,
) -> list[dict[str, Any]]:
    """Return the most similar documents with source indexes and scores."""
    require_sklearn()
    if not query.strip():
        raise ValueError("query cannot be empty")
    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    vectorizer, matrix = build_index(documents)
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix).ravel()
    ranked = sorted(enumerate(scores), key=lambda item: (-item[1], item[0]))

    return [
        {
            "index": index,
            "score": round(float(score), 3),
            "text": documents[index],
        }
        for index, score in ranked[:top_k]
    ]


def build_context(
    query: str,
    documents: list[str],
    top_k: int = 3,
) -> str:
    """Build numbered context from the most relevant documents."""
    results = search_documents(query, documents, top_k=top_k)
    if not results or results[0]["score"] <= 0:
        return "没有找到相关内容。"

    lines = [
        f"[{position}] {result['text']}"
        for position, result in enumerate(results, start=1)
        if result["score"] > 0
    ]
    return "\n\n".join(lines) if lines else "没有找到相关内容。"


def main() -> None:
    documents = [
        "Python variables store values for later use.",
        "Functions organize reusable Python logic.",
        "TF-IDF ranks documents by word importance.",
    ]
    print(search_documents("Python functions", documents))


if __name__ == "__main__":
    main()
