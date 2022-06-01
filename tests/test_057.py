from unittest import TestCase

try:
    from problems.problem_057 import sum_fraction_sequence
except Exception:
    def sum_fraction_sequence(x):
        return None


class ProblemTests(TestCase):
    def test_one(self):
        input = 1
        expected = 1/2
        result = sum_fraction_sequence(input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )

    def test_two(self):
        input = 2
        expected = (1/2) + (2/3)
        result = sum_fraction_sequence(input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )

    def test_three(self):
        input = 3
        expected = 1/2 + 2/3 + 3/4
        result = sum_fraction_sequence(input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )

    def test_five(self):
        input = 5
        expected = 1/2 + 2/3 + 3/4 + 4/5 + 5/6
        result = sum_fraction_sequence(input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )
