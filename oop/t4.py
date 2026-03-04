from typing_extensions import override
class Parent:
    Area_Rectangle=0
    def __init__(self,length, width):
        self.length=length
        self.width=width
    def area(self):
        Area_Rectangle=self.length*self.width
        print(f" The area of the rectangle is {Area_Rectangle}")

class Squre(Parent):
    def __init__(self):
        print(f"The Child Class is here working !")
    @override
    def area(self):
        print("The area of the squre")

Squre_Obj=Squre()
Squre_Obj.area()


        