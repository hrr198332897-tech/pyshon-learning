"""Run all lesson and exercise tests from one command."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK_ROOTS = ("lessons", "exercises", "projects")
SUBPROCESS_ENV = {**os.environ, "PYTHONUTF8": "1"}


def find_test_directories() -> list[Path]:
    directories: set[Path] = set()
    for root_name in CHECK_ROOTS:
        root = ROOT / root_name
        for test_file in root.rglob("test*.py"):
            directories.add(test_file.parent)
    return sorted(directories, key=lambda path: str(path.relative_to(ROOT)))


def run_directory(directory: Path) -> int:
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
    return subprocess.run(command, cwd=ROOT, env=SUBPROCESS_ENV, check=False).returncode


def main() -> int:
    directories = find_test_directories()
    if not directories:
        print("No test directories were found.")
        return 1

    failed: list[Path] = []
    for directory in directories:
        if run_directory(directory) != 0:
            failed.append(directory)

    print("\nCheck summary")
    print(f"Test directories: {len(directories)}")
    print(f"Failed directories: {len(failed)}")

    if failed:
        for directory in failed:
            print(f"FAILED: {directory.relative_to(ROOT)}")
        return 1

    print("Result: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
