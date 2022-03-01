import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_030 import find_second_largest
else:
    from problems.problem_030 import find_second_largest


class ProblemTests(TestCase):
    def test_empty_list_returns_none(self):
        values = []
        result = find_second_largest(values)
        self.assertTrue(
            result is None,
            msg="The second largest of an empty list should be None",
        )

    def test_list_of_one_item_returns_none(self):
        values = [10]
        result = find_second_largest(values)
        self.assertTrue(
            result is None,
            msg="The second largest of an empty list should be None",
        )

    def test_two_value_list_calculates_average(self):
        values = [10, 20]
        expected = 10
        result = find_second_largest(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The second largest of {values} should be {expected}",
        )

    def test_seven_value_list_calculates_average(self):
        values = [50, 15, 10, 10, 10, 20, 100]
        expected = 50
        result = find_second_largest(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The second largest of {values} should be {expected}",
        )
