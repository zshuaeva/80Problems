import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_011 import is_divisible_by_5
else:
    from problems.problem_011 import is_divisible_by_5


class ProblemTests(TestCase):
    def test_divisible_by_5(self):
        value = is_divisible_by_5(10)
        self.assertEqual("buzz", value, msg="10 is divisible by 5")

    def test_is_not_divisible_by_5(self):
        value = is_divisible_by_5(7)
        self.assertEqual(7, value, msg="7 is not divisible by 5")
