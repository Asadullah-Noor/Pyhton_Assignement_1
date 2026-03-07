from typing_extensions import override
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self ,length, width):
        self.length=length
        self.width=width
    @override
    def area(self):
        return self.length*self.width
class Squre(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
print("----------Square Class Object is calling here -------------")
sqr_obj=Squre(10)
print(sqr_obj.area())
print("-----------Rectangle function is calling here---------------")
rect_obj=Rectangle(20,10)
print(rect_obj.area())
