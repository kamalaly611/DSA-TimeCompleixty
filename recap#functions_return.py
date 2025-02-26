import math
def add(a,b):
    add=a+b
    print("Operation is Add",add)
a=9
b=3
add(a,b)

def subs(a,b):
    subs=a-b
    print("Operation is Substraction",subs)

a=a
b=3
subs(a,b)

def div(a,b):
    div=a/b
    print("Operation is Divide",div)

a=9
b=3
div(a,b)

def mul(a,b):
    mul=a*b
    print("Operation is Multiplication",mul)

a=9
b=3
mul(a,b)

def Expo(a,b):
    poweer=a**b
    print("Operation is Exponential",poweer)

a=9
b=3
Expo(a,b)

def Mod(a,b):
    Modulo=a%b
    print("Operation is Mod",Mod)

a=9
b=3
Mod(a,b)

def squ(a):
    square= math.sqrt(a)
    print("Operation is Suaqreroot",square)

a=9
squ(a)

def floor(a,b):
    result = a // b  # Floor division
    print("Operation is floor",result)

a=9
b=3
floor(a,b)
