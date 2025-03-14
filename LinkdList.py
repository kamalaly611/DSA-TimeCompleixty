#its linear Data Structures:
#first we will make a single Node

# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None
# a=Node(1)
# b=Node(2)
# c=Node(3)
# a.next=b
# b.next=c
# c.next=None

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkdList:
    def __init__(self):
        self.head=None
        self.n=0
    
    def __len__(self):
        #Returns the number of Nodes in the linkdList:

        return self.n
    def insert_head(self,value):
         #new node
         new_node=Node(value)

         #Create connection
         new_node.next=self.head
         
         #Reassign Head
         self.head=new_node
         #increament n
         self.n+=1
    def __str__(self):

        curr = self.head

        result = ''

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]








L=LinkdList()

print(len(L))
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(len(L))
print(L)
    
