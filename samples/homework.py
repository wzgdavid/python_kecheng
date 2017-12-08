# 根据代码画示意图
# 简单变量
# 1)  a = b = c = 0 ;  
#     a = 1;b=2
# 1.5)  a=0;b=0;c=0
# 2)  x, y = 3, 4
#     x, y = y, x
# 4)  a = b = c = [] ; 
# 4.5)  a=[];b=[];c=[]
# 容器
# 1)  lst = [1, 2, 3, 4, 5]
# 2)  lst2 = [1, 2, [3, 4]]
#         lst2[0] = 11
#         lst2[2][0] = 33
# 3)  dct = {'name': 'tom',
#             'age':  99,
#             'scores': [77, 88, 99]   }
#     
# 函数
# 1)  def foo(a, b=0):pass
# 2)  def foo(a, b=[]):pass
# 3)  def foo(a, b):
#         name = 'tom'
#         scores = [77, 66, 88]


print('-----------------列表扁平化-----------------------')
#lst = [3, 7, [0, [9, 5], 7], 1] 把这个列表扁平化处理
#lst2 = [3, 7, 0, 9, 5, 7, 1] # 扁平化处理结果
# 'abc-efg-'.replace('-','+') # 可用replace
import re
lst = [3, 7, [0, [9, 5], 7], 1]
lst_str = str(lst) # 字符串形式‘[3, 7, [0, [9, 5], 7], 1]’
lst_str2 = lst_str.replace(']', '').replace('[', '')
#lst_str2 = re.sub(r'[\[\]]', '', lst_str)
splited_lst = lst_str2.split(',') # 返回列表
lst2 = [int(n) for n in splited_lst]
print(lst2) 

print('-----------------分数值计算-----------------------')
# 找出这个scores里的最大值和最小值
scores = [55,66,77,88,99,44]
high = 0
low = 99
for score in scores:
    if score > high:
        high = score
    if score < low:
        low = score

print(high, low)



# 有这样一个记录分数的字典，找出不及格的同学名字
scores = {'cat': 55, 'tom': 77, 'pig': 59, 'moon': 99}
bujige = []
for name, score in scores.items():
    if score < 60:
        bujige.append(name)
print(bujige)


print('-----------------号码段 运营商-----------------------')
# 随机产生n个手机号码
移动 = (134,135,136,137,138,139,147,150,151,152,157,158,159,188)
联通 = (130,131,132,155,156,186)
电信 = (133,153,180,189)
import random
def random_phone_number():
    yys = 134,135,136,137,138,139,147,150,151,152,157,158,159,130,131,132,155,156,186,130,131,132,155,156,186,133,153,180,189,133,153,180,189
    head = str(random.choice(yys))
    body = ''.join( [str(random.randint(0,9)) for n in range(8)] )
    return head + body
#for n in range(10):
#    print(random_phone_number())
#numbers = [random_phone_number() for n in range(10)]
#print(numbers)
# 这里才开始作业
numbers = ['18660983737', '13824131713', '15582824315', '18999006336', '15584533465', '13263949074', '15991465635', '15195635532', '13956594791', '18937591568']
# 根据给到的手机号码，计算三个运营商的用户比例(没讲函数前)
user_yidong = user_liantong = user_dianxin = 0
for number in numbers:
    qian3 = int(number[:3])
    if qian3 in 移动:
        user_yidong += 1
    elif qian3 in 联通:
        user_liantong += 1
    elif qian3 in 电信:
        user_dianxin += 1
print(user_yidong, user_liantong, user_dianxin)

print('-----------------号码段 运营商2-----------------------')
# 同样的号码段，把号码和运营商组合在一个字典里  
# 既字典的键是号码， 值是对应的运营商
# 比如 numbers = {
#     '18660983737': '联通',
#     '13824131713': '移动',
# }
numbers_dict = {}
for number in numbers:
    qian3 = int(number[:3])
    if qian3 in 移动:
        numbers_dict[number] = '移动'
    elif qian3 in 联通:
        numbers_dict[number] = '联通'
    elif qian3 in 电信:
        numbers_dict[number] = '电信'
print(numbers_dict)


print('-----------------键值颠倒----------------------')
#输入的字典 = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
#颠倒字典中的键和值 {'sdf':'1ff3'}
#写一个函数返回{123: 'cat', 666: 'tom', 555: ['pig', 'moon']}
#写一个函数，接收一个字典，返回一个键值颠倒字典，
#如果值不重复的话，直接键值颠倒
#如果值重复的话，把原来字典的键放在列表里
#做一下异常处理，检查这个参数是不是一个字典
#然后检查key是不是字符串，value是不是数字
#一个不符合就整个不处理

# 简化版本，不用做异常处理
def reverse_keyvalue(dct):
    if not isinstance(dct, dict):
        raise TypeError('必须是个字典')
    keys_is_str = [isinstance(key, str) for key in dct]
    values_is_number = [isinstance(value, int) for value in dct.values()]
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





