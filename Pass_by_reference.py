class Coustmer:
    def __init__(self,name):
        self.name=name
    def greet(coust):
        #print('hello',coust.name)
        coust.name='chintu'
        print(coust.name)

cust=Coustmer('Kamal')
cust.greet()

print(cust.name)

def modify_list(lst):
    lst.append(4)
    print(lst)

my_list = [1, 2, 3]
modify_list(my_list)  

print("Original List after modification:", my_list)  

def modify_string(s):
  
    s += " World"  
    print("Modified String inside function:", s)

my_str = "Hello"

modify_string(my_str) 
print("Original String after modification:", my_str)  


#Collection of Custom Objects collection of objects. 
# This is a common approach in real-world scenarios, 
# such as managing customer records or handling product inventories.
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'I am {self.name} and I am {self.age} years old')

customers = [Customer('Kamal', 22), Customer('Mishi', 9), Customer('Fari', 4)]
for customer in customers:
    customer.intro()


