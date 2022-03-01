import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_038 import reverse_dictionary
else:
    from problems.problem_038 import reverse_dictionary


class ProblemTests(TestCase):
    def test_empty_dictionary(self):
        input = {}
        expected = {}
        result = reverse_dictionary(input)
        self.assertDictEqual(
            expected,
            result,
            msg=f"The reverse of {input} should be {expected}",
        )

    def test_one_item_dictionary(self):
        input = {"key": "value"}
        expected = {"value": "key"}
        result = reverse_dictionary(input)
        self.assertDictEqual(
            expected,
            result,
            msg=f"The reverse of {input} should be {expected}",
        )

    def test_many_item_dictionary(self):
        input = {"key1": 1, "key2": 2, "key3": 100}
        expected = {1: "key1", 2: "key2", 100: "key3"}
        result = reverse_dictionary(input)
        self.assertDictEqual(
            expected,
            result,
            msg=f"The reverse of {input} should be {expected}",
        )
