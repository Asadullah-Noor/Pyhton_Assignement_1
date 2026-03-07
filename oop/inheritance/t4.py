class Parent:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # def area(self):
    #     area_rectangle = self.length * self.width
    #     print(f"The area of the rectangle is {area_rectangle}")


class Square(Parent):
    def __init__(self, side):
        super().__init__(side, side)
        print("The Child Class is here working!")

    def area(self):
        area_square = self.length * self.width
        print(f"The area of the square is {area_square}")


Square_Obj = Square(5)
Square_Obj.area()