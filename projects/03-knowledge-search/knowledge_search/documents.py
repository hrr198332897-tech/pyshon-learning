"""Load and chunk local knowledge documents."""

from __future__ import annotations

from pathlib import Path


SUPPORTED_SUFFIXES = {".md", ".txt"}


def chunk_text(
    text: str,
    max_chars: int = 200,
    overlap: int = 40,
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


def load_documents(
    root: Path,
    max_chars: int = 200,
    overlap: int = 40,
) -> list[dict[str, object]]:
    """Load supported files and split them into source-aware chunks."""
    if not root.exists():
        raise FileNotFoundError(f"document directory does not exist: {root}")
    if not root.is_dir():
        raise ValueError(f"document path is not a directory: {root}")

    chunks: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue

        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue

        source = path.relative_to(root).as_posix()
        for position, chunk in enumerate(
            chunk_text(text, max_chars=max_chars, overlap=overlap),
            start=1,
        ):
            chunks.append(
                {
                    "source": source,
                    "position": position,
                    "text": chunk,
                }
            )

    if not chunks:
        raise ValueError(f"no supported documents found in: {root}")
    return chunks
