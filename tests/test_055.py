import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_055 import simple_roman
else:
    try:
        from problems.problem_055 import simple_roman
    except Exception:
        def simple_roman(x):
            return None


param_list = [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VII"),
    (9, "IX"),
    (10, "X"),
]


class ProblemTests(TestCase):
    def test_numbers(self):
        for input, expected in param_list:
            result = simple_roman(input)
            self.assertEqual(
                expected,
                result,
                msg=f"For input {input}, expected {expected}",
            )
