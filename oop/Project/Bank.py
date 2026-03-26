from abc import ABC, abstractmethod
from datetime import datetime
# --- Custom Exceptions ---
class InsufficientFundsError(Exception):
    pass
class MinimumBalanceError(Exception):
    pass
class OverdraftLimitError(Exception):
    pass
class AccountNotMaturedError(Exception):
    pass
# --- Transaction Class ---
class Transaction:
    def __init__(self, type_, amount, balance_after):
        self.type = type_
        self.amount = amount
        self.balance_after = balance_after
        self.date = datetime.now()
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.type} | Amount: {self.amount} | Balance: {self.balance_after}"
# --- Base Bank Account Class ---
class Bank(ABC):
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self._balance = balance  # protected attribute
        self._transactions = []  # store transaction history
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    def get_balance(self):
        return self._balance
    def account_info(self):
        return f"Account: {self._account_number}, Owner: {self._owner}, Balance: {self._balance}"
    def show_transactions(self):
        if not self._transactions:
            return "No transactions yet."
        return "\n".join(str(t) for t in self._transactions)
    def transfer(self, target_account, amount):
        """Transfer money from this account to another account"""
        if not isinstance(target_account, Bank):
            raise ValueError("Target must be a Bank account")
        self.withdraw(amount)
        target_account.deposit(amount)
        self._transactions.append(Transaction(f"Transfer to {target_account._account_number}", amount, self._balance))
        target_account._transactions.append(Transaction(f"Transfer from {self._account_number}", amount, target_account._balance))
        return f"Transferred {amount} to {target_account._account_number}"
# --- Savings Account ---
class SavingsAccount(Bank):
    MIN_BALANCE = 500
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(Transaction("Deposit", amount, self._balance))
        return self._balance
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._balance - amount < self.MIN_BALANCE:
            raise MinimumBalanceError(f"Cannot withdraw! Minimum balance of {self.MIN_BALANCE} required.")
        self._balance -= amount
        self._transactions.append(Transaction("Withdraw", amount, self._balance))
        return self._balance
# --- Current Account ---
class CurrentAccount(Bank):
    OVERDRAFT_LIMIT = -1000
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(Transaction("Deposit", amount, self._balance))
        return self._balance
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._balance - amount < self.OVERDRAFT_LIMIT:
            raise OverdraftLimitError(f"Cannot withdraw! Overdraft limit of {self.OVERDRAFT_LIMIT} exceeded.")
        self._balance -= amount
        self._transactions.append(Transaction("Withdraw", amount, self._balance))
        return self._balance

# --- Fixed Deposit Account ---
class FixedDepositAccount(Bank):
    def __init__(self, account_number, owner, balance=0, matured=False):
        super().__init__(account_number, owner, balance)
        self.matured = matured
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(Transaction("Deposit", amount, self._balance))
        return self._balance

    def withdraw(self, amount):
        if not self.matured:
            raise AccountNotMaturedError("Withdrawal denied! Account has not matured yet.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient balance")
        self._balance -= amount
        self._transactions.append(Transaction("Withdraw", amount, self._balance))
        return self._balance
# --- Example Usage ---
if __name__ == "__main__":
    # Savings Account
    savings = SavingsAccount("SA1001", "Asadullah", 2000)
    print(savings.account_info())
    savings.deposit(500)
    try:
        savings.withdraw(1800)
    except MinimumBalanceError as e:
        print(e)
    print(savings.account_info())
    print("\nTransactions:")
    print(savings.show_transactions())

    # Current Account
    current = CurrentAccount("CA1001", "Asadullah", 200)
    print("\n" + current.account_info())
    try:
        current.withdraw(1000)  # Allowed
        current.withdraw(500)   # Exceeds overdraft
    except OverdraftLimitError as e:
        print(e)
    print(current.account_info())

    # Transfer Example (corrected)
    print("\nTransfer 300 from Savings to Current:")
    savings.transfer(current, 100)  # Pass the actual account object
    print(savings.account_info())
    print(current.account_info())

    # Fixed Deposit (unique account number)
    fd = FixedDepositAccount("FD1001", "Asadullah", 5000)
    print("\n" + fd.account_info())
    try:
        fd.withdraw(1000)  # Not matured
    except AccountNotMaturedError as e:
        print(e)
    fd.matured = True
    fd.withdraw(1000)
    print(fd.account_info())