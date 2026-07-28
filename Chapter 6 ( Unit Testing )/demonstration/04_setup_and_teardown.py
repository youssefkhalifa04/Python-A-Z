"""Chapter 6 - setUp and tearDown

This file shows how to prepare data before each test and clean it after.
"""

import unittest


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        self.account.withdraw(20)
        self.assertEqual(self.account.balance, 80)

    def tearDown(self):
        self.account = None


if __name__ == "__main__":
    unittest.main()
