balance=20000
def deposit():
    ask=int(input("Enter The amount for Deposit: "))
    global balance
    balance+=ask
    

def withdraw():
    ask_2=int(input("Enter The amount For withdrawal: "))
    global balance
    if ask_2<balance:
        balance-=ask_2
    
def CurrentBalnacec():
    global balance
    print(f'Your Current balance is {balance}')

deposit()
withdraw()
CurrentBalnacec()