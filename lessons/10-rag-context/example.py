"""Worked examples for lesson 10."""

from __future__ import annotations


def chunk_text(
    text: str,
    max_chars: int = 120,
    overlap: int = 20,
) -> list[str]:
    """Split text into overlapping character windows."""
    if max_chars < 1:
        raise ValueError("max_chars must be at least 1")
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    if overlap >= max_chars:
        raise ValueError("overlap must be smaller than max_chars")
    if not text.strip():
        return []

    step = max_chars - overlap
    chunks: list[str] = []
    for start in range(0, len(text), step):
        chunk = text[start : start + max_chars].strip()
        if chunk:
            chunks.append(chunk)
        if start + max_chars >= len(text):
            break
    return chunks


def normalize_chunks(chunks: list[str]) -> list[str]:
    """Strip chunks and remove empty entries."""
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def build_prompt(question: str, contexts: list[str]) -> str:
    """Build a grounded answer prompt with numbered context."""
    if not question.strip():
        raise ValueError("question cannot be empty")

    cleaned = normalize_chunks(contexts)
    if not cleaned:
        raise ValueError("contexts cannot be empty")

    numbered = "\n".join(
        f"[{index}] {context}"
        for index, context in enumerate(cleaned, start=1)
    )
    return (
        "只根据下面的上下文回答问题。\n"
        "如果上下文不足，明确回答“不知道”。\n"
        "不要编造来源，并在回答后列出使用的来源编号。\n\n"
        f"上下文:\n{numbered}\n\n"
        f"问题: {question.strip()}\n"
        "回答:"
    )


def main() -> None:
    text = (
        "Python 函数用于组织可复用逻辑。"
        "变量用于保存值。"
        "测试用于验证行为。"
    )
    contexts = chunk_text(text, max_chars=20, overlap=4)
    print(build_prompt("Python 函数有什么作用？", contexts))


if __name__ == "__main__":
    main()
