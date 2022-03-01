import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_068 import Person
else:
    try:
        from problems.problem_068 import Person
    except Exception:
        class Person:
            pass


class ProblemTests(TestCase):
    def test_person_has_three_parameters(self):
        Person("", [], [])

    def test_person_tastes_normal_things(self):
        person = Person("Kim", [], [])
        result = person.taste("tofu")
        self.assertTrue(
            result is None,
            msg="Kim doesn't have an opinion about tofu",
        )

    def test_person_tastes_icky_things(self):
        person = Person("Kim", ["hamburger"], [])
        result = person.taste("hamburger")
        self.assertTrue(
            result is False,
            msg="Kim does not like hamburger",
        )

    def test_person_tastes_yummy_things(self):
        person = Person("Kim", [], ["kale"])
        result = person.taste("kale")
        self.assertTrue(
            result is True,
            msg="Kim likes kale",
        )
