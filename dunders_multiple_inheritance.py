class Book:
    def __init__(self,title, author, publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
    def desribe(self):
        return f'The {self.title} is written by {self.author} in year of {self.publication_year}'
    
    def is_available(self,other):
        if other == self.title:
            return f'Yes'
        return f'No'
class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre):
        # Call the parent class's constructor to initialize common attributes
        super().__init__(title, author, publication_year)
        self.genre = genre

    def is_available(self,other):
        # Use the parent class's is_available method to return True or False
        if super().is_available(other) == 'Yes':
            return True
        return False

    def describe(self):
        # Extend the parent class's describe method to include the genre
        parent_description = super().describe()
        return f"{self.genre} | {parent_description}"

class nFictionBook(Book):
    def __init__(self,title, author, publication_year,subject):
        super().__init__(title, author, publication_year)
        self.subject=subject
        
        # super().is_available(other)
        def is_available(self,other):
            
            if other == self.subject:
                return 'Yes, it\'s Famous'
            elif other in ['Alchesmist', 'Fourty Rules']:
                return 'Yes, it\'s Famous'
            return 'Not Famous'
        
        #return f'Not Famous'
        # var4==super().desribe()
        # return f'The {self.title} is written by {self.author} in year of {self.publication_year} and subject is {self.subject}'
        

obj1=Book('Alchesmist','Khalid',2009)
print(obj1.desribe())
print(obj1.is_available('Alchesmist'))
obj2=FictionBook('Marvouls','Kamal',2010,'Sad')
print(obj2.is_available('Sad'))
print(obj2.desribe())
obj3=nFictionBook('Fourty','Mishi',2009,'English')
print(obj3.is_available('English'))
    