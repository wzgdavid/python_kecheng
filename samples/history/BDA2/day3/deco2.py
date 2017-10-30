from deco import count_time, return_str

#import deco
@count_time
@return_str
def add(a, b):
    '''这里默认接收int，返回int'''
    for n in range(99999999):
        pass
    return a+b

@count_time
def sub(a, b):
    return a-b
@count_time
def sub2(a, b, c=0,d=0):
    return a-b-c


    