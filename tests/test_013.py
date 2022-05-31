from unittest import TestCase
from problems.problem_013 import can_make_pasta


class ProblemTests(TestCase):
    def test_can_make_pasta_with_flour_eggs_and_oil(self):
        value = can_make_pasta(["flour", "eggs", "oil"])
        self.assertTrue(value, msg="All the ingredients are there!")

    def test_can_make_pasta_with_oil_flour_and_eggs(self):
        value = can_make_pasta(["oil", "flour", "eggs"])
        self.assertTrue(value, msg="All the ingredients are there!")

    def test_can_make_pasta_with_eggs_flour_and_oil(self):
        value = can_make_pasta(["eggs", "flour", "oil"])
        self.assertTrue(value, msg="All the ingredients are there!")

    def test_cannot_make_pasts_without_flour(self):
        value = can_make_pasta(["eggs", "salt", "oil"])
        self.assertTrue(value is False, msg="You're missing flour")

    def test_cannot_make_pasts_without_oil(self):
        value = can_make_pasta(["eggs", "flour", "salt"])
        self.assertTrue(value is False, msg="You're missing oil")

    def test_cannot_make_pasts_without_eggs(self):
        value = can_make_pasta(["salt", "flour", "oil"])
        self.assertTrue(value is False, msg="You're missing oil")
