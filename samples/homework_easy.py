'''
针对零基础的同学，应该再简单点，先让他们有编程的感觉
这里的零基础是指总来没接触过任何编程
'''
# 计算这个列表里有几个1
lst = [1,1,2,2,1,1,2,3,4,2,1]
cnt = 0
for n in lst:
    if n == 1:
        cnt += 1
print(cnt)



#输入的字典 = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
#颠倒字典中的键和值 {'sdf':'1ff3'}
#写一个函数返回{123: 'cat', 666: 'tom', 555: ['pig', 'moon']}
#写一个函数，接收一个字典，返回一个键值颠倒字典，
#如果值不重复的话，直接键值颠倒
#如果值重复的话，把原来字典的键放在列表里
#做一下异常处理，检查这个参数是不是一个字典
#然后检查key是不是字符串，value是不是数字
#一个不符合就整个不处理

# 简化版本，不用做异常处理 (其实还是不适合初学者)
def reverse_keyvalue(dct):
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



# 统计一段文本中单词的出现次数
text = '''
File system paths                      have historically been represented 
as str or bytes objects. This has led to people who 
write code which operate on file system paths to assume 
that such objects are only one of those two types 
(an int representing a file descriptor does not count 
as that is not a file path). Unfortunately that 
assumption prevents alternative object representations 
of file system paths like pathlib from working with pre-existing code,
 including Python’s standard library.
'''


import string
print(string.punctuation)