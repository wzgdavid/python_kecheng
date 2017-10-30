Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 1
>>> a = b =1
>>> a = 1
>>> b = 1
>>> pow(4,2)
16
>>> pow(4,3)
64
>>> 4**3
64
>>> 13//3
4
>>> 7/2
3.5
>>> a = 7
>>> b = 2
>>> a/b
3.5
>>> a/float(b)
3.5
>>> int a = 1
SyntaxError: invalid syntax
>>> 1.0 == 1
True
>>> if a>1:
	print('aaa')

	
aaa
>>> for n in range(9):
	print(1)
print(1)
SyntaxError: invalid syntax
>>> b = 10
>>> lst = [1,2,3]
>>> lst2 = list(lst)
>>> lst.append(4)
>>> lst.insert(0, 0)
>>> lst
[0, 1, 2, 3, 4]
>>> l = 'abc'
>>> lst.extend(l)
>>> lst
[0, 1, 2, 3, 4, 'a', 'b', 'c']
>>> lst.extend(list(l))
>>> lst
[0, 1, 2, 3, 4, 'a', 'b', 'c', 'a', 'b', 'c']
>>> lst.pop('c')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    lst.pop('c')
TypeError: 'str' object cannot be interpreted as an integer
>>> lst.pop()
'c'
>>> lst.remove('b')
>>> lst
[0, 1, 2, 3, 4, 'a', 'c', 'a', 'b']
>>> help(list.remove)
Help on method_descriptor:

remove(...)
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.

>>> lst
[0, 1, 2, 3, 4, 'a', 'c', 'a', 'b']
>>> lst[3:5]
[3, 4]
>>> lst[3:]
[3, 4, 'a', 'c', 'a', 'b']
>>> lst[13:15]
[]
>>> 'adfsadfsafsaf'[88:99]
''
>>> lst
[0, 1, 2, 3, 4, 'a', 'c', 'a', 'b']
>>> lst[999999:2]
[]
>>> lst
[0, 1, 2, 3, 4, 'a', 'c', 'a', 'b']
>>> lst[::3]
[0, 3, 'c']
>>> lst[::-2]
['b', 'c', 4, 2, 0]
>>> lst[::-1]
['b', 'a', 'c', 'a', 4, 3, 2, 1, 0]
>>> reversed(lst)
<list_reverseiterator object at 0x00276C70>
>>> list(reversed(lst))
['b', 'a', 'c', 'a', 4, 3, 2, 1, 0]
>>> lst = [[],[],[]]
>>> lst[0].append(10)
>>> lst
[[10], [], []]
>>> id(lst[0])
47154960
>>> id(lst[1])
46442496
>>> id(lst[2])
2084136
>>> lst2 = [[]]*3
>>>  id(lst2[0])
 
SyntaxError: unexpected indent
>>> id(lst2[0])
47028144
>>> id(lst2[1])
47028144
>>> [[]]**3
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    [[]]**3
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> 5**3
125
>>> 5*3
15
>>> t = (1,2)
>>> type(t)
<class 'tuple'>
>>> t = 1,2
>>> type(t)
<class 'tuple'>
>>> t = (1,)
>>> t
(1,)
>>> ttt = 2,
>>> ttt
(2,)
>>>  dir(list)
 
SyntaxError: unexpected indent
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t = ((3,4),(1,2))
>>> t[0]
(3, 4)
>>> t[1][0]
1
>>> t[1][0] = 5
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    t[1][0] = 5
TypeError: 'tuple' object does not support item assignment
>>> t
((3, 4), (1, 2))
>>> (3,4,(1,2))
(3, 4, (1, 2))
>>> t1 = 1,2,3,4
>>> t1
(1, 2, 3, 4)
>>> t = ([3,4],[1,2])
>>> t
([3, 4], [1, 2])
>>> t[1][0] = 5
>>> t
([3, 4], [5, 2])
>>> t[1].append(6)
>>> t
([3, 4], [5, 2, 6])
>>> t[1] = 1
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    t[1] = 1
TypeError: 'tuple' object does not support item assignment
>>> lst = [1,2,3]
>>> s = 'abc'
>>> zip(s, lst)
<zip object at 0x02CF8918>
>>> list(zip(s, lst))
[('a', 1), ('b', 2), ('c', 3)]
>>> list(zip(s, lst, s))
[('a', 1, 'a'), ('b', 2, 'b'), ('c', 3, 'c')]
>>> s2 = 'abcd'
>>> s3 = 'xyzwopq'
>>> zip(s,s1,s2)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    zip(s,s1,s2)
NameError: name 's1' is not defined
>>> zip(s,s2,s3)
<zip object at 0x02CF8AD0>
>>> list(zip(s,s2,s3))
[('a', 'a', 'x'), ('b', 'b', 'y'), ('c', 'c', 'z')]
>>> s
'abc'
>>> ss = []
>>> zip(ss,s2,s3)
<zip object at 0x02CF8B20>
>>> list(zip(ss,s2,s3))
[]
>>> s = 'bcdae'
>>> lst = [3,4,2,1,5]
>>> zipped = zip(s,lst)
>>> zipped
<zip object at 0x02CF8B20>
>>> zipped = list(zip(s,lst))
>>> zipped
[('b', 3), ('c', 4), ('d', 2), ('a', 1), ('e', 5)]
>>> sorted(zipped)
[('a', 1), ('b', 3), ('c', 4), ('d', 2), ('e', 5)]
>>> from operator import itemgetter
>>> sorted(zipped, key=itemgetter(1))
[('a', 1), ('d', 2), ('b', 3), ('c', 4), ('e', 5)]
>>> sorted(zipped, key=itemgetter(-1))
[('a', 1), ('d', 2), ('b', 3), ('c', 4), ('e', 5)]
>>> import pprint
>>> pprint.pprint(zipped)
[('b', 3), ('c', 4), ('d', 2), ('a', 1), ('e', 5)]
>>> s = 'aabbccabacc'
>>> lst = [1,2,3,3,3,2,2,2,1,1,1,2,2]
>>> z = zip(s, lst)
>>> z
<zip object at 0x02CF8B20>
>>> z = list(zip(s, lst))
>>> z
[('a', 1), ('a', 2), ('b', 3), ('b', 3), ('c', 3), ('c', 2), ('a', 2), ('b', 2), ('a', 1), ('c', 1), ('c', 1)]
>>> sorted(z, key=itemgetter(0,1))
[('a', 1), ('a', 1), ('a', 2), ('a', 2), ('b', 2), ('b', 3), ('b', 3), ('c', 1), ('c', 1), ('c', 2), ('c', 3)]
>>> sorted(z, key=itemgetter(0))
[('a', 1), ('a', 2), ('a', 2), ('a', 1), ('b', 3), ('b', 3), ('b', 2), ('c', 3), ('c', 2), ('c', 1), ('c', 1)]
>>> z1= z
>>> z.sort(key=itemgetter(0))
>>> z
[('a', 1), ('a', 2), ('a', 2), ('a', 1), ('b', 3), ('b', 3), ('b', 2), ('c', 3), ('c', 2), ('c', 1), ('c', 1)]
>>> lst4 = []
>>> for n in range(1,6):
	lst4.append(n*n)

	
