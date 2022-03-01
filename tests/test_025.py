import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_025 import calculate_sum
else:
    from problems.problem_025 import calculate_sum


class ProblemTests(TestCase):
    def test_empty_list_returns_none(self):
        values = []
        result = calculate_sum(values)
        self.assertTrue(
            result is None,
            msg="The sum of an empty list should be None",
        )

    def test_list_of_one_value_returns_that_value(self):
        values = [10]
        expected = 10
        result = calculate_sum(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of {values} should be {expected}",
        )

    def test_two_value_list_calculates_average(self):
        values = [10, 20]
        expected = 30
        result = calculate_sum(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of {values} should be {expected}",
        )

    def test_five_value_list_calculates_average(self):
        values = [5, 10, 15, 20, 50]
        expected = 100
        result = calculate_sum(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of {values} should be {expected}",
        )
