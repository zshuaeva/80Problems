import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_059 import specific_random
else:
    try:
        from problems.problem_059 import specific_random
    except Exception:
        def specific_random():
            return None


class ProblemTests(TestCase):
    def test_values(self):
        first = specific_random()
        self.assertTrue(
            first % 5 == 0,
            msg="Number is not divisible by 5",
        )
        self.assertTrue(
            first % 7 == 0,
            msg="Number is not divisible by 7",
        )
        self.assertGreaterEqual(
            first,
            10,
            msg="Number is not greater than or equal to 10",
        )
        self.assertLessEqual(
            first,
            500,
            msg="Number is not less than or equal to 500",
        )
