from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
    def fuel_type(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car")
        return f"Engine started"
    def stop_engine(self):
        return f"Engine stoped"
    def fuel_type(self):
        return f"Fuel type: Petrol"
class ElectricScooter(Vehicle):
    def start_engine(self):
        print("ElectricScooter")
        return f"Engine started"
    def stop_engine(self):
        return f"Fuel type: Electric"
    def fuel_type(self):
        return f"Fuel type: Petrol"
class Bike(Vehicle):
    def start_engine(self):
        print("Bike")
        return f"Engine started"
    def stop_engine(self):
        return f"Engine Stopped"
    def fuel_type(self):
        return f"Fuel type: Petrol"
    
print(Car().start_engine())
print(Car().stop_engine())
print(Car().fuel_type())
print(Bike().start_engine())
print(Bike().stop_engine())
print(Bike().fuel_type())
print(ElectricScooter().start_engine())
print(ElectricScooter().stop_engine())
print(ElectricScooter().fuel_type())