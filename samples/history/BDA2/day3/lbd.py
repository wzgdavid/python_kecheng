from operator import itemgetter

def add(a,b):
    return a+b

#add2 = lambda a, b:a+b

#print(add2(1,3))


s = 'bcdae'
lst = [3,4,2,1,5]
zipped = zip(s,lst)
#sz = sorted(zipped, key=itemgetter(0))
#print(sz)
def foo(element):
    return element[0]
#sz = sorted(zipped, key=foo)
sz = sorted(zipped, key=lambda element:element[0])
print(sz)
help(sorted)