from abc import ABC,abstractmethod
class Bank(ABC):
    def __init__(self,accountNumber,owner,balance):
        self.__accountNumber=accountNumber
        self.__owner=owner
        self.__balance=balance
    @abstractmethod
    def deposit(self,amount):
       pass
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance-=amount
            return self.__balance
        if amount<=0:
            return f"Invalid input!"
    def display_account_info(self):
        print(f"The total Balance is {self.__balance}")
        print("If you interested to deposit the amount please check it again")
class SavingsAccount(Bank):
    def deposit(self, amount):
        return super().deposit(amount)
    MIN_Balance=500
    def withdraw(self, amount):
        if self._Bank__balance - amount<self.MIN_Balance:
            print("Withdrawals are not allowed if the balance would drop below this minimum.")
        else:
            self._Bank__balance-=amount
            print(f"Withdrawn: {amount}")
            print(f"New Balance: {self.balance}")
class CurrentAccount(Bank):
    overdraft=-1000
    def deposit(self, amount):
        return super().deposit(amount)
    def withdraw(self,amount):
        if self._Bank__balance - amount<self.overdraft:
            print("Allows an overdraft of up to -1000.")
        else:
            self._Bank__balance -=amount
            print(f"Withdrawn: {amount}")
            print(f"New Balance: {self.balance}")
class FixedDepositAccount(Bank):
    def __init__(self,accountNumber,owner,balance,matured=False):
        super().__init__(accountNumber,owner,balance)
        self.matured=matured
    def deposit(self, amount):
        return super().deposit(amount)
    def withdraw(self, amount):
        if not self.matured:
            print("Withdrawal denied! Account has not matured yet.")
        else:
            if amount <= self._Bank__balance:
                self._Bank__balance -= amount
                print(f"Withdrawn: {amount}")
                print(f"New Balance: {self.balance}")
            else:
                print("Insufficient balance")
class Encapsulate_cls(Bank):
    balance=0
    def deposit(self, amount):
        return super().deposit(amount)
    def get_balance(self,):
        return self._Bank__balance
    def set_balance(self, value):
        self._Bank__balance = value
account=SavingsAccount(20000, "Asadullah" , "ls23bsse0103") 
print(account.deposit(2000))
