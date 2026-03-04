from typing_extensions import override
class Employ:
    def __init__(self,name, salary):
        self.name=name 
        self.salary=salary
    def calculate_bonus(self):
        return (self.salary*0.10)
class Manager(Employ):
    @override
    def calculate_bonus(self):
        return (self.salary*0.20)
employee_obj=Employ("Asadullah",2000)
manager_obj=Manager("Ali Hamza",40000)
print("---------Employee Bonus is-------------")
print(employee_obj.calculate_bonus())
print("---------Manager Bonus is -------------")
print(manager_obj.calculate_bonus())
