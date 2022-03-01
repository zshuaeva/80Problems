import os
from unittest import TestCase

if os.environ.get("SOLUTION_TEST"):
    from solutions.solution_076 import BankAccount
else:
    try:
        from problems.problem_076 import BankAccount
    except Exception:
        class BankAccount:
            pass


class ProblemTests(TestCase):
    def test_bank_account_needs_opening_balance(self):
        BankAccount(0)

    def test_get_balance_returns_current_balance(self):
        account = BankAccount(100)
        self.assertEqual(
            100,
            account.get_balance(),
            msg="Expected 100 in the bank account",
        )

    def test_withdraw_removes_money_from_account(self):
        account = BankAccount(100)
        account.withdraw(30)
        self.assertEqual(
            70,
            account.get_balance(),
            msg="Expected 70 in the bank account after 30 withdraw",
        )

    def test_deposit_adds_money_to_account(self):
        account = BankAccount(100)
        account.deposit(40)
        self.assertEqual(
            140,
            account.get_balance(),
            msg="Expected 140 in the bank account after 40 deposit",
        )

    def test_cannot_go_into_negative_balance(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(110)
