class Person():
    def __init__(self, name):
        self.__name = name

    def __move(self):# private
        print('person is move')

    @property
    def name(self):
        return self.__name    

    @name.setter
    def name(self, name):
        self.__name = name

    def eat(self, food):
        print('Person {} is eating {}'.format(self.__name, food))
    
    @classmethod
    def foo(cls):
        print('', cls.__name__)


# 子类继承父类所有非私有的所有方法
class Student(Person):
    def study(self):
        print('Student study')

    def eat(self, food):
        # super调用父类方法
        super().eat(food) # super(Student, self).eat(food)
        print('Student {} is eating {}'.format(self.name, food))
    
    #def foo(self):
    #    print('fooooooooooooooooo')


def test_person():
    p = Person('tom')
    print(p.name)
    p.eat('cake')
    Person.foo()
    #p.get_a_name('cat')
    
    #p.__move()
    
    #AttributeError: 'Person' object has no attribute '__move'
    #AttributeError: 'Person' object has no attribute 'eat'

def foo_student():
    print('--------------继承---------------')
    s = Student('jack') # __init__  self.__name = jack
    print(s.name)
    s.eat('cake')
    s.foo()
    s.study()
    
    print('--------------多重继承---------------')

print(__name__)

if __name__ == '__main__':
    print(__name__)
    #foo_student()