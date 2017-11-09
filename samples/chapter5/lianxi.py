from operator import itemgetter

'''
1  统计一段文本中元音的个数，生成一个字典
 比如counter = {'a': 11, 'e': 15, 'i': 16, 'o': 12, 'u': 4}

'''
text = 'hsfjl jnoaien nopasn  ndof npan '
yuanyin = 'aeiou'
counter = dict.fromkeys(yuanyin, 0)
for c in text.lower():
   if c in yuanyin:
       counter[c] += 1
print(counter)


'''
练习2
 phone_number = {'marty': 1234, 'dave': 6666, 'kerry': 5555}
 颠倒字典中的键和值 打印{1234: 'marty', 6666: 'dave', 5555: 'kerry'}
'''
phone_number = {'marty': 1234, 'dave': 6666, 'kerry': 5555}

pn = dict.fromkeys(phone_number.values())
for name, number in phone_number.items():
    pn[number] = name
print(pn)

# 值有重复的情况
# 可以把相同值的键放在一个列表里
dct = {}
for name, phone in phone_number.items():
    if phone in dct:
        dct[phone].append(name)
    else:
        dct[phone] = [name]
print(dct)

'''
3, 有两门课的成绩，打印出两门课都及格的学生名字
'''
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}

# 用for
math_jige = set()
english_jige = set()
for name, score in math.items():
    if score >= 60:
        math_jige.add(name)
for name, score in english.items():
    if score >= 60:
        english_jige.add(name)
both_jige = math_jige & english_jige
#print(both_jige)

# 生成式
math_jige = {name for name, score in math.items() if score >= 60}
english_jige = {name for name, score in english.items() if score >= 60}
both_jige = math_jige & english_jige
#print(both_jige)


'''
4, 按成绩从高到低，打印出学生的名字

'''
math = {'cat': 66, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}

scores = set(math.values())
sorted_scores = sorted(list(scores))
for score in sorted_scores:
    for name, score2 in math.items():
        if score == score2:
            print(name)

# 用itemgetter
sorted_scores = sorted(math.items(), key = itemgetter(1))
for name, score in sorted_scores:
    print(name)

# BDA3上课时想出来的课后练习
#输入的字典 = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
#颠倒字典中的键和值 {'sdf':'1ff3'}
#写一个函数返回{123: 'cat', 666: 'tom', 555: ['pig', 'moon']}
#写一个函数，接收一个字典，返回一个键值颠倒字典，
#如果值不重复的话，直接键值颠倒
#如果值重复的话，把原来字典的键放在列表里
#做一下异常处理，检查这个参数是不是一个字典
#然后检查key是不是字符串，value是不是数字
#一个不符合就整个不处理

def reverse_keyvalue(dct):
    if not isinstance(dct, dict):
        raise TypeError('必须是个字典')
    
    keys_is_str = [isinstance(key, str) for key in dct]
    values_is_number = [isinstance(value, str) for value in dct.values()]
    if not all(keys_is_str):
        raise KeyError('键必须是字符串')
    if not all(values_is_number):
        raise ValueError('值必须是数字')
    # 检查完毕
    dict_return = {}
    for key, value in dct.items():
        if value not in dict_return:
            dict_return[value] = key
        else:
            dict_return[value] = [dict_return[value]]
            dict_return[value].append(key)
    print(dict_return)
    return dict_return
dct = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}

reverse_keyvalue(dct)