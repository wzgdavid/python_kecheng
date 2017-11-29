print('----------------lambda-------------------')
def foo(a):
    return a+1

lam1 = lambda a: a+1
print(lam1(1))

lst = [(1,2), (4,1), (3,5)]

sorted_lst = sorted(lst, key=lambda item: item[1])
#student.age
#       .name
#students = [s1, s2, s3]
#attrgetter('age')
#sorted_lst = sorted(students, key=lambda student: student.age)
print(sorted_lst)

def xaddone(x):
    return x+1
xs = 1, 2, 3, 4
# y = x + 1   lambda x:x+1
ys = list(map(lambda x:x+1, xs))
#ys = map(xaddone, xs)
#print(list(ys))

#map reduce
from functools import reduce
reduce(lambda x,y: x+y, ys)
#ys = [2,3,4,5] #14
print(reduce( lambda x,y: x+y , ys))

str_number = '12345' # 转成 int 12345
numbers = map(lambda x:int(x), str_number)# [1, 2, 3, 4, 5]
# 匿名函数参数规则顺序 都一样，位置参数，后，默认参数
print(reduce(lambda x,y:10*x+y, numbers))


print('----------------生成器-------------------')

lst = [n*n for n in range(9)]

g = (n*n for n in range(4)) # 
#for n in g:
#    print(n)
#print('第二个循环')
#for n in g:
#    print(n)
#print(next(g))

def foo():  # yield
    yield 1
    yield 2
    return  # StopIteration
    yield 3
    yield 4    
def bar():
    for n in range(4):
        yield n*n

g = foo()
print(next(g)) # 1
print(next(g)) # 2
#print(next(g)) # 
#print(next(g))
#print(next(g))#
#
def fib_g(n):
    a, b = 0, 1
    while(n>0):
        yield a
        a, b = b, a+b
        n-=1
print('------------fib_g-----------')
g = fib_g(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(fib_g(4)))