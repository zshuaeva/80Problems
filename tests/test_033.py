from unittest import TestCase
from problems.problem_033 import sum_of_first_n_even_numbers


class ProblemTests(TestCase):
    def test_negative_number_returns_none(self):
        value = -1
        result = sum_of_first_n_even_numbers(value)
        self.assertTrue(
            result is None,
            msg=f"The sum of the first {value} even numbers should be None",
        )

    def test_zero(self):
        value = 0
        expected = 0
        result = sum_of_first_n_even_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )

    def test_one(self):
        value = 1
        expected = 2
        result = sum_of_first_n_even_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )

    def test_three(self):
        value = 3
        expected = 12
        result = sum_of_first_n_even_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )

    def test_ten(self):
        value = 10
        expected = 110
        result = sum_of_first_n_even_numbers(value)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of the first {value} numbers should be {expected}",
        )
