#Python Dictionaries
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

#Accessing Dictionary items:
#I. Accessing single values:
#Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
#Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
#II. Accessing multiple values:
#We can print all the values in the dictionary using values() method.
#Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
#III. Accessing keys:
#We can print all the keys in the dictionary using keys() method.
#Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
#IV. Accessing key-value pairs:
#We can print all the key-value pairs in the dictionary using items() method.
#Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  