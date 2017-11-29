#def add(*arg,**kwarg):
#    print(arg, kwarg)
    

#add(3,4,5,key=1, reverse=False, name='cat')
#print(type(foo))
#add(1,2,3,4,5,5,5,5,5,5,5)
#print(a)

#b, *c,a,d = 1,2,3,4,5,5,5,5,5,5,55
#print(b, a)

class ArgExcetiopn(Exception):
    pass

def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgExcetiopn('we need int')
    return a+b
#a = add(1, '')
try:
    a = add(1, '')
    print(a)
except ArgExcetiopn as e:
    print(e)
    print('--------------ArgExcetiopn--------------')
except NameError as e:
    print(e)
    print('--------------NameError--------------')
except Exception as e:
    print(e)
    print('-------------Exception---------------')
print('llllll')