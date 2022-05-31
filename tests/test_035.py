from unittest import TestCase
from problems.problem_035 import count_letters_and_digits


class ProblemTests(TestCase):
    def test_empty_string_has_no_letters_and_no_digits(self):
        value = ""
        expected_letters = 0
        expected_digits = 0
        num_letters, num_digits = count_letters_and_digits(value)
        self.assertEqual(
            num_letters,
            expected_letters,
            msg=f"The expected number of letters in {value} is {expected_letters}",
        )
        self.assertEqual(
            num_digits,
            expected_digits,
            msg=f"The expected number of digits in {value} is {expected_digits}",
        )

    def test_alpha_string_has_only_letters_and_no_digits(self):
        value = "abcde abcde"
        expected_letters = 10
        expected_digits = 0
        num_letters, num_digits = count_letters_and_digits(value)
        self.assertEqual(
            num_letters,
            expected_letters,
            msg=f"The expected number of letters in {value} is {expected_letters}",
        )
        self.assertEqual(
            num_digits,
            expected_digits,
            msg=f"The expected number of digits in {value} is {expected_digits}",
        )

    def test_numerical_string_has_only_letters_and_no_digits(self):
        value = "1 2 3 4 5 6"
        expected_letters = 0
        expected_digits = 6
        num_letters, num_digits = count_letters_and_digits(value)
        self.assertEqual(
            num_letters,
            expected_letters,
            msg=f"The expected number of letters in {value} is {expected_letters}",
        )
        self.assertEqual(
            num_digits,
            expected_digits,
            msg=f"The expected number of digits in {value} is {expected_digits}",
        )

    def test_alnum_string_has_only_letters_and_no_digits(self):
        value = "1a 2b 3 4c 5d 6e"
        expected_letters = 5
        expected_digits = 6
        num_letters, num_digits = count_letters_and_digits(value)
        self.assertEqual(
            num_letters,
            expected_letters,
            msg=f"The expected number of letters in {value} is {expected_letters}",
        )
        self.assertEqual(
            num_digits,
            expected_digits,
            msg=f"The expected number of digits in {value} is {expected_digits}",
        )
