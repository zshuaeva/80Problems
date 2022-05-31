from unittest import TestCase

try:
    from problems.problem_062 import basic_calculator
except Exception:
    def remove_duplicates(x, y, z):
        return None


class ProblemTests(TestCase):
    def test_addition(self):
        input = (3, "+", 2)
        expected = 5
        result = basic_calculator(*input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} from inputs {input[0]}, {input[1]}, {input[2]}",
        )

    def test_subtraction(self):
        input = (3, "-", 2)
        expected = 1
        result = basic_calculator(*input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} from inputs {input[0]}, {input[1]}, {input[2]}",
        )

    def test_multiplication(self):
        input = (3, "*", 2)
        expected = 6
        result = basic_calculator(*input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} from inputs {input[0]}, {input[1]}, {input[2]}",
        )

    def test_division(self):
        input = (3, "/", 2)
        expected = 1.5
        result = basic_calculator(*input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} from inputs {input[0]}, {input[1]}, {input[2]}",
        )
