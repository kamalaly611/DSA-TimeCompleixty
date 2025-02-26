class Employee:
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=f'{self.first}.{self.last}@email.Com'
        self.pay=pay
    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt=1.10

    def __init__(self,first,last,pay,prog_lang):
        super(). __init__ (first,last,pay) # its for handling single inheritance 
        #Employee. __init__ (self,first,last,pay) if wants to handle multiple inheritance
        self.prog_lang=prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
         super(). __init__ (first,last,pay) # its for handling single inheritance   
         if employees is None:
            self.employees=[]
         else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())



dev_1=Developer('Kamal','Hussain',50000,'Python-Programming')
dev_2=Developer('Test','ward',60000,'Cpp-Programming')

mgr_1=Manager('Kamal','Hussain',70000,[dev_1])
# print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
print(isinstance(mgr_1,Developer))
print(issubclass(Developer,Employee))



print(dev_1.email)
print(dev_2.prog_lang)
dev_1.apply_raise()
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)



print(help(Developer))

class Emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f'The name of Employee : {self.id} is {self.name}')
class Pro(Emp):
    def showlanugae(self):
        print('The lanuage is Java and rubby Nails:')

e1=Emp('Kamal',302)
e1.showDetails()
e2=Emp('Mishi',102)
e2.showDetails()
e2.showlanguage()