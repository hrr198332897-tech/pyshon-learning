"""Progress checks for the task dataclass exercise."""

import unittest

from task_dataclass import StudyTask, log_task, mark_complete, summarize_tasks


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class TaskDataclassTests(unittest.TestCase):
    def test_task_validation(self) -> None:
        with self.assertRaises(ValueError):
            StudyTask("", 30)
        with self.assertRaises(ValueError):
            StudyTask("lesson", -1)

    def test_mark_complete_returns_new_task(self) -> None:
        original = StudyTask("lesson", 30)
        updated = call_or_skip(self, mark_complete, original)
        self.assertFalse(original.completed)
        self.assertTrue(updated.completed)

    def test_summarize_tasks(self) -> None:
        tasks = [
            StudyTask("lesson", 30, completed=True),
            StudyTask("project", 60),
        ]
        result = call_or_skip(self, summarize_tasks, tasks)
        self.assertEqual(
            result,
            {"total": 2, "completed": 1, "pending": 1, "total_minutes": 90},
        )

    def test_log_task(self) -> None:
        logger = __import__("logging").getLogger("task_dataclass_test")
        logger.setLevel(__import__("logging").INFO)
        task = StudyTask("lesson", 30, completed=True)
        try:
            with self.assertLogs(logger, level="INFO") as captured:
                log_task(logger, task)
        except NotImplementedError as exc:
            self.skipTest(str(exc))
        self.assertIn("title=lesson", captured.output[0])
        self.assertIn("completed=True", captured.output[0])


if __name__ == "__main__":
    unittest.main()
