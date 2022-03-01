import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_066 import Book
else:
    try:
        from problems.problem_066 import Book
    except Exception:
        class Book:
            pass


class ProblemTests(TestCase):
    def test_book_has_author_and_title(self):
        Book("", "")

    def test_book_get_author(self):
        book = Book("Zahara", "My Trip Abroad")
        self.assertEqual(
            "Author: Zahara",
            book.get_author(),
            msg="Expected get_author to return 'Author: Zahara'",
        )

    def test_book_get_title(self):
        book = Book("Zahara", "My Trip Abroad")
        self.assertEqual(
            "Title: My Trip Abroad",
            book.get_title(),
            msg="Expected get_title to return 'Title: My Trip Abroad'",
        )
