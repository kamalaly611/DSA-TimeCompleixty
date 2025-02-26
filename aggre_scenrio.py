# Book class (Composition)
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


# Library class (Composition - owns books)
class Library:
    def __init__(self):
        self.books = []  # List of Book objects

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def remove_book(self, book):
        if isinstance(book, Book) and book in self.books: # here method will check with the gven book if its presented or not
            self.books.remove(book)

    def list_books(self):
        return [book.get_details() for book in self.books] # these method basically iterate through book==book1 & book==book2 instances 
    #  in result which return formatted string 


# Member class (Aggregation - borrows books)
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List of Book objects

    def borrow_book(self, book, library): # here libaray is passed as
        if isinstance(book, Book) and book in library.books: # libary.books means the instances comes from self.books of libary class
            self.borrowed_books.append(book)
            library.remove_book(book)
            print(f"{self.name} borrowed '{book.title}'")

    def return_book(self, book, library):
        if isinstance(book, Book) and book in self.borrowed_books:  # checking in self.borrowed_books = [] as well if  presents
            self.borrowed_books.remove(book)
            library.add_book(book)
            print(f"{self.name} returned '{book.title}'")

    def get_borrowed_books(self):
        return [book.get_details() for book in self.borrowed_books]


# Librarian class (Aggregation - manages books)
class Librarian:
    def __init__(self, name):
        self.name = name

    def process_book_return(self, book, member, library):
        if isinstance(book, Book) and book in member.borrowed_books:
            member.return_book(book, library)
            print(f"Librarian {self.name} processed return of '{book.title}'")


# ---------------- Testing the System ----------------

# Create books
book1 = Book("1984", "George Orwell", "12345")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "54321")

# Create a library and add books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create a member
member = Member("John Doe")

# Borrow a book
member.borrow_book(book1, library) # here

# Display borrowed books
print("\nBorrowed Books:")
for details in member.get_borrowed_books():
    print(details)

# Display remaining books in library
print("\nAvailable Books in Library:")
for details in library.list_books(): #calling list_books methods
    print(details)

# Create a librarian
librarian = Librarian("Alice")

# Member returns the book
librarian.process_book_return(book1, member, library)

# Display books in library after return
print("\nAvailable Books in Library After Return:")
for details in library.list_books():
    print(details)
   


