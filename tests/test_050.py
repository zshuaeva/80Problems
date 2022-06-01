from unittest import TestCase

try:
    from problems.problem_050 import halve_the_list
except Exception:
    def halve_the_list(l): return None


class ProblemTests(TestCase):
    def test_empty_list(self):
        value = []
        expected = [], []
        result = halve_the_list(value)
        self.assertListEqual(
            expected[0],
            result[0],
            msg=f"The first half of the list {value} should be {expected[0]}",
        )
        self.assertListEqual(
            expected[1],
            result[1],
            msg=f"The second half of the list {value} should be {expected[1]}",
        )

    def test_even_list(self):
        value = [1, 2, 3, 4, 5, 6]
        expected = [1, 2, 3], [4, 5, 6]
        result = halve_the_list(value)
        self.assertListEqual(
            expected[0],
            result[0],
            msg=f"The first half of the list {value} should be {expected[0]}",
        )
        self.assertListEqual(
            expected[1],
            result[1],
            msg=f"The second half of the list {value} should be {expected[1]}",
        )

    def test_odd_list(self):
        value = [1, 2, 3, 4, 5]
        expected = [1, 2, 3], [4, 5]
        result = halve_the_list(value)
        self.assertListEqual(
            expected[0],
            result[0],
            msg=f"The first half of the list {value} should be {expected[0]}",
        )
        self.assertListEqual(
            expected[1],
            result[1],
            msg=f"The second half of the list {value} should be {expected[1]}",
        )
