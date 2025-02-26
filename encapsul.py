# class Acount:
#     def __init__(self,acc_no,acc_pass):
        
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#     def restPass(self):
#         print(self.__acc_pass)
    
# obj=Acount(1234,'Kamal@123')
# obj.restPass()


class Person:
    __name='anoymous'
    
    def __hello(self):
        print('hello person')

    def welcome(self):
        self.__hello()
        

p1=Person()
print(p1.welcome())
