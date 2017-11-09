Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d= {}
>>> type(d)
<class 'dict'>
>>> d = dict()
>>> type(d)
<class 'dict'>
>>> d1 ={}
>>> d == d1
True
>>> 1.0 == 1
True
>>> d is d1
False
>>> dct = {'bob': 99, 'tom': 80}
>>> dct
{'bob': 99, 'tom': 80}
>>> name = ['bob', 'tom', 'jack']
>>> scores = [99,88,77]
>>> z = zip(name, scores)
>>> dct2 = dict(z)
>>> dct3
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dct3
NameError: name 'dct3' is not defined
>>> dct2
{'bob': 99, 'tom': 88, 'jack': 77}
>>> dct3 = dict([('bob',99), ('tom', 88), ('jack', 77)])
>>> dct3
{'bob': 99, 'tom': 88, 'jack': 77}
>>> dct4 = dict([('bob',99), ('tom', 88), ('jack', )])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dct4 = dict([('bob',99), ('tom', 88), ('jack', )])
ValueError: dictionary update sequence element #2 has length 1; 2 is required
>>> dct5 = dict(bob=99, tom=88,jack=70)
>>> dct5
{'bob': 99, 'tom': 88, 'jack': 70}
>>> dct6 = dict.fromkeys(['a', 'b'], 1)
>>> dct6
{'a': 1, 'b': 1}
>>> dict.fromkeys(['a', 'b'])
{'a': None, 'b': None}
>>> dict.fromkeys(['a', 'a'])
{'a': None}
>>> dct
{'bob': 99, 'tom': 80}
>>> dct3
{'bob': 99, 'tom': 88, 'jack': 77}
>>> dct3['bob']
99
>>> dct3['aaaaa']
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dct3['aaaaa']
KeyError: 'aaaaa'
>>> dct3.get('bob')
99
>>> dct3.get('bobo')
>>> aaa= dct3.gt('aaa')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    aaa= dct3.gt('aaa')
AttributeError: 'dict' object has no attribute 'gt'
>>> aaa= dct3.get('aaa')
>>> aaa
>>> print(aaa)
None
>>> aaa= dct3.get('aaa', 1)
>>> aaa
1
>>> aaa= dct3.get('bob', 1)
>>> aaa
99
>>> dct
{'bob': 99, 'tom': 80}
>>> dct['jerry'] = 77
>>> dct
{'bob': 99, 'tom': 80, 'jerry': 77}
>>> dct['tom'] = 78
>>> dct
{'bob': 99, 'tom': 78, 'jerry': 77}
>>> d2 = {'jack': 66, 'apple':65}
>>> dct.update(d2)
>>> dct
{'bob': 99, 'tom': 78, 'jerry': 77, 'jack': 66, 'apple': 65}
>>> d3 = {'jack': 100, 'apple':65}
>>> dct.update(d3)
>>> dct
{'bob': 99, 'tom': 78, 'jerry': 77, 'jack': 100, 'apple': 65}
>>> del dct['jack']
>>> dct
{'bob': 99, 'tom': 78, 'jerry': 77, 'apple': 65}
>>> tom = dct.pop('tom')
>>> tom
78
>>> dct
{'bob': 99, 'jerry': 77, 'apple': 65}
>>> dct.clear()
>>> dct
{}
>>> dct3.keys
<built-in method keys of dict object at 0x02D37420>
>>> dct3.keys()
dict_keys(['bob', 'tom', 'jack'])
>>> dct3
{'bob': 99, 'tom': 88, 'jack': 77}
>>> dct3b = dict.fromkeys(dct3.keys())
>>> dct3b
{'bob': None, 'tom': None, 'jack': None}
>>> for n in dct3.keys():
	print(n)

	
bob
tom
jack
>>> dct3.values()
dict_values([99, 88, 77])
>>> help(dct3.values())
Help on dict_values object:

class dict_values(object)
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).

