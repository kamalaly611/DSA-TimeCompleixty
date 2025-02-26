class Employee:
    num_of_emp=0
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=f'{first}.{last}@Comany.Com'
        Employee.num_of_emp+=1

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_arise(self):
        self.pay=int(self.pay*self.raise_amount)


print(Employee.num_of_emp)

emp_1=Employee('Kamal','Hussain',50000)
emp_2=Employee('Test','User',6000)

# print(emp_1.pay)
# emp_1.apply_arise()
# print(emp_1.pay)
# emp_1.raise_amount=1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
print(Employee.num_of_emp)


    