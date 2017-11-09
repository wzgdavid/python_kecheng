Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'hello {} !'.format('world')
'hello world !'
>>> 'hello {} {} !'.format('world')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    'hello {} {} !'.format('world')
IndexError: tuple index out of range
>>> 'hello {} {} !'.format('world', 'tom')
'hello world tom !'
>>> 'hello {0} {1} !'.format('world', 'tom')
'hello world tom !'
>>> 'hello {0} {1} !'.format('world')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    'hello {0} {1} !'.format('world')
IndexError: tuple index out of range
>>> 'hello {0} {0} !'.format('world')
'hello world world !'
>>> 'a'.center(9)
'    a    '
>>> 'a'.center(8)
'   a    '
>>> len('a'.center(8))
8
>>> s = 'abcde'
>>> lst = [1,2,3,4]
>>> lst[0]
1
>>> s[0]
'a'
>>> s[2]
'c'
>>> s[4]
'e'
>>> s[5]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[5]
IndexError: string index out of range
>>> t = (1,2,3)
>>> lst
[1, 2, 3, 4]
>>> t[2]
3
>>> s
'abcde'
>>> s[0:3] # 切片  slice
'abc'
>>> s[1:3]
'bc'
>>> s[1:99]
'bcde'
>>> s[99:999]
''
>>> bool('')
False
>>> a = s[99:999]
>>> if a:
	print('asdfsdf')

	
