while True:
    Ask_user = input("Do you want to continue studying or take a break? (continue/break/stop): ").lower()

    if Ask_user == "continue":
        print("You have been allotted 30 minutes for study.")
        # Simulate study session (you can add more functionality here if needed)
    elif Ask_user == "break":
        print("You have been allotted 5 minutes for a break.")
        # Simulate break session (you can add more functionality here if needed)
    elif Ask_user == "stop":
        print("Study session ended. Goodbye!")
        break
    else:
        print("Invalid input. Please type 'continue', 'break', or 'stop'.")
