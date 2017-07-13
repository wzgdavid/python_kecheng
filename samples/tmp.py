def decorator(func):
    def wrapper(*args, **kw):
        rtn = func(*args, **kw)
        return rtn
    return wrapper

a = decorator

def deco(func):
    def wrapper(a, b):
        rtn = func(a, b)
        return rtn+1
    return wrapper
def add(a, b):
    return a+b

@deco
def mul(a, b):
    return a*b
add = deco(add)
print(mul(1,2))