from unittest import TestCase
from problems.problem_028 import remove_duplicate_letters


class ProblemTests(TestCase):
    def test_empty_string_returns_empty_string(self):
        value = ""
        expected = ""
        result = remove_duplicate_letters(value)
        self.assertEqual(
            expected,
            result,
            msg=f"With all duplicates removed, {value} should be {expected}",
        )

    def test_string_with_unique_letters_is_the_same(self):
        value = "abcdefg"
        expected = "abcdefg"
        result = remove_duplicate_letters(value)
        self.assertEqual(
            expected,
            result,
            msg=f"With all duplicates removed, {value} should be {expected}",
        )

    def test_string_with_all_same_letters_returns_single_letter(self):
        value = "aaaaaaaaaaaaaaaaa"
        expected = "a"
        result = remove_duplicate_letters(value)
        self.assertEqual(
            expected,
            result,
            msg=f"With all duplicates removed, {value} should be {expected}",
        )

    def test_string_with_various_things_removes_duplicates(self):
        value = "akdlsidjalfkajdladksj"
        expected = "akdlsijf"
        result = remove_duplicate_letters(value)
        self.assertEqual(
            expected,
            result,
            msg=f"With all duplicates removed, {value} should be {expected}",
        )
