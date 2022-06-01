from unittest import TestCase

try:
    from problems.problem_081 import Dog, Cat, Snake
except Exception:
    class Dog:
        pass
    class Cat:
        pass
    class Snake:
        pass


class ProblemTests(TestCase):
    def test_dog_says_bark(self):
        self.assertEqual(
            "Bark!",
            Dog(4, "brown").speak(),
            msg="Dog should say 'Bark!'",
        )

    def test_cat_says_miao(self):
        self.assertEqual(
            "Miao!",
            Cat(4, "brown").speak(),
            msg="Cat should say 'Miao!'",
        )

    def test_snake_says_sssss(self):
        self.assertEqual(
            "Sssssss!",
            Snake(0, "brown").speak(),
            msg="Snake should say 'Sssssss!'",
        )

    def test_dog_is_described(self):
        self.assertEqual(
            "Dog has 4 legs and is primarily brown",
            Dog(4, "brown").describe(),
            msg="Dog has 4 legs and is primarily brown",
        )

    def test_cat_is_described(self):
        self.assertEqual(
            "Cat has 4 legs and is primarily orange",
            Cat(4, "orange").describe(),
            msg="Cat has 4 legs and is primarily orange",
        )

    def test_snake_is_described(self):
        self.assertEqual(
            "Snake has 0 legs and is primarily green",
            Snake(0, "green").describe(),
            msg="Snake has 0 legs and is primarily green",
        )
