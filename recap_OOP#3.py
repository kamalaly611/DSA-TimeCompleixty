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
        self.pay=int(self.pay*self.raise_amou)
        return self.pay
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amou=amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or  day.weekday()==6:
            return False
        
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)   

import datetime

my_date=datetime.date(2016,7,10)

print(Employee.is_work_day(my_date))

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_2)
print(new_emp_1.email)
print(new_emp_1.pay)

