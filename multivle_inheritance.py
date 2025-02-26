class Vehicle:
    def __init__(self,fule_type):
        self.fule_type=fule_type
        
    def start(self):
        print( f"Vehicle started Charging with {self.fule_type}.")
        

# Parent class 2
class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity
        print("Charging the vehicle.")
    def charge(self):
        print(f'Charging the vehicle with {self.battery_capacity}')

class HybridCar(Vehicle, ElectricVehicle):
    def __init__(self, fuel_type, battery_capacity):
        # Initialize both parent classes
        Vehicle.__init__(self, fuel_type)  # Initialize Vehicle
        ElectricVehicle.__init__(self, battery_capacity)  # Initialize ElectricVehicle

    def switch_mode(self):
        print("Switched to hybrid mode.")


obj = HybridCar("Petrol", "50 kWh")
obj.start()
obj.charge()
obj.switch_mode()