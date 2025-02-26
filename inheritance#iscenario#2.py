class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def display_info(self):
        return f"'{self.title}' was written by {self.author} and published in {self.year_published}."

class Ebook(Book):
    def __init__(self, title, author, year_published, file_size):
        super().__init__(title, author, year_published)
        self.file_size = file_size

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info} File size: {self.file_size}."

# Testing the classes
book_objc = Book('Alchemist', 'Paulo Coelho', 2005)
ebook_objc = Ebook('Alchemist', 'Paulo Coelho', 2005, '1.5MB')

print(book_objc.display_info())
print(ebook_objc.display_info())
print(book_objc.display_info())

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
class Payment:
    def process_payment(self):
        return "Processing payment..."

class CreditCardPayment(Payment):
    def process_payment(self):
        var_1 = super().process_payment()
        return f'Processing payment... via Credit Card via PayPal'

class PayPalPayment(CreditCardPayment):
    def process_payment(self):
        #var_2=super().process_payment()
        return f'Processing payment... via Credit Card'
    
    
Payment_objc=Payment()
CreditCardPayment_objc=CreditCardPayment()
PayPalPaymentObjc=PayPalPayment()
print(Payment_objc.process_payment())
print(CreditCardPayment_objc.process_payment())
print(PayPalPaymentObjc.process_payment())

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def introduce(self):
        return f"Hi, I am {self.name}, and I am {self.age} years old."

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    
    def introduce(self):
        var=super().introduce()
        return f"{var}. I am in grade {self.grade}."

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name, age)
        self.subject=subject
        super().introduce()
    def introduce(self):
        return f"{super().introduce()} I teach {self.subject}."
        
objc_Person=Person('Kamal',23)
print(objc_Person.introduce())
objc_Studnet=Student('Ali-Zain',9,'A++')
print(objc_Studnet.introduce())
objc_Teacher=Teacher('Zoya',12,'Cs')
print(objc_Teacher.introduce())
