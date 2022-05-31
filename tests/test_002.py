from unittest import TestCase
from problems.problem_002 import minimum_value


class ProblemTests(TestCase):
    def test_returns_min_value_if_first_parameter(self):
        value = minimum_value(1, 3)
        self.assertEqual(1, value)

    def test_returns_min_value_if_second_parameter(self):
        value = minimum_value(3, 2)
        self.assertEqual(2, value)

    def test_returns_value_if_equal_parameters(self):
        value = minimum_value(3, 3)
        self.assertEqual(3, value)
