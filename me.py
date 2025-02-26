class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def double_size(self):
        # Explicitly create a new Rectangle with doubled dimensions
        return Rectangle(self.length * 2, self.width * 2)

rect1 = Rectangle(5, 10)
rect2 = rect1.double_size()  # Creates a new Rectangle


class Product:
    def __init__(self,name,quatity,price):
        self.name=name
        self.quatity=quatity
        self.price=price
    
    def __add__(self,other):
        if self.name == other.name:
             return Product(self.name, self.quatity + other.quatity, self.price)
        else:
            raise TypeError("Cannot combine products with different names!")
            
    def __gt__(self, other):
        if isinstance(other, Product):
            return (self.quatity * self.price) > (other.quatity * other.price)
        else:
            raise TypeError("Comparison must be between two Product instances!")
    def __str__(self):
        return f"{self.name} - Quantity: {self.quatity}, Price: ${self.price}"
        
# Create product instances
p1 = Product("Laptop", 5, 1000)
p2 = Product("Laptop", 3, 1000)
p3 = Product("Phone", 10, 500)

# Add quantities of the same product
combined = p1 + p2

# Compare total values of products
if p3 > combined:
    print("Phones are worth more than laptops!")
else:
    print("Laptops are worth more than phones!")

# Print combined product details
print("\nCombined Product:")
print(combined)


class Book:
    def __init__(self,title,author,copies):
        self.title=title
        self.author=author
        self.copies=copies
    
    def __add__(self, other):
        if isinstance(other, Book) and self.title == other.title and self.author == other.author:
            return Book(self.title, self.author, self.copies + other.copies)
        else:
            raise TypeError("Cannot combine books with different titles or authors!")
            
    def __sub__(self, value):
        if isinstance(value, int):
            if self.copies >= value:
                return Book(self.title, self.author, self.copies - value)
            else:
                raise ValueError("Cannot remove more copies than available!")
        elif isinstance(value, Book):
            if self.title == value.title and self.author == value.author:
                return Book(self.title, self.author, max(0, self.copies - value.copies))
            else:
                raise TypeError("Cannot subtract copies of different books!")
        else:
            raise TypeError("Subtraction only supports integers or books!")            
            
            
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    

    def __str__(self):
        return f'{self.title} {self.author} {self.copies}'


book1 = Book("Python Programming", "John Doe", 5)
book2 = Book("Python Programming", "John Doe", 3)
book3 = Book("Machine Learning", "Jane Smith", 7)

new_stock = book1 + book2
print("Adding New Stock:")
print(new_stock)
print('Removing New stock!')
remaing_item=new_stock-2
print(remaing_item)
print('Checking Books can not have same title or author')
print(book1==book2)



class Wallet:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def __add__(self,value):
        if isinstance(value,Wallet):
            return Wallet(self.owner,self.balance+value.balance)
        else:
            raise TypeError("Cannot combine Wallet !")
    def __sub__(self, value):
        if isinstance(value, (int, float)):  # Deduct a specific amount
            if self.balance >= value:
                return Wallet(self.owner, self.balance - value)
            else:
                raise ValueError("Insufficient balance!")
        elif isinstance(value, Wallet):  # Transfer funds between wallets
            if self.balance >= value.balance:
                return Wallet(self.owner, self.balance - value.balance)
            else:
                raise ValueError("Insufficient balance to transfer!")
        else:
            raise TypeError("Invalid type for subtraction!")

    def __eq__(self,val):
        if isinstance(val,Wallet):
            return self.balance == val.balance
        return False
            
    
    def __str__(self):
        
        return f"Owner: {self.owner}, Balance: {self.balance}"
        

# Create wallet instances
wallet1 = Wallet("Alice", 1000)
wallet2 = Wallet("Bob", 500)

# Combine wallets
combined_wallet = wallet1 + wallet2
print(combined_wallet)  # Owner: Alice, Balance: 1500

# Transfer funds
wallet_1 = wallet1 - 300
wallet_2 = wallet2 - 200
print(wallet_1)  # Owner: Alice, Balance: 700
print(wallet_2)  # Owner: Bob, Balance: 300

# Compare wallets
if wallet1 == wallet2:
    print("Wallets have the same balance!")
else:
    print("Wallet balances are different!")
