#update()
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
#Removing items from dictionary:    
#clear():
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
#pop():
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
#popitem():
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

#del:
#we can also use the del keyword to remove a dictionary item.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
#If key is not provided, then the del keyword will delete the dictionary entirely.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)