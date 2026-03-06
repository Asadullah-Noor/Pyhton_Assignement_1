class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    @property
    def balance(self):
        return self.__balance      # read-only access

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount > self.__balance:
            print("Insufficient balance")
            return
        self.__balance -= amount
acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)   # allowed
# acc.balance = 10000  # NOT allowed