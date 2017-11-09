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