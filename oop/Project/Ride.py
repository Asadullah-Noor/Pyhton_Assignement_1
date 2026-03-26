from abc import ABC,abstractmethod
class NoDriverAvailableException(Exception):
    pass
class DriverAlreadyBookedException(Exception):
    pass
class User(ABC):
    def __init__(self,user,Start_location,End_location):
        self.user=user
        self.Start_location=Start_location
        self.End_location=End_location
    @abstractmethod
    def Request_Ride(self):
        pass

    def Assign_Driver(self):
        pass
    
    def CalculatePrice(self):
        if not self.Start_location || not self.End_location:
            raise f"Please enter the both starting and engding location"
        if self.Start_location && self.End_location:
            total_Price=20*(self.Start_location+self.End_location)
        else:
            raise ValueError("Please Enter the Valid location here")
class Driver(User):


class Ride:

class RideManager: