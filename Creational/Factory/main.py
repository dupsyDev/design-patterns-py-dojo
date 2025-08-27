from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def notify(self, message):
        pass

class EmailNotification(Notification):

    def notify(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):

    def notify(self, message):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):

    def notify(self, message):
        print(f"Sending Push: {message}")


class NotificationFactory(ABC):

    @abstractmethod
    def create_notification(self):
        pass

class EmailNotificationFactory(NotificationFactory):

    def create_notification(self) -> Notification:
        return EmailNotification()
    
class SMSNotificationFactory(NotificationFactory):

    def create_notification(self) -> Notification:
        return SMSNotification()
    
class PushNotificationFactory(NotificationFactory):

    def create_notification(self) -> Notification:
        return PushNotification()
    
def get_factory(channel:str) -> NotificationFactory:
    if channel == "email":
        return EmailNotificationFactory()
    elif channel == "sms":
        return SMSNotificationFactory()
    elif channel == "push":
        return PushNotificationFactory()
    else:
        raise ValueError("Unknown notification channel")
    
if __name__ == "__main__":
    user_input = ""
    while user_input != "0":
        user_input = input("Which notification do you want to send? ")
        if user_input == "0":
            print(f"Exiting program!!!")
            continue
        try: 
            factory = get_factory(user_input)
            notification = factory.create_notification()
            notification.notify("Hello from Factory Method pattern!")
        except ValueError as ex:
            print(f"{ex}")
            print(f"Try again!!!")


    