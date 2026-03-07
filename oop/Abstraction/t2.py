from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    def refund(slef,amount):
        pass

class CreditCardPayment(Payment):
    def pay(self,amount):
        return f"Cash is belongs to the CreditCard Payment {amount}"
    def refund(self, amount):
        return f"Cash is refund to the CreditCard Payment {amount}"
class PayPalPayment(Payment):
     
     def pay(self,amount):
          return f"Cash is belongs to the PayPal Payment {amount}"
     def refund(slef, amount):
        return f"Cash is refund to the Paypal Payment {amount}"
class CryptoPayment(Payment):
     def pay(self,amount):
          return f"Cash is belongs to the CryptoPayment {amount}"
     def refund(slef, amount):
        return f"Cash is refund to the CryptoPayment {amount}"

print(CreditCardPayment().pay(500))