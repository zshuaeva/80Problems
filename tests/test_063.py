from unittest import TestCase

try:
    from problems.problem_063 import shift_letters
except Exception:
    def shift_letters(s):
        return None


class ProblemTests(TestCase):
    def test_empty_string(self):
        input = ""
        expected = ""
        result = shift_letters(input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )

    def test_noor(self):
        input = "Noor"
        expected = "Opps"
        result = shift_letters(input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )

    def test_Zahara(self):
        input = "Zahara"
        expected = "Abibsb"
        result = shift_letters(input)
        self.assertEqual(
            expected,
            result,
            msg=f"Expected {expected} for input {input}",
        )
