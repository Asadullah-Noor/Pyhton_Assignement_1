from abc import ABC, abstractmethod

# --- Custom Exceptions ---
class NoDriverAvailableException(Exception):
    pass

class DriverAlreadyBookedException(Exception):
    pass


# --- Fare Strategy (Abstraction) ---
class FareStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class StandardFare(FareStrategy):
    def calculate_fare(self, distance):
        return 20 * distance


# --- User Class ---
class User:
    def __init__(self, name, start_location, end_location):
        self.name = name
        self.start_location = start_location
        self.end_location = end_location

    def request_ride(self, ride_manager):
        return ride_manager.create_ride(self)


# --- Driver Class ---
class Driver:
    def __init__(self, name):
        self.name = name
        self.available = True


# --- Ride Class ---
class Ride:
    def __init__(self, user, driver, distance, fare_strategy):
        self.user = user
        self.driver = driver
        self.distance = distance
        self.fare = fare_strategy.calculate_fare(distance)

    def ride_details(self):
        return f"User: {self.user.name}, Driver: {self.driver.name}, Fare: {self.fare}"


# --- Ride Manager ---
class RideManager:
    def __init__(self):
        self.drivers = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def find_driver(self):
        for driver in self.drivers:
            if driver.available:
                return driver
        raise NoDriverAvailableException("No drivers available")

    def create_ride(self, user):
        if not user.start_location or not user.end_location:
            raise ValueError("Invalid locations")

        driver = self.find_driver()

        if not driver.available:
            raise DriverAlreadyBookedException("Driver already booked")

        # Assign driver
        driver.available = False

        # Example: distance calculation (simple)
        distance = abs(user.end_location - user.start_location)

        ride = Ride(user, driver, distance, StandardFare())

        return ride
manager = RideManager()

d1 = Driver("Ali")
d2 = Driver("Ahmed")

manager.add_driver(d1)
manager.add_driver(d2)

user = User("Asadullah", 2, 10)

ride = user.request_ride(manager)

print(ride.ride_details())