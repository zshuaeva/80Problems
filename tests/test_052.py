from unittest import TestCase

try:
    from problems.problem_052 import generate_lottery_numbers
except Exception:
    def generate_lottery_numbers(): return None


class ProblemTests(TestCase):
    def test_random_and_different(self):
        result1 = generate_lottery_numbers()
        result2 = generate_lottery_numbers()
        self.assertFalse(
            result1 == result2,
            msg="It does not make unique lists of lottery numbers",
        )
        self.assertEqual(
            len(set(result1)),
            6,
            msg="The list did not have all unique numbers",
        )
        self.assertEqual(
            len(set(result2)),
            6,
            msg="The list did not have all unique numbers",
        )
