"""Command-line interface for local knowledge search."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Sequence

from knowledge_search.answer import answer_question
from knowledge_search.documents import load_documents
from knowledge_search.index import build_index, search
from knowledge_search.provider import load_llm_config, make_llm_generator


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description="Search a local knowledge directory.")
    parser.add_argument(
        "--documents",
        type=Path,
        default=Path("examples/notes"),
        help="directory containing .md and .txt files",
    )
    parser.add_argument("--query", required=True, help="question or search query")
    parser.add_argument("--top-k", type=int, default=3, help="number of chunks to retrieve")
    parser.add_argument(
        "--show-context",
        action="store_true",
        help="print retrieved context after the answer",
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="send retrieved context to the configured remote model",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the knowledge search application."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        chunks = load_documents(args.documents)
        index = build_index(chunks)
        generator = None
        if args.use_llm:
            config = load_llm_config(os.environ)
            generator = make_llm_generator(config)
        result = answer_question(
            args.query,
            chunks,
            index,
            top_k=args.top_k,
            generator=generator,
        )
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"Error: {exc}")
        return 2

    print(result["answer"])
    print("\nSources:")
    for position, source in enumerate(result["sources"], start=1):
        print(
            f"[{position}] {source['source']} "
            f"#{source['position']} ({source['score']})"
        )
    if args.show_context:
        print("\nRetrieved context:")
        for position, item in enumerate(search(args.query, chunks, index, top_k=args.top_k), start=1):
            print(f"[{position}] {item['source']} #{item['position']} ({item['score']})")
            print(item["text"])

    return 0
