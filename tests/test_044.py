import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_044 import translate
else:
    from problems.problem_044 import translate


class ProblemTests(TestCase):
    def test_empty_list(self):
        keys = []
        dictionary = {"one": 1, "two": 2}
        expected = []
        result = translate(keys, dictionary)
        self.assertListEqual(
            expected,
            result,
            msg=f"The keys {keys} in {dictionary} should be {expected}",
        )

    def test_no_occurrences(self):
        keys = ["three", "four"]
        dictionary = {"one": 1, "two": 2}
        expected = [None, None]
        result = translate(keys, dictionary)
        self.assertListEqual(
            expected,
            result,
            msg=f"The keys {keys} in {dictionary} should be {expected}",
        )

    def test_many_occurrences(self):
        keys = ["one", "one", "two", "three", "two"]
        dictionary = {"one": 1, "two": 2}
        expected = [1, 1, 2, None, 2]
        result = translate(keys, dictionary)
        self.assertListEqual(
            expected,
            result,
            msg=f"The keys {keys} in {dictionary} should be {expected}",
        )

    def test_one_occurrence(self):
        keys = ["three", "one", "four"]
        dictionary = {"one": 1, "two": 2}
        expected = [None, 1, None]
        result = translate(keys, dictionary)
        self.assertListEqual(
            expected,
            result,
            msg=f"The keys {keys} in {dictionary} should be {expected}",
        )
