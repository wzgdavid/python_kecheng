# 魔术方法
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

    def __str__(self):
        return 'name: {}, age: {}'.format(self.name, self.age)

    def __len__(self): # 可以len函数
        return self.age

    def __add__(self, other): # 可以用 + 操作符
        #return self.age + other.age
        return self.name + other.name
    
    def __eq__(self, other): # ==
        return self.age == other.age
    def __gt__(self, other): # >
        return self.age > other.age
    def __ge__(self, other): # >=
        return self.age >= other.age
    def __getitem__(self, item):
        if item == 'name':
            return self.name
        elif item == 'age':
            return self.age
    
    def __setitem__(self, item, value):
        if item == 'name':
            self.name = value
        elif item == 'age':
            self.age = value

    #def __iter__(self):
    #    return self.name, self.age
# 链表  双向链表  队列
p = Person('tom', 77)
p2 = Person('jack', 14)
print(p)
print(len(p))
print(p + p2)  # p > p2  p==p2
print(p == p2)
print(p > p2)
print(p['age'])
p['name'] = 1
print(p['name'])

from collections import Iterable
print( isinstance(p, Iterable) )

#for n in p:
#    print(n)