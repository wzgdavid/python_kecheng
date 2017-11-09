
# 写注释时井号后面空一格
scores = {'michael': 95, 'bob': 75, 'tom': 50}
print( scores.items(), type(scores.items()) )
#print( list(zip([1,2], [3,4])) )
# 字典的遍历
#for key in scores: # 不需要in scores.keys()
#    print(key, scores[key])
#for item in [('michael', 95), ('bob', 75)]:
# scores.items() 就是[('michael', 95), ('bob', 75)]一个结构
#for item in scores.items(): # 
#    print(item[0], item[1])
#for key, value in scores.items():
#    print(key, value)

# 根据scores中的分数，打印出及格不及格
# michael  及格
# tom   不及格
for name, score in scores.items():
    if score >=60:
        print(name, '及格')
    else:
        print(name, '不及格')

# 练习 统计元音个数
text = '''
eturn the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.
'''
# counter = {'a':0, 'e':0....}
yuanyin = 'aeiou'
# 构建键是元音字母的字典
counter = dict.fromkeys(list(yuanyin), 0)

for char in text.lower():
    if char in yuanyin:
        counter[char] += 1  # 字典做了选择
print(counter)

大写字母 = 'A'
if 大写字母 == 'A':
    对应的小写 = 'a'
elif 大写字母 == 'B':
    对应的小写 = 'b'
elif 大写字母 == 'C':
    对应的小写 = 'c'
print(对应的小写)
# 构建一个键为大写，值为小写的字典
# 大小写对应的字典 = {'A': 'a', 'B':'b',。。。。。26个母}
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_dict = dict()
# 第一种方式，遍历
for c in alpha:
    alpha_dict[c.upper()] = c
#print(alpha_dict)
# 第二种方式， 用zip
alpha_dict = dict(zip(alpha.upper(), alpha))
#print(alpha_dict)
# 字典有选择功能
#print(alpha_dict['A'])

# 键值颠倒  值没有重复
scores = {'michael': 95, 'bob': 75, 'tom': 50}
# scores2 = {95: 'michael', 75: 'bob', 50: 'tom'}
scores2 = {}
for name, score in scores.items():
    scores2[score] = name
#print(scores2)
# 用zip
scores3 = dict(zip(scores.values(), scores.keys()))
#print(scores3)

# 键值颠倒  值有重复
print('--------------键值颠倒  值有重复---------------------')
scores = {'michael': 95, 'bob': 75, 'tom': 50, 'cat':50}
# scores2 = {50: ['tom', 'cat'], 75: ['bob']} 用列表放值
scores2 = dict.fromkeys(scores.values())
print(scores2)
for name, score in scores.items():
    # scores2[scores]
    # 判断scores2对应的值是不是list
    if isinstance(scores2[score], list):
        scores2[score].append(name)
    elif scores2[score] == None:
        scores2[score] = [name]
print(scores2)