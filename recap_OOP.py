# class Car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def full(self):
#         return f'This the car named as {self.brand} and color is {self.color}'

# obj=Car('Mercedes','Black')
# print(obj.brand)
# print(obj.color)
# # initializing another object:
# # obj_2=Car('Toyotta','White')
# # print(obj.brand)
# # print(obj.color)
# print(obj.full())

class Employee:
    num_of_emp=0
    raise_amou=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=f'{first}.{last}@gmail.com'

        Employee.num_of_emp=+1

    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay=int(self.pay*Employee.raise_amou)
        return self.pay


print('Before Insitating',Employee.num_of_emp)
emp_1=Employee('Kamal','Hussain',60000)
emp_2=Employee('Fariya','Wali',3000)
# print(emp_1.email)
# print(emp_1.fullname())
# print(Employee.raise_amou)
# print(emp_1.raise_amou)
# print(emp_2.raise_amou)
emp_1.raise_amou=1.05

print(emp_1.raise_amou) # Hence we can get the valriable of class through ins
print(Employee.raise_amou)
#emp_1.apply_raise()
print(emp_2.raise_amou)
print(Employee.num_of_emp)