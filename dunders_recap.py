class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    # Comparison based on price
    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price

    # Adding two products to create a bundle
    def __add__(self, other):
        bundle_name = f"{self.name} + {other.name}"
        bundle_price = self.price + other.price
        bundle_rating = round((self.rating + other.rating) / 2, 2)  # Average rating
        return Product(bundle_name, bundle_price, bundle_rating)

    # Displaying product details
    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Rating: {self.rating}"

# Example Usage
if __name__ == "__main__":
    product1 = Product("Laptop", 1000, 4.5)
    product2 = Product("Tablet", 500, 4.2)

    # Comparing products
    print(product1 > product2)  # True
    print(product1 == product2)  # False

    # Creating a bundle
    bundle = product1 + product2
    print(bundle)  # Product: Laptop + Tablet, Price: $1500, Rating: 4.35

    # Displaying individual products
    print(product1)  # Product: Laptop, Price: $1000, Rating: 4.5
    print(product2)  # Product: Tablet, Price: $500, Rating: 4.2
