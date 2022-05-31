from unittest import TestCase

try:
    from problems.problem_064 import temperature_differences
except Exception:
    def temperature_differences(highs, lows):
        return None


class ProblemTests(TestCase):
    def test_empty_lists(self):
        highs = []
        lows = []
        expected = []
        result = temperature_differences(highs, lows)
        self.assertListEqual(
            expected,
            result,
            msg="Expected the differences {expected}",
        )

    def test_one_item_lists(self):
        highs = [80]
        lows = [50]
        expected = [30]
        result = temperature_differences(highs, lows)
        self.assertListEqual(
            expected,
            result,
            msg="Expected the differences {expected}",
        )

    def test_multi_item_lists(self):
        highs = [100, 20, 70, 10]
        lows = [80, 19, 30, -10]
        expected = [20, 1, 40, 20]
        result = temperature_differences(highs, lows)
        self.assertListEqual(
            expected,
            result,
            msg="Expected the differences {expected}",
        )
