class Book:
    current_page=1
    def __init__(self,title,author,total_number_pages):
        self.author=author
        self.title=title
        self.total_number_pages=total_number_pages
        self.current_page=1

    def  turn_page(self):
        if(self.current_page>self.total_number_pages):
            print(f'Hence the requested {self.current_page} exceeds the limits')
        else:
            self.current_page+=1
            print(f' the turn page is {self.current_page}')
    def read_pages(self,page_num):
        
        if (self.current_page+page_num>self.total_number_pages):
                self.current_page=self.total_number_pages
                print(f"You are now at the last page {self.total_number_pages}.")
        else:
             self.current_page+=page_num
             print(f"You are now on page {self.current_page}.")
    def book_status(self):
        return f"You are on {self.current_page} of {self.total_number_pages} in {self.title} by {self.author}."
 
booky=Book('Harry potter','Kamal',500)
booky.turn_page()
booky.read_pages(4)
print(booky.book_status())