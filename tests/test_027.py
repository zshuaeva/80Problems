from unittest import TestCase
from problems.problem_027 import max_in_list


class ProblemTests(TestCase):
    def test_empty_list_returns_none(self):
        values = []
        result = max_in_list(values)
        self.assertTrue(
            result is None,
            msg="The maximum value of an empty list should be None",
        )

    def test_can_find_max_in_list_of_one(self):
        values = [10]
        expected = 10
        result = max_in_list(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The max value of {values} should be {expected}",
        )

    def test_can_find_max_in_list_of_two(self):
        values = [10, 3]
        expected = 10
        result = max_in_list(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The max value of {values} should be {expected}",
        )

    def test_can_find_max_in_list_of_three(self):
        values = [10, 3, 18]
        expected = 18
        result = max_in_list(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The max value of {values} should be {expected}",
        )

    def test_can_find_max_in_list_of_four(self):
        values = [20, 10, 3, 18]
        expected = 20
        result = max_in_list(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The max value of {values} should be {expected}",
        )

    def test_can_find_max_in_list_of_five(self):
        values = [20, 100, 10, 3, 18]
        expected = 100
        result = max_in_list(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The max value of {values} should be {expected}",
        )
