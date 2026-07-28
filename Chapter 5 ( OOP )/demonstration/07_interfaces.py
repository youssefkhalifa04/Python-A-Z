"""Chapter 5 - Interfaces

In Python, interfaces are usually represented with abstract base classes.
A class that follows an interface must implement the required methods.
"""

from abc import ABC, abstractmethod

print("--- Interfaces ---")


class Notification(ABC): # an interface defines a contract that classes must follow
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


notifications = [EmailNotification(), SMSNotification()]

for notification in notifications:
    notification.send("Welcome to the course!")
