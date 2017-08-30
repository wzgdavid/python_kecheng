'''

'''

from time import time

def return_str(func):
    '''
    让原来的函数返回str类型
    func是需要被修改行为的函数'''
    def wrapper(*args, **kwargs): # a, b 原来的参数
        #rtn =  # add(1, 2)
        return str(func(*args, **kwargs))  # str(add(1, 2))
    return wrapper

def count_time(func):
    '''给函数加上计算运行时间的功能'''
    def wrapper(*args, **kwargs):
        time1 = time()
        func(*args, **kwargs)    # add(1, 2)
        time2 = time()
        print(time2 - time1)
    return wrapper

#add = count_time(return_str(add))
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
#add(1,2)

__age = 99
_age = 80
if __name__ == '__main__':
    sub2(1,2,3)

    #add = return_str(add)
    #print(type(add(1,2)))
    print('deco.py name is {}'.format(__name__))