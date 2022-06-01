from unittest import TestCase
from problems.problem_026 import calculate_grade


class ProblemTests(TestCase):
    def test_empty_list_returns_none(self):
        values = []
        result = calculate_grade(values)
        self.assertTrue(
            result is None,
            msg="The grade of an empty list should be None",
        )

    def test_can_calculate_A(self):
        values = [90]
        expected = "A"
        result = calculate_grade(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The grade for {values} should be {expected}",
        )

    def test_can_calculate_F(self):
        values = [80, 30]
        expected = "F"
        result = calculate_grade(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The grade for {values} should be {expected}",
        )

    def test_can_calculate_C(self):
        values = [80, 80, 80, 79, 78]
        expected = "C"
        result = calculate_grade(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The grade for {values} should be {expected}",
        )

    def test_can_calculate_D(self):
        values = [61, 62, 63, 64, 65, 66]
        expected = "D"
        result = calculate_grade(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The grade for {values} should be {expected}",
        )

    def test_can_calculate_B(self):
        values = [99, 80, 99, 80, 99, 80]
        expected = "B"
        result = calculate_grade(values)
        self.assertEqual(
            expected,
            result,
            msg=f"The grade for {values} should be {expected}",
        )
