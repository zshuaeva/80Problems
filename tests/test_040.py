from unittest import TestCase
from problems.problem_040 import add_csv_lines


class ProblemTests(TestCase):
    def test_empty_list(self):
        input = []
        expected = []
        result = add_csv_lines(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"The total of {input} should be {expected}",
        )

    def test_one_line_list(self):
        input = [
            "1,2,10"
        ]
        expected = [13]
        result = add_csv_lines(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"The total of {input} should be {expected}",
        )

    def test_many_item_dictionary(self):
        input = [
            "1,2,10",
            "3",
            "100,1,3"
        ]
        expected = [13, 3, 104]
        result = add_csv_lines(input)
        self.assertListEqual(
            expected,
            result,
            msg=f"The total of {input} should be {expected}",
        )
