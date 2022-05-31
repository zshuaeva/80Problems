from unittest import TestCase
from problems.problem_046 import make_sentences


class ProblemTests(TestCase):
    def test_three_one_word_lists(self):
        lists = [["I"], ["like"], ["programming"]]
        expected = ["I like programming"]
        result = make_sentences(*lists)
        self.assertSetEqual(
            set(expected),
            set(result),
            msg=f"The sentences from {lists} should be {expected}",
        )

    def test_two_two_word_and_one_one_word_lists(self):
        lists = [["I", "You"], ["like", "love"], ["programming"]]
        expected = [
            "I like programming",
            "I love programming",
            "You like programming",
            "You love programming",
        ]
        result = make_sentences(*lists)
        self.assertSetEqual(
            set(expected),
            set(result),
            msg=f"The sentences from {lists} should be {expected}",
        )

    def test_more_lists(self):
        lists = [["You"], ["brew", "drink"], ["tea"]]
        expected = ["You brew tea", "You drink tea"]
        result = make_sentences(*lists)
        self.assertSetEqual(
            set(expected),
            set(result),
            msg=f"The sentences from {lists} should be {expected}",
        )

    def test_3x2_lists(self):
        lists = [["I", "You"], ["play", "watch"], ["chess", "cards"]]
        expected = [
            "I play chess",
            "I play cards",
            "I watch chess",
            "I watch cards",
            "You play chess",
            "You play cards",
            "You watch chess",
            "You watch cards",
        ]
        result = make_sentences(*lists)
        self.assertSetEqual(
            set(expected),
            set(result),
            msg=f"The sentences from {lists} should be {expected}",
        )
