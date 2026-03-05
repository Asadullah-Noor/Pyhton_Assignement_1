class Payment:
    def pay(slef, amount):
        return amount
class CreditCard(Payment):
    def pay(slef, amount):
        return super().pay(amount)
class PayPal(Payment):
    def pay(slef, amount):
        return super().pay(amount)
class BankTransfer(Payment):
    def pay(self, amount):
        return super().pay(amount)
    
class CashOnDelivery(Payment):
    def pay(slef, amount):
        return super().pay(amount)
CC=CreditCard()
PP=PayPal()
BT=BankTransfer()
COD=CashOnDelivery()
Payment=[
    CC.pay(30),
    PP.pay(40),
    BT.pay(50),
    COD.pay(60)
]
for i in Payment:
    print(i)