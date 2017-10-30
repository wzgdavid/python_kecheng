def foo():
    def bar():
        print('here in bar' )
    print('here in foo')
    return bar

#func = foo()

def g2():
    yield 'a'
    yield 'b'
    raise StopIteration
    yield 'c'
    yield 'd'

g = g2()
#print(next(g))
#print(next(g))
#print(next(g))

class A():
    pass

A.x = 1
a = A()
a.y = 2
#print(a.y)

class Base():
    def foo(self):
        print('Base foo')
class Base2():
    def foo(self):
        print('Base2 foo')
class A(Base):
    #def foo(self):
    #    #super().foo()
    #    print('A foo')
    pass
class B():
    pass
#class B():
#    pass
class C(A, B):
    pass
#c = C()
#c.foo()

class mylist(list):
    pass

mylist = [1,2,3,4]
print(mylist[1])