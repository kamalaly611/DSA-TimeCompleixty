# University class (Composition - Owns Departments)
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
    
    def add_department(self, department):
        if isinstance(department, Department):
            self.departments.append(department)

    def list_departments(self):
        #return [department.name for department in self.departments]#  self.departments = [cs_department, math_department]
     #  department.name in [cs_department, math_department]
        department_names = []
        for department in self.departments:
            department_names.append(department.name)
        return department_names
# Department class (Composition - Owns Professors)
class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []  # Fixed spelling
    
    def add_professor(self, professor):
        if isinstance(professor, Professor):
            self.professors.append(professor)
    
    def list_professors(self):
        #return [professor.get_details() for professor in self.professors]  # Fixed reference
        professor_details = []
        for professor in self.professors:
            professor_details.append(professor.get_details())# here it triggers professor.getdetails which iterate through complete object
        return professor_details

# Professor class (Aggregation - Can exist independently but linked to Students)
class Professor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.students = []

    def assign_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def list_students(self):
        #return [student.get_details() for student in self.students]  # Fixed comprehension
        student_details = []
        for student in self.students:
            student_details.append(student.get_details())
        return student_details
    

    def get_details(self):
        return f"Professor: {self.name}, Specialization: {self.specialization}"
# Student class (Independent but linked to Professors)
class Student:
    def __init__(self, name, enrolled_department):
        self.name = name
        self.enrolled_department = enrolled_department
    
    def get_details(self):
        return f"Student: {self.name}, Enrolled in: {self.enrolled_department.name}"
    

# Testing on Instances 
university = University("Tech University")

# Create departments
cs_department = Department("Computer Science")
math_department = Department("Mathematics")
# print(cs_department.name)
# print(math_department.name)
# Add departments to the university
university.add_department(cs_department)
university.add_department(math_department)

# Create professors
prof1 = Professor("Dr. Alan", "AI & ML")
prof2 = Professor("Dr. Taylor", "Algebra")

# Assign professors to departments
cs_department.add_professor(prof1)
math_department.add_professor(prof2)

# Create students
student1 = Student("Alice", cs_department)
student2 = Student("Bob", math_department)

# Assign students to professors
prof1.assign_student(student1)
prof2.assign_student(student2)

# Display departments
print("\nDepartments in University:")
print(university.list_departments())

# Display professors in each department
print("\nProfessors in Departments:")
for department in university.departments:
    print(f"\n{department.name} Department:")
    for professor in department.list_professors():
        print(f"  - {professor}")

# Display students assigned to each professor
print("\nStudents assigned to Professors:")
for department in university.departments:
    for professor in department.professors:  # Fixed spelling
        print(f"\n{professor.get_details()}:")
        for student in professor.list_students():
            print(f"  - {student}")
