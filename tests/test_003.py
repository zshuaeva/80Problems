import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_003 import max_of_three
else:
    from problems.problem_003 import max_of_three


class ProblemTests(TestCase):
    def test_returns_max_value_if_first_parameter(self):
        value = max_of_three(9, 8, 7)
        self.assertEqual(9, value)

    def test_returns_max_value_if_second_parameter(self):
        value = max_of_three(1, 7, 3)
        self.assertEqual(7, value)

    def test_returns_max_value_if_third_parameter(self):
        value = max_of_three(1, 2, 3)
        self.assertEqual(3, value)

    def test_returns_max_value_if_equal_parameters_1(self):
        value = max_of_three(8, 8, 7)
        self.assertEqual(8, value)

    def test_returns_max_value_if_equal_parameters_2(self):
        value = max_of_three(4, 6, 6)
        self.assertEqual(6, value)

    def test_returns_max_value_if_equal_parameters_3(self):
        value = max_of_three(7, 2, 7)
        self.assertEqual(7, value)

    def test_returns_max_value_if_all_equal_parameters(self):
        value = max_of_three(3, 3, 3)
        self.assertEqual(3, value)
