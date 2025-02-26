#How to create tuples in

tup=(12,13,14,15)
tup2=("Red","Blue","Green", "Yellow")
print("These is an tuple", tup)
print("These is an tuple", tup2)
print("These is for Tuple1",type(tup),"These is for Tuple2",type(tup2))

#Tuple Indexes with postive indexing

print(tup[0])
print(tup[1])
print(tup[2])
#Tuple with negqative indexing 
print(tup2[-1])
print(tup2[-2])
print(tup2[-3])

#Range of Index:
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
#operation of tuple:

tup3=("Red","Blue","Green", "Yellow")
temp=list(tup3)
temp.append("Russian")
temp.pop(3)
temp[2]="Fariyal"
tup3=tuple(temp)
print("Here is the updated tuple",tup3)
#concatenate two tuples without converting them to list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# Count Method for Tuple():
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print('Count of 3 in Tuple1 is:', tuple1.count(1))
