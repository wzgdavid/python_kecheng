#class Student():
#    x = 1  # 类属性

#lst = list()   # 实例化一个对象 
#s = Student()  # 实例化一个对象 
#print(type(s)) 
#print(Student.x)
## 对象中找不到的变量，到类的属性中找，包括动态
#print(s.x)  
#Student.a = 2   # 动态绑定
#del Student.x   # 删除一个属性
#print(s.a)

print('-------------实例属性------------')
class Student():
    x = 1  # 类属性
    def __init__(self, name, score): # 前后都两个下划线
        # 实例(instance)初始化函数
        self.__name = name
        self.__score = score
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    @property
    def name(self): # 对应get_name
        return self.__name

    @name.setter
    def name(self, name): # set_name
        self.__name = name

    def study(self, subject): #  对象方法
        self.subject = subject # 随时可以绑定属性
        print('{} is studying .'.format(self.__name))

    # 以两个下划线命名的方法或属性为私有
    def __eat(self, food): 
        pass

    # 以一个下划线命名的方法或属性为惯例上的私有
    def _run(self):
        print('{} is running .'.format(self.name))
    # public int private_run(){}

    @staticmethod 
    def foo():# 静态方法
        print('student foo is staticmethod')

    @classmethod
    def bar(cls):# 类方法
        print('student foo is classmethod',cls.__name__)

s = Student('tom',99)
#s.get_name()
print(s.name)
s.name = 'cat' # s.set_name('cat')
print(s.name)
s.study('english')

print(s.subject)
s._run()  # s._run(s)

Student.foo()
Student.bar() # 默认传一个类本身作为参数Student.bar(Student)

# 类也是一个对象
#class type():
#    pass
#    ...
#
#Student = type() # type Student = new type(...)
#                 # type  str = new type(...)