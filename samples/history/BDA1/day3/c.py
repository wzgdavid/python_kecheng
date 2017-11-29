class Person():
    def eat(self):
        print('Person eat somthing')


class Student(Person):
    x = 77
    def __str__(self):
        return '{}  {}'.format(self.name, self.score)
    
    def __getitem__(self, itemname):
        if itemname == 'name':
            return self.name
        if itemname == 'score':
            return self.score


    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
    def print(self):
        self.__foo()
        print(self.__name, self.__score)
    def play(self):
        print('student play')
    def __foo(self):
        print('private foo')

    def _bar(self):
        print('private bar')
    
    @staticmethod
    def move():
        print('staticmethod move')

    @classmethod
    def fly(cls):

        print(cls.__name__)
        print('classmethod move')

    def __eq__(self, other):
        return self.score == other.score

class Boy(Person):
    def play(self):
        print('boy play')

    def eat(self):
        print('boy eat')

class Pupil(Student, Boy):
    def print(self):
        print(self.score, self.name)

    def fly(self, a, b):
        print('Pupil fly')
    
    def __len__(self):
        return 123

s1 = Student('tom', 99)
s2 = Student('cat', 99)
print(hasattr(s1, 'fly'))
#print(s1 == s2)
#print(s1['score'])
#print(s1)
#print(str(s1))
#
print(dir(s1))

#p = Pupil('jack', 80)
#mylist = Mylist([1,2,3,4])
#print(mylist)
#print(len(p))
#print(len(mylist))
#print(dir(Pupil))
#print(hasattr(Pupil, '__class__'))
#s = Student('tom', 99)
#p = Pupil('jack', 80)
#p.print()
#p.fly(1,2)
#p.play()
#p.eat()
#s.print()

#move()
#Student.fly()



#print(s.name)
#s.name = 'jack'
#print(s.name)
#s.name = 'jack'
#print(s.name)
#print(s.score)
#s._bar()
#