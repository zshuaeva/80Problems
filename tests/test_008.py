import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_008 import is_palindrome
else:
    from problems.problem_008 import is_palindrome


class ProblemTests(TestCase):
    def test_is_palindrome(self):
        value = is_palindrome("rotator")
        self.assertTrue(value, msg="rotator is a palindrome")

    def test_is_not_palindrome(self):
        value = is_palindrome("unittest")
        self.assertTrue(value is False, msg="python is not a palindrome")
