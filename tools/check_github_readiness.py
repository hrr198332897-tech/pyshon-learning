"""Read-only checks for local Git and GitHub remote readiness."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_git(*args: str, timeout: float = 15.0) -> tuple[int, str]:
    """Run a Git command and capture standard output and error."""
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=timeout,
        check=False,
    )
    output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
    return result.returncode, output


def check_local() -> list[tuple[bool, str, str]]:
    """Return local repository checks as success, label, detail."""
    checks: list[tuple[bool, str, str]] = []

    code, output = run_git("rev-parse", "--is-inside-work-tree")
    checks.append((code == 0 and output == "true", "Git repository", output or "not found"))

    code, output = run_git("branch", "--show-current")
    checks.append((code == 0 and output == "main", "Current branch", output or "unknown"))

    code, output = run_git("remote", "get-url", "origin")
    checks.append((code == 0 and bool(output), "Remote origin", output or "not configured"))

    code, output = run_git("status", "--porcelain")
    checks.append((code == 0 and not output, "Working tree", "clean" if not output else output))

    code, output = run_git("tag", "--list")
    tags = ", ".join(output.splitlines()) if output else "none"
    checks.append((code == 0, "Version tags", tags))

    return checks


def check_remote() -> tuple[bool, str, str]:
    """Check whether the configured GitHub remote already exists."""
    code, remote_url = run_git("remote", "get-url", "origin")
    if code != 0 or not remote_url:
        return False, "Remote access", "remote origin is not configured"

    code, output = run_git("ls-remote", "--exit-code", "origin")
    if code == 0:
        return True, "Remote access", f"reachable: {remote_url}"
    if "not found" in output.lower() or "repository" in output.lower():
        return False, "Remote access", "repository not found or not accessible"
    return False, "Remote access", output or "remote check failed"


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description="Check GitHub publishing readiness.")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="skip the network remote-access check",
    )
    return parser


def main() -> int:
    """Run all readiness checks."""
    args = build_parser().parse_args()
    checks = check_local()
    if not args.offline:
        checks.append(check_remote())

    failed = 0
    for success, label, detail in checks:
        marker = "OK" if success else "ACTION"
        print(f"[{marker}] {label}: {detail}")
        if not success and label != "Remote access":
            failed += 1

    remote_ready = any(
        success and label == "Remote access"
        for success, label, _ in checks
    )
    if args.offline:
        print("[SKIP] Remote access: offline mode")
    elif not remote_ready:
        print("Next: create the empty GitHub repository, then run this script again.")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
