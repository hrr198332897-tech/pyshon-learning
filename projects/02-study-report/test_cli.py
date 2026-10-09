"""Integration tests for the study report command-line application."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    pd = None


PROJECT_DIR = Path(__file__).resolve().parent
SAMPLE_PATH = PROJECT_DIR / "examples" / "sessions.csv"


@unittest.skipIf(pd is None, "pandas is not installed")
class CliTests(unittest.TestCase):
    def test_cli_prints_report(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "study_report", "--input", str(SAMPLE_PATH)],
            cwd=PROJECT_DIR,
            env={**os.environ, "PYTHONUTF8": "1"},
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("# Study Report", result.stdout)
        self.assertIn("- Top label: ai (120 minutes)", result.stdout)

    def test_cli_writes_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "study_report",
                    "--input",
                    str(SAMPLE_PATH),
                    "--output",
                    str(output),
                ],
                cwd=PROJECT_DIR,
                env={**os.environ, "PYTHONUTF8": "1"},
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(output.exists())
            self.assertIn("| python | 105 |", output.read_text(encoding="utf-8"))

    def test_cli_reports_missing_input(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "study_report", "--input", "missing.csv"],
            cwd=PROJECT_DIR,
            env={**os.environ, "PYTHONUTF8": "1"},
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Error:", result.stdout)


if __name__ == "__main__":
    unittest.main()
