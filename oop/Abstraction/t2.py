from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        return f"Cash belongs to the CreditCard Payment: {amount}"

    def refund(self, amount):
        return f"Cash is refunded to the CreditCard Payment: {amount}"


class PayPalPayment(Payment):

    def pay(self, amount):
        return f"Cash belongs to the PayPal Payment: {amount}"

    def refund(self, amount):
        return f"Cash is refunded to the PayPal Payment: {amount}"


class CryptoPayment(Payment):

    def pay(self, amount):
        return f"Cash belongs to the CryptoPayment: {amount}"

    def refund(self, amount):
        return f"Cash is refunded to the CryptoPayment: {amount}"


# Test
print(CreditCardPayment().pay(500))
print(PayPalPayment().refund(200))
print(CryptoPayment().pay(1000))