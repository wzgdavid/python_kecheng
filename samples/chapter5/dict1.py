names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

index = names.index('Bob')
#print(scores[index])

scores = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
scores['Bob']



# 统计一段文本中元音的个数，生成一个字典
text = '''This library reference manual describes the standard library 
that is distributed with Python. It also describes some of the optional 
components that are commonly included in Python distributions.'''

yuanyin = ('a', 'e', 'i', 'o', 'u')
counter = dict.fromkeys(yuanyin, 0)
for c in text.lower():
   if c in yuanyin:
       counter[c] += 1
print(counter)






'''
phone_number = {'marty': 1234, 'dave': 6666, 'kerry': 5555}
 颠倒字典中的键和值（值没有重复）
 结果{1234: 'marty', 6666: 'dave', 5555: 'kerry'}
'''
# 用for
phone_number = {'marty': 1234, 'dave': 6666, 'kerry': 5555}
pn = dict.fromkeys(phone_number.values())
for name, number in phone_number.items():
    pn[number] = name
print(pn)

# 字典生成式
pn2 = {number:name  for name, number in phone_number.items()}
print(pn2)