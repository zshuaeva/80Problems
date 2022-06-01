from unittest import TestCase
from problems.problem_047 import check_password


class ProblemTests(TestCase):
    def test_good_password_with_at(self):
        password = "A0z@ac"
        result = check_password(password)
        self.assertTrue(
            result is True,
            msg=f"The password {password} meets all of the requirements."
        )

    def test_good_password_with_dollar_sign(self):
        password = "A0z$ac"
        result = check_password(password)
        self.assertTrue(
            result is True,
            msg=f"The password {password} meets all of the requirements."
        )

    def test_good_password_with_exclamtion_mark(self):
        password = "A0z!ac"
        result = check_password(password)
        self.assertTrue(
            result is True,
            msg=f"The password {password} meets all of the requirements."
        )

    def test_too_short_password(self):
        password = "A0z@"
        result = check_password(password)
        self.assertTrue(
            result is False,
            msg=f"The password {password} is too short."
        )

    def test_too_long_password(self):
        password = "A0z@abcabcabcabcabcabc"
        result = check_password(password)
        self.assertTrue(
            result is False,
            msg=f"The password {password} is too long."
        )

    def test_no_number(self):
        password = "Aaz@ac"
        result = check_password(password)
        self.assertTrue(
            result is False,
            msg=f"The password {password} has no number."
        )

    def test_has_no_capital_letter(self):
        password = "a0z@ac"
        result = check_password(password)
        self.assertTrue(
            result is False,
            msg=f"The password {password} has no uppercase letter."
        )

    def test_has_no_lowercase_letter(self):
        password = "A0Z@AC"
        result = check_password(password)
        self.assertTrue(
            result is False,
            msg=f"The password {password} has no lowercase letter."
        )

    def test_has_no_special_character(self):
        password = "A0z1ac"
        result = check_password(password)
        self.assertTrue(
            result is False,
            msg=f"The password {password} has no special character."
        )
