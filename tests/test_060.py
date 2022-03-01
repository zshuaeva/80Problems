from cmath import exp
import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_060 import only_odds
else:
    try:
        from problems.problem_060 import only_odds
    except Exception:
        def only_odds(x):
            return None


class ProblemTests(TestCase):
    def test_empty_list(self):
        input = []
        expected = []
        result = only_odds(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )

    def test_all_odd_numbers(self):
        input = [11, 13, 21, 31, 9, 5]
        expected = [11, 13, 21, 31, 9, 5]
        result = only_odds(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )

    def test_all_even_numbers(self):
        input = [12, 34, 98, 10, 2]
        expected = []
        result = only_odds(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )

    def test_mix(self):
        input = [12, 34, 11, 13, 21, 31, 9, 5, 98, 10, 2]
        expected = [11, 13, 21, 31, 9, 5]
        result = only_odds(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )
