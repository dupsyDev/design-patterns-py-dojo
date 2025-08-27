from abc import ABC, abstractmethod
from datetime import datetime


class Notifier(ABC):

    @abstractmethod
    def send(self, message):
        pass

class SimpleNotification(Notifier):

    def send(self, message):
        return f"Sending: {message}"


class NotifierDecorator(Notifier):
    def __init__(self, notification: Notifier, user_config):
        self._notification = notification
        self._user_config = user_config

    @abstractmethod
    def send(self, message, user_config):
        pass

class TimestampDecorator(NotifierDecorator):
    def __init__(self):
        self._key = "timestamp"

    def send(self, message, user_config):
        if self._key in user_config and user_config[self._key]:
            date_today = datetime.today().strftime('%Y-%m-%d')
            message = f"[{date_today}] {message}"
        return self._notification.send(message)
    
class EncryptionDecorator(NotifierDecorator):
    def __init__(self):
        self._key = "encryption"

    def send(self, message, user_config):
        if self._key in user_config and user_config[self._key]:
            message = message[::-1]
        return self._notification.send(message)
     
class PriorityDecorator(NotifierDecorator):
    def __init__(self):
        self._key = "priority"

    def send(self, message, user_config):
        if self._key in user_config and user_config[self._key]:
            message = message + " [HIGH]"
        return self._notification.send(message)
    
class ReadReceiptDecorator(NotifierDecorator):
    def __init__(self):
        self._key = "read_receipt"

    def send(self, message, user_config):
        if self._key in user_config and user_config[self._key]:
            message = message + " [READ_RECEIPT:xyz123]"
        return self._notification.send(message)

if __name__ == "__main__":

    user1 = { "timestamp": True, "encryption": True, "priority": False, "read_receipt": True }
    user2 = { "timestamp": False, "encryption": True, "priority": True, "read_receipt": False }
    notification1 = TimestampDecorator(ReadReceiptDecorator(PriorityDecorator(EncryptionDecorator(SimpleNotification()))))
    print(notification1.send(user1))
    print(notification1.send(user2))