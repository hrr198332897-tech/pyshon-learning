"""Progress checks for the JSON study log exercise."""

import tempfile
import unittest
from pathlib import Path

from study_log import add_entry, load_entries, save_entries, total_minutes


def call_or_skip(test: unittest.TestCase, function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class StudyLogTests(unittest.TestCase):
    def test_save_and_load_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study-log.json"
            entries = [{"day": 1, "minutes": 60}]

            call_or_skip(self, save_entries, path, entries)
            loaded = call_or_skip(self, load_entries, path)
            self.assertEqual(loaded, entries)

    def test_missing_file_returns_empty_list(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.json"
            result = call_or_skip(self, load_entries, path)
            self.assertEqual(result, [])

    def test_invalid_json_raises_value_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.json"
            path.write_text("{broken", encoding="utf-8")

            try:
                load_entries(path)
            except NotImplementedError as exc:
                self.skipTest(str(exc))
            except ValueError:
                return
            self.fail("无效 JSON 应触发 ValueError")

    def test_add_entry_returns_new_list(self) -> None:
        original = [{"day": 1, "minutes": 30}]
        updated = call_or_skip(self, add_entry, original, day=2, minutes=60)
        self.assertEqual(original, [{"day": 1, "minutes": 30}])
        self.assertEqual(updated[-1], {"day": 2, "minutes": 60})

    def test_total_minutes(self) -> None:
        entries = [{"day": 1, "minutes": 30}, {"day": 2, "minutes": 60}]
        result = call_or_skip(self, total_minutes, entries)
        self.assertEqual(result, 90)


if __name__ == "__main__":
    unittest.main()
