def add(a, b, c=4):
    print(a)
    return a+b+c

#print(add(b=4, a=1))

#def add(a, b):
#    rtn = 0
#    if isinstance(a, int) and isinstance(b, int):
#        rtn = a+b
#    
#    return rtn
#
#print(add('sdfsdf','2'))

#Exception
class MyError(TypeError):
    pass

def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('we need int')
    rtn = a+b
    return rtn
add(2,1)
try:
    power('abc')
except Exception as e:
    print(e)
finally:
    print('finally---------------------------------')




#try:
#    print(add('sdfsdf',1))
#except Exception as e:
#    pass
#for sfsfsf:
#    try:
#        crawl()
#    except Exception as e:
#        print(e)
#