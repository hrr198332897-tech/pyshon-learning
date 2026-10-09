"""Verify the local Python and Git learning environment."""

from __future__ import annotations

import importlib
import platform
import sys
from pathlib import Path


REQUIRED_MODULES = ("csv", "json", "pathlib", "sqlite3", "statistics")
REQUIRED_PATHS = (
    Path("README.md"),
    Path("ROADMAP.md"),
    Path(".git"),
)


def check_modules() -> list[str]:
    """Return the names of required modules that cannot be imported."""
    missing: list[str] = []
    for module_name in REQUIRED_MODULES:
        try:
            importlib.import_module(module_name)
        except ImportError:
            missing.append(module_name)
    return missing


def main() -> int:
    root = Path.cwd()
    missing_modules = check_modules()
    missing_paths = [path for path in REQUIRED_PATHS if not (root / path).exists()]

    print("Python environment check")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Python executable: {sys.executable}")
    print(f"Operating system: {platform.system()} {platform.release()}")
    print(f"Working directory: {root}")
    print(f"Standard library: {'OK' if not missing_modules else 'MISSING ' + ', '.join(missing_modules)}")
    print(f"Repository files: {'OK' if not missing_paths else 'MISSING ' + ', '.join(map(str, missing_paths))}")

    if missing_modules or missing_paths:
        print("Result: FIX REQUIRED")
        return 1

    print("Result: READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
