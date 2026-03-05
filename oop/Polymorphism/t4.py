class Animal:
    def speak(self):
        print("Hello Mister Asadullah think beyond the limit")
        
class Dog(Animal):
    def speak(self):
        print("The Dog is barking")

class Cat(Animal):
    def speak(self):
      print("The Cat is meowing")

class Bird(Animal):
    def speak(self):
        print("The bird is chripping")
    
def animalSound(animal):
        animal.speak()
d=Dog()
c=Cat()
b=Bird()

animalSound(d)
animalSound(c)
animalSound(b)