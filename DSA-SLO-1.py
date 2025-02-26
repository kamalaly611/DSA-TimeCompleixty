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
