# class Human:
#     def __init__(self,numheart):
#         self.eyes=2
#         self.numheart=numheart

#     def eat(self):
#         print('I can Eat')
#     def work(self):
#         print('I can work')

# class Male(Human):
#     def __init__(self, numheart,name,iddd):
#         super().__init__(numheart)
#         self.name=name
#         self.iddd=iddd


#     def sleep(self):
#         print('I can sleep whole day')
        
# class Boy(Male):
#     def __init__(self, numheart, name, iddd,gender):
#         super().__init__(numheart, name, iddd)
#         self.gender=gender
    
#     def __str__(self):
#         return f'Numheart: {self.numheart}, Name: {self.name}, ID: {self.iddd}, Gender: {self.gender}'

#     def work(self):
#         #Human.work(self)
#         super().work()
#         print('I can code')
# class Programmer:
#     def work(self):
#         print('I can Write Programms')



# boy_1=Boy(1,'Kamal',1234,'Male')
# boy_1.work()
# print(f'Eyes: {boy_1.eyes}')

# print(boy_1)

class Employee:
    
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
    def info(self):
        return f'Name: {self.name} Employee_id: {self.employee_id}'

class Developer(Employee):
    def __init__(self, name, employee_id, programming_languages):
        super().__init__(name, employee_id)
        self. programming_languages= programming_languages
        
    def info(self):
        return f'{super().info()} Languages{self.programming_languages}'

class Manger(Employee):
    def __init__(self, name, employee_id,team_size):
        super().__init__(name, employee_id)
        self.team_size=team_size
        
    def info(self):
        return f'{super().info()} Team-Size: {self.team_size}'

# class Techlead(Developer,Manger): My approach wrong.====>
#     def __init__(self, name, employee_id, programming_languages,team_size):
#         print('Init from joint')
#         Developer.__init__(self, name, employee_id, programming_languages)
#         Manger.__init__(self, name, employee_id, team_size)

#  chatgpt approach 
class Techlead(Employee):
    def __init__(self, name, employee_id, programming_languages, team_size):
        super().__init__(name, employee_id)
        self.programming_languages = programming_languages
        self.team_size = team_size

    def info(self):
        return f'{super().info()} | Languages: {self.programming_languages} | Team Size: {self.team_size}'

objc=Techlead('Kamal',123,'Python',22)
print(objc.info())
print(Techlead.mro())
    

    