def foo():
    def bar():
        print('here in bar' )
    #bar = 1
    print('here in foo')
    return bar


#bar2 = foo()

#bar2()
##def dfsfd(sdf):
##    return sdf[1]
#sorted(lst, key=lambda x:x[1])
#
#add = lambda x, y:x+y
#add(2, 1)

#def foo(n):
#    for x in range(n):
#        yield x**2
#
#g2 = foo(5)
##for n in g2:
##    print(n)
#print(g2)
##print(next(g2))
##print(next(g2))
##print(next(g2))

#def foo(*args, **kw):
#    print(args)
#    print(kw)
#foo(1,3,4,key=11,reverse=True)



def return_str(func):
    def wrapper(a, b):
        rtn = str(func(a, b))
        return rtn
    return wrapper

@return_str
def add(a, b):
    return a+b
#
@return_str
def mul(a, b):
    return a*b

print(type(add(1,3)), add(1,3))
add = return_str(add)
#print(type(add(1,3)), add(1,3))