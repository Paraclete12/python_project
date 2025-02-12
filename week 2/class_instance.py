# we would learn about class here!!

class Rectangle:
    """This is a class for Car"""
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        """This is a method to calculate the area of a rectangle"""
        self.area = self.length * self.width
        return self.area
    
    def perimeter(self):
        """This is a method to calculate the perimeter of a rectangle"""
        self.perimeter = 2 * (self.length + self.width)
        return self.perimeter
    

print(f'The Area of this rectangle is {Rectangle(5, 4).area()}') 
print(f'The perimeter of this rectangle is {Rectangle(5, 4).perimeter()}')
    
            