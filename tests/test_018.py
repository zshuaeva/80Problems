from unittest import TestCase
from problems.problem_018 import is_palindrome


class ProblemTests(TestCase):
    def test_is_palindrome(self):
        value = is_palindrome("rotator")
        self.assertTrue(value, msg="rotator is a palindrome")

    def test_is_not_palindrome(self):
        value = is_palindrome("unittest")
        self.assertTrue(value is False, msg="python is not a palindrome")
