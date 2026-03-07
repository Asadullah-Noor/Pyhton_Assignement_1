from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def calculate_salary(slef,salary):
        pass
class FullTimeEmployee(Employee):
    def calculate_salary(slef,salary):
        return salary
class PartTimeEmployee(Employee):
    def calculate_salary(slef,hour,hourly_rate):
        return hourly_rate*hour
class Freelancer(Employee):
     def calculate_salary(slef,Project_Fee):
        return Project_Fee
print(FullTimeEmployee().calculate_salary(2000))
print(PartTimeEmployee().calculate_salary(30,2000))
print(Freelancer().calculate_salary(2000))

