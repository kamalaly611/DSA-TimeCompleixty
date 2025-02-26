class Math:
    def __init__(self,num):
        self.num=num
    def addtoNum(self,n):
        self.num=self.num+n
    
    @staticmethod
    def add(a,b):
        return a+b
    
a=Math(7) # Object Created 
a.addtoNum(9)
print(a.num)
print(a.add(8,7))