>>> s[-5:-1]
'abcd'
>>> s[-1]
'e'
>>> s
'abcde'
>>> s[-2]
'd'
>>> s[-1:-5]
''
>>> s[999:99]
''
>>> s[5:3]
''
>>> s[3:3]
''
>>> lst = [1,2,3,4,5]
>>> lst[999:99]
[]
>>> lst[-999:99]
[1, 2, 3, 4, 5]
>>> s
'abcde'
>>> s + s
'abcdeabcde'
>>> 'a'*7
'aaaaaaa'
>>> [1]*9
[1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> [[1]]*5
[[1], [1], [1], [1], [1]]
>>> lst = [[1]]*5
>>> lst
[[1], [1], [1], [1], [1]]
>>> id(lst[0])
48125256
>>> id(lst[1])
48125256
>>> id(lst[-1])
48125256
>>> lst2 = [[1], [1], [1], [1], [1]]
>>> lst2
[[1], [1], [1], [1], [1]]
>>> id(lst2[0])
50581768
>>> id(lst2[1])
50403656
>>> '大范甘迪'
'大范甘迪'
>>> a = [1]
>>> a = 1
>>> b = 1
>>> ss = 'a'
>>> sss = 'a'
>>> a = [1]
>>> b = [1]
>>> c = []
>>> d = []
>>> id(c)
50403272
>>> id(d)
48125704
>>> id([])
48126280
>>> id(ss)
33087136
>>> id(sss)
33087136
>>> id('a')
33087136
>>> 'a' in 'abcde'
True
>>> 'a' not in 'sss'
True
>>> 'aa' in 'abcde'
False
>>> 'a' not in 'sadf'
False
>>> 1 in [2,3,4]
False
>>> 1 not in (4,5,6)
True
>>> 'abc' > 'abd'
False
>>> ord('c')
99
>>> ord('d')
100
>>> 'abcd' > 'abc'
True
>>> ord(' ')
32
>>> s
'abcde'
>>> s[1:]
'bcde'
>>> s[:4]
'abcd'
>>> s[:]
'abcde'
>>> id(s) == id(s[:]) # s is s[:]
True
>>> s is s[:]
True
>>> lst
[[1], [1], [1], [1], [1]]
>>> lst = [1,2,3,4,5]
>>> lst[:]
[1, 2, 3, 4, 5]
>>> lst is lst[:]
False
>>> t = (1,2,3)
>>> t[:]
(1, 2, 3)
>>> t is t[:]
True
>>> len(t)
3
>>> max(t)
3
>>> sum(t)
6
>>> sum(range(1, 101))
5050
>>> sum(range(2, 101,2))
2550
>>> s
'abcde'
>>> s = 'abcdefgh'
>>> s[1:5:2]
'bd'
>>> range(1, 101)[1:5:2]
range(2, 6, 2)
>>> for n in range(1, 101)[1:5:2]:
	print(n)

	
2
4
>>> lst = [3,4,5,1,6,7]
>>> sorted(lst)
[1, 3, 4, 5, 6, 7]
>>> lst
[3, 4, 5, 1, 6, 7]
>>> sorted(lst, reversed=True)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    sorted(lst, reversed=True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> sorted(lst, reverse=True)
[7, 6, 5, 4, 3, 1]
>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> sorted('asdfsdf')
['a', 'd', 'd', 'f', 'f', 's', 's']
>>> reversed('4156')
<reversed object at 0x0000000003014E80>
>>> print(reversed('4156'))
<reversed object at 0x0000000002D7EE80>
>>> list(reversed('4156'))
['6', '5', '1', '4']
>>> str(reversed('4156'))
'<reversed object at 0x0000000002D7EE80>'
>>> for n in reversed('4156'):
	print(n)

	
6
5
1
4
>>> s = 'abcde'
>>> for n in s:
	print(n)

	
a
b
c
d
e
>>> len(s)
5
>>> for i, n in enumerate(s):
	print(i, n)

	
0 a
1 b
2 c
3 d
4 e
>>> s
'abcde'
>>> a = (1,3)
>>> a = 1,3
>>> type(a)
<class 'tuple'>
>>> t = (1)
>>> type(t)
<class 'int'>
>>> t = 1,
>>> type(t)
<class 'tuple'>
>>> t
(1,)
>>> a = 'hello world'
>>> a.count('e')
1
>>> a.count('aaaa')
0
>>> a.startswith('hello w')
True
>>> a.endswith('rld')
True
>>> a.isalpha('asdfasdf')
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a.isalpha('asdfasdf')
TypeError: isalpha() takes no arguments (1 given)
>>> a.isalpha()
False
>>> 'asdfasdf'.isaplpha()
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    'asdfasdf'.isaplpha()
AttributeError: 'str' object has no attribute 'isaplpha'
>>> 'asdfasdf'.isalpha()
True
>>> '111'.isnumeric()
True
>>> int('111')
111
>>> 'sdf123'.isalnum()
True
>>> 'object has no attribute'.split()
['object', 'has', 'no', 'attribute']
>>> '121214-1231231-123123-123123'.split('-')
['121214', '1231231', '123123', '123123']
>>> '021-57896781'.split('-')
['021', '57896781']
>>> '-'.join(['021', '57896781'])
'021-57896781'
>>> ' '.join(lst)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    ' '.join(lst)
TypeError: sequence item 0: expected str instance, int found
>>> lst = [1,2,34]
>>> ''.join(lst)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    ''.join(lst)
TypeError: sequence item 0: expected str instance, int found
>>> lst = ['1','2','34']
>>> ''.join(lst)
'1234'
>>> lst = [1,3,4,5]
>>> lst2 = []
>>> for n in lst:
	lst2.append(str(n))

	
>>> lst2
['1', '3', '4', '5']
>>> ''.join(lst2)
'1345'
>>> s
'abcde'
>>> s.find('c')
2
>>> s.find('cc')
-1
>>> s.index('c')
2
>>> s.index('cc')
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    s.index('cc')
ValueError: substring not found
>>> 'sd  fs    '.strip()
'sd  fs'
>>> '{}'.format(0.1234)
'0.1234'
>>> '{.2f}'.format(0.1234)
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    '{.2f}'.format(0.1234)
AttributeError: 'float' object has no attribute '2f'
>>>  '{:.2f}'.format(0.1234)
 
SyntaxError: unexpected indent
>>> '{:.2f}'.format(0.1234)
'0.12'
>>> '{:.2f},  {:.1f}'.format(0.1234, 9.5678)
'0.12,  9.6'
>>> '{0}{1}'.format('hello ', 'world')
'hello world'
>>> '{1}{0}'.format('hello ', 'world')
'worldhello '
>>> '{0:.2f},  {1:.1f}'.format(0.1234, 9.5678)
'0.12,  9.6'
>>> '{1:.2f},  {0:.1f}'.format(0.1234, 9.5678)
'9.57,  0.1'
>>> '{:.2f},  {:.1f}'.format(0.1234)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    '{:.2f},  {:.1f}'.format(0.1234)
IndexError: tuple index out of range
>>> '{},  {0}'.format(0.1234)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    '{},  {0}'.format(0.1234)
ValueError: cannot switch from automatic field numbering to manual field specification
>>> '{0},  {0}'.format(0.1234)
'0.1234,  0.1234'
>>> '{0:.2f},  {0:.1f}'.format(0.1234)
'0.12,  0.1'
>>> '{1:.2f},  {1:.1f}'.format(0.1234, 9.5678)
'9.57,  9.6'
>>> 
