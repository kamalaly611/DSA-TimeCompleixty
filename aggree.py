# FoodItem is a simple class (Composition)
class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name}: ${self.price}"

# Order contains multiple FoodItems (Composition)
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.food_items = []  # List of FoodItem objects
        self.status = "Pending" 
    """
   these method is for adding food method which will take object1 as refernce and will cross check isnstance or not

           """
    def add_food_item(self, food_item):
        if isinstance(food_item, FoodItem):# here food item is obje1 so its instance of Fooditme 
            self.food_items.append(food_item)# heree actuall objec1 is here 

    def update_status(self, new_status):
        self.status = new_status

    def get_order_details(self):
        items = [item.get_details() for item in self.food_items]
        return f"Order ID: {self.order_id}, Status: {self.status}, Items: {', '.join(items)}"

# Customer has multiple Orders (Aggregation)
class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []  # List of Order objects

    def place_order(self, order):
        if isinstance(order, Order):
            self.orders.append(order)# now self.orders.append(order_id=101) 

    def get_orders(self):
        return [val.get_order_details() for val in self.orders]

# Restaurant processes Orders (Aggregation)
class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.orders = []  # List of Order objects

    def process_order(self, order):
        if isinstance(order, Order):
            order.update_status("Completed")
            self.orders.append(order)
            print(f"Order {order.order_id} has been processed.")

# --------- TESTING THE SYSTEM ---------

# Creating food items
obj1 = FoodItem("Pizza", 12)
obj2 = FoodItem("Burger", 8)
obj3 = FoodItem("Pasta", 10)

# Creating an order and adding food items
order1 = Order(order_id=101)
order1.add_food_item(obj1)# now here obj1 is passed as reference to Order now it will add all object 1 behaveiou in food method:
order1.add_food_item(obj2)

order2 = Order(order_id=102)
order2.add_food_item(obj3)

# Creating a customer and placing orders
customer = Customer("John Doe")
customer.place_order(order1)
customer.place_order(order2)

# Creating a restaurant and processing an order
restaurant = Restaurant("Food Paradise")
restaurant.process_order(order1)

# Displaying customer orders
print("\nCustomer Orders:")
for details in customer.get_orders():
    print(details)

# Displaying processed orders in the restaurant
print("\nRestaurant Processed Orders:")
for order in restaurant.orders:
    print(order.get_order_details())
