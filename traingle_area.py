def calculate_area(dimension1, dimension2, shape="triangle"):
    if shape == "triangle":
        area_triangle = 0.5 * dimension1 * dimension2
        return area_triangle
    elif shape == "rectangle":
        area_rectangle = dimension1 * dimension2
        return area_rectangle
  
n1 = float(input("Enter length or base:"))
n2 = float(input("Enter width or height:"))
shape = input("Enter shape type (triangle or rectangle): ")
print("Area:", calculate_area(n1, n2, shape))
