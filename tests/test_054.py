import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_054 import check_input
else:
    try:
        from problems.problem_054 import check_input
    except Exception:
        def check_input(x): return None


class ProblemTests(TestCase):
    def test_throws_for_input(self):
        msg = "Expected ValueError for input 'raise'"
        with self.assertRaises(ValueError, msg=msg):
            check_input("raise")

    def test_returns_input_otherwise(self):
        input = "whatever"
        result = check_input(input)
        self.assertEqual(
            input,
            result,
            msg=f"Expected result {result} for input {input}",
        )
