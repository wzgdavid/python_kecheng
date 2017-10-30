class Rec():
    def __init__(self, width, high):
        self.__width = width
        self.__high = high
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width
    @property
    def high(self):
        return self.__high
    @high.setter
    def high(self, high):
        self.__high = high
    @property
    def area(self):
        return self.__high * self.__width
    
    def __repr__(self):
        return "{}-{}-{}".format(self.width, self.high,self.area)

    def __add__(self, other):
        print(self.area + other.area)
        return self.area + other.area

    def __eq__(self, other):
        print(self.area == other.area)
        return self.area == other.area
        
r = Rec(6,7)
r2 = Rec(5,7)
print(r.area)
print(r)
r + r2
r == r2