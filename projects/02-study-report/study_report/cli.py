"""Command-line interface for the study report project."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from study_report.data import load_sessions
from study_report.report import build_markdown_report, write_report


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description="Generate a Markdown study report.")
    parser.add_argument("--input", type=Path, required=True, help="input CSV file")
    parser.add_argument("--output", type=Path, help="optional Markdown output file")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the report generator."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        frame = load_sessions(args.input)
        content = build_markdown_report(frame)
        if args.output is None:
            print(content, end="")
        else:
            write_report(args.output, content)
            print(f"Report written to {args.output}")
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"Error: {exc}")
        return 2

    return 0
