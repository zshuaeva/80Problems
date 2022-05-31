from unittest import TestCase
from problems.problem_036 import pad_left


class ProblemTests(TestCase):
    def test_single_digit_to_five_characters_with_0_pad(self):
        value = 1
        length = 5
        pad = "0"
        expected = "00001"
        result = pad_left(value, length, pad)
        self.assertEqual(
            expected,
            result,
            msg=f"Padding {value} to width {length} with {pad} should create {expected}",
        )

    def test_single_digit_to_five_characters_with_space_pad(self):
        value = 1
        length = 5
        pad = " "
        expected = "    1"
        result = pad_left(value, length, pad)
        self.assertEqual(
            expected,
            result,
            msg=f"Padding {value} to width {length} with {pad} should create {expected}",
        )

    def test_three_digit_to_two_characters_with_space_pad(self):
        value = 100
        length = 2
        pad = " "
        expected = "100"
        result = pad_left(value, length, pad)
        self.assertEqual(
            expected,
            result,
            msg=f"Padding {value} to width {length} with {pad} should create {expected}",
        )

    def test_three_digit_to_six_characters_with_dot_pad(self):
        value = 100
        length = 6
        pad = "."
        expected = "...100"
        result = pad_left(value, length, pad)
        self.assertEqual(
            expected,
            result,
            msg=f"Padding {value} to width {length} with {pad} should create {expected}",
        )
