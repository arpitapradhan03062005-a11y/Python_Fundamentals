class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

object = Rectangle(2,4)
print("AREA :",object.area())
print("PERIMETER :",object.perimeter())