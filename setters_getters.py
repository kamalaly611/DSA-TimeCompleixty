# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         #self.email=f'{self.fname}.{self.lname}@gmail.com'
        
#     def explain(self):
#         return f'This Employee is {self.fname} {self.lname}'
#     @property
#     def email(self):
#         return f'{self.fname}.{self.lname}@gmail.com'
#     @email.setter
#     def email(self,string):
#         print("Setting Now..........")
#         names=string.split('@')[0]
#         self.fname,self.lname=names.split('.')
        

# # Example usage
# obje = Employee('Kamal', 'Hussain')
# print(obje.email)  # Output: Kamal.Hussain@gmail.com
# print(obje.explain())  # Output: This Employee is Kamal Hussain

# obje.email = "this.that@codewithharry.com"
# print(obje.email)  # Output: this.that@gmail.com
# print(obje.explain())  # Output: This Employee is this that
##############################################################################################################################
# class Students:
#     def __init__(self,name,grade):
#         self.name=name
#         self._grade=grade
#     def get_grade(self):
#         #return self._grade
#         return self._grade
    
    
#     def set_grade(self, value):
#         if 0 <= value <= 100:  # Validation: grade must be between 0 and 100
#             self._grade = value
#         else:
#             raise ValueError("Grade must be between 0 and 100")
# # Example
# student = Students("Ali", 85)

# # Get the grade
# print(student.get_grade())  # Output: 85

# # Set a new valid grade
# student.set_grade(95)
# print(student.get_grade())  # Output: 95

# Try setting an invalid grade
# student.set_grade(150)  # This will raise a ValueError
# class User:
#     def __init__(self, username):
#         self.username = username
#         self._password = None  # Private attribute for password

#     @property
#     def password(self):
#         return self._password  # Getter to retrieve the password

#     @password.setter
#     def password(self, new_password):
#         if len(new_password) >= 8:
#             self._password = new_password
#         else:
#             print("Password must be at least 8 characters")

# # Create a User instance
# user = User("Kamal")

# # Set an invalid password
# user.password = "1234"  # Output: Password must be at least 8 characters
# print(user.password)

# # Set a valid password
# user.password = "Secure@123"

# # Get the password
# print(user.password)  # Output: Secure@123

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Use a private attribute to store salary

    @property
    def salary(self):
        return f"Salary of the Employee is {self._salary}"  # Access the private attribute

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            print("Sorry, salary cannot be negative")
        else:
            self._salary = amount  # Set the private attribute

# Test the Employee class
emp = Employee("Alice", 5000)

emp.salary = 8000  # Valid salary update
emp.salary = -2000  # Invalid salary, should show an error

print(emp.salary)  # Output: Salary of the Employee is 8000
