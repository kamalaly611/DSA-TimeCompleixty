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
    def append(self,item): # if the size and n are equal than  the array will be resizes:::
         if self.n==self.size:
             #resize
             self._resize(self.size*2) # will call the  _resize function and will double the initial size:

        #append 
         self.A[self.n] = item 
         self.n = self.n + 1
    
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

print(len(L))
    

        
        