>>> lst4
[1, 4, 9, 16, 25]
>>> [n*n for n in range(1,6)]
[1, 4, 9, 16, 25]
>>> 'hello'
'hello'
>>> [c.upper()for c in 'hello']
['H', 'E', 'L', 'L', 'O']
>>> 'hello'.upper()
'HELLO'
>>> ''.join([c.upper()for c in 'hello'])
'HELLO'
>>> str(['H', 'E', 'L', 'L', 'O'])
"['H', 'E', 'L', 'L', 'O']"

>>> [ n*n for n in range(1, 11)if n%2==1]
[1, 9, 25, 49, 81]
>>> [1,2,3,'a',[],2,4,None]
[1, 2, 3, 'a', [], 2, 4, None]
>>> lstc = [1,2,3,'a',[],2,4,None]
>>> [n*n for n in lstc if isinstance(n, int)]
[1, 4, 9, 4, 16]
>>> [n*n for n in lstc if type(n)== int]
[1, 4, 9, 4, 16]
>>> [n for n in lstc if type(n)== int or type(n)== str ]
[1, 2, 3, 'a', 2, 4]
>>> [n*n for n in lstc if isinstance(n, (int, str)))]
SyntaxError: invalid syntax
>>> [n*n for n in lstc if isinstance(n, (int, str))]
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    [n*n for n in lstc if isinstance(n, (int, str))]
  File "<pyshell#147>", line 1, in <listcomp>
    [n*n for n in lstc if isinstance(n, (int, str))]
TypeError: can't multiply sequence by non-int of type 'str'
>>> [n for n in lstc if isinstance(n, (int, str))]
[1, 2, 3, 'a', 2, 4]
>>> [ n*n for n in range(1, 11)if n%2==1]
[1, 9, 25, 49, 81]
>>> [ n*n if n%2==1 else n for n in range(1, 11)]
[1, 2, 9, 4, 25, 6, 49, 8, 81, 10]
>>> lstc = [1,2,3,'a',[],2,4,None]
>>> lstc
[1, 2, 3, 'a', [], 2, 4, None]
>>> [n.upper()if isinstance(n, str) else n for n in lstc]
[1, 2, 3, 'A', [], 2, 4, None]
>>> [n.upper()if isinstance(n, str) else 0 for n in lstc]
[0, 0, 0, 'A', 0, 0, 0, 0]
>>> [j+i for i in 'abc' for j in'xyz']
['xa', 'ya', 'za', 'xb', 'yb', 'zb', 'xc', 'yc', 'zc']
>>> for i in 'abc':
	for j in 'xyz':
		print(j+i)

		
xa
ya
za
xb
yb
zb
xc
yc
zc
>>> [i*j for i in range(10) for j in range(10)]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 0, 9, 18, 27, 36, 45, 54, 63, 72, 81]
>>> [i*j for i in range(10) for j in range(10)if i%2==1 and j%2==0]
[0, 2, 4, 6, 8, 0, 6, 12, 18, 24, 0, 10, 20, 30, 40, 0, 14, 28, 42, 56, 0, 18, 36, 54, 72]
>>> [i*j for i in range(10)if i%2==1  for j in range(10)if j%2==0]
[0, 2, 4, 6, 8, 0, 6, 12, 18, 24, 0, 10, 20, 30, 40, 0, 14, 28, 42, 56, 0, 18, 36, 54, 72]
>>> [i*j for i in range(10) for j in range(10)if (i%2==1 and j%2==0) or (i%2==0 and j%2==1)]
[0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 2, 6, 10, 14, 18, 0, 6, 12, 18, 24, 4, 12, 20, 28, 36, 0, 10, 20, 30, 40, 6, 18, 30, 42, 54, 0, 14, 28, 42, 56, 8, 24, 40, 56, 72, 0, 18, 36, 54, 72]
>>> (i*j for i in range(10) for j in range(10))
<generator object <genexpr> at 0x02D0F060>
>>> {i*j for i in range(10) for j in range(10)}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45, 48, 49, 54, 56, 63, 64, 72, 81}
>>> help(isinstance)
Help on built-in function isinstance in module builtins:

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.

>>> 
