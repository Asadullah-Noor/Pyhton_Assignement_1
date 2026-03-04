class Person:
    def __init__(self, name ,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"The Person Class is here ")
class Student(Person):
    def __init__(self,grade,name,age):
        self.grade=grade
        super().__init__(name,age)
    def display(self):
        print(f"Student name is  : {self.name}, age is {self.age} and grade is {self.grade}")

Student_Obj=Student("A","Asadullah Noor",23)
Student_Obj.display()
