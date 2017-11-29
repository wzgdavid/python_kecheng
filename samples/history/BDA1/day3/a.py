def add(a, b, c=0):
    return a+b+c



def foo(lst, a):
    lst.append(a)

l = [1,2,4]

foo(l,5)

#print(l)

def bar(a):

    a+=1
    #print(a)
aa = 5
#print(id(aa))
bar(aa)

def bar(a, b):
    return a, b , {'chang':a, 'kuang':b, 'zhouchang':(a+b)*2, 'minaji': a*b}

changfangxing = bar(3,4)
#print(changfangxing)
#zhoucahngmaing = changfangxing[2]
#print(zhoucahngmaing['zhouchang'])


*args, info = bar(3,4)
#print(info['zhouchang'])
#print(args)
a, *b, c = 1,2,3,4,5,6
#print(a)
#print(b)
#print(c)






#print(add(1,2))
#add(1,3,3,3,3,3,3,3,3)

#def bar(**bbbb):
#    #print(b)
#    print(bbbb)
#
#bar(lkjklj=2, fsdf=2,key=66)
#a = 1
#def foo():
#    global a
#    b =2
#    print(a, b)
#
#foo()
#
#print(a)

def add(a, b):
    
    return a+b
#add2 = ad
d
#print(add2(4,5))

def sub(a, b):
    return a-b

def select(op, a, b):

    return op(a,b)

result = select(add,3,6) # add(3, 6)
print(result)

