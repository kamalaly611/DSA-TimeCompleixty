import getpass

class Atm:
    counter=0
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.sno=Atm.counter

        Atm.counter=Atm.counter+1


        self.menu()


    def menu(self):
        while True:
            user_input = input("""
                Hello, How would you like to proceed?
                1. Create PIN
                2. Deposit
                3. Withdraw
                4. Check Balance
                5. Exit
                Enter your choice: """)

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print('Thank you for using the ATM. Goodbye!')
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")

    #  Encapsulated: Private PIN
    def create_pin(self):
        pin = getpass.getpass("Enter a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            self.__pin = pin
            print('---- PIN created successfully ----')
        else:
            print("Invalid PIN! Please enter exactly 4 digits.")

    #  Encapsulated: Private balance with getter
    def get_balance(self):
        return self.__balance

    #  Deposit with validation
    def deposit(self):
        temp = getpass.getpass('Enter your PIN: ')
        if temp == self.__pin:
            try:
                amount = int(input('Enter the deposit amount: '))
                if amount > 0:
                    self.__balance += amount
                    print(f"Deposit successful! New balance: {self.__balance}")
                else:
                    print("Deposit amount must be greater than 0.")
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        else:
            print('Invalid PIN!')

    #  Withdraw with validation
    def withdraw(self):
        temp = getpass.getpass('Enter your PIN: ')
        if temp == self.__pin:
            try:
                amount = int(input('Enter the amount: '))
                if amount > 0 and amount <= self.__balance:
                    self.__balance -= amount
                    print('Transaction successful!')
                elif amount > self.__balance:
                    print('Insufficient funds!')
                else:
                    print("Withdrawal amount must be greater than 0.")
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        else:
            print('Invalid PIN!')

    # Encapsulated: Checking balance
    def check_balance(self):
        temp = getpass.getpass('Enter your PIN: ')
        if temp == self.__pin:
            print(f"Your current balance is: {self.__balance}")
        else:
            print('Invalid PIN!')


c1 = Atm()
print('Current instance is',c1.counter)
# #obj.__create_pin
# c2 = Atm()
# print(c2.counter)
# c3 = Atm()
# print(c3.counter)
# c4 = Atm()
# print(c4.counter)
# c5=[c1,c2,c3,c4]
# for i in c5:
#     #if i==c1:
#     print(i.counter)
#     #print(c1.counter)#