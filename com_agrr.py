class Libary:
    def __init__(self,name):
        self.name=name
        self.books=[]
        self.members=[]

    def add_book(self,book):
        if isinstance(book, Books) and book not in self.books:
            self.books.append(book)
            
    
    def add_member(self,member):
         if isinstance(member, Member) and member not in self.members:
            self.members.append(member)
            
    
    def list_books(self):
        list_books = []
        for book in self.books:
            if book.available:  # Only list available books
                list_books.append(book.title)
        return list_books

        
    def update_book_status(self, book, status):
        if book in self.books and isinstance(status, bool):
            book.available = status
    
    def is_book_available(self, book):
        return book in self.books and book.available

class Books:
    def __init__(self,title,author,isbn,available=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available = available
    
    def get_details(self):
        return f'Title: {self.title} Author: {self.author} Avialable:{self.available} ISBN: {self.isbn}'
    
class Member:
    
    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]
    
    def borrow_book(self,book, library):
        #if isinstance(book,Books) and book.get_details() for self.available=True:
           #if isinstance(book, Books) and book.available == True:
           if isinstance(book, Books) and library.is_book_available(book):
               self.borrowed_books.append(book)
               #book.available = False
               library.update_book_status(book, False)
               return f'Borrowed: {book.title}'
           return f'Cannot borrow: {book.title} is unavailable'
            
        
    def return_book(self,book, library):
        if book in self.borrowed_books:
            #self.avaibale =True
            self.borrowed_books.remove(book)
            library.update_book_status(book, True)
            

    def list_borrowed_books(self):
        list_borrowed_books=[]
        for book in self.borrowed_books:
            #list_borrowed_books.append(book)
            list_borrowed_books.append(book.get_details())
        return list_borrowed_books

class Staff:
    
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    # def add_book_to_library(self,book, library):
    #     if isinstance(book,Libary):
    #         self.books.append(book)
    #         library.add_book(book)

    def add_book_to_library(self, book, library):
        if isinstance(book, Books):
            library.add_book(book)
    def manage_book_status(self, book, library, status):
        if book in library.books and isinstance(status, bool):
            library.update_book_status(book, status)

# Creating instances
library = Libary("City Library")

# Creating books
book1 = Books("Python Basics", "John Doe", "12345")
book2 = Books("Advanced Python", "Jane Smith", "67890")

# Creating members
member1 = Member("Alice")
member2 = Member("Bob")

# Creating staff
staff1 = Staff("Mr. Johnson", "Librarian")

# Adding books to the library
staff1.add_book_to_library(book1, library)
staff1.add_book_to_library(book2, library)

# Adding members to the library
library.add_member(member1)
library.add_member(member2)

# Listing books in the library
print("Available Books:", library.list_books())

# Borrowing books
print(member1.borrow_book(book1, library))

print("\nBooks after borrowing:")
print("Available Books:", library.list_books())
print("Borrowed by Alice:", member1.list_borrowed_books())

# Returning books
member1.return_book(book1, library)

print("\nBooks after returning:")
print("Available Books:", library.list_books())
print("Borrowed by Alice:", member1.list_borrowed_books())

# Staff updating book status
staff1.manage_book_status(book2, library, False)
print("\nBooks after staff marks as unavailable:")
print("Available Books:", library.list_books())





             


        




        
        