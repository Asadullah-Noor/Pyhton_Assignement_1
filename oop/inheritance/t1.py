class Dog:
    species="Canine"
    def __init__(self, name , age):
        self.name=name
        self.age=age
    def display(self):
        return f" Name of Species is :  {self.name} and the age of species is {self.age}"

dg=Dog('Cat',10)

print(dg.display())