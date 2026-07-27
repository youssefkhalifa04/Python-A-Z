"""Chapter 5 - Polymorphism

This file shows how different classes can share the same method name while
producing different behavior.
"""

print("--- Polymorphism ---")


class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using a credit card.")


class PayPal:
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


class Cash:
    def pay(self, amount):
        print(f"Paid {amount} in cash.")


def checkout(payment_method, amount):
    payment_method.pay(amount)


payments = [CreditCard(), PayPal(), Cash()]

for payment in payments:
    checkout(payment, 25)

print("Same method name, different behavior depending on the object type.")
