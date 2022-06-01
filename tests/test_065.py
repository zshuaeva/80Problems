from unittest import TestCase

try:
    from problems.problem_065 import biggest_gap
except Exception:
    def biggest_gap(nums):
        return None


class ProblemTests(TestCase):
    def test_two_numbers(self):
        nums = [10, 5]
        expected = 5
        result = biggest_gap(nums)
        self.assertEqual(
            expected,
            result,
            msg="Expected the biggest gap to be {expected} for {nums}",
        )

    def test_three_numbers(self):
        nums = [10, 5, 20]
        expected = 15
        result = biggest_gap(nums)
        self.assertEqual(
            expected,
            result,
            msg="Expected the biggest gap to be {expected} for {nums}",
        )

    def test_many_numbers(self):
        nums = [12, 13, 100, 0, 10, 5]
        expected = 100
        result = biggest_gap(nums)
        self.assertEqual(
            expected,
            result,
            msg="Expected the biggest gap to be {expected} for {nums}",
        )

    def test_other_three_numbers(self):
        nums = [20, 5, 10]
        expected = 15
        result = biggest_gap(nums)
        self.assertEqual(
            expected,
            result,
            msg="Expected the biggest gap to be {expected} for {nums}",
        )

    def test_many_numbers_gap_at_end(self):
        nums = [12, 13, 100, 0, 10, 200]
        expected = 190
        result = biggest_gap(nums)
        self.assertEqual(
            expected,
            result,
            msg="Expected the biggest gap to be {expected} for {nums}",
        )
