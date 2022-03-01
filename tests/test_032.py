import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_032 import sum_of_first_n_numbers
else:
    from problems.problem_032 import sum_of_first_n_numbers


class ProblemTests(TestCase):
    def test_negative_number_returns_none(self):
        value = -1
        result = sum_of_first_n_numbers(value)
        self.assertTrue(
            result is None,
            msg=f"The sum of the first {value} numbers should be None",
        )

    def test_zero(self):
        value = 0
        expected = 0
        result = sum_of_first_n_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )

    def test_one(self):
        value = 1
        expected = 1
        result = sum_of_first_n_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )

    def test_three(self):
        value = 3
        expected = 6
        result = sum_of_first_n_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )

    def test_ten(self):
        value = 10
        expected = 55
        result = sum_of_first_n_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )
