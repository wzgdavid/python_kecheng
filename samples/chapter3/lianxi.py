#练习
#小明身高1.75，体重80.5kg。请根据BMI公式（体重(千克)除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：

bmi = 80.5/(1.75**2)
bmi = 28
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')






#请利用循环依次对列表中的每个名字打印出Hello, xxx!
lst = ['Bart', 123, 234, 'Lisa', 'Adam']
for n in lst:
    if isinstance(n, str):
        print('Hello {}!'.format(n))

for n in lst:
    if not isinstance(n, str):
        continue
    print('Hello {}!'.format(n))

# 练习二
# 统计出一段文本中的元音的个数
text = '''
Python is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple 
but effective approach to object-oriented programming.
'''
a_num = e_num = i_num = o_num = u_num = 0
for n in text:
    if n == 'a' or n == 'A':
        a_num += 1
    elif n == 'e' or n == 'E':
        e_num += 1
    elif n == 'i' or n == 'I':
        i_num += 1
    elif n == 'o' or n == 'O':
        o_num += 1
    elif n == 'u' or n == 'U':
        u_num += 1
    else:
        pass
print('number of {} is {}'.format('a', a_num))
print('number of {} is {}'.format('e', e_num))
print('number of {} is {}'.format('i', i_num))
print('number of {} is {}'.format('o', o_num))
print('number of {} is {}'.format('u', u_num))