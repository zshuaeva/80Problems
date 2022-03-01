import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_012 import fizzbuzz
else:
    from problems.problem_012 import fizzbuzz


class ProblemTests(TestCase):
    def test_divisible_by_3_and_5(self):
        value = fizzbuzz(30)
        self.assertEqual("fizzbuzz", value, msg="30 is divisible by 5 and 3")

    def test_divisible_by_5(self):
        value = fizzbuzz(10)
        self.assertEqual("buzz", value, msg="10 is divisible by 5")

    def test_divisible_by_3(self):
        value = fizzbuzz(6)
        self.assertEqual("fizz", value, msg="6 is divisible by 3")

    def test_is_not_divisible_by_3_nor_5(self):
        value = fizzbuzz(19)
        self.assertEqual(19, value, msg="19 is not divisible by 5")
