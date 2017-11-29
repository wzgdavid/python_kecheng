Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [n*n for n in range(4)]
[0, 1, 4, 9]
>>> g = (n*n for n in range(4))
>>> g
<generator object <genexpr> at 0x02D37450>
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    next(g)
StopIteration
>>> for n in g:
	print(n)

	
>>> g = (n*n for n in range(4))
>>> for n in g:
	print(n)

	
0
1
4
9
>>> g = (n*n for n in range(4))
>>> next(g)
0
>>> for n in g:
	print(n)

	
1
4
9
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    next(g)
StopIteration
>>> next([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    next([1,2,3,4])
TypeError: 'list' object is not an iterator
>>> dir(g)
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
>>> def foo():
	yield 1

	
>>> foo
<function foo at 0x02D3E660>
>>> type(foo)
<class 'function'>
>>> import time
>>> time.time()
1502864749.0758119
>>> time.time()
1502864753.7848117
>>> time1 = time.time()
>>> time2 = time.time()
>>> time2 - time1
5.119000196456909
>>> def foo():
	time_start = time.time()
	for n in range(8):
		print(n)
	used_time = time.time()-time_start
	print(used_time)

	
>>> foo()
0
1
2
3
4
5
6
7
0.07000017166137695
>>> class Student():
	pass

>>> student = Student()
>>> type(student)
<class '__main__.Student'>
>>> type(Student)
<class 'type'>
>>> type(type)
<class 'type'>
>>> type(type(type))
<class 'type'>
>>> class P():
	x = 1

	
>>> class C1(P):
	pass

>>> class C2(P):
	pass

>>> print(P.x, C1.x, C2.x)
1 1 1
>>> C1.x = 2
>>> print(P.x, C1.x, C2.x)
1 2 1
>>> Parent.x = 3
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    Parent.x = 3
NameError: name 'Parent' is not defined
>>> P.x = 3
>>> print(P.x, C1.x, C2.x)
3 2 3
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
