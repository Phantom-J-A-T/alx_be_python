class  Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"The area of the Rectangle is {self.width * self.height}"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"The area of the Circle is {3.14 * self.radius ** 2}"
