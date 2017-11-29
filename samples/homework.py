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