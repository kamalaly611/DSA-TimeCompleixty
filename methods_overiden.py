# class Vehicle:
#     def describe(self):
#         print("This is a generic vehicle.")
# class Car(Vehicle):
#     def describe(self):
#         print("This is a car.")

# obc=Vehicle()
# objcc=Car()
# obc.describe()
# objcc.describe()

# class Shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y

# rec=Shape(3,5)
# print(rec.area())
    
class Shape:
    def __init__(self, name):
        """Initialize the shape with a name."""
        self.name = name
    
    def area(self):
        """Generic area method for shapes."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def describe(self):
        """Describe the shape."""
        return f"This is a shape called {self.name}"


class Rectangle(Shape):
    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def describe(self):
        """Override to add specific details about the rectangle."""
        return f"A rectangle with width {self.width} and height {self.height}"


class Square(Rectangle):
    def __init__(self, side_length):
        """Initialize a square as a special case of a rectangle."""
        super().__init__(side_length, side_length)
        self.name = "Square"  # Update the name for square
    
    def describe(self):
        """Override to describe a square."""
        return f"A square with side length {self.width}"


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with a radius."""
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return 3.14 * (self.radius ** 2)

    def describe(self):
        """Override to describe a circle."""
        return f"A circle with radius {self.radius}"


# Instantiate and Test
shapes = [
    Rectangle(4, 5),
    Square(3),
    Circle(7)
]

for shape in shapes:
    print(shape.describe())
    print(f"Area: {shape.area()}")
    print("-" * 30)
