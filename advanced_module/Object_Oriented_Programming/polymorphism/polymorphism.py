# Polymorphism in Object-Oriented Python
# Polymorphism is the principle that allows
# classes derived from the same superclass
# have the same methods (with the same signature)
# but different behaviors.
# Method signature = Same name and quantity
# of parameters (return is not part of the signature)
# Opinion + principles that count:
# Method signature: name, parameters and return the same
# SO"L"ID
# Liskov substitution principle
# Objects of a superclass must be replaceable
# subclass objects without breaking the application.
# Method overloading 🐍 = ❌
# Method override 🐍 = ✅
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...


class NotificationEmail(Notification):
    def send(self) -> bool:
        print('Email: sending - ', self.message)
        return True


class NotificationSMS(Notification):
    def send(self) -> bool:
        print('SMS: sending - ', self.message)
        return False


def notify(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print('Notification sent')
    else:
        print('Notification NOT sent')


notification_email = NotificationEmail('testing email')
notify(notification_email)

notification_sms = NotificationSMS('testing SMS')
notify(notification_sms)