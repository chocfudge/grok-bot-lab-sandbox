import unittest

from src.health import classify_load


class LoadClassificationTests(unittest.TestCase):
    def test_low_load_is_ok(self):
        self.assertEqual(classify_load(20), "OK")

    def test_boundary_is_ok(self):
        self.assertEqual(classify_load(80), "OK")

    def test_high_load_is_degraded(self):
        self.assertEqual(classify_load(81), "DEGRADED")

    def test_invalid_load_raises(self):
        with self.assertRaises(ValueError):
            classify_load(101)


if __name__ == "__main__":
    unittest.main()
