class Library:
    def __init__(self):
        """Initialize the library with no books."""
        self.no_of_books = 0
        self.books = []

    def add_book(self, book_name):
        """Add a book to the library and update the book count."""
        self.books.append(book_name)
        self.no_of_books += 1

    def print_books(self):
        """Print all books in the library."""
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

    def get_no_of_books(self):
        """Return the number of books in the library."""
        return self.no_of_books

# Main program
def main():
    library = Library()

    while True:
        print("\nLibrary Menu")
        print("1. Print all books")
        print("2. Add a book")
        print("3. Get the number of books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.print_books()
        elif choice == '2':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
            print(f"Book '{book_name}' added successfully!")
        elif choice == '3':
            print(f"Number of books: {library.get_no_of_books()}")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Note: The data is not persisted after the program stops because the books//
# are stored in an instance variable (in memory) and not saved to a file or database.
