from abc import ABC,abstractmethod
class Bank(ABC):
    __account_number=0
    __owner_name=""
    __balance=10000000000000
    @abstractmethod
    def deposit(self,amount):
       if amount<=0 and amount<=5000:
           print("Value should be Greater to zero and less than 100000")
       if amount>0 and amount <=100000:
            self.__balance += amount
            return self.__balance
       else:
           print("Pleae enter valid input")
    def withdraw(amount):
        pass
    def display_account_info():
        pass
