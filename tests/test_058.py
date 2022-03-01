import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_058 import group_cities_by_state
else:
    try:
        from problems.problem_058 import group_cities_by_state
    except Exception:
        def group_cities_by_state(x):
            return None


class ProblemTests(TestCase):
    def test_empty_list(self):
        input = []
        expected = {}
        result = group_cities_by_state(input)
        self.assertDictEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )

    def test_discrete_states(self):
        input = ["New York, NY", "San Jose, CA", "Portland, OR"]
        expected = {
            "NY": ["New York"],
            "CA": ["San Jose"],
            "OR": ["Portland"],
        }
        result = group_cities_by_state(input)
        self.assertDictEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )

    def test_common_states(self):
        input = ["Seattle, WA", "Olympia, WA", "Topeka, KS", "Wichita, KS"]
        expected = {
            "WA": ["Seattle", "Olympia"],
            "KS": ["Topeka", "Wichita"],
        }
        result = group_cities_by_state(input)
        self.assertDictEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )
