import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_017 import is_inside_bounds
else:
    from problems.problem_017 import is_inside_bounds


class ProblemTests(TestCase):
    def test_is_inside_bounds(self):
        value = is_inside_bounds(5, 5, 2, 3, 4, 4)
        self.assertTrue(
            value is True,
            msg="5, 5 is inside the bounds of (2, 3) x (6, 7)",
        )

    def test_is_too_far_up(self):
        value = is_inside_bounds(0, 0, -1, 4, 4, 4)
        self.assertTrue(
            value is False,
            msg="0, 0 is outside the bounds of (-1, 4) x (3, 8)",
        )

    def test_is_too_far_down(self):
        value = is_inside_bounds(0, 10, -1, 4, 4, 3)
        self.assertTrue(
            value is False,
            msg="0, 10 is outside the bounds of (-1, 4) x (3, 7)",
        )

    def test_is_too_far_left(self):
        value = is_inside_bounds(5, 5, 10, 4, 4, 3)
        self.assertTrue(
            value is False,
            msg="5, 5 is outside the bounds of (10, 4) x (14, 7)",
        )

    def test_is_too_far_right(self):
        value = is_inside_bounds(5, 5, -4, 4, 4, 3)
        self.assertTrue(
            value is False,
            msg="5, 5 is outside the bounds of (-4, 4) x (0, 7)",
        )
