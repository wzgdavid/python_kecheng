from collections import Iterable

dct = {'a':1, 'b':2}
lst = [1,2,3,4]
zipped_object = zip(list('abcd'), lst)
g = (n**2 for n in range(6))
s = set('sheep')

isinstance(dct.keys(), Iterable)
isinstance(dct.values(), Iterable)
isinstance(dct.items(), Iterable)
isinstance(lst, Iterable)
isinstance(zipped_object, Iterable)
isinstance(g, Iterable)
isinstance(s, Iterable)


# 用map写
def is_iterable(object):
    return isinstance(object, Iterable)

iterable_items = [dct.keys(), dct.values(),dct.items(),
    lst, zipped_object, g, s
] 

mapped = map(is_iterable, iterable_items)
print(isinstance(mapped, Iterable))
isiter = list(map(is_iterable, iterable_items))
print(isiter)