from typing_extensions import override

class Vehicle:
    def __init__(self,Brand):
        self.Brand=Brand
    def start(self):
        print(f"Vehicle Started")

class Car(Vehicle):
    def __init__(self,Door,Brand):
        super().__init__(Brand)
        self.Door=Door
    @override
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def __init__(self,type,Brand):
         super().__init__(Brand)
         self.type=type
    @override
    def start(self):
        print(f"The {self.type} is Bike")

parent_class=Vehicle("Honda")
print(parent_class.Brand)
parent_class.start()
Car_Obj=Car("Flying Car Door","Sport")
print(Car_Obj.Brand)
Car_Obj.start()
print("The Brand name of the vehicle",Car_Obj.Brand)
Bike_obj=Bike("Yamha","Sports")
Bike_obj.start()

    

