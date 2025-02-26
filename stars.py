def print_pattern(num):
    """
    Function to print a pattern based on the input number.

    Args:
    - num: Integer number (number of lines to print)

    Returns:
    - None
    """
    for i in range(1, num + 1):
        for j in range(i):
            print("*", end="")
        print()

# Test the function
print_pattern(3)
print()
print_pattern(4)
