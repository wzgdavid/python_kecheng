class Rectangle():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError
        self.__height = height
        
    @property
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return 'height is {1}, width is {0}, area is {2}'.format(
                self.__width, self.__height, self.area
            )

    def __add__(self, other):
        return self.area + other.area

r = Rectangle(4, 6)
r.height = 5
print(r.height)
print(str(r))

r1 = Rectangle(4, 6)
r2 = Rectangle(5, 5)

print(r1+r2)
