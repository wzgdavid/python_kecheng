import json

dct = {'tom': 90,'bob':90}
#print(dct)


score = [99,90,89]
#zipped = zip(names, score)
#dct = dict(zipped)
#print(id(dct))
#print(dct)
#dct = dict(tom=99, bob=90)
#print(id(dct))
#names = ['tom', 'jerry', 'bob']
#dct = dict.fromkeys(names, 0)
#print(dct)


#del dct1['cat']
#print(dct1)
#print(dct1.pop('py'))
#
#dct1.clear()
#print(dct1)
#dct1['time']
dct1 = {'tom': 90, 'bob': 99}
dct2 = {'tom': 80, 'cat': 70, 'py':66}
#dct['cat'] = 80
dct1.update(dct2)
#print(dct1.get('time', 60))
#print(dct1.get('tom', 60))
#print(dct1.keys())
#print(dct1.values())
#for value in dct1.values():
#    print(value)

dct1 = {'tom': 80, 'bob': 99, 'cat': 70, 'py': 66}
dct2 = {'tom': 0, 'bob': 0, 'cat': 0, 'py': 0}

#dct2 = dict.fromkeys('dct1.keys()', 0)
#print(dct2)

#for key in dct1:
#    print(key, dct1[key])
#
#for k, v in dct1.items():
#    print(k, v)
#
#for item in dct1.items():
#    print(item[0], item[1])
text = '''
is a non-negative integer, then JSON array elements and
    object members will be pretty-printed with that indent level. An indent
    level of 0 will only insert newlines
'''
yuanyin = 'aeiou'
counter = dict.fromkeys(yuanyin, 0)
for char in text.lower():
    if char in yuanyin:
        counter[char] += 1
#print(counter)
#dct2 = {}
#for 键, 值 in dct1.items():
#    dct2[值] = 键
#print(dct2)

#english = {'tom': 95, 'bob':85, 'cat':44}
#e = {value:key for key, value in math.items()}
#print(e)
#mjige = {n for n, s in math.items() if s>=60}
#ejige = {n for n, s in english.items() if s>=60}
#print(mjige & ejige)

from operator import itemgetter
math = {'tom': 45, 'bob':75, 'cat':88, 'py':55}
items = list(math.items())
print(items)
sorted_items = sorted(items, key=lambda x:x[1])

items.sort(lambda item:item[1])
#print(items)
for name, score in items:
    print(name)

t = ('bob', 75)
lambda item:item[1]
def foo(t):
    return t[1]
score = foo(t)
print(75)

#def foo(iter, key):
