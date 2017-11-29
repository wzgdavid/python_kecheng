class Rectangle():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
    
    @property
    def mianji(self):
        return self.__width * self.__height

    def __str__(self):
        return '{} {} {}'.format(self.__width, self.__height, self.mianji)

    def __add__(self, other):
        return self.mianji + other.mianji
        
    def __eq__(self, other):
        widtheq = self.__width == other.__width
        heighteq = self.__height == other.__height
        return widtheq and heighteq


r1 = Rectangle(10, 9)
r2 = Rectangle(10, 9)
print(r1 == r2)

