import ctypes

class DynamicArrays:
    def __init__(self):
        self.n=0
        self.size=1
        self.array=self.__makearray(self.size)
    
    def __makearray(self,size):# _makearray() Method (Creating a Low-Level Array)
        return (size*ctypes.py_object)() #array objects refernece 
    def __str__(self): #[1,'hello',2,3.5,5,7]
        result='' # we kept result as empty string becasue , its end result which we need for
        for i in range(self.n):
            result=result+str(self.array[i])+','
        
        return '[' + result[:-1] + ']'
        
    def __resize(self,new_capacity):
        new_array=self.__makearray(new_capacity)
        self.size=new_capacity
        #copy the content of A to B
        for i in range(self.n):
            new_array[i] = self.array[i] 
        #Reassign Arrays:
        self.array=new_array
        #Update values
        self.capacity=new_capacity

    def append(self,item): # l.append(2) before that will ensure ki space is empty or not
        if self.n==self.size:
            self.__resize(self.size*2) # will call the  _resize function and will double the initial size:
        #append
        self.array[self.n]=item
        self.n = self.n + 1
    def __len__(self):
        return self.n
    #Indexing
    def index(self,item):#[1,2,3,4,5]
        for i in range(self.n):
            if self.array[i]==item:
                return i # 
            
        raise ValueError(f"{item} not found in the list")  # Proper error handling
    def pop(self):#[1,2,3,4,5]
        if self.n == 0:
            raise IndexError("pop from empty list")  # Raise proper error 
        self.n-=1
        item = self.array[self.n]
        self.array[self.n] = None
        return item # which values is poped must be displayed
    def clear(self):#[1,2,3,4,5]
        self.n=0
        self.size=1
    def insert(self, pos, item):
        if not 0 <= pos <= self.n:  # Validate index range
         raise IndexError("Invalid index")
        if self.size==self.n:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.array[i]=self.array[i-1]
        
        self.array[pos]=item
        self.n+=1
    
    def __delitem__(self,pos):#[1,2,5,2,3,4] delete arr[2]
            if 0<= pos < self.n:    
                for i in range(pos,self.n-1):
                    self.array[i]=self.array[i+1] # []
            self.n-=1
    
    def remove(self,item):
        pos=self.index(item)
        if type(pos)==int:
            #delete
            self.__delitem__(pos)
        else:
            return pos
    
    def sort(self):
        if not all(isinstance(self.array[i], (int, float)) for i in range(self.n)):
            return "TypeError: Cannot sort a list with mixed data types"
        for i in range(self.n):
            for j in range(0, self.n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
    def max(self,key=None):
        if self.n==0:
            raise ValueError('List is empty')
        max_value=self.array[0]
        for i in range(1,self.n):
            current_value=self.array[i]
            if key:       # I have't use these case in my life
                current_value = key(current_value)
            if current_value>max_value:
                max_value=current_value
        
        return max_value
    def min(self,key=None): #[1,5,2,3,4]
        if self.n==0:
            raise ValueError('List is empty')
        min_value=self.array[0]
        for i in range(1,self.n):
            current_value=self.array[i]
            if key:
                current_value=key(current_value)
            if current_value<min_value:
                min_value=current_value
        
        return min_value
    def sum(self):
        result=0
        for i in range(self.n):
            result+=self.array[i]
        return result
    def extend(self, iterable):
        new_size=self.n+len(iterable)
        if new_size>self.size:
            self.__resize(max(self.size * 2, new_size))  # Resize efficiently
            for item in iterable:
                if self.n == self.size:
                    self.__resize(self.size * 2)  # Resize if needed
                self.array[self.n] = item
                self.n += 1
    def negativeindex(self,index):#[1,2,3,4,5]
        if index<0:
            return self.array[self.n + index]
    def __getitem__(self,index):
        if isinstance(index,slice):
            start,stop,step=index.indices(self.n)
            new_list=DynamicArrays()
            #iterate through valid slic range:
            for i in range(start,stop,step):
                new_list.append(self.array[i])
            return new_list
        # Handle Single Index  cases
        elif 0<=index<self.n:
            return self.array[index]
        #Handle Negative index
        elif -self.n <= index < 0:  
            return self.array[self.n+index]
        # Handke out of bounds index
        else:
            raise IndexError['Index is out of range']
    
    def merge(self,items):
        if isinstance(items,list):
             for item in items:
                 self.append(item)
    
    
    






        

        

arr=DynamicArrays()
arr.append(1)
arr.append(5)
arr.append(2)
arr.append(3)
arr.append(4)

print(arr)
print(arr.n)
print(arr.index(5))
#print(arr.pop())
#print(arr)
# arr.clear()
# print(arr)
#arr.insert(1,2)
#print(arr)
#del arr[2]
#print(arr)
#arr.remove(2)
print(arr)
arr.sort()
print(arr)
print('Max Value is=',arr.max())
print('Min Value is=',arr.min())
print(arr.sum())
arr.extend([6, 7, 8])
print(arr)
print(arr.negativeindex(-3))
print(arr[0:2:1])
print(arr[::-1])
arr.merge([6,7,8])
print(arr)