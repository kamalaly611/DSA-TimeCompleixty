class Battery:
    def __init__(self, capacity):
        self.capacity = capacity  # Initialize battery capacity

class Laptop:
    def __init__(self):
        self.battery = Battery(5000)  # Composition: Battery is created inside Laptop

    def show_battery_info(self):
        print(f"Laptop Battery Capacity: {self.battery.capacity} mAh")

# Creating a Laptop instance
my_laptop = Laptop()
my_laptop.show_battery_info()
