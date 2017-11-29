# 
point1 = (3, 4)
point2 = (1, 5)

def add(point1, point2):
    p1 = point1[0] + point2[0]
    p2 = point1[1] + point2[1]
    return p1, p2

# print(add(point1, point2))
x, y = add(point1, point2)
#x, y = 4, 9
#print(x,y)

def add(a, b):
    return a+b

def multipy(a, b):
    return a*b

def foo(a, b, func=add):
    '''func是个函数，a，b是我要操作的数字
    foo(1, 2, add)
    add(1, 2)
    '''
    return func(a,b) 

#print(foo(2, 4, multipy))

def bar(select):
    def add(a, b):
        return a+b
    def multipy(a, b):
        return a*b
    def sub(a, b):
        return a-b
    if select == '+':
        rtn = add
    elif select == '-':
        rtn = sub
    elif select == '*':
        rtn = multipy
    return rtn
add2 = bar('+')
#add2   ==  def add(a, b):
#        return a+b
#def add2(a, b):
#    return a+b
print(add2(3,5))