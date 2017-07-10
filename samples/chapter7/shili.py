class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            self.grade = 'A'
        elif self.score >= 60:
            self.grade =  'B'
        else:
            self.grade = 'C'
        return self.grade
    
    def _foo(self):
        print('_foo')
    def __bar(self):
        print('__bar')

s = Student('tom', 79)
print(s.get_grade())
#s.__bar()


'''
访问控制
'''
class Student2():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score

    def __str__(self):
        return '{}\' score is {}'.format(self.__name, self.__score)
    def __len__(self):
        return self.__score

    def __getitem__(self, item):
        if item is 'name':
            return self.__name
        elif item is 'score':
            return self.__score
    def __setitem__(self, item, value):
        if item is 'name':
            self.__name = value
        elif item is 'score':
            self.__score = value
    
    def __add__(self, other):
        return self.__score + other.__score
    
    @staticmethod
    def foo():
        print('call staticmethod')

    @classmethod
    def foo2(cls):
        print('foo2 is a classmethod of {}'.format(cls.__name__))

class Student3(Student2):
    def __init__(self, name, score):
        super(Student3, self).__init__(name, score)

s2 = Student2('trump', 99)
s3 = Student2('tom', 70)
print(s2.get_score())
s2.score = 88
print(s2.score)
print(s2)
s2['name'] = 'disney'
print(s2['name'])
print(s2+s3)
#__str__()
#__len__()
#__getitem__()
#__setitem__()

s33 = Student3('ff', 33)
print(s33.score)

Student2.foo()
Student2.foo2()
