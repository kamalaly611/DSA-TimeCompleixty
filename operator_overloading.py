class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Creating two Point objects
p1 = Point(2, 3)
p2 = Point(4, 5)


# Adding the two Point objects
p3 = p1 + p2

# Displaying the result
print(p3)  # Output: Point(6, 8)

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __add__(self,x):
        
        return Rectangle(self.length + x.length, self.width + x.width)    
    def __str__(self):
        return f'Rectangale {self.length},{self.width}'

rec=Rectangle(5,4)
rec2=Rectangle(7,6)
print(rec+rec2)
                        
