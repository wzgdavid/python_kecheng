在编程的语境下，函数（function）指的是一个有命名的、执行某个计算的语句序列。 在定义一个函数的时候，你需要指定函数的名字和语句序列。 之后，你可以通过这个名字“调用（call）”该函数。
在python中，函数也是对象，可以把函数赋值给变量，可以当参数传递
已经接触过的内建函数
    id()    type()      isinstance()        str()       int()
    float()     list()       dict()        set()         tuple()
    sorted()        enumerate()

如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

pass语句什么都不做，那有什么用？实际上pass可以用来作占位符
pass还可以用在其他语句里，比如：
if age >= 18:
    pass
缺少了pass，代码运行就会有语法错误


位置参数
# 定义
def foo(a, b):
    return a+b

# 调用
foo(1, 2)

练习
写一个函数，输入身高（米）体重（千克）
根据BMI公式（体重(千克)除以身高的平方）返回结果
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖

默认参数
 如果在函数调用时没有为参数提供值，则使用预先定义的默认值
 默认参数一定要定义在非默认参数后
 def net_conn(host, port=80, stype='tcp'):
 默认参数的值一般使用不可变对象
关键字参数
 关键字参数是让调用者通过参数名来区分参数，这样允许参数确实或不按顺序
 关键字参数仅仅针对函数的调用
 net_conn(stype='udp', host='phaze')

 关键字参数与默认参数示例
def net_conn(host, port=80, stype='tcp'):
    print(host, port, stype)
net_conn('phaze', 8000, 'udp')
net_conn('phaze')
net_conn('phaze', stype='udp')
net_conn(stype='udp', host='phaze')
net_conn('deli', 8080)
net_conn(port=81, host='chino')


异常处理
参数检验
 没有异常处理的话，我们要检验参数的每种可能性
 还要为错误返回一个特殊值，如None或0，这可能和函数逻辑无关
 
def power(n):
    # 接收一个int，求int的平方，如果是其他类型则抛异常
    if not isinstance(n, int):
        raise TypeError('need an int')
    return n * n

捕获异常  
try:
    power('abc')
except Exception as e:
    print(e)
finally:
    print('finally---------------------------------')

练习2
写一个计算次方的函数，进行参数检查，默认值是计算平方
def power(n, cifang=2):
    if not isinstance(n, (int, float)):
        raise Exception('n need to be a number')
    if not isinstance(cifang, (int, float)):
        raise Exception('cifang need to be a number')
    return n**cifang

练习3
list1,list2,list3的输出是什么？请解释你的答案
def append_list(val, lst=[]):
    lst.append(val)
    return lst

list1 = append_list(10)
list2 = append_list(123,[])
list3 = append_list('a')

函数返回值
return，  没有return等于返回None
返回多个值 
 def foo():
    return x, y

 x, y = foo()
 其实返回的是一个元组，实际上还是一个值
 t = foo()

变量作用域
全局变量能在函数内部被访问
局部变量只能在函数内部访问
局部没定义的变量会到外部找相同名称的变量

a = 1           # 全局变量
def foo():
    b = 2   # 局部变量
    print(a+b)

def foo(a):
    a = 2
print(a)


函数式编程
函数作为参数 
def add(a, b):
       return a+b
def multipy(a, b):
       return a*b
def foo(a, b, func):
       return func(a, b)

print(foo(2, 4, multipy))

函数返回函数
def foo():
    def bar():
        print('here in bar' )
    print('here in foo')
    return bar
func = foo()       # 函数返回一个函数
func()
foo2 = foo          # 另一个变量指向函数

递归
斐波那契数列是这样的一列数字：0、1、1、2、3、5、8、13.....
第0项是0，第1项是1。从第2项开始，每一项都等于前两项之和。
写一个函数，返回第n项的值
def fib(n):
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = fib(n-2) + fib(n-1)
    return value

利用元组实现斐波那契
0、  1、  1、  2、  3、  5、  8、  13
def fib(n):
    a, b = 0, 1
    while(n>0):
        a, b = b, a+b
        n-=1
    return a

匿名函数lambda
有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
def add(x, y):
    return x + y



lambda x, y: x + y

生成器（ generator ）
要创建一个生成器，第一种方法，只要把一个列表生成式的[]改成()，就创建了一个生成器

g = (x * x for x in range(10))

生成器保存的是算法，不是保存元素，所以不占内存
next(g)可以依次得到生成器的元素，调用一次运行一次
生成器只能被遍历一次，遇到StopIteration停止遍历


yield定义生成器
自定义函数的时候，用yield可生成生成器，执行到 yield时，fib 函数就返回一个迭代值，下次迭代时，代码从 yield的下一条语句继续执行
def g2():
    yield 'a'
    yield 'b'
def fib(n):
    a, b = 0, 1
    while(n>0):
        yield a
        a, b = b, a+b
        n-=1

装饰器（Decorator）(上课还是不讲好，初学学这个一下子接受不了)
这种在代码运行期间动态增加功能的方式，称之为“装饰器” 。
定义装饰器
def decorator(func):
    def wrapper(*args, **kw):  # *args, **kw 表示所有参数
        rtn = func(*args, **kw)
        return rtn
    return wrapper
使用
@decorator
def foo():
    pass

字典实现选择功能
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def multipy(a, b):
    return a*b
operator = { '+': add, 
             '*': multipy,
             '-': sub,}
operator['-'](3, 4)
