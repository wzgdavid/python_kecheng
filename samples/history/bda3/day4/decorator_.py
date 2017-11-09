
#a = 1
#b = 2
#c = 3
#def pow(num)
#    return num**2
# 定义装饰器
def return_string(func): # func代表需要改变行为的原函数
    def wrapper(a, b):
        return str(func(a, b))
    return wrapper  #

# 定义一个装饰器，
def print_line(func):
    def wrapper(a, b):
        print('----------------------')
        return func(a,b)
    return wrapper  #

#add = print_line(return_string(add))
@print_line
@return_string  # 应用装饰器
def add(a, b): # 默认认为参数和返回值都是数字
    return a+b

@return_string
def sub(a, b): 
    return a-b

@return_string
def multiply(a, b): 
    return a*b


#print('----------------------')
print(add(1,2))
sub(1,2)
#print(type(add(1,2)))  
#print(type(sub(1,2))) 
#print(type(multiply(3,2))) 
#add = to_string( add )
#sub = to_string( sub )
#...
#add = to_string( add(1, 2) ) # 
#print(type(add(1,2)))  # 返回str类型的值
a = 1
b = 2
#foo(add, sub)

#汽车加工厂     
#
#发动机  a b c        3
#轮胎    t1  t2  t3     3
#颜色    r g  blue w b   5   3*3*5 = 45
#
#a   t2    blue
#发动机  a     t2     blue 

