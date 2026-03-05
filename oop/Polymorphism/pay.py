class Payment:
    def pay(self, amount):
        return amount
class CreditCardPayment(Payment):
    def pay(self,amount):
        return amount
class DebitCardPayment(Payment):
    def pay(self,amount):
        return amount
class COD(Payment):
    def pay(self,amount):
        return amount
    
CP=CreditCardPayment()
print("Credit Card Payment",CP.pay(500))
D=DebitCardPayment()
print("Debit Crad payment",D.pay(300))
C=COD()
print("Cash On delivery",C.pay(200))
    