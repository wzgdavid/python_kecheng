from operator import itemgetter

text = '''a qweras dpoiujnb
chgfmgkj nfmACBOPa
'''
yuanyin = 'aeiou'
counter = dict.fromkeys(yuanyin, 0)

for n in text.lower():
    if n in yuanyin:
        counter[n] += 1
#print(counter)


dct = {123: 'cat', 666: 'tom', 555: 'pig'}
dct2 = {}
for key, value in dct.items():
    dct2[value] = key
#print(dct2)
dct3 = {key for key, value in dct.items()}
#print(dct3)


# 求两门课都及格学生名字
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}
## for
#mjige = set()
#ejige = set()
#for name, score in math.items():
#    if score>=60:
#        mjige.add(name)
#for name, score in english.items():
#    if score>=60:
#        ejige.add(name)
#print(mjige & ejige)

mjige = {name for name, score in math.items() if score>=60}
ejige = {name for name, score in english.items() if score>=60}
#print(type(ejige))
#print(mjige & ejige)

mitems = math.items()
sortedm = sorted(mitems, key=itemgetter(1), reverse=True)
print(sortedm)
#for item in reversed(sortedm):
#    print(item[0])
for name, score in sortedm:
    print(name)