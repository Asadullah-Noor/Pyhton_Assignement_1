from typing_extensions import override

import math

class Shape:

    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi *self.radius* self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

class Triangle(Shape):
    def __init__(self, base,length):
         self.base=base
         self.length=length

    def area(self):
        return 0.5*self.base*self.length

Shape =[
    Circle(5),
    Rectangle(4,6),
    Triangle(3,8)
]

for i in Shape:
    print("Area :", i.area())