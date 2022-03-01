import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_042 import pairwise_add
else:
    from problems.problem_042 import pairwise_add


class ProblemTests(TestCase):
    def test_empty_lists(self):
        inputs = [], []
        expected = []
        result = pairwise_add(*inputs)
        self.assertListEqual(
            expected,
            result,
            msg=f"The pairwise sums of {input} should be {expected}",
        )

    def test_one_element_lists(self):
        inputs = [3], [8]
        expected = [11]
        result = pairwise_add(*inputs)
        self.assertListEqual(
            expected,
            result,
            msg=f"The pairwise sums of {input} should be {expected}",
        )

    def test_three_element_lists(self):
        inputs = [3, 1, 1000], [8, 1010, 9]
        expected = [11, 1011, 1009]
        result = pairwise_add(*inputs)
        self.assertListEqual(
            expected,
            result,
            msg=f"The pairwise sums of {input} should be {expected}",
        )
