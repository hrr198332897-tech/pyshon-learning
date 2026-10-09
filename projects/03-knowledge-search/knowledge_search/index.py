"""Build TF-IDF indexes and search document chunks."""

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
        raise RuntimeError("scikit-learn is required for knowledge search")


def build_index(chunks: list[dict[str, object]]) -> tuple[Any, Any]:
    """Build a character-level TF-IDF index for document chunks."""
    require_sklearn()
    if not chunks:
        raise ValueError("chunks cannot be empty")

    texts = [str(chunk["text"]) for chunk in chunks]
    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 4))
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix


def search(
    query: str,
    chunks: list[dict[str, object]],
    index: tuple[Any, Any],
    top_k: int = 3,
) -> list[dict[str, object]]:
    """Return chunks with positive similarity, ordered by score."""
    require_sklearn()
    if not query.strip():
        raise ValueError("query cannot be empty")
    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    vectorizer, matrix = index
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix).ravel()
    ranked = sorted(enumerate(scores), key=lambda item: (-item[1], item[0]))

    results: list[dict[str, object]] = []
    for index_position, score in ranked[:top_k]:
        if score <= 0:
            continue
        result = dict(chunks[index_position])
        result["score"] = round(float(score), 3)
        results.append(result)
    return results
