import math
from unittest import TestCase

try:
    from problems.problem_051 import safe_divide
except Exception:
    def safe_divide(n, d): return None


class ProblemTests(TestCase):
    def test_zero_denominator(self):
        n = 10
        d = 0
        expected = math.inf
        result = safe_divide(n, d)
        self.assertEqual(
            expected,
            result,
            msg="The result with a zero denominator should be math.inf",
        )

    def test_non_zero_denominator(self):
        n = 10
        d = 2
        expected = 10 / 2
        result = safe_divide(n, d)
        self.assertEqual(
            expected,
            result,
            msg=f"The result of 10 / 2 should be {expected}",
        )
