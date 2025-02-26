class BankAccount:
    num_of_accounts=0

    def __init__(self,Holder_name, balance):
        self.Holder_name=Holder_name
        self.balance=balance
        
        BankAccount.num_of_accounts=1
    def depositmoney(self,amount):
        self.balance+=amount
        print(f"Deposit successful. New balance: {self.balance}")
        
    def  withdrawMoney(self,amount):
        if (self.balance<amount):
            print("Insufficient funds")
            
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")

BankAc=BankAccount('Kamal',600)    
print(f"Initial balance: {BankAc.balance}")
BankAc.depositmoney(100)
BankAc.withdrawMoney(200)
BankAc.withdrawMoney(600)

