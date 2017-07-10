

'''斐波那契数列指的是这样的一列数字：0、1、1、2、3、5、8、13.....
第0项是0，第1项是1。从第2项开始，每一项都等于前两项之和。
写一个函数，返回第n项的值
'''
def fib(n):
    if n == 0 :
        rtn = 0
    elif n == 1 :
        rtn = 1
    else:
        rtn = fib(n-2) + fib(n-1)
    return rtn

print(fib(3))

lambda x, y: x + y
def add(x, y):
    return x + y




'''
变量作用域
变量的查找顺序，从内往外
'''
c = 3
def bar():
    a = 1
    #a = 2
    def foo():
        #c = 4  # 没这个变量c ，程序会往上一级查找
        b = 2
        print(a+b+c)
    foo()

bar()


'''
字典用作switch
'''
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def multipy(a, b):
    return a*b
dct = { '+': add, 
        '*': multipy,
        '-': sub,
        }
result = dct['-'](3, 4)

