x = [1, 2, 3, 4]
y = {'A': 1, 'B': 2}

print(dir(x))
print(dir(y))
print(help(x.reverse))
print(help(y.fromkeys))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=Person('Kamal',22)
print(obj.__dict__)

x=[1,2,5,6,7]
help(x.sort)

class Car:
    wheels=4
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        return f'The Brand of car is {self.brand} and Model is {self.model}'
    
obj=Car('ODI',128)
print(obj.display())
print(dir(Car))
print(obj.__dict__)
# help(Car)
class Employee:
    def __init__(self, name, idd):
        self.name = name
        self.idd = idd

    def get_details(self):
        print(f'Name of Employee is {self.name} and their ID is {self.idd}')

class Manager(Employee):  # Fixed spelling from Manger to Manager
    def __init__(self, name, idd, department):
        super().__init__(name, idd)
        self.department = department

    def get_details(self):
        # Call the base class method to print basic details
        super().get_details()
        # Add the department info
        print(f'Department: {self.department}')

# Create objects and display details
obj_1 = Employee('Kamal', 123)
obj_1.get_details()

obj_2 = Manager('Ali', 1222, 'IT')
obj_2.get_details()


class Employee:
    def __init__(self,name,idd):
        self.name=name
        self.idd=idd
    
    def get_details(self):
        return f'Name of Employee is {self.name} and his ID is {self.idd}'
class Manger(Employee):
    def __init__(self,name,idd,department):
            super().__init__(name,idd)
            self.department=department
        
        
    def get_details(self):

        print(f"{super().get_details()}, Department: {self.department}")

obj_1=Employee('Kamal',123)
print(obj_1.get_details())
obj_2=Manger('Ali',1222,'IT')
obj_2.get_details()