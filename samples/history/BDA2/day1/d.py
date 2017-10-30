Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'hello world'
>>> lst = list(s)
>>> lst
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> 'o' in lst
True
>>> s2 = 'hello'
>>> s > s2
True
>>> a = 'abc'
>>> b = 'sheep'
>>> a < b
True
>>> ord('a')
97
>>> ord('s')
115
>>> ord(' ')
32
>>> lst2 = [1,2,3]
>>> lst
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> lst > lst2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lst > lst2
TypeError: '>' not supported between instances of 'str' and 'int'
>>> lst2 = ['1','2','3']
>>> lst > lst2
True
>>> ord('A')
65
>>> len(s)
11
>>> max(s)
'w'
>>> max('aA')
'a'
>>> min([1,2,3,4])
1
>>> sorted(s)
[' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

>>> reversed(s)
<reversed object at 0x02D1D690>
>>> str(reversed(s))
'<reversed object at 0x02D1DC90>'
>>> list(reversed(s))
['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
>>> lst = [2,4,5,61]
>>> for n in reversed(lst):
	print(n)

	
61
5
4
2
>>> sum(lst)
72
>>> s
'hello world'
>>> s.endswith('world')
True
>>> s.startswith('hell')
True
>>> 'sdf+_+_+'.isalpha()
False
>>> '12312314+dgdg+_+'.isnumeric()
False
>>> '1231213'.isnumeric()
True
>>> '1231.213'.isnumeric()
False
>>> s
'hello world'
>>> s.count('l')
3
>>> s.count('lo')
1
>>> 'asdf123'.isalpha()
False
>>> 'asdf123'.isalnum()
True
>>> 'asdf 123'.isalnum()
False
>>> s.upper()
'HELLO WORLD'
>>> s
'hello world'
>>> s.split('')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.split('')
ValueError: empty separator
>>> s.split()
['hello', 'world']
>>> s.split('l')
['he', '', 'o wor', 'd']
>>> s.split('0')
['hello world']
>>> s.split('h')
['', 'ello world']
>>> lst = s.split('l')
['he', '', 'o wor',
 
SyntaxError: multiple statements found while compiling a single statement
>>> lst = s.split('l')
>>> lst
['he', '', 'o wor', 'd']
>>> 'l'.join(lst)
'hello world'
>>> xlh = '12345 12344 123124 123123'
>>> '-'.join(xlh.split())
'12345-12344-123124-123123'
>>> xlh.replace(' ', '-')
'12345-12344-123124-123123'
>>> s.find('h')
0
>>> s.find('l')
2
>>> l
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> s
'hello world'
>>> s.find('x')
-1
>>> s.index('l')
2
>>> s.index('X')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.index('X')
ValueError: substring not found
>>> s.index('ll')
2
>>> 'pi is {}'.format(3.1415926)
'pi is 3.1415926'
>>> 'pi is {.2f}'.format(3.1415926)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    'pi is {.2f}'.format(3.1415926)
AttributeError: 'float' object has no attribute '2f'
>>> 'pi is {:.2f}'.format(3.1415926)
'pi is 3.14'
>>> 'pi is {:.2f}'.format(3.1415926, 1,111111)
'pi is 3.14'
>>> 'pi is {:.2f}'.format(3.1415926, 1.111111)
'pi is 3.14'
>>> 'pi is {0:.2f}'.format(3.1415926, 1.111111)
'pi is 3.14'
>>> 'pi is {1:.2f}'.format(3.1415926, 1.111111)
'pi is 1.11'
>>> 'hello %s' % 'world'
'hello world'
>>> 'hello {}'.format('world')
'hello world'
>>> 'hello %d' % 1
'hello 1'
>>> 'hello %s  %s' % 'world', '!'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    'hello %s  %s' % 'world', '!'
TypeError: not enough arguments for format string
>>> 'hello %s  %s' % ('world', '!')
'hello world  !'
>>> 'hello {}{}'.format('world', '!')
'hello world!'
>>> 'hello %s ' %('world', '!')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    'hello %s ' %('world', '!')
TypeError: not all arguments converted during string formatting
>>>  'hello {}'.format('world', '!')
 
SyntaxError: unexpected indent
>>> 'hello {}'.format('world', '!')
'hello world'
>>> url = 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#tensorflow'
>>> url.spilt('/')[2]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    url.spilt('/')[2]
AttributeError: 'str' object has no attribute 'spilt'
>>> url.split('/')[2]
'www.lfd.uci.edu'
>>> len('banana'.split())-1
0
>>> len('banana'.split('a'))-1
3
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> lst
['he', '', 'o wor', 'd']
>>> lst = [1,2,3,4]
>>> lst.append(5)
>>> lst
[1, 2, 3, 4, 5]
>>> lst2 = list('1234')
>>> lst2
['1', '2', '3', '4']
>>> l = []
>>> l
[]
>>> len(l)
0
>>> bool(l)
False
>>> l = list()
>>> l
[]
>>> help(list.append)
Help on method_descriptor:

append(...)
    L.append(object) -> None -- append object to end

>>> lst
[1, 2, 3, 4, 5]
>>> lst.append([99,88])
>>> lst
[1, 2, 3, 4, 5, [99, 88]]
>>> lst = [1,2,3]
>>> lst
[1, 2, 3]
>>> lst.extend([99, 88])
>>> lst
[1, 2, 3, 99, 88]
>>> help([].extend)
Help on built-in function extend:

extend(...) method of builtins.list instance
    L.extend(iterable) -> None -- extend list by appending elements from the iterable

>>> lst
[1, 2, 3, 99, 88]
>>> lst.insert(2, 4)
>>> lst
[1, 2, 4, 3, 99, 88]
>>> lst.insert(5 , 100)
>>> lst
[1, 2, 4, 3, 99, 100, 88]
>>> lst.insert(-2 , 101)
>>> lst
[1, 2, 4, 3, 99, 101, 100, 88]
>>> lst.insert(1112, 4)
>>> lst
[1, 2, 4, 3, 99, 101, 100, 88, 4]
>>> lst[8]
4
>>> lst = [1,2,3]
>>> lst.remove(1)
>>> lst
[2, 3]
>>> lst = list('abcd')
>>> lst.remove('a')
>>> lst
['b', 'c', 'd']
>>> lst.remove('aa')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    lst.remove('aa')
ValueError: list.remove(x): x not in list
>>> help([].remove)
Help on built-in function remove:

remove(...) method of builtins.list instance
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.

>>> lst
['b', 'c', 'd']
>>> poped = lst.pop()
>>> poped
'd'
>>> lst
['b', 'c']
>>> lst = list('abcd')
>>> lst.pop(1)
'b'
>>> lst
['a', 'c', 'd']
>>> del lst[0]
>>> lst
['c', 'd']
>>> lst = list('black sheep')
>>> lst
['b', 'l', 'a', 'c', 'k', ' ', 's', 'h', 'e', 'e', 'p']
>>> lst.sort()
>>> lst
[' ', 'a', 'b', 'c', 'e', 'e', 'h', 'k', 'l', 'p', 's']
>>> lst = list('black sheep')
>>> lst2 = sorted(lst)
>>> lst2
[' ', 'a', 'b', 'c', 'e', 'e', 'h', 'k', 'l', 'p', 's']
>>> lst
['b', 'l', 'a', 'c', 'k', ' ', 's', 'h', 'e', 'e', 'p']
>>> lst[0] = 'c'
>>> lst
['c', 'l', 'a', 'c', 'k', ' ', 's', 'h', 'e', 'e', 'p']
>>> lst[1:9:2]
['l', 'c', ' ', 'h']
>>> lst[1:9:3]
['l', 'k', 'h']
>>> range(1, 20, 2)
range(1, 20, 2)
>>> for n in range(1, 20, 2):
	print(n)

	
1
3
5
7
9
11
13
15
17
19
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> lst = []
>>> if len(lst)==0:
	print('list is 空')

	
list is 空
>>> if not lst:
	print('空')

	
空
>>> if lst:
	print('这个列表非空')

	
>>> lst = [1]
>>> 
>>> if lst:
	print('这个列表非空')

	
这个列表非空
>>> '    a   '.strip()
'a'
>>> b = '    a   '.strip()
>>> b
'a'
>>> [1,2] *3
[1, 2, 1, 2, 1, 2]
>>> [ [ ] ] * 3

[[], [], []]
>>> [1] * 3
[1, 1, 1]
>>> [[10], [], []]
