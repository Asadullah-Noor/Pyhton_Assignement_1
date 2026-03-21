class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print("Interest added.")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            print(f"{amount} withdrawn with overdraft.")
        else:
            print("Overdraft limit exceeded.")


# Main program
if __name__ == "__main__":
    acc1 = SavingsAccount("Ali", 1000, 0.05)
    acc2 = CurrentAccount("Ahmed", 500, 300)

    acc1.deposit(200)
    acc1.add_interest()
    print("Savings Balance:", acc1.get_balance())

    acc2.withdraw(700)
    print("Current Balance:", acc2.get_balance())