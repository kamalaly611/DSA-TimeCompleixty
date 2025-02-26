# check it:
class Student:
    total_students=0
    
    def __init__(self,name, age,grades):
        self.name=name
        self.age=age
        self.grades=grades
        
        Student.total_students+=1
        
    @classmethod
    def increment_students(cls):
        cls.total_students+=1
        return cls.total_students
    @staticmethod
    def is_valid_grade(grades):
        if grades>0 or grades <100:
            return 'Yes the grade is between 0 to 100 '
        return 'grade is not between 0 to 100'
        
    def calculate_average(self):
        
        
        return sum(self.grades) / len(self.grades)

    def add_grade(self, new_grade):
        if 0<=new_grade <=100:
            self.grades.append(new_grade)
            return "Return Grade Succesfully"
        return "Invalid grade. Must be between 0 and 100."
var1=Student.increment_students
        
student1 = Student("Ali", 15, [85, 90, 78])

# Test the methods
print(Student.total_students)               # Check total students
print(Student.increment_students())         # Increment total students
print(Student.is_valid_grade(88))           # Validate a grade
print(student1.add_grade(-1))               # Add a valid grade
print(student1.calculate_average())         # Calculate the average grade
print(student1.grades)                      # Check updated grades
print(var1)