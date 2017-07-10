def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        rtn = func(*args, **kw)
        print('called %s():' % func.__name__)
        return rtn
    return wrapper

def return_int(func):
    def wrapper(a, b):
        rtn = int(func(a, b))
        return rtn
    return wrapper

#@return_int
def add(a, b):
    return a+b

#@return_int
def sub(a,b):
    return a-b

def multipy(a, b):
    return a*b

add = return_int(add)
print(add(1,3.0))
print(sub(1,3.0))



#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。