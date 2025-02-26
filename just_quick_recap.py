def hello(greet,name='You'):
    return f'{greet} {name}, Function'

print(hello('Hi',name='Kamal'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

course=['Math', 1, 'English,2']
info={'name': 'Kamal', 'age': 22}
student_info(*course,**info)
print(type(course))





# Function Definition:
def calSum(a,b):# Parameters
    sum=a+b
    # print(sum)
    return sum

summ=calSum(2,7)#Function Calling with parameters
print(summ)

n = 5  # Example number
result = 1  # Start with 1 since multiplying by 1 doesn't change the value

for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    result *= i  # Multiply the current result by i

print(f"The factorial of {n} is {result}")  # Output the result
PKR=275
def convergen(n):
    return n*PKR

convergen(10) 

def show(n):
    if(n-1==-1):
        return
    print(n)
    show(n-1)
    for i in range(1,6):
        print(i)

show(3)

def calc_sum(n): 
     if (n == 0): 
         return 0
     else:
         print(f' Current Recursion at {n}')
         result=calc_sum(n-1) + n
         print(f' Current Recursion after sum at {n}')    
         return result
     
sum = calc_sum(5) 
print(sum)