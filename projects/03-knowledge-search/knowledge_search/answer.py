"""Construct grounded prompts and local extractive answers."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from knowledge_search.index import search


def build_prompt(question: str, results: list[dict[str, object]]) -> str:
    """Build a numbered, grounded prompt from search results."""
    if not question.strip():
        raise ValueError("question cannot be empty")
    if not results:
        raise ValueError("results cannot be empty")

    context_lines = [
        f"[{index}] ({result['source']} #{result['position']}) {result['text']}"
        for index, result in enumerate(results, start=1)
    ]
    context = "\n".join(context_lines)
    return (
        "只根据下面的上下文回答问题。\n"
        "如果上下文不足，明确回答“不知道”。\n"
        "不要编造来源，并在回答后列出使用的来源编号。\n\n"
        f"上下文:\n{context}\n\n"
        f"问题: {question.strip()}\n"
        "回答:"
    )


def extractive_answer(results: list[dict[str, object]]) -> str:
    """Return a grounded fallback answer from the best matching chunk."""
    if not results:
        return "不知道：没有找到相关内容。"

    top = results[0]
    return (
        f"根据 [1] {top['text']}\n\n"
        f"来源: [1] {top['source']} #{top['position']}"
    )


def answer_question(
    question: str,
    chunks: list[dict[str, object]],
    index: tuple[Any, Any],
    top_k: int = 3,
    generator: Callable[[str], str] | None = None,
) -> dict[str, Any]:
    """Retrieve context and optionally pass it to a model generator."""
    results = search(question, chunks, index, top_k=top_k)
    if not results:
        return {"answer": "不知道：没有找到相关内容。", "sources": []}

    prompt = build_prompt(question, results)
    answer = generator(prompt) if generator is not None else extractive_answer(results)
    return {
        "answer": answer,
        "sources": [
            {
                "source": result["source"],
                "position": result["position"],
                "score": result["score"],
            }
            for result in results
        ],
    }
