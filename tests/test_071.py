from unittest import TestCase

try:
    from problems.problem_071 import Employee
except Exception:
    class Employee:
        pass


class ProblemTests(TestCase):
    def test_employee_has_two_parameters(self):
        Employee("", "")

    def test_employee_get_fullname(self):
        o = Employee("Lulu", "Zadig")
        expected = "Lulu Zadig"
        self.assertEqual(
            expected,
            o.get_fullname(),
            msg="Expected fullname to be {expected}",
        )

    def test_employee_email(self):
        o = Employee("Lulu", "Zadig")
        expected = "lulu.zadig@company.com"
        self.assertEqual(
            expected,
            o.get_email(),
            msg="Expected fullname to be {expected}",
        )
