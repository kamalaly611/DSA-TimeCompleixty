class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __mul__(self,scalar):
        return Vector(self.x*scalar.x,self.y*scalar.y)
        #return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    

spaceship_position = Vector(10, 20)
movement_vector = Vector(5, 3)  
spaceship_position = Vector(10, 20)
wind_vector = Vector(-2, 1)   
print(Vector.__mul__)
speed_multiplier = Vector(2,3)
# Calculate New scaled_movement
scaled_movement = movement_vector * speed_multiplier

new_position = spaceship_position + scaled_movement + wind_vector

print("Spaceship's New Position:", new_position)

class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name       # Item name/type (e.g., "Apple")
        self.price = price     # Price of one unit
        self.quantity = quantity  # Number of units

    # Overload + to combine quantities of the same item
    def __add__(self, other):
        if self.name == other.name and self.price == other.price:  # Same item, same price
            return CartItem(self.name, self.price, self.quantity + other.quantity)
        else:
            raise ValueError("Cannot combine items with different names or prices")

    # Overload * to calculate total cost
    def __mul__(self, _):
        return self.price * self.quantity

    def __str__(self):
        return f'{self.quantity} units of {self.name} @ ${self.price} each'

# Example Usage
item1 = CartItem("Apple", 10, 3)  # 3 units of Apple at $10 each
item2 = CartItem("Banana", 15, 2)  # 2 units of Banana at $15 each
item3 = CartItem("Apple", 10, 5)  # 5 more units of Apple at $10 each

# Combine item1 and item3
combined_item = item1 + item3
print("Combined Item:", combined_item)

# Calculate total cost of the combined item
total_cost_combined = combined_item * 1  # Multiplying by 1 just to trigger __mul__
print("Total Cost of Combined Item:", total_cost_combined)

