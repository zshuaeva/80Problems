import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_010 import is_divisible_by_3
else:
    from problems.problem_010 import is_divisible_by_3


class ProblemTests(TestCase):
    def test_divisible_by_3(self):
        value = is_divisible_by_3(6)
        self.assertEqual("fizz", value, msg="6 is divisible by 3")

    def test_is_not_divisible_by_3(self):
        value = is_divisible_by_3(7)
        self.assertEqual(7, value, msg="7 is not divisible by 3")
