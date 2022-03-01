import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_022 import gear_for_day
else:
    from problems.problem_022 import gear_for_day


class ProblemTests(TestCase):
    def test_gear_on_cloudy_workday(self):
        value = gear_for_day(True, False)
        self.assertTrue(
            "laptop" in value,
            msg="You need your laptop on a workday",
        )
        self.assertTrue(
            "umbrella" in value,
            msg="You need an umbrella on a cloudy day",
        )
        self.assertFalse(
            "surfboard" in value,
            msg="It's a workday, no time for surfing",
        )

    def test_gear_on_sunny_workday(self):
        value = gear_for_day(True, True)
        self.assertTrue(
            "laptop" in value,
            msg="You need your laptop on a workday",
        )
        self.assertFalse(
            "umbrella" in value,
            msg="Not a cloud in the sky, no need for that umbrella",
        )
        self.assertFalse(
            "surfboard" in value,
            msg="It's a workday, no time for surfing",
        )

    def test_gear_on_cloudy_weekend(self):
        value = gear_for_day(False, False)
        self.assertFalse(
            "laptop" in value,
            msg="It's not a workday, you don't need your laptop",
        )
        self.assertFalse(
            "umbrella" in value,
            msg="It's not a workday, you don't need your umbrella",
        )
        self.assertTrue(
            "surfboard" in value,
            msg="It's a workday, surf's up!",
        )

    def test_gear_on_sunny_weekend(self):
        value = gear_for_day(False, False)
        self.assertFalse(
            "laptop" in value,
            msg="It's not a workday, you don't need your laptop",
        )
        self.assertFalse(
            "umbrella" in value,
            msg="It's not a workday, you don't need your umbrella",
        )
        self.assertTrue(
            "surfboard" in value,
            msg="It's a workday, surf's up!",
        )
