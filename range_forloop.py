expenses=[1200,1500,1300,1700] #these lines is for creating the list as expnese

total_expenses=0 #these varaible stores total expenese of all months and its firstly intialized as zero
for i in range(len(expenses)): # now these is for lopp which will first take length of list and than range will be set from 0 to 3 and it will iterate
    expense=expenses[i] # now expenses[i] is the indices of each element in the list and it has assinged the values to expense 
    print(f'Months {i+1}, expenses: {expense}') # now we have used 'f string to print the expenese from month 1 to 4 
    total_expenses +=expense # now we have add total expense to expnese of each iteration for the final sum of t
print("Total expnese", total_expenses)
print(expense)