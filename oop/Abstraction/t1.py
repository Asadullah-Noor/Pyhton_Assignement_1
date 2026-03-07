from abc import ABC ,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):

    def __init__(self,length,width):
      self.width=width
      self.length=length

    def area(self):
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi *self.radius**2
    
Rc=Rectangle(10,20)
print(Rc.area())
Cr=Circle(4)
print(Cr.area())