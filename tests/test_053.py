import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_053 import username_from_email
else:
    try:
        from problems.problem_053 import username_from_email
    except Exception:
        def username_from_email(): return None


class ProblemTests(TestCase):
    def test_simple_name(self):
        input = "noor@hotmail.com"
        expected = "noor"
        result = username_from_email(input)
        self.assertEqual(
            expected,
            result,
            msg=f"For {input} the username is {expected}",
        )

    def test_dotted_name(self):
        input = "zahara.boor@hotmail.com"
        expected = "zahara.boor"
        result = username_from_email(input)
        self.assertEqual(
            expected,
            result,
            msg=f"For {input} the username is {expected}",
        )

    def test_weird_name(self):
        input = "zahara.boor+test-email@hotmail.com"
        expected = "zahara.boor+test-email"
        result = username_from_email(input)
        self.assertEqual(
            expected,
            result,
            msg=f"For {input} the username is {expected}",
        )
