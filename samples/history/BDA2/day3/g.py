#def fib(n):
#    a, b = 0, 1
#    while n>0:
#        a, b = b, a+b
#        n -= 1
#        #print(a)
#    yield a

#for n in fib(4):
#    print(n)
#(n for n in range(1, 4))
def foo():
    yield 1
    yield 2
    return 
    yield 3
    

g = foo()

#print(next(g))
#print(next(g))
#print(next(g))


def foo(n):
    for i in range(1, n):
        yield i
        return
    yield i

g = foo(4)

for n in g:
    print(n)