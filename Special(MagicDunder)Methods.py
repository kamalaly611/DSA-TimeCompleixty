class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def __str__(self):
        return f'{self.name} Costs ${self.price}'
    def __repr__(self,):
        #return f'Product(name='{self.name}', price={self.price})'
        return f"Product(name='{self.name}', price={self.price})" 
# Create Objects
p=product('Laptop',1200)

# Outputs
# print(str(p))  # Laptop costs $1200 (user-friendly output)
# print(repr(p)) # Product(name='Laptop', price=1200) (debugging output)
print(p)
##########################################################################################################
class Person:

    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):        
        return self.name.split()[-1]    

    def giveRaise(self, percent):
        self.pay = float(self.pay * (1 + percent))

    def __repr__(self): # or __str__
        return f'[Person: {self.name}, {self.pay}]'


# Code not automatically run when imported into another module  
if __name__ == '__main__':

    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(sue.name, sue.pay)
   
    sue.giveRaise(.10)                    # instead of hardcoding
    print('$%0.2f'% sue.pay)

    print(sue)