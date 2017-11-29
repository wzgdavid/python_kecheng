#callable
#def 函数名():
#    代码块
#def sorted(iter, key=None, reverse=False)
#sorted(lsit)
# 
def my_abs(x):
    if x < 0:
        x = -x
    return x
print(my_abs(-1))

# a位置参数  b 默认参数
# positional argument  and default argument
def add(a, b=0):
    return a+b
add(1)
# 函数调用的时候，b=0这种形式称作关键字参数 keyword argument
# sorted(lst, key=xxxxx, reverse=True) key和reverse是关键字参数
# 关键字参数不必用定义的顺序调用
add(a=3, b=8)
add(b=3, a=8)
add(3, 7)  # a=3  b =7 
# 定义函数时，位置参数写在默认参数前面
def add2(a, b=0, c=0):
    return a+b+c
# 调用函数时，位置参数写在关键字参数前面
#add2(2, a=1, b=2)  # 传了2个a，一个位置参数，一个关键字

# 定义一个求次方的函数，默认求平方
#def power(a, n=2):
#    #if isinstance(a, (int, float)) and isinstance(n, (int, float)):
#    #    print(a**n)
#    #    return a**n
#    if not isinstance(a, (int, float)) or not isinstance(n, (int, float)):
#        print('参数异常')
#        return
#    print(a**n)
#    return a**n

# 抛异常
def power(a, n=2):
    if not isinstance(a, (int, float)) or not isinstance(n, (int, float)):
        raise TypeError('参数异常')   # raise == java throw
    print(a**n)
    return a**n
#power(4, '4')
try:
    1/0
    aaa
    power(4, '4')

except TypeError as e:
    #raise e
    print(e) # 
except NameError as e:
    #raise e
    print(e) # 
except Exception as e:
    #raise e
    pass
#urls = [url1, url2, url3.......]


#def foo():
#    if asdfsa:
#        if asdfsdf:
#            if asdfasd:
#                if
#
#def foo():
#    if not sadfsadf :
#
#    if not sfsf:
#    if not sadfsadf:
#
#    if not sfsf:
#    

def my_add(a, b):
    pass
# 尽量用不可变类型做默认参数
def append_list(val, lst=[]):
    lst.append(val)
    return lst

def append_list2(val, lst=None):
    if lst == None:
        lst = [] # 每次调用时，[]都是一个不同对象
    lst.append(val)
    return lst

list1 = append_list(10)
list2 = append_list(123,[1])
list3 = append_list('a')
print(list1, list2, list3)
# [10] [123] ['a']

a = b=c=d=f=g=14
#if a>0 and b>0 and c>0 and d>0:
##if a>0 or b>0 or c>0 or d>0:
conditions = [a>0, all, c>0, d>0]
conditions = [1, 2,3]

print( all( [] ) ) # all true
#print( all ())
print( any( [] ))