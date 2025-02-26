def greet(fx):
    def mfx(*args, **kwargs):
        print('Good Morning ')
        result = fx(*args, **kwargs)
        print(f'Thanks for using this {fx.__name__}')
        return result
        #fx()
        
    return mfx
@greet
def hello():
    print('Hello World')
@greet
def add(a,b):
    print(a+b)
# calling Functions?????
hello()
add(9,7)


# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("*You add sprinkles 🎊*")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("*You add fudge 🍫*")
#         func(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream 🍨")

# get_ice_cream("Kulfa")

# import time

# # Decorator to time the function and add messages
# def time_logger(func):
#     def wrapper(*args, **kwargs):
#         print("Starting the function...")
#         start_time = time.time()  # Record start time
#         result = func(*args, **kwargs)  # Execute the decorated function
#         end_time = time.time()  # Record end time
#         print(f"Function completed in {end_time - start_time:.5f} seconds")
#         return result
#     return wrapper

# # Factorial function
# @time_logger
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# # Test the factorial function
# print("Factorial Result:", factorial(5))


# import time
# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
#         return result
#     return wrapper

# @time_it
# def calc_square(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     return result

# @time_it
# def calc_cube(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     return result

# array = range(1,100000)
# out_square = calc_square(array)
# out_cube = calc_cube(array)