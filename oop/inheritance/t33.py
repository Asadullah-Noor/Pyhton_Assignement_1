from typing_extensions import override

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"Paying {self.amount} using generic payment")


class CreditCardPayment(Payment):
    @override
    def pay(self):
        print(f"Paying {self.amount} using Credit Card")


class PayPalPayment(Payment):
    @override
    def pay(self):
        print(f"Paying {self.amount} using PayPal")


class CryptoPayment(Payment):
    @override
    def pay(self):
        print(f"Paying {self.amount} using Cryptocurrency")


# Polymorphism: store in a list
payments = [
    CreditCardPayment(200),
    PayPalPayment(150),
    CryptoPayment(500)
]

# Loop through and call pay()
for p in payments:
    p.pay()