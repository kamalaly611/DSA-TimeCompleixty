def greet(fx):
    def mfx():
        print('Good Morning ')
        fx()
        print('Thanks for using this function')
    return mfx
@greet
def hello():
    print('Hello World')
def add(a,b):
    print(a+b)
hello()
add(9,7)

import logging

# Configure logging to display messages on the console
logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

# Test the decorated function with values
print("Result:", my_function(3, 4))  # Should log the function call and return the sum
print("Result:", my_function(10, 15))  # Another test with different values