>>> dct3.items()
dict_items([('bob', 99), ('tom', 88), ('jack', 77)])
>>> 1 in [1,2,3]
True
>>> 'bob' in dct3
True
>>> 'bob' in dct3.keys()
True
>>> 99 in dct3.values()
True
>>> for item in dct3:
	print(item)

	
bob
tom
jack
>>> for key in dct3:
	print(dct3[key])

	
99
88
77
>>> for key in dct3:
	print(key, dct3[key])

	
bob 99
tom 88
jack 77
>>> for item in dct3.items():
	print(item)

	
('bob', 99)
('tom', 88)
('jack', 77)
>>> for item in dct3.items():
	print(item[0], item[1])

	
bob 99
tom 88
jack 77
>>> for key, value in dct3.items():
	print(key, value)

	
bob 99
tom 88
jack 77
>>> item = ('bob', 99)
>>> key ,value = item
>>> key,value
('bob', 99)
>>> key
'bob'
>>> lst = [1,2,3,4]
>>> next(lst)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    next(lst)
TypeError: 'list' object is not an iterator
>>> g = (n for n in range(9))
>>> next(g)
0
>>> next(g)
1
>>> s = {}
>>> s = set()
>>> type(s)
<class 'set'>
>>> list dict set
SyntaxError: invalid syntax
>>> 
>>> s2 = {1, ,2, 3}
SyntaxError: invalid syntax
>>> s2 = {1, 2, 3}
>>> type(s2)
<class 'set'>
>>> s3 = set('abcd')
>>> s3
{'a', 'b', 'd', 'c'}
>>> s3 = set('sheep')
>>> s3
{'p', 'h', 's', 'e'}
>>> lst = [1,2,3,4,4,4,4,4,4]
>>> lst2 = list(set(lst))
>>> lst
[1, 2, 3, 4, 4, 4, 4, 4, 4]
>>> lst2
[1, 2, 3, 4]
>>> lst2.add(5)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    lst2.add(5)
AttributeError: 'list' object has no attribute 'add'
>>> s3.add(5)
>>> s3
{5, 's', 'p', 'e', 'h'}
>>> s3.add(6)
>>> s3
{5, 's', 'p', 6, 'e', 'h'}
>>> s3.update({1,2,5})
>>> s3
{1, 2, 5, 's', 'p', 6, 'e', 'h'}
>>> s.remove('e')
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    s.remove('e')
KeyError: 'e'
>>> s3.remove('e')
>>> s3
{1, 2, 5, 's', 'p', 6, 'h'}
>>> dir(s3)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set('shop' )> set('sheep')
False
>>> set('shop' )
{'p', 'h', 's', 'o'}
>>> set('sheep')
{'p', 'h', 's', 'e'}
>>> s1 = set([1,2,3,4])
>>> s2 = set([1,2,3,4,5])
>>> s1 > s2
False
>>> s2 = set([1,2,3,5])
>>> s1>s2
False
>>> s1<s2
False
>>> s3 = set([1,2,3,4,5])
>>> s3>s1
True
>>> s2
{1, 2, 3, 5}
>>> s1 == s2
False
>>> set('qwe') == set('ewq')
True
>>> s1 | s2
{1, 2, 3, 4, 5}
>>> s1 & s2
{1, 2, 3}
>>> s1 - s2
{4}
>>> s1
{1, 2, 3, 4}
>>> s2
{1, 2, 3, 5}
>>> s2 -s1
{5}
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> s1+ s2
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    s1+ s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s = {}
>>> type(s)
<class 'dict'>
>>> id
<built-in function id>
>>> id()
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    id()
TypeError: id() takes exactly one argument (0 given)
>>> lst= [1,2,3,4]
>>> enumerate(lst)
<enumerate object at 0x02CF7CB0>
>>> list(enumerate(lst))
[(0, 1), (1, 2), (2, 3), (3, 4)]
>>> list(enumerate('abcd'))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
>>> 1 and 1 and 2 and 4 and 4
4
>>> all([1,1,2,4,4])
True
>>> any([1,1,1,1,0])
True
>>> all([1,0,2,4,4])
False
>>> 


