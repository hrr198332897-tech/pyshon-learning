"""Run all lesson and exercise tests from one command."""

from __future__ import annotations

import argparse
import re
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK_ROOTS = ("lessons", "exercises", "projects", "tools")
SUBPROCESS_ENV = {**os.environ, "PYTHONUTF8": "1"}


def find_test_directories() -> list[Path]:
    directories: set[Path] = set()
    for root_name in CHECK_ROOTS:
        root = ROOT / root_name
        for test_file in root.rglob("test*.py"):
            directories.add(test_file.parent)
    return sorted(directories, key=lambda path: str(path.relative_to(ROOT)))


def run_directory(directory: Path) -> tuple[int, int, int]:
    relative = directory.relative_to(ROOT)
    print(f"\n== {relative} ==", flush=True)
    command = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        str(directory),
        "-t",
        str(directory),
        "-v",
    ]
    result = subprocess.run(
        command, cwd=ROOT, env=SUBPROCESS_ENV, check=False,
        capture_output=True, text=True, encoding="utf-8",
    )
    output = result.stdout + result.stderr
    print(output, end="", flush=True)
    totals = re.findall(r"Ran (\d+) tests?", output)
    skipped = re.findall(r"skipped=(\d+)", output)
    return result.returncode, sum(map(int, totals)), sum(map(int, skipped))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exercise", help="Check one exercise directory, e.g. 02-variables-and-input")
    parser.add_argument("--strict", action="store_true", help="Fail if any test is skipped")
    args = parser.parse_args()
    directories = find_test_directories()
    if args.exercise:
        directories = [p for p in directories if p.parent == ROOT / "exercises" and p.name == args.exercise]
        if not directories:
            parser.error("exercise not found or contains no tests")
    if not directories:
        print("No test directories were found.")
        return 1

    failed: list[Path] = []
    total = skipped = 0
    for directory in directories:
        code, count, skip_count = run_directory(directory)
        total += count
        skipped += skip_count
        if code != 0:
            failed.append(directory)

    print("\nCheck summary")
    print(f"Test directories: {len(directories)}")
    print(f"Failed directories: {len(failed)}")

    print(f"Tests run: {total}; skipped: {skipped}")
    if failed:
        for directory in failed:
            print(f"FAILED: {directory.relative_to(ROOT)}")
        return 1

    if args.strict and skipped:
        print("Result: INCOMPLETE (strict mode rejects skipped tests)")
        return 1
    if skipped:
        print("Result: CHECKS OK; learning completion is NOT verified (skipped tests)")
    else:
        print("Result: OK; independent mastery still requires explanation and a new task")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
