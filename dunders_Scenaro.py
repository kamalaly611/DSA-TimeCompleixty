class BankAccount:
    def __init__(self, holder_name: str, balance: float):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount: float) -> str:
        if amount <= 0:
            return "Sorry, the deposit amount cannot be negative or zero."
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}"

    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            return "Sorry, the withdrawal amount cannot be negative or zero."
        elif amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"Amount of {amount} withdrawn successfully. Current balance: {self.balance}"

    def __add__(self, other: "BankAccount") -> float:
        return self.balance + other.balance

    def __gt__(self, other: "BankAccount") -> bool:
        return self.balance > other.balance

    def __eq__(self, other: "BankAccount") -> bool:
        return self.balance == other.balance

    def __str__(self) -> str:
        return f"Account Holder: {self.holder_name}, Balance: {self.balance:.2f}"


# Example Usage:
account1 = BankAccount("Khalid", 1200)
account2 = BankAccount("Sami", 1300)

print(account1 > account2)  # False
print(account1 + account2)  # 2500
print(account1)             # Account Holder: Khalid, Balance: 1200.00
print(account2)             # Account Holder: Sami, Balance: 1300.00
print(account1.deposit(0))  # Sorry, the deposit amount cannot be negative or zero.
print(account1.deposit(500))  # Deposit of 500 successful. Current balance: 1700.00
print(account1.withdraw(299))  # Amount of 299 withdrawn successfully. Current balance: 1401.00
print(account1.withdraw(1500)) # Insufficient balance.
