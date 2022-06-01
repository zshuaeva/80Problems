from unittest import TestCase
from problems.problem_031 import sum_of_squares


class ProblemTests(TestCase):
    def test_empty_list_returns_none(self):
        values = []
        result = sum_of_squares(values)
        self.assertTrue(
            result is None,
            msg="The sum of the squares of an empty list should be None",
        )

    def test_two_value_list_calculates_average(self):
        values = [10, 20]
        expected = 500
        result = sum_of_squares(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the squares of {values} should be {expected}",
        )

    def test_seven_value_list_calculates_average(self):
        values = [1, 2, 3, 4, 5]
        expected = 55
        result = sum_of_squares(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the squares of {values} should be {expected}",
        )
