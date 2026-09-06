"""Chapter 4 - Custom errors

This file shows how to create your own exception classes.
"""

print("--- Custom errors ---")


class AgeError(Exception):
    pass


class BalanceError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    if age < 18:
        raise AgeError("You must be at least 18 years old.")
    return age


def withdraw_from_account(balance, amount):
    if amount > balance:
        raise BalanceError(f"Insufficient funds. Balance: {balance}, Requested: {amount}")
    return balance - amount


try:
    age = check_age(15)
except AgeError as error:
    print(f"Age error: {error}")

try:
    new_balance = withdraw_from_account(100, 150)
except BalanceError as error:
    print(f"Balance error: {error}")

try:
    age = check_age(25)
    print(f"Age check passed. Age: {age}")
except AgeError as error:
    print(f"Age error: {error}")
