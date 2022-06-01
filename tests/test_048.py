from unittest import TestCase

try:
    from problems.problem_048 import count_word_frequencies
except Exception:
    def count_word_frequencies(sentence): return None


class ProblemTests(TestCase):
    def test_empty_string(self):
        sentence = ""
        expected = {}
        result = count_word_frequencies(sentence)
        self.assertDictEqual(
            expected,
            result,
            msg=f"The expected word count for {sentence} is {expected}"
        )

    def test_unique_words(self):
        sentence = "veni vidi didici"
        expected = {"veni": 1, "vidi": 1, "didici": 1}
        result = count_word_frequencies(sentence)
        self.assertDictEqual(
            expected,
            result,
            msg=f"The expected word count for {sentence} is {expected}"
        )

    def test_repeated_words(self):
        sentence = "I came I saw I learned"
        expected = {"I": 3, "came": 1, "saw": 1, "learned": 1}
        result = count_word_frequencies(sentence)
        self.assertDictEqual(
            expected,
            result,
            msg=f"The expected word count for {sentence} is {expected}"
        )

    def test_all_repeated_words(self):
        sentence = "Hey Hey Hey Hey"
        expected = {"Hey": 4}
        result = count_word_frequencies(sentence)
        self.assertDictEqual(
            expected,
            result,
            msg=f"The expected word count for {sentence} is {expected}"
        )
