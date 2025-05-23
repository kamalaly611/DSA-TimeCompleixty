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
        #return "[" + ", ".join(str(self.A[i]) for i in range(self.n)) + "]"
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

 
# loop iterates through ith to n-1  
        # what if we don't have empty string in intial so the last result will be
        #

    def __getitem__(self, index):
        if isinstance(index, slice):
            # Handle slicing
            start, stop, step = index.indices(self.n)  # Get start, stop, step from slice object
            sliced_list = Mylist()  # Create a new Mylist to store the sliced elements
            for i in range(start, stop, step):
                sliced_list.append(self.A[i])
            return sliced_list
        elif 0 <= index < self.n:
            return self.A[index]
        elif -self.n <= index < 0:
            return self.A[self.n + index]  # Handle negative indexing
        else:
            return 'IndexError: Index out of range'

        
    def append(self,item): # if the size and n are equal than  the array will be resizes:::
         if self.n==self.size:
             #resize
             self._resize(self.size*2) # will call the  _resize function and will double the initial size:

        #append 
         self.A[self.n] = item 
         self.n = self.n + 1
    def pop(self):
        if self.n == 0:
            return '[]'  
        popped_value = self.A[self.n - 1]
        self.n -= 1
        return popped_value  # Return instead of print
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
            print('Yes size was full so resize happens')
            self._resize(self.size*2)
        
        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        
        self.A[pos]=item
        self.n += 1
    def remove(self, item):
        pos = self.find(item)
        if isinstance(pos, int):  # Ensure valid index
            self.__delitem__(pos)
        else:
            raise ValueError(f"{item} not found in list")

    
    def __delitem__(self,pos):
        #delete 
        if 0<=pos<self.n:

            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
        
            self.n-=1
    def sort(self):
        try:
            for i in range(self.n):  # Outer loop runs n times
                for j in range(0, self.n - i - 1):  # Inner loop runs (n-i-1) times
                    if self.A[j] > self.A[j + 1]:  # Compare adjacent elements
                        self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]  # Swap elements
        except TypeError:
            return "TypeError: Cannot sort a list with mixed data types"
    
    def min(self):
        if self.n == 0:
            return "ValueError: List is empty" #[1,2,3,4,5]

        if not all(isinstance(item, (int, float)) for item in self.A[:self.n]):
            return "TypeError: Cannot find min in a list with mixed data types"

        min_value = self.A[0]  # Assume the first element is the smallest
        for i in range(1, self.n):
            if self.A[i] < min_value: 
                min_value = self.A[i]
        return min_value

    def max(self):
        self.sort()
        if isinstance(self.A[self.n-1], (int, float)):
            return self.A[self.n-1]
        else:
            return "TypeError: Cannot sort a list with mixed data types"
        
    def sum(self):
        result=0
        for i in range(self.n):
            result=result+self.A[i] #[1,2,3,4,5]
        return result
    def extend(self, iterable):
        for item in iterable:
            self.append(item)
    
    def negativeIndexing(self, index):
        if index < 0:  # Convert negative index to positive
            
            return self.A[self.n + index]
    def merge(self, other):
        """
        Merges the current Mylist with another Mylist.
        :param other: Another Mylist object to merge with.
        :return: A new Mylist containing elements from both lists.
        """
        # Create a new Mylist to store the merged result
        merged_list = Mylist()

        # Append all elements from the current list
        for i in range(self.n):
            merged_list.append(self.A[i])

        # Append all elements from the other list
        for i in range(other.n):
            merged_list.append(other.A[i])

        return merged_list
        
    
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
print('Self.n==',L.n)
print(L)
# print(L[4])
print(L.pop())
print(L)    
#print(L.clear())
print(L)
print(L.find(4.5))        
L.insert(0,0)
print(L)        
L.insert(1,'Khalid')
print(L)
L.__delitem__(2)  # Delete at index 2
print("After Deletion at index 2:", L)
L.__delitem__(300)  # Delete at index 2
print(L)
print('After the Remove Item')
L.remove(4.5)
L.remove('Khalid')
L.remove('hello')
L.remove(False)
L.remove(False)
L.append(5)
L.append(4)
L.append(3)
L.append(2)
L.append(1)

print(L)
L.sort()
print(L)
print(L.min())
print(L.max())
print(L.sum())
#L.extend([3, 4, 5])
#print(L)  # Output: [1,2,3,4,5]
print(L.negativeIndexing(-1))
# Slicing examples
print("Slice(1, 4):", L[1:4])  # Output: [2, 3, 4]
print("Slice(None, None, -1):", L[::-1])  # Output: [5, 4, 3, 2, 1] (Reverse)
print("Slice(-4, -1):", L[-4:-1])  # Output: [2, 3, 4]
print("Slice(0, 5, 2):", L[0:5:2])  # Output: [1, 3, 5]
L2 = Mylist()
L2.append(4)
L2.append(5)
L2.append(6)
print(L2)

merged = L.merge(L2)
print("Merged List:", merged)  # Output: [1, 2, 3, 4, 5, 6]