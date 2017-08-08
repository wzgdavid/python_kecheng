类和实例
面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板
类定义
class Student():
    pass
实例化一个类
student = Student()


实例属性和方法
class中定义的函数即实例方法，函数的第一个位置参数代表实例本身，惯例上用self
class Student():
    def __init__(self, name, score): # 初始化实例属性
        self.name = name        # 实例属性
        self.score = score
    def print_name(self):                 # 定义一个方法
        print(self.name)

访问控制
名称前的单下划线，用于指定该名称属性为函数内部使用，是一种约定俗成的惯例，但外部可以访问到
名称前的双下划线，表示私有成员，只有类内部能访问，连子类对象也不能访问到这个数据。
class Student():
     def __init__(self, name, score): # 初始化实例属性
        self._name = name           # 私有实例属性
        self._score = score    
    def _foo(self):             # 私有方法
        print('_foo')
    def __bar(self):            # 私有方法
        print('__bar')

外部访问私有变量
通过一个方法
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score

使用装饰器
    @property
    def score(self):               # 以属性名定义函数
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score


静态方法，类方法
静态方法同过类名调用，不需要实例来调用
创建一个函数move(),是创建在全局命名空间
 Person.move()      # 调用静态方法语义更清晰
 Animal.move()
类方法比静态方法多了一个参数绑定
    @staticmethod       
    def foo():      # 静态方法
    @classmethod
    def foo2(cls):      # 类方法，参数绑定类本身
        print('foo2  {}'.format(cls.__name__))

继承
class Pupil(Student):
    def __init__(self, name, score):            
        super(Pupil, self).__init__(name, score)        # 子类中调父类方法
不用特意调用父类方法，子类会继承父类所有非私有方法和属性
class Pupil(Student): # Student的子类
    pass

方法重写，子类中相同名字的方法会覆盖父类中的方法，无论这个方法是实例方法，类方法，还是静态方法，也无论参数如何的变化
class Pupil(Student):
    def _foo(self, name):           # 这三种情况都会覆盖父类中
                print(‘instance_foo in Pupil’)  # 的_foo方法
    @classmethod                
    def _foo(cls):              # 类中定义相同名字的方法
                print(‘classmethod_foo in Pupil’)   # 最后一个会覆盖前面所有的
    @staticmethod               # 比如左边3个同时定义
    def _foo():             
                print('staticmethod_foo in Pupil')

练习
class Parent():           
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x, Child1.x, Child2.x)     # 这3 个print的输出是什么
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)


类内建函数
issubclass(类，类)
两个参数都是类，判断前者是不是后者的子类
issubclass(Pupil, Student)
 isinstance(实例，类)
判断前者是不是后者的实例，后者可以是前者的父类
isinstance(student, Student)
isinstance(pupil, Student)
 dir()，hasattr()
dir(student)                     # 列出实例或类的所有属性和方法
hasattr(student, ‘_foo’)   # 可以判断实例或类是否有某属性或方法


魔术方法
定制类
__str__
__len__
__eq__
__getitem__
__setitem__


练习
写一个矩形类Rectangle，
1, 有宽__width和高__high两个属性，并且可通过@property 和 @setter取得宽和高，
2, 写一个方法可以获得矩形的面积
3, 可通过print打印出实例的宽，高和面积 __str__ 
    rec = Rectangle(4, 5)
        print(rec)
4, rec1 + rec2 = 他们的总面积  __add__
5, rec1==rec2，用长和宽相等来判断  __eq__


深拷贝(copy)，浅拷贝(deepcopy)
Python中对象的赋值都是进行对象引用（内存地址）传递
使用copy.copy()，可以进行对象的浅拷贝，它复制了对象，但对于对象中引用的其他对象，依然使用原始的引用.
如果需要复制一个对象，以及它引用的所有对象可以使用copy.deepcopy()进行深拷贝
对于不可变类型没有被拷贝一说，因为内存中只有一份
from copy import copy, deepcopy
l = [['a'], 1, 2]
l1 = copy(l)
l2 = deepcopy(l)

