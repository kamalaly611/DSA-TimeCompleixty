class University:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def info(self):
        return f'Name: {self.name} Location:{self.location}'

class Program(University):
    def __init__(self,name,location,program_name):
        University.__init__(self,name,location)
        self.program_name=program_name
    def info(self):
        return f'{super().info()} ProgramName: {self.program_name}'

class Department(University):
    def __init__(self,name,location,departmen_name):
        University.__init__(self,name,location)
        self.departmen_name=departmen_name
    
    def info(self):
        return f'{super().info()} ProgramName: {self.departmen_name}'

class Student(Program,Department):
    def __init__(self, name, location, program_name,departmen_name,student_name,GPA):
        Program.__init__(self,name, location, program_name)
        Department.__init__(self,name,location,departmen_name)
        self.student_name=student_name
        self.GPA=GPA
        self.programVal=Program.info(self)
        self.department=Department.info(self)
    
    def info(self):
        return f'{self.programVal} {self.department} StudnetName: {self.student_name} GPA: {self.GPA}'
    
class Faculty(Department):
    def __init__(self, name, location, departmen_name,faculty_name,specialization):
        super().__init__(name, location, departmen_name)
        self.faculty_name=faculty_name
        self.specialization=specialization
    
    def info(self):
        return f'FacultyName: {self.faculty_name} Specialization: {self.specialization}'

obj = University('Global Tech', 'Silicon Valley')
obj1 = Program('Global Tech', 'Silicon Valley', 'AI and Machine Learning')
obj2 = Department('Global Tech', 'Silicon Valley', 'Computer Science')
obj3 = Student('Global Tech', 'Silicon Valley', 'AI and Machine Learning', 'Computer Science', 'Alice', 3.9)
obj4 = Faculty('Global Tech', 'Silicon Valley', 'Computer Science', 'Dr. Smith', 'Machine Learning')

print(obj.info())
print(obj1.info())
print(obj2.info())
print(obj3.info())
print(obj4.info())
