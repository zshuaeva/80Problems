import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_020 import has_quorum
else:
    from problems.problem_020 import has_quorum


class ProblemTests(TestCase):
    def test_quorum_exists_when_everyone_is_there(self):
        members = ["Basia", "Noor", "Laila", "Talia", "Zahara"]
        present = ["Basia", "Noor", "Laila", "Talia", "Zahara"]
        value = has_quorum(present, members)
        self.assertTrue(
            value is True,
            msg="Everyone is present. That is a quorum.",
        )

    def test_quorum_exists_when_80_percent_there(self):
        members = ["Basia", "Noor", "Laila", "Talia", "Zahara"]
        present = ["Basia", "Noor", "Laila", "Zahara"]
        value = has_quorum(present, members)
        self.assertTrue(
            value is True,
            msg="80% of the people are there. That is a quorum.",
        )

    def test_quorum_exists_when_60_percent_there(self):
        members = ["Basia", "Noor", "Laila", "Talia", "Zahara"]
        present = ["Noor", "Laila", "Zahara"]
        value = has_quorum(present, members)
        self.assertTrue(
            value is True,
            msg="60% of the people are there. That is a quorum.",
        )

    def test_quorum_does_not_exist_when_40_percent_there(self):
        members = ["Basia", "Noor", "Laila", "Talia", "Zahara"]
        present = ["Basia", "Noor"]
        value = has_quorum(present, members)
        self.assertTrue(
            value is False,
            msg="40% of the people are there. That is not a quorum.",
        )

    def test_quorum_does_not_exist_when_20_percent_there(self):
        members = ["Basia", "Noor", "Laila", "Talia", "Zahara"]
        present = ["Noor"]
        value = has_quorum(present, members)
        self.assertTrue(
            value is False,
            msg="20% of the people are there. That is not a quorum.",
        )

    def test_quorum_does_not_exist_when_no_one_is_there(self):
        members = ["Basia", "Noor", "Laila", "Talia", "Zahara"]
        present = []
        value = has_quorum(present, members)
        self.assertTrue(
            value is False,
            msg="0% of the people are there. That is not a quorum.",
        )

    def test_quorum_does_not_exist_when_exactly_half_are_there(self):
        members = ["Basia", "Noor", "Laila", "Talia"]
        present = ["Basia", "Laila"]
        value = has_quorum(present, members)
        self.assertTrue(
            value is True,
            msg="50% of the people are there. That is a quorum.",
        )
