class Students:
    def __init__(self,name,age,GPA,courses):
        self.name=name
        self._age=age
        self._GPA=GPA
        self._courses=courses
    @property
    def age(self):
        return f'Age of the student is {self._age}'
    @property
    def GPA(self):
        return f'CGPA of the student is {self._GPA}'
    @property
    def courses(self):
        return f"Courses the student is enrolled in: {', '.join(self._courses)}"
    
    @age.setter
    def age(self,new_age):
        if(16<=new_age<=30):
            self.age=new_age
        else:
            print('Age is not Eligible::')
    @GPA.setter
    def GPA(self,new_GPA):
        if(0<=new_GPA<=4):
            self.GPA=new_GPA
        else:
            print('Not Eligible::')
    # Setter for courses
    @courses.setter
    def courses(self, new_course):
        if new_course not in self._courses:
            self._courses.append(new_course)
        else:
            print("Course already exists.")

objc=Students('John',20,3.5,['Math','Physics'])       
objc.age=15
objc.GPA=4.5
objc.courses="Chemistry"
objc.courses='Math'
print(objc.name)
print(objc.age)
print(objc.GPA)
print(objc.courses)