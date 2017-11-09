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
        raise TypeError('dct参数必须是字典')
    # 所有键是不是字符串的布尔值[True, False, True,......]
    keys_are_str = [isinstance(key, str) for key in dct]
    values_are_number = [isinstance(value, (int, float))
        for value in dct.values()]
    if not all(keys_are_str):
        raise KeyError('所有键必须是字符串')
    if not all(values_are_number):
        raise ValueError('所有值必须是数字')
    # 检查完毕
    dict_reversed = {} # 键值颠倒的字典
    for name, score in dct.items():
        if not score in dict_reversed: # 
            dict_reversed[score] = name
        else:
            # 555：'pig'  ==>  555:['pig']
            dict_reversed[score] = [dict_reversed[score]]
            dict_reversed[score].append(name)
    print(dict_reversed)

dct = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
#dct = 1
reverse_keyvalue(dct)
