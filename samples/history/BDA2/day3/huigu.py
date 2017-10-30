def add(a, b=0):
    '''
    两个数字相加，a , b ddff
    '''
    print(a,b)
    return a+b


add(2, 1)
add(1)

#def foo(val, lst=[]):
#    lst.append(val)
#    return lst

#改写
def foo(val, lst=None):
    if lst == None:
        lst = []
    lst.append(val)
    return lst
    
list1 = foo(10)
print(list1)
list2 = foo(123, [])
print(list2)
list3 = foo('a')
print(list3)

