import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_073 import Student
else:
    try:
        from problems.problem_073 import Student
    except Exception:
        class Student:
            pass


class ProblemTests(TestCase):
    def test_student_has_one_parameter(self):
        Student("")

    def test_student_add_score(self):
        student = Student("Kim")
        student.add_score(90)

    def test_student_add_score_get_averate(self):
        expected = 90
        student = Student("Kim")
        student.add_score(90)
        result = student.get_average()
        self.assertEqual(
            expected,
            result,
            msg="Average score of 1 90 score should be 90",
        )

    def test_student_with_no_scores_has_none_average(self):
        student = Student("Kim")
        self.assertIsNone(
            student.get_average(),
            msg="A student with no scores should have a None average",
        )

    def test_student_add_two_scores_get_averate(self):
        expected = 80
        student = Student("Kim")
        student.add_score(90)
        student.add_score(70)
        result = student.get_average()
        self.assertEqual(
            expected,
            result,
            msg="Average score 70 and 90 should be 80",
        )
