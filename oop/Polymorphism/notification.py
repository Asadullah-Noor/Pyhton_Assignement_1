class Notification:
    def send(self, message):
        print(f"Printing the Base class message{message}")
class EmailNotification(Notification):
    def send(self,message):
        print(f"Email Notfication is {message}")
class SMSNotification(Notification):
    def send(self,message):
        print(f"SMS notification is {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Push the Notification is {message}")

Notification=[EmailNotification(),SMSNotification(),PushNotification()]

for N in Notification:
    N.send("Hello")

