page5
字典
字典是一种容器，能存储任意个数的python对象，包括容器
字典和序列型容器的区别是存储和访问数据方式不同，序列用数字，按顺序索引，字典是一种映射类型，用不可变类型做键，最常见的使用字符串。
创建字典
 d = {}             # 空字典
 d = dict()             # 用dict类创建
 d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
 d = dict([('Michael', 95), ('Bob', 75), ('Tracy', 85)])
 d = dict.fromkeys([‘a’, ‘b’], 1)   # 1是值，默认None

page6
添加元素
 scores = {'michael': 95, 'bob': 75}
 scores[‘tom’ ] = 60    # 添加
 scores[‘bob’] = 99 # 如果键已存在，会更新掉原值，键唯一
 scores.update({‘tom’: 99, ‘cat’: 88})    # 同样是，无则添加，有则更新
删除元素
 del scores[‘tom’ ]
 scores.pop(‘bob’)  # 删除bob键并返回对应的值
 scores.clear()               # 清空字典

page7
获取值
 scores[‘bob’]             # 没有对应的键会报错
 scores.get(‘bob’)          # 通过get获取值，不会报错，无值返回None
 scores.get(‘bob’, 99)  # 有默认值返回默认值
 scores.keys()      # 获取所有键
 scores.values()    # 获取所有值
判断字典中是否有某个键
 'bob' in scores

page8

遍历
 打印出所有键和值
 for name in scores:
    print(name, scores[name])


 for name, score in scores.items(): # 键值对遍历
    print(name, score)
 for item in scores.items(): # 每次迭代，items()方法返回一个元组
    print(item)

page9
练习1
 统计一段文本中元音的个数，生成一个字典，键是被统计的字母，值是对应的个数
 比如counter = {'a': 11, 'e': 15, 'i': 16, 'o': 12, 'u': 4}

page10
练习2
 phone_number = {'cat': 123, 'tom': 666, 'pig': 555}
 颠倒字典中的键和值 打印{123: 'cat', 666: 'tom', 555: 'pig'}

page11
练习3
 phone_number = {'cat': 1234, 'tom': 666, 'pig': 555,'apple',666}
 颠倒字典中的键和值 打印{1234: ['cat'], 666: ['tom','apple'], 555: ['pig']}



page12
集合
 集合和字典类似，也是一组key的集合，但不存储value，
 集合没有重复
集合创建
 s = set([1, 2, 3, 4])  # set的参数是个可迭代对象
 s = set('abcde')   
 s2 = {1, 2, 3, 4}      # 直接创建  
 s = set()          # 空集合， 不能 s = {},这是个字典

page13
集合更新
 s.add(1)
 s.update([1, 2, 5])        # 参数是可迭代对象
 s.remove(1)
集合比较
 <  子集      > 超集     == 元素相同  !=
 set('shop') == set('posh')
 set('shop') <  set('cheeseshop')

page14
集合操作
 并集
>>>  set('shop')| set('cheese')     
 交集    
>>>  set('shop')& set('cheese')
 相对补集
>>>  set('shop')- set('cheese')

删除一个list里面的重复元素

page15
练习4
1, 有两门课的成绩，打印出两门课都及格的学生名字
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}

page16
练习5
2,按成绩从高到低，打印出学生的名字
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
# 用itemgetter


