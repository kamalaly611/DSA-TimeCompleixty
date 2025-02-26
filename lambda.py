# Creating Lambda Functions:
# Checking Even or odd number using Lamdda functions
even_odd=lambda x:'Even' if x%2==0 else 'Odd'
print(even_odd(8))
# Three cases using Tradtional function def ,
l=[2,4,34,5,6]
def return_lis(l):
    evem_sum=0
    odd_sum=0
    div_3=0
    for i in l:
        if i%2==0:
            evem_sum=evem_sum+i
        if i%2!=0:
            odd_sum=odd_sum+i
        if i%3==0:
            div_3=div_3+i
    return(evem_sum,odd_sum,div_3)        

result = return_lis(l)
print(result) 
# Checking For HOFS way
print('Checking For HOFS way')
def return_lis(func,l):
    result=0
    for i in l:
        if func(i):
            result=result+i
    return result
            
l=[2,4,34,5,6]    

x=lambda x:x%2==0
y=lambda x:x%2!=0
z=lambda x:x%3==0

print(return_lis(x,l))
print(return_lis(y,l))
print(return_lis(z,l))

# How Map works: Map Func expects first an lambda function and iterator
l=[2,4,5,6,7,8]
x=list(map(lambda x:x*2,l))
print(x)
# Checking Even List using Map function
l=[2,4,5,6,7,8]
x=list(map(lambda x:x%2==0,l))
print(x)
# Checking for List Attributes in Dictiorary:
people = [
    {"name": "Ali", "father_name": "Ahmed", "address": "1234 Street, City, Country"},
    {"name": "Sara", "father_name": "Hassan", "address": "5678 Avenue, City, Country"},
    {"name": "Zain", "father_name": "Bilal", "address": "91011 Road, City, Country"}
]

x=list(map(lambda people:people['name'],people))
y=list(map(lambda people:people['address'],people))
z=list(map(lambda people:people['father_name'],people))
print('Names are:=',x)
print('Address are:=',y)
print('father_names are:=',z)
# Filters proferms iterable based on the given coditions:
num=[232,3,5,68,53,6,8,5,9]
x=list(filter(lambda numbers:numbers<9,num))
print(x)
#reduce() is a function in Python that repeatedly applies a given function 
# to the elements of an iterable, combining them into a single value.
import functools
num=[232, 3, 5, 68, 53, 6, 8, 5, 9]
x=functools.reduce(lambda x,y:x+y,num)
print('Redce Code',x)
y=functools.reduce(lambda x,y:x if x<y else y,num)
print('Reduce Becomes',y)
#  firstly it will compare 232 wit 3 condition says 3 is less
# Now between 3 and 5 coditions says 3 is less so x=3
# now between 3 and 68 coditions says 3 is less so x=3
# now between 3 and 53 coditions says 3 is less so x=3
# now between 3 and 6 coditions says 3 is less so x=3
# now between 3 and 8 coditions says 3 is less so x=3
# now between 3 and 5 coditions says 3 is less so x=3
# now between 3 and 9 coditions says 3 is less so x=3
# So Finally values becomes 3 it reduces step by step









