class Student():
    def __init__(self, name, score):
        '''初始化一个实例'''
        self.__name = name
        self.__score = score
    def eat(self, food):
        '''定义一个对象方法'''
        print('{} eat {}'.format(self.__name, food))
    #def get_name(self):
    #    return self.__name
    #def set_name(self, name):
    #    self.__name = name
    @property # get_name
    def name(self):
        return self.__name

    @name.setter # set_name
    def name(self, name):
        self.__name = name

    @property 
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
    
    @classmethod # 类方法
    def move(cls):
        print('{} is move'.format(cls.__name__))

    @staticmethod # 静态方法
    def fly():
        print('静态方法fly')
student = Student('tom', 78)
#print(student.__name)
#student.eat('cake')
#student.set_name('dog')


student.__score = 44
print(student.__score)
Student.move()
Student.fly()

#print(student.name)
#student.age = 1