def debug(func):
    func._debug_called = False  # Add a flag to track calls
    def wrapper(*args, **kwargs):
        if not func._debug_called:
            print(f'Testing the function which comes first is {func.__name__}')
            func._debug_called = True
        result = func(*args, **kwargs)
        func._debug_called = False  # Reset flag after execution
        return result
    return wrapper


@debug
def greet(name,greetings='Hello'):
    print(f'{greetings},{name} Sweat Heart')
@debug
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result=n * factorial(n - 1)
    #print(f"Intermediate result for factorial({n}): {result}")  
    return result
@debug
def value():
    print(factorial(5))


# Test the factorial function
greet('Hey','Zindagi')
factorial(5)
value()