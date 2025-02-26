# OverdraftError that inherits from Exception.

class OverdraftError(Exception):
    pass
current=2000

try:
    a=int(input("Press 1 For withdraw and 2 for Deposist:="))
    if a==1:
        ask=int(input("what money You want to withdraw:="))
        if(ask<2000):
            current-=ask
            print(f'You Successfully withdraw the amount,${current}')
        else:
            raise OverdraftError
    elif a==2:
        ask2=int(input('How much money you want to Deposit:='))
        current+=ask2
        print(f'The amount has been Deposisted ,${current}')
except OverdraftError as e:
    print(f"OverdraftError: Insufficient funds. Your balance is ${current}, but you attempted to withdraw {a}.")
