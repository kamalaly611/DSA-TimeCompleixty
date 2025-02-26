# ### Scenario: Online Learning Platform  
# Imagine an online learning platform with two types of users:  
# 1. **User**: General users who can browse and enroll in courses.  
# 2. **Instructor**: Specialized users who can create courses in addition to browsing and enrolling.  

# ### What to do:
# 1. Create a base class `User` with common attributes like 
# `name` and `email` and methods like `browse_courses`.  
# 2. Create a derived class `Instructor` that inherits from `User` but adds an additional method `create_course`.  
# You can implement this scenario and share your code. 
# Once you share it, I’ll review and provide feedback. 😊
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def browser_courses(self,course_name,course_id):
        self.course_name=course_name
        self.course_id=course_id

class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.created_courses = [] 
    def create_course(self, course_name):
        if course_name not in self.created_courses:
            self.created_courses.append(course_name)


user=User('Kamal','etopiyaly@gmail.com')
user.browser_courses(['Bio', 'Chemistry', 'Ics'], 298)

# Create an Instructor object
instructor = Instructor('Test', 'Test@gmail.com')
instructor.create_course('Csss')

# Print created courses by the instructor
print(instructor.created_courses)