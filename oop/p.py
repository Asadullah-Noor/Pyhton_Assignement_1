class Animal:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self._age = age           # protected attribute

    def speak(self):
        return "Animal makes a sound"

    def get_age(self):
        return self._age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def info(self):
        return f"Dog: {self.name}, Breed: {self.breed}, Age: {self._age}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

    def info(self):
        return f"Cat: {self.name}, Color: {self.color}, Age: {self._age}"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(animal.info())
            print(animal.speak())


# Main execution
if __name__ == "__main__":
    dog1 = Dog("Buddy", 3, "Golden Retriever")
    cat1 = Cat("Whiskers", 2, "White")

    zoo = Zoo()
    zoo.add_animal(dog1)
    zoo.add_animal(cat1)

    zoo.show_animals()