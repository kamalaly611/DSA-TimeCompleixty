class Person:
    def __init__(self, Name, Age, Address, Occupation):
        self.Name=Name
        self.Age=Age
        self.Address=Address
        self.Occupation=Occupation
    def introduce(self):
        return f" Hi my name is {self.Name} and I am {self.Age} year's old and I live in {self.Address}, and I am an {self.Occupation}"
        

Person_1=Person("Kamal Hussain","22","Islamabad","Data Scinetist")
print(Person_1.Name)
print(Person_1.Age)
print(Person_1.Address)
print(Person_1.Occupation)
print(Person_1.introduce())

# Student class with its attributes:


class Student:
    college_name="SZABIST" # These are class attributes:
    name='Anonymous'
    def __init__(self,fullname):
        self.name=fullname
        print('Adding New Students')
        # Precdece of object attributes is greater than > class attributes 
        # class attr < obj attr if the are with same name
s1=Student('Karan')
print(s1.name)

# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average along with static method for printing hello world 
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print('hello world')

    def average(self):
        sum_marks = self.marks[0] + self.marks[1] + self.marks[2]
        average = sum_marks / len(self.marks)
        return f'Hi, your name is {self.name}, your marks are {self.marks}, and your average is {average}'

s1 = Students('Kamal', [91, 92, 93])
print(s1.name)
print(s1.average())  # Call the average method to print the formatted string
s1.hello()
        
        