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
        # self.head = None
        # self.tail = None  # Maintain tail pointer

class LinkdList:
    def __init__(self):
        self.head=None
        self.n=0
    
    def __len__(self):
        #Returns the number of Nodes in the linkdList:

        return self.n
    #now Insering Head at  Begining
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
    
    # These will append the new node at
    def append(self,value):
        new_node=Node(value)
        
        if self.head==None:
            #empty list
            self.head=new_node
            self.n+=1
            return 
        
        curr=self.head
        
        while curr.next!=None:
            curr=curr.next
        
        #you are at the last Node
        curr.next=new_node
        
        #Increament self.n because a new value added
        self.n+=1

        # new_node = Node(value)
        # if self.head is None:
        #     self.head = new_node
        #     self.tail = new_node  # Update tail
        # else:
        #     self.tail.next = new_node  # Directly append
        #     self.tail = new_node  # Update tai
    #4 → 3 → 2 → 1 → None
    def insert_after(self,after,value):
        #Head → [4] → [3] → [2] → [1] → None

        new_node=Node(value)
        #[100] → None
        
        curr=self.head # curr=4
        while curr != None:
            if curr.data==after: #curr = 4 (not 3, move to next) --curr = 3 (match found, break loop)
                break
            curr=curr.next
        print(curr.data)     # so works perfectly for single list Node
        #case 1 break item found
        if curr !=None:
            new_node.next=curr.next
            curr.next=new_node
            self.n+=1
            
        #case 2 loop run complete --> item ! found->curr->None
        else:
            return 'item Not found'
    
    def clear(self):
        self.head=None
        self.n=0
    
    def delHead(self):
        if self.head==None:
            return 'Empty LinkList'
        self.head=self.head.next
        self.n -= 1  # Decrement node count
        
    def pop(self):
        if self.head==None:
            return 'Empty Linkdlist' 


        curr=self.head
        if curr.next==None:
            return self.delHead()
      
        while curr.next.next !=None:
            curr=curr.next
        #now curr.next at 2nd last Node 
        curr.next=None #5->4->3->300->2->1->5->None:
        self.n-=1




        








L=LinkdList()

#print(len(L))
# L.insert_head(1)
# L.insert_head(2)
# L.insert_head(3)
# L.insert_head(4)
#print(len(L))
print(L)
#L.append(5)
print(L)
#L.insert_head(5)
print(L)
#L.insert_after(3,300)
print(L)
# L.clear()
# print(L)
# print(L.delHead())
print(L.pop())

