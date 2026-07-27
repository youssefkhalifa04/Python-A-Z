"""Chapter 5 - Encapsulation

This file explains public, protected, and private attributes in Python.
Python does not enforce access modifiers strictly, so encapsulation is based on
conventions and controlled access through methods.
"""

print("--- Encapsulation ---")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner # public attribute
        self._branch_code = "MAIN-01"  # protected attribute
        self.__pin = 1234 # private attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money.")
        elif amount > 0:
            self.__balance -= amount

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def is_valid_pin(self, pin):
        return pin == self.__pin


account = BankAccount("Sara", 100)
print("Public owner:", account.owner) # Accessing public attribute
print("Protected branch code:", account._branch_code) # Accessing protected attribute (not recommended)
print("Access through method:", account.get_balance()) # Accessing private attribute through method 

account.deposit(50)
account.withdraw(30)
account.show_balance()

print("PIN valid?", account.is_valid_pin(1234))
