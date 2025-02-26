class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class InstitutionMember:
    def __init__(self, member_id):
        self.member_id = member_id

    def get_details(self):
        return f"Member ID: {self.member_id}"


class Faculty(Person, InstitutionMember):
    def __init__(self, name, age, member_id, subject):
        Person.__init__(self, name, age)
        InstitutionMember.__init__(self, member_id)
        self.subject = subject

    def get_details(self):
        person_details = Person.get_details(self)
        institution_details = InstitutionMember.get_details(self)
        return f"{person_details}, {institution_details}, Subject: {self.subject}"

    def assign_duty(self, duty):
        return f"Faculty {self.name} is assigned to: {duty}"


class HOD(Faculty):
    def __init__(self, name, age, member_id, subject, department, faculty_list):
        super().__init__(name, age, member_id, subject)
        self.department = department
        self.faculty_list = faculty_list  # List of faculty members

    def get_details(self):
        parent_details = super().get_details()
        return f"{parent_details}, Department: {self.department}, Faculty Count: {len(self.faculty_list)}"

    def assign_duties_to_all(self, duty_list):
        if len(duty_list) != len(self.faculty_list):
            return "Error: Mismatch between faculty count and duties provided."
        
        assignments = {}
        for faculty, duty in zip(self.faculty_list, duty_list):
            assignments[faculty.name] = faculty.assign_duty(duty)
        return assignments


# Test the scenario
faculty1 = Faculty("Alice", 35, "F001", "Mathematics")
faculty2 = Faculty("Bob", 40, "F002", "Physics")
faculty3 = Faculty("Charlie", 50, "F003", "Chemistry")

hod = HOD(
    name="Dr. Smith",
    age=55,
    member_id="H001",
    subject="Management",
    department="Science",
    faculty_list=[faculty1, faculty2, faculty3]
)

# Outputs
print(hod.get_details())  # Details of the HOD with department and faculty count
print(hod.assign_duties_to_all(["Exam Coordination", "Lab Supervision", "Syllabus Review"]))  # Assign duties to all faculty
