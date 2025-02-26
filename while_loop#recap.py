secret_num = 7

while True:  # Infinite loop until the correct guess is found
    numm = int(input("Enter your number: "))
    if numm > secret_num:
        print("Your guess is too high!")
    elif numm < secret_num:
        print("Your guess is too low!")
    else:
        print("You found the secret number! Congratulations!")
        break  # Exit the loop once the correct guess is made
