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


