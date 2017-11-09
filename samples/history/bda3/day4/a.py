# 函数返回值
def foo():
    return 1, 2, 3

#a = foo()
#print(a)
#a,b,c = foo()
#print(a,b,c)

def add(a, b):
    print(a)
    a = 1
    print(a)
    return a+b

a = 2
b = 3
print(add(a, b))
print(a)
print('----------------函数返回函数-------------------')
def bar():
    print(a)# 局部找不到的变量去上一层找，
#bar()
# 闭包
a = 99
def foo(): # 定义域
    a = 88
    def bar():# 可以把函数名看成普通变量
        # a是几，看函数在哪里定义
        # 不是看在哪里调用
        print('bar in foo ,a is ',a)            
    #bar() 
    def bar3():
        print('bar3 in foo ,a is ',a)  
    return bar, bar3

def bar1():
    print('bar1 out foo, a is ', a)
bars = foo()
bars[1]()
bar1()

a = 1
b = a
print (id(1))
foo = id
print(foo(1))

print('----------------函数做参数-------------------')
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def select_function(function, a, b):
    # 不明白时代入具体值，比如add(a, b)
    return function(a, b)  # add(a, b)
#help(id)
result = select_function(sub, 1,3)
print(result)

print('----------------递归-------------------')
def fib(n):
    if n == 0:
        rtn = 0
    elif n == 1:
        rtn = 1
    else:
        rtn = fib(n-1) + fib(n-2)
    return rtn
print(fib(7))


lst = [3, 7, [0, [9, 5], 7], 1]
#lst2 = [3, 7, 0, 9, 5, 7, 1] # 扁平化处理,用递归


def flatten_list(lst, rtn=None):
    if rtn == None:
        rtn = []
    for n in lst:
        if isinstance(n, list):
            flatten_list(n, rtn)
            # flatten_list([0, [9, 5], 7], [3, 7])
        else:
            rtn.append(n)
    return rtn
print(flatten_list(lst))
print(flatten_list(lst))

def fib(n):
    a, b = 0, 1
    while(n):
        a, b, n= b, a+b, n-1
        
    return a
print(fib(240))

'''


'''