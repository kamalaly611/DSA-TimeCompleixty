class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching.")

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []  # Aggregation: list to hold teacher objects

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)

    def display_teachers(self):
        print(f"School: {self.name}")
        print("Teachers:")
        for teacher in self.teachers:
            print(f"- {teacher.name}")

# Create independent Teacher objects
teacher1 = Teacher("Mr. Smith")
teacher2 = Teacher("Ms. Johnson")

# Create independent School objects
school1 = School("Greenwood High")
school2 = School("Riverdale Academy")

# Add teachers to schools (aggregation relationship)
school1.add_teacher(teacher1)
school1.add_teacher(teacher2)
school2.add_teacher(teacher1)

# Display teachers for each school
school1.display_teachers()
school2.display_teachers()
