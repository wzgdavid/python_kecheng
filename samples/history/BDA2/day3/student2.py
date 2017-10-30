class Person():
    def move(self):
        print('person is move')
    pass

class Student(Person):
    def __init__(self, name, score):
        '''初始化一个实例'''
        self.__name = name
        self.__score = score

    def __eat(self, food):
        '''定义一个对象方法'''
        print('{} eat {}'.format(self.__name, food))

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
    

    @staticmethod # 静态方法
    def fly():
        print('静态方法fly')

class Animal():
    @classmethod
    def move(cls):
        print('Animal is move 2')

class Pupil(Student, Animal):
    def __str__(self):
        return 'name is {}, score is {}'.format(self.name, self.score)
    #def move(self):
    #    print('Pupil move')
    def __len__(self):
        return self.score
    def __gt__(self, other):
        return self.score > other.score
    def __eq__(self, other):
        return self.score == other.score
    def __getitem__(self, item):
        if item == 'name':
            rtn = self.name
        elif item == 'score':
            rtn =  self.score
        return rtn
    def __setitem__(self, item, value):
        if item == 'name':
            self.name = value
        elif item == 'score':
            self.score = value
        
#s = Student('tom', 78)
p = Pupil('tom', 99)
p2 = Pupil('tom', 99)
#print(p.name)
p.move()
#print(issubclass(Pupil, Person))
#print(dir(p))
#'attr' in dir(p)
#print(p)
#print(len(p))
#print(p == p2)
p['name'] = 1
print(p.name)




