from abc import ABC, abstractmethod

# --- Base Bank Account Class ---
class Bank(ABC):
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self._balance = balance  # protected attribute

    @abstractmethod
    def deposit(self, amount):
        """Deposit money into the account"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money from the account"""
        pass

    def get_balance(self):
        return self._balance

    def account_info(self):
        return f"Account: {self._account_number}, Owner: {self._owner}, Balance: {self._balance}"


# --- Savings Account ---
class SavingsAccount(Bank):
    MIN_BALANCE = 500

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if self._balance - amount < self.MIN_BALANCE:
            return f"Cannot withdraw! Minimum balance of {self.MIN_BALANCE} required."
        self._balance -= amount
        return self._balance


# --- Current Account ---
class CurrentAccount(Bank):
    OVERDRAFT_LIMIT = -1000

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if self._balance - amount < self.OVERDRAFT_LIMIT:
            return f"Cannot withdraw! Overdraft limit of {self.OVERDRAFT_LIMIT} exceeded."
        self._balance -= amount
        return self._balance


# --- Fixed Deposit Account ---
class FixedDepositAccount(Bank):
    def __init__(self, account_number, owner, balance=0, matured=False):
        super().__init__(account_number, owner, balance)
        self.matured = matured

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if not self.matured:
            return "Withdrawal denied! Account has not matured yet."
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self._balance:
            return "Insufficient balance"
        self._balance -= amount
        return self._balance


# --- Example Usage ---
if __name__ == "__main__":
    print("=== Savings Account ===")
    savings = SavingsAccount("SA1001", "Asadullah", 2000)
    print(savings.account_info())
    print("Deposit 500:", savings.deposit(500))
    print("Withdraw 1800:", savings.withdraw(1800))
    print("Withdraw 1500:", savings.withdraw(1500))  # Should fail due to MIN_BALANCE
    print(savings.account_info())

    print("\n=== Current Account ===")
    current = CurrentAccount("CA1001", "Asadullah", 200)
    print(current.account_info())
    print("Withdraw 1000:", current.withdraw(1000))  # Allowed, overdraft
    print("Withdraw 500:", current.withdraw(500))    # Should fail, exceeds overdraft
    print(current.account_info())

    print("\n=== Fixed Deposit Account ===")
    fd = FixedDepositAccount("FD1001", "Asadullah", 5000)
    print(fd.account_info())
    print("Withdraw 1000 (not matured):", fd.withdraw(1000))
    fd.matured = True
    print("Withdraw 1000 (matured):", fd.withdraw(1000))
    print(fd.account_info())