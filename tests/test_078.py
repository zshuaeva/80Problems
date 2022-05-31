import math
from unittest import TestCase

try:
    from problems.problem_078 import Circle
except Exception:
    class Circle:
        pass


class ProblemTests(TestCase):
    def test_circle_has_radius_parameter(self):
        Circle(0)

    def test_circle_cannot_have_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_circle_can_calculate_its_perimeter(self):
        circle = Circle(3)
        expected = 2 * math.pi * 3
        self.assertEqual(
            expected,
            circle.calculate_perimeter(),
            msg=f"Expected circle with radius 3 to have perimeter {expected}",
        )

    def test_circle_can_calculate_its_area(self):
        circle = Circle(3)
        expected = math.pi * 9
        self.assertEqual(
            expected,
            circle.calculate_area(),
            msg=f"Expected circle with radius 3 to have area {expected}",
        )
