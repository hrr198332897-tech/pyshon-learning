"""Progress checks for the scikit-learn classifier exercise."""

import unittest

try:
    import sklearn
except ImportError:
    sklearn = None

from classifier import build_model, make_dataset, split_dataset, train_and_evaluate


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class ClassifierTests(unittest.TestCase):
    def test_make_dataset(self) -> None:
        features, labels = call_or_skip(self, make_dataset)
        self.assertEqual(features.shape, (120, 4))
        self.assertEqual(len(labels), 120)

    def test_split_dataset(self) -> None:
        features, labels = call_or_skip(self, make_dataset)
        train_x, test_x, train_y, test_y = call_or_skip(self, split_dataset, features, labels)
        self.assertEqual((len(train_x), len(test_x)), (90, 30))
        self.assertEqual((len(train_y), len(test_y)), (90, 30))

    def test_build_model(self) -> None:
        model = call_or_skip(self, build_model)
        self.assertIn("scale", model.named_steps)
        self.assertIn("classifier", model.named_steps)

    def test_train_and_evaluate(self) -> None:
        features, labels = call_or_skip(self, make_dataset)
        train_x, test_x, train_y, test_y = call_or_skip(self, split_dataset, features, labels)
        result = call_or_skip(self, train_and_evaluate, train_x, train_y, test_x, test_y)
        self.assertGreaterEqual(result["accuracy"], 0.85)
        self.assertEqual(len(result["predictions"]), 30)


if __name__ == "__main__":
    unittest.main()
