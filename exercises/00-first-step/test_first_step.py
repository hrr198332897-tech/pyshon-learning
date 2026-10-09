"""Check that the first message is filled in."""

import unittest

import first_step


class FirstStepTests(unittest.TestCase):
    def test_message_is_text(self) -> None:
        self.assertIsInstance(first_step.message, str)
        self.assertTrue(first_step.message.strip())


if __name__ == "__main__":
    unittest.main()
