import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_016 import is_inside_bounds
else:
    from problems.problem_016 import is_inside_bounds


class ProblemTests(TestCase):
    def test_is_inside_bounds(self):
        value = is_inside_bounds(5, 5)
        self.assertTrue(value, "5, 5 is inside the bounds")

    def test_is_too_far_up(self):
        value = is_inside_bounds(5, -1)
        self.assertTrue(value is False, "5, -1 is outside the bounds")

    def test_is_too_far_down(self):
        value = is_inside_bounds(5, 11)
        self.assertTrue(value is False, "5, 11 is outside the bounds")

    def test_is_too_far_left(self):
        value = is_inside_bounds(-5, 5)
        self.assertTrue(value is False, "-5, 5 is outside the bounds")

    def test_is_too_far_right(self):
        value = is_inside_bounds(5, 12)
        self.assertTrue(value is False, "5, 12 is outside the bounds")
