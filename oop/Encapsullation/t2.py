class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private attribute

    # Getter — read-only access
    @property
    def salary(self):
        return self.__salary

    # Setter — controlled write access
    @salary.setter
    def salary(self, amount):
        if amount < self.__salary:
            print("Salary cannot decrease")
            return
        if amount > 1_000_000:
            print("Salary cannot exceed 1,000,000")
            return
        if amount < 0:
            print("Salary cannot be negative")
            return
        self.__salary = amount

    # Increase salary with validation
    def increase_salary(self, amount):
        if amount <= 0:
            print("Increase must be positive")
            return
        if self.__salary + amount > 1_000_000:
            print("Salary cannot exceed 1,000,000")
            return
        self.__salary += amount


# ---------------- Example Usage ----------------
emp = Employee("Sara", 50000)

# Using setter
emp.salary = 60000      # ✅ allowed
print(emp.salary)       # 60000

emp.salary = -10        # ❌ error: Salary cannot be negative
emp.salary = 2_000_000  # ❌ error: Salary cannot exceed 1,000,000

# Using increase_salary method
emp.increase_salary(10000)  # ✅ allowed
print(emp.salary)            # 70000

emp.increase_salary(-500)    # ❌ error: Increase must be positive