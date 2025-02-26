class Car:
    def __init__(self,model,brand,color):
        self.brand=brand
        self.model=model
        self.color=color
    #Method Descripe the car Engine Starting:
    def start_engine(self):
        return f"The {self.color} {self.brand} {self.model}'s Engine Has started"

# Create the car Object:
my_car=Car('Fortuner','Toyta','White')
print(my_car.model)
print(my_car.brand)
print(my_car.color)
print(my_car.start_engine())

# Create The Second Car Object:
my_new_car=Car('Benz ','Mercedes','Gray')
print(my_new_car.model)
print(my_new_car.brand)
print(my_new_car.color)     
print(my_new_car.start_engine())
