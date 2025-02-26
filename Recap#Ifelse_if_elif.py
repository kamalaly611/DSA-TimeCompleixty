num=int(input("Enter The applicant's credit score: "))
if num >= 700:
    print("Applicant is Eligible for the loan.")
elif 600 <= num <= 699:
    annual_revenue = input("Is the applicant's Annual Revenue Enough (yes/no)?: ")
    employment_status = input("Does the applicant have a current job (yes/no)?: ")
    
    if annual_revenue == 'yes' and employment_status == 'yes':
        print("You can still avail the loan.")
    else:
        print("Sorry, you can't take the loan at this moment.")
else:
    print("Loan is rejected directly.")

# Calulate the current time and display greet messages according to the time
import time

