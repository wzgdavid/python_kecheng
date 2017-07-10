from effects.echo import foo
from copy import copy, deepcopy


class A():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = [1,2,3]
        self.name = 'aname'



if __name__ == '__main__':
    #print  foo(1,2)
    a = A()
    print a.a
    cls = type(a)
    print cls

    ac = copy(a)
    adc = deepcopy(a)
    print a.c == ac.c
    print a.c == adc.c
    #print b.b
    a.c[0] = 3
    print ac.c
    print adc.c