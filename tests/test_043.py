import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_043 import find_indexes
else:
    from problems.problem_043 import find_indexes


class ProblemTests(TestCase):
    def test_empty_lists(self):
        search_list = []
        search_value = 1
        expected = []
        result = find_indexes(search_list, search_value)
        self.assertListEqual(
            expected,
            result,
            msg=f"The indexes of {search_value} in {search_list} should be {expected}",
        )

    def test_no_occurrences(self):
        search_list = [100, 9, 100, 100, 9, 100]
        search_value = 1
        expected = []
        result = find_indexes(search_list, search_value)
        self.assertListEqual(
            expected,
            result,
            msg=f"The indexes of {search_value} in {search_list} should be {expected}",
        )

    def test_many_occurrences(self):
        search_list = [100, 9, 100, 100, 9, 100]
        search_value = 100
        expected = [0, 2, 3, 5]
        result = find_indexes(search_list, search_value)
        self.assertListEqual(
            expected,
            result,
            msg=f"The indexes of {search_value} in {search_list} should be {expected}",
        )

    def test_one_occurrence(self):
        search_list = [100, 9, 100, 100, 100, 100]
        search_value = 9
        expected = [1]
        result = find_indexes(search_list, search_value)
        self.assertListEqual(
            expected,
            result,
            msg=f"The indexes of {search_value} in {search_list} should be {expected}",
        )
