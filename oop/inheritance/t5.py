from typing_extensions import override
class Animal:
    def __init__(self, name , age):
        self.name=name
        self.age=age
    def speak(self):
        print("Animal Makes Sound")
    
class Dog(Animal):
     
     @override
     def speak(self):
         print("Dogs Barks")
class Cat(Animal):
    @override
    def speak(self):
        print("Cat Meows")

Dog_obj=Dog("dofffy","12")
Cat_obj=Cat("Cat",21)
print(Dog_obj.name)
Dog_obj.speak()
Cat_obj.speak()



