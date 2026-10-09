"""Tests for the GitHub readiness helper."""

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "check_github_readiness.py"


class GithubReadinessTests(unittest.TestCase):
    def test_offline_check(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--offline"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertIn(result.returncode, {0, 1}, result.stderr)
        self.assertIn("[OK] Git repository", result.stdout)
        self.assertIn("[OK] Current branch: main", result.stdout)
        self.assertIn("Working tree:", result.stdout)
        self.assertIn("[SKIP] Remote access: offline mode", result.stdout)


if __name__ == "__main__":
    unittest.main()
