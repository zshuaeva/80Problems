from unittest import TestCase
from problems.problem_007 import is_palindrome


class ProblemTests(TestCase):
    def test_is_palindrome(self):
        value = is_palindrome("repaper")
        self.assertTrue(value, msg="repaper is a palindrome")

    def test_is_not_palindrome(self):
        value = is_palindrome("unittest")
        self.assertTrue(value is False, msg="unittest is not a palindrome")
