from abc import ABC,abstractmethod
class Bank(ABC):
    def __init__(self,balance,owner,accountNumber):
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
    print("Hello I m Asadullah Noor") 
    def deposit(self,amount):
        if amount <=0 or amount>10000:
            print("Invalid Amount")
        else:
            self._Bank__balance+=amount
            return self._Bank__balance

    
account=SavingsAccount(20000, "Asadullah" , "ls23bsse0103") 
account.display_account_info()
