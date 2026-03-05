class Animal:
    def speak():
        print("Hello Mister Asadullah think beyond the limit")
class Dog(Animal):
    def speak():
        print("The Dog is barking")

class Cat(Animal):
    def speak():
      print("The Cat is meowing")

class Bird(Animal):
    def speak():
        print("The bird is chripping")
    def animalSound():
        Animal.speak()
b=Bird()
b.animalSound