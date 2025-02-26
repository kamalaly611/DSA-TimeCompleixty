class Employee:
    def setId(self,Id):
        self.Id=Id
        # whenever I  Have to initialize I have to call SetID method
    def getId(self):
        return self.Id 
#getter of Id method
    
# calling Side
E1=Employee()
E1.setId(100)
print(E1.getId()) 
print(E1)