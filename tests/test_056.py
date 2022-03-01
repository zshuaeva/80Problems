import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_056 import num_concat
else:
    try:
        from problems.problem_056 import num_concat
    except Exception:
        def num_concat(x, y):
            return None


class ProblemTests(TestCase):
    def test_concat(self):
        left = 123
        right = 981
        expected = "123981"
        result = num_concat(left, right)
        self.assertEqual(
            expected,
            result,
            msg="Expected \"123981\" for numbers 123 and 981",
        )
