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
    def __init__(self, notification: Notifier):
        self._notification = notification

    @abstractmethod
    def send(self, message):
        pass

class TimestampDecorator(NotifierDecorator):
    def send(self, message):
        date_today = datetime.today().strftime('%Y-%m-%d')
        return self._notification.send(f"[{date_today}] {message}")
    
class EncryptionDecorator(NotifierDecorator):
    def send(self, message):
        reversed_message = message[::-1]
        return self._notification.send(reversed_message)
     
class PriorityDecorator(NotifierDecorator):
    def send(self, message):
        priority_message = message + " [HIGH]"
        return self._notification.send(priority_message)
    
class ReadReceiptDecorator(NotifierDecorator):
    def send(self, message):
        receipt_message = message + "[READ_RECEIPT:xyz123]"
        return self._notification.send(receipt_message)

if __name__ == "__main__":

    notification = SimpleNotification()
    notification = EncryptionDecorator(notification)
    notification = TimestampDecorator(notification)
    notification = PriorityDecorator(notification)
    notification = ReadReceiptDecorator(notification)
    print(notification.send("Hello Helly"))

    notification = SimpleNotification()
    notification = TimestampDecorator(notification)
    notification = EncryptionDecorator(notification)
    notification = ReadReceiptDecorator(notification)
    notification = PriorityDecorator(notification)
   
    print(notification.send("Hello Akash"))