# import sys

# L=[]
# for i in range(100):
#     print(f'{i} Bite,{sys.getsizeof(L)}')
#     L.append(i)

###############################################################################################
import ctypes

class Mylist:
    def __init__(self):
        self.size=1
        self.n=0
        # create a C type ka array with size -> self.size
        self.A=self.__make_array(self.size)
    def __len__(self):
        return self.n 
    
    def __str__(self):
        #[1,2,3]
        result=''
        for i in range(self.n):
            result=result+str(self.A[i]) + ','# loop iterates through ith to n-1  
        # what if we don't have empty string in intial so the last result will be
        #
        return '[' + result[:-1] + ']'
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return 'index is out of range'

        
    def append(self,item): # if the size and n are equal than  the array will be resizes:::
         if self.n==self.size:
             #resize
             self._resize(self.size*2) # will call the  _resize function and will double the initial size:

        #append 
         self.A[self.n] = item 
         self.n = self.n + 1
    def pop(self):
        if self.n==0:
            return '[]'
        print(self.A[self.n-1 ])
        self.n=self.n-1
    def clear(self):
        self.n=0
        self.size=1
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return 'ValueError -Not in List'
    def insert(self,pos,item):
        if self.n==self.size:
            self._resize(self.size*2)
        
        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        
        self.A[pos]=item
        self.n=self.n+1

    
    
    def _resize(self,new_capcity):
        #crete a new array with  new capcity
        B=self.__make_array(new_capcity)
        self.size=new_capcity
        #copy the content of A to B
        for i in range(self.n):
            B[i]=self.A[i]
        #reAssign A
        self.A=B
            
    def __make_array(self,capcity):
        return (capcity*ctypes.py_object)()

L= Mylist()

L.append(1)
L.append('hello')
L.append(False)
L.append(4.5)
L.append('Hey')

# print(L)
# print(L[4])
print(L.pop())
print(L)    
#print(L.clear())
print(L)
print(L.find(4.5))        
print(L.insert(0,0))
print(L)        
print(L.insert(1,'Khalid'))
print(L)        