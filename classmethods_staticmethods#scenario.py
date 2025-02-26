class Libary:
    total_books=100
    @classmethod
    def update(cls,num):
        cls.total_books=num
        return cls.total_books
    @staticmethod
    def is_valid_book(title):
        if not isinstance(title, str) or not title.strip():
            return False
        return True

print(Libary.update(7))
print(Libary.is_valid_book(''))
print(Libary.is_valid_book('Python Programming'))  # Should return True

class Employee:
    total_employees = 0  # Class variable to track total employees

    def __init__(self, name):
        self.name = name  # Instance variable for employee name
        #Employee.total_employees += 1  # Increment total employees when a new instance is created

    @classmethod
    def increment_total_employees(cls):
        # Increment the total employee count
        cls.total_employees += 1
        return cls.total_employees

    @staticmethod
    def is_valid_name(name):
        # Check if the name is a string and has at least 2 characters
        if not isinstance(name, str) or len(name) < 2:
            return 'Invalid Name as length is <2'
        return 'Valid Name as length is >2'

# Test the class
# Create a new employee
emp1 = Employee("Kamal")
print(Employee.total_employees)  # Output: 1

# Increment total employees using the classmethod
print(Employee.increment_total_employees())  # Output: 2

# Validate names using the staticmethod
print(Employee.is_valid_name("Kamal"))  # Output: True
print(Employee.is_valid_name("K"))  # Output: False
print(Employee.is_valid_name(123))  # Output: False


class Product:
    total_product=0

    def __init__(self, name, price, stock):
        self.name=name
        self.price=price
        self.stock=stock
        

        Product.total_product+=1

    @classmethod
    def add_to_inventory(cls):
        cls.total_product+=1
        return cls.total_product
    @staticmethod
    def is_valid_price(price):
        if price<0:
            return 'Invalid Price its Negative'
        return 'Valid Price '
    
    def purchase(self, quantity):
        # Check if enough stock is available
        if self.stock >= quantity:
            self.stock -= quantity  # Reduce stock by the purchased quantity
            return f"Purchase successful! Remaining stock: {self.stock}"
        else:
            return "Purchase failed! Not enough stock."

# Create a product instance
product1 = Product("Socks", 20, 5)

# Test the methods
print(Product.total_product)  # Check total products
print(Product.is_valid_price(20))  # Validate price
print(product1.purchase(6))  # Purchase 2 items