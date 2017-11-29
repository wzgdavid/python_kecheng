def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

def multiply(a, b): 
    return a*b

dct = {'+': add,
       '-': sub,
       '*': multiply
}

#add(1,2)
print(dct['-'](1, 2))

def foo(a, b, c=0): # 位置参数写在默认参数
    print(a, b, c)
foo(1, b=9)  # 

raise try except

函数式编程
lambda x: x+1 
函数作为参数和返回值
all()  any()   map() reduce  



