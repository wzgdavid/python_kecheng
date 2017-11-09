class Person():
    def move(self):
        print('Person move')

class Animal():
    pass
    #def move(self):
    #    print('Animal move')

# 在几个父类没有共同父类的情况下，
# Animal和Person没有共同父类
# 子类中没有的方法或属性会到父类中查找
# 查找顺序是从左往右（前往后）
class Student(Animal,Person):
    pass

s = Student()
s.move() 

print('============父类有共同父类================')
class Base():
    def move(self):
        print('Base move')

class Person(Base):
    pass
    def move(self):
        print('Person move')

class Animal(Base):
    pass
    #def move(self):
    #    print('Animal move')
        
class Student(Animal,Person):
    pass

s = Student()
s.move() 


print('============父类没有共同父类================')
class Base1():
    def move(self):
        print('Base1 move')
class Base2():
    def move(self):
        print('Base2 move')
    pass
class Person(Base1):
    pass
    def move(self):
        print('Person move')
class Animal(Base2):
    pass
    #def move(self):
    #    print('Animal move')
class Student(Animal,Person):
    pass
s = Student()
s.move() 

print('============父类有共同父类111================')
class Base1(Base):
    def move(self):
        print('Base1 move')
class Base2(Base):
    #def move(self):
    #    print('Base2 move')
    pass
class Person(Base1):
    pass
    def move(self):
        print('Person move')
class Animal(Base2):
    pass
    #def move(self):
    #    print('Animal move')

class Student(Animal,Person):
    pass
s = Student()
s.move() 

print(issubclass(Student, Base))
print(isinstance(s, Base2))
print(dir(Student))
print(dir(s))

class ABC(list, Student):
    pass

a = ABC('123')
a.move()
a.append(5)
# 判断对象有没有某某属性或方法
print(hasattr(a, 'move'))
print(hasattr(a, 'append'))
print(hasattr(a, '__init__'))
print(hasattr(list, 'append'))