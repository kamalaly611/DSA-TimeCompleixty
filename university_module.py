# class A:
#     def display(self):
#         print('Displaying from A class')

# class B:
#     def display(self):
#         print('Displaying from B class')

# class C:
#     def show(self):
#         print('Displaying from C class')
# class D(B,C):
#     def display(self):
#         print('Displaying from D class')
#         A.display(self)

# d1=D()
# d1.display()
# print(D.mro())

class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def show(self):
        return f'Uni-Name:{self.uni_name}'
    
class CourseName(University):
    def __init__(self, uni_name,course_name):
        super().__init__(self,uni_name)
        self.course_name=course_name
    def show(self):
        return f'{super().show()} CourseName: {self.course_name}'

class Branch(University):
    def __init__(self, uni_name,branch_name):
        University.__init__(self,uni_name)
        self.branch_name=branch_name
    def show(self):
        return f'{super().show()} Branch: {self.branch_name}'

class Student(CourseName,Branch):
    def __init__(self,student_name,course_name,branch_name,uni_name):
        CourseName.__init__(self, uni_name, course_name)
        Branch.__init__(self, uni_name, branch_name)
        self.student_name=student_name
    def show(self):
        return f'{super().show()} Studen_name:{self.student_name}'


class Faculty(Branch):
    def __init__(self,faculty_name, uni_name,branch_name):
        super().__init__(uni_name,branch_name)
        self.faculty_name=faculty_name
    def show(self):
        return f'{super().show()} Faculty:{self.faculty_name}'


obj = Faculty('John Doe', 'XYZ University', 'IT')
print(obj.show())


student_obj = Student('Alice', 'Data Science', 'CS', 'XYZ University')
print(student_obj.show())
print(Student.mro())