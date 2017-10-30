def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multipy(a, b):
    return a*b

add2 = add
operator={
    'add': [add,sub,multipy],
    'sub': sub,
    'multipy': multipy
}

print(operator['add'](5,2))
