"""Tests for lesson 8 worked examples."""

import unittest

try:
    import sklearn
except ImportError:
    sklearn = None

from example import build_model, make_dataset, split_dataset, train_and_evaluate


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class ExampleTests(unittest.TestCase):
    def test_make_dataset_is_reproducible(self) -> None:
        first_features, first_labels = make_dataset()
        second_features, second_labels = make_dataset()
        self.assertEqual(first_features.shape, (120, 4))
        self.assertTrue((first_labels == second_labels).all())

    def test_split_dataset(self) -> None:
        features, labels = make_dataset()
        train_x, test_x, train_y, test_y = split_dataset(features, labels)
        self.assertEqual(len(train_x), 90)
        self.assertEqual(len(test_x), 30)
        self.assertEqual(len(train_y), 90)
        self.assertEqual(len(test_y), 30)

    def test_pipeline_structure(self) -> None:
        model = build_model()
        self.assertEqual(model.named_steps["scale"].__class__.__name__, "StandardScaler")
        self.assertEqual(
            model.named_steps["classifier"].__class__.__name__,
            "LogisticRegression",
        )

    def test_train_and_evaluate(self) -> None:
        features, labels = make_dataset()
        train_x, test_x, train_y, test_y = split_dataset(features, labels)
        result = train_and_evaluate(train_x, train_y, test_x, test_y)
        self.assertGreaterEqual(result["accuracy"], 0.85)
        self.assertEqual(len(result["predictions"]), 30)


if __name__ == "__main__":
    unittest.main()
