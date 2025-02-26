class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def get_info(self):
        return f"Driver: {self.name}, Vehicle: {self.vehicle}"

class Passenger:
    def __init__(self, name):
        self.name = name

class Ride:
    def __init__(self, driver):
        self.driver = driver
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def start_ride(self):
        print(f"Ride started with {self.driver.get_info()} and passengers: {[p.name for p in self.passengers]}")

driver = Driver("Alice", "Tesla Model S")
ride = Ride(driver)
ride.add_passenger(Passenger("Bob"))
ride.add_passenger(Passenger("Charlie"))
ride.start_ride()
