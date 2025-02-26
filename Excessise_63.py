import random

def check(comp,user):
    if(comp==user):
        return 0
    if(comp==0 and user==1) or (comp==1 and user==2) or (comp==2 and user==0):
        return -1
    return 1
    
choices={0:'Snake',1:'Water',2:'Gun'}
comp=random.randint(0,2)

user=int(input('Chose 0 for Snake 1 for Water 2 for Gun: \n'))

score=check(comp,user)
print('Computer Choice is:',choices[comp])
print('User Choice is: ',choices[user])

if score == 0:
    print("It's a draw!")
elif score == -1:
    print("You lose!")
else:
    print("You won!")

    