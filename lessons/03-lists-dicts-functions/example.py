"""Worked examples for lesson 3."""

from __future__ import annotations


def count_words(text: str) -> dict[str, int]:
    """Count unique words after lowercasing and removing simple punctuation."""
    counts: dict[str, int] = {}
    for raw_word in text.lower().split():
        word = raw_word.strip(".,!?;:()[]{}\"'")
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def add_word(vocabulary: dict[str, int], word: str) -> None:
    """Add one occurrence of a word to the vocabulary."""
    vocabulary[word] = vocabulary.get(word, 0) + 1


def top_words(
    vocabulary: dict[str, int],
    limit: int = 3,
) -> list[tuple[str, int]]:
    """Return the most common words with deterministic tie-breaking."""
    ranked = sorted(vocabulary.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:limit]


def build_summary(text: str) -> str:
    """Build a short summary for the most common word."""
    counts = count_words(text)
    if not counts:
        return "文本中没有可统计的词。"

    word, count = top_words(counts, limit=1)[0]
    return f"共 {len(counts)} 个词，最常出现的是 {word}（{count} 次）。"


def main() -> None:
    text = "Python makes AI tools. Python is practical for AI."
    print(count_words(text))
    print(top_words(count_words(text)))
    print(build_summary(text))


if __name__ == "__main__":
    main()
