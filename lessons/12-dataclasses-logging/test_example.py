"""Tests for lesson 12 worked examples."""

import unittest

from example import (
    StudySession,
    completed_sessions,
    configure_logger,
    log_summary,
    total_by_label,
)


class ExampleTests(unittest.TestCase):
    def test_study_session(self) -> None:
        session = StudySession("2026-10-09", 60, "python")
        self.assertEqual(session.minutes, 60)

    def test_study_session_is_immutable(self) -> None:
        session = StudySession("2026-10-09", 60, "python")
        with self.assertRaises(Exception):
            session.minutes = 90

    def test_study_session_validation(self) -> None:
        with self.assertRaises(ValueError):
            StudySession("2026-10-09", -1, "python")
        with self.assertRaises(ValueError):
            StudySession("10-09-2026", 60, "python")

    def test_total_by_label(self) -> None:
        sessions = [
            StudySession("2026-10-08", 30, "python"),
            StudySession("2026-10-09", 60, "ai"),
            StudySession("2026-10-10", 45, "python"),
        ]
        self.assertEqual(total_by_label(sessions), {"ai": 60, "python": 75})

    def test_completed_sessions(self) -> None:
        sessions = [
            StudySession("2026-10-08", 30, "python"),
            StudySession("2026-10-09", 60, "ai"),
        ]
        self.assertEqual([session.minutes for session in completed_sessions(sessions)], [60])

    def test_log_summary(self) -> None:
        logger = configure_logger("test_study_lesson")
        sessions = [StudySession("2026-10-09", 60, "ai")]
        with self.assertLogs(logger, level="INFO") as captured:
            log_summary(logger, sessions)
        self.assertIn("sessions=1 total_minutes=60", captured.output[0])


if __name__ == "__main__":
    unittest.main()
