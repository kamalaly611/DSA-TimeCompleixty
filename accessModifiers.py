class Std:
    def __init__(self,name,rollno,age):
        self.name=name #Public Attrubute
        self._rollno=rollno# Protected Attrubute
        self.__age=age#private Attrubute
    def display(self):
        print(f'Im {self.name} from Stduent class')
    
class Branch(Std):
    def __init__(self,name,rollno,classer,age):
        super().__init__(name,rollno,age)
        self.classer=classer
        super().display()
    def display(self):
            return f'Im {self.name} rollno is {self._rollno} and class {self.classer} and my age is {self._Std__age}'
        

b1=Std('Kamal',123,6)
b2=Branch('Mishi',7,'12th',9)
print(b1.name)
print(b1._rollno)
print(b2._Std__age)
print(b2.display())

##############################################################################################
class Car():
     def __init__(self,windows,doors,enginetype):
          self.windows=windows
          self.doors=doors
          self.enginetype=enginetype
          
     