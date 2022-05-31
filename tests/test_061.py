from unittest import TestCase

try:
    from problems.problem_061 import remove_duplicates
except Exception:
    def remove_duplicates(x):
        return None


class ProblemTests(TestCase):
    def test_empty_list(self):
        input = []
        expected = []
        result = remove_duplicates(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )

    def test_all_unique_numbers(self):
        input = [11, 13, 21, 31, 9, 5]
        expected = [11, 13, 21, 31, 9, 5]
        result = remove_duplicates(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )

    def test_all_duplicate_numbers(self):
        input = [12, 11, 13, 11, 13, 12]
        expected = [12, 11, 13]
        result = remove_duplicates(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )

    def test_mix(self):
        input = [1, 3, 3, 3, 3, 1, 12, 1, 2, 3, 3, 1, 2]
        expected = [1, 3, 12, 2]
        result = remove_duplicates(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"Expected {expected} from input {input}",
        )
