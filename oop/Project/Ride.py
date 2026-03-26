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
    def Request_Ride(self,User):
        pass
    def Assign_Driver(self):
        pass
    def CalculatePrice(self):
        if not self.Start_location || not self.End_location:
            raise f"Please enter the both starting and engding location"
        if self.Start_location && self.End_location:
            total_Price=20*(self.Start_location + self.End_location)
        else:
            raise ValueError("Please Enter the Valid location here")
class Driver(User):
     def Assign_Driver(self,user,Driver):
        if not self.user
           raise Exception("User is not available so we could not add the Driver")
        if self.user:
            return f"The User {self.user} assign Driver is {self.Driver}"
class Ride:
    def RequestRide(self):
        if not self.user:
            raise Exception("User is not Available")
        if self.user:
            print("Request for the Rider")


class RideManager: