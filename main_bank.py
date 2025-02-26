balance = 3000  # Define balance as a global variable for all functions

def check_balance(num):
    global balance
    if num <= balance:
        return 'Balance is sufficient'
    else:
        return 'Balance is insufficient'

def depositing(num):
    global balance
    balance += num
    return balance

def withdraw(num):
    global balance
    if num <= balance:
        balance -= num
        return f'You have withdrawn {num}. New balance is {balance}.'
    else:
        return 'Insufficient balance to withdraw that amount.'

if __name__ == '__main__':
    print("Balance check:", check_balance(600))
    print("Depositing amount:", depositing(600))
    print("Withdrawal attempt:", withdraw(600))
