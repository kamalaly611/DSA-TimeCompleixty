class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Name of the account owner
        self.balance = balance  # Current balance in the account

    # Overload + operator to merge two accounts
    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balance + other.balance
            return BankAccount(self.account_holder, new_balance)  # Correct indentation
        else:
            raise TypeError("Can only merge with another BankAccount")

    # Overload - operator to withdraw from the account
    def __sub__(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal")
        return BankAccount(self.account_holder, self.balance - amount)

    # Display account details
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

# Example Usage
# Create two accounts
account1 = BankAccount("John", 500)  # John's account with $500
account2 = BankAccount("Alice", 300)  # Alice's account with $300

# Merge the accounts
merged_account = account1 + account2 # Now these will trigger the __add__
print("After Merging:")
print(merged_account)

# Withdraw from the merged account
updated_account = merged_account - 200
print("\nAfter Withdrawal:")
print(updated_account)
