class Payment:
    def pay(self, amount):
        print(f"Processing payment of {amount}")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class BankTransfer(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Bank Transfer")

class CashOnDelivery(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cash on Delivery")


payments = [CreditCard(), PayPal(), BankTransfer(), CashOnDelivery()]

for p in payments:
    p.pay(1000)