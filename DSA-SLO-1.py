import time

start=time.time() # these approach is not appreicated because not following startanderis 
for i in range(1,101):#can be differnt due to differnt specs of machines 
    print(i) # logic and algos differs so no realtion b/w time & input
end=time.time()-start
print(end)
import time
###############################################################################################
start=time.time()
def count_down(n):
    while n > 0:
        print(n)
        n -= 1
end=start-time.time()
count_down(8)
print(end)

###############################################################################################
def intStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    
    while i > 0:
        result = digits[i % 10] + result # digits[3]+ ''==> '3'+''
        
        i = i // 10  # Use integer division to properly remove the last digit
    
    return result  # Return after processing all digits 

print(intStr(123))  # Output: "123"
###############################################################################################
# time complexity O(n)
def fact(n):
    answer=1
    while n>1:
        answer *=n
        n-=1
    return answer
###############################################################################################
L = [1, 2, 3, 4, 5]
#i = 0 to len(L) - 1

for i in range(0, len(L)):  # o(n)
    # i+1 intially just take value no depend on outer loop i value
    for j in range(i + 1, len(L)):  # Inner loop
       #print("({}, {})".format(L[i], L[j]))  # Print pairs
        print(f'{L[i],L[j]}')

###############################################################################################
A=[1,2,3,4]
B=[2,3,4,5,6]
for i in A: #O(n)
     for j in B: #O(n)
         if i<j:   ## order of complexity will be O(n,m) or n~2 bcouz depend upon list elements &
             print("({}, {})".format(i,j))


###############################################################################################
A=[1,2,3,4]
B=[2,3,4,5]
for i in A: #O(n)
    for j in B:#O(n)
        for k in range(100000):
             print("({}, {})".format(i,j))
 #time-complexity 
###############################################################################################

L = [1, 2, 3, 4, 5]

for i in range(0, len(L) // 2):  # Loop runs for half of the list
    other = len(L) - 1 - i  # Find the corresponding element from the end
    temp = L[i]  # Store current element in temp
    L[i] = L[other]  # Swap elements
    L[other] = temp  # Complete the swap

print(L)  # Output: [5, 4, 3, 2, 1]
###############################################################################################
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1) #  O(n) because it take linear calls for inputs

print(fact(5))
###############################################################################################
def fib(n):
    if n-1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
          #here the input is add output is multilplied hence its exponetial behaviour


###############################################################################################
def power(num):
    if num < 1:
        return 0
    elif num ==1:
        print(1)
        return 1
    else: # here if we see when input is added the f.calls are decreased means its log functions
        prev =power(num//2)
        curr = prev*2
        print(curr)     #time-complexity is O(log)
        return curr
    
###############################################################################################
def mod(a,b):
    if b <= 0:
        return -1
    div=a//b #time complextiy is constant becasue there are no operations and loops recursions
    return a-div*b 

mod(5.3)

###############################################################################################
def sum_digits(num):
    sum = 0
    while (num > 0):
        sum+=num%10
        num//=10
    return sum # 
###############################################################################################
sum_digits(123)

#This is exponential time complexity, meaning the function grows very fast as 𝑛

# T(n)={3T(n-1) if n>0
#      {1, otherwise

###############################################################################################

def powerset(s, index=0, current_subset=None):
    """Generate the powerset of a given set using recursion."""
    if current_subset is None:
        current_subset = []
    
    if index == len(s):    #The function generates all subsets → 2`n` subsets


        return [current_subset]
    
    return powerset(s, index + 1, current_subset) + powerset(s, index + 1, current_subset + [s[index]])

# Example usage  
example_set = [1, 2, 3]
print(powerset(example_set))
