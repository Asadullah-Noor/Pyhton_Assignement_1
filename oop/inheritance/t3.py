class Parent:
    def __init__(self):
        print("This is the parent Class")
    def greet(self):
        print("My name is AsadUllah")
class Child(Parent):
    def __init__(self):
        super().__init__()

Call=Child()
Call.greet()