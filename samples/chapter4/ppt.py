序列定义
序列是这样的一些python类型，它们的成员是有序排列的，并且可以通过下标偏移量访问到它的一个或者几个成员，它包括字符串，列表和元组
序列操作
 seq[i]             索引，获得下表为i的元素
 seq[m:n]       切片,获得下标从m到n间的元素集合
切片没有越界的概念，结果只是取不到数据
 seq * n            序列重复n次
 seq1 + seq2    连接序列
 obj in seq     判断obj元素是否包含在seq中
 seq1 > seq2        比较


序列操作，
s = 'abcd'
s[0]                'a'
s[1:3]              'bc'
s[-1]   # 反向索引      'd'
s[-3:-1]            'bc'
s[2:] # 默认到结尾       'cd'
s[:3] # 从头开始索引  'abc'
s[:]  # 返回本身，如果是列表的话，返回一个拷贝
 'a' in s           True
序列函数
len(seq)        返回序列长度
max(seq)        返回序列中最大值
min(seq)        返回序列中最小值
sorted(seq)     返回另一个排过序的列表
reversed(seq)   返回一个reversed object
sum(seq)        求和
enumerate(seq)      对于一个可迭代的（iterable）的对象（如列表、字符串），enumerate将其组成一个索引序列


字符串
字符串方法>>> quest = 'what is your favorite color?'
quest.count(‘or’)       # 计数指定的字符创    2
quest.endswith(‘color?’)    # 判断是否已特定字符串结尾  True
quest.startswith('What')    # False
quest.isalpha()     # 判断是否只包含字母
quest.isnumeric()       # 判断是否只包含数字
quest.isalnum()     # 判断是否只包含字母或数字  
quest.upper()           # 转换成大写
quest.lower()           # 转换成小写
quest.capitalize()      # 首字母大写
字符串方法
>>> quest.split(s)          # 以s为分隔符，分隔字符串，返回列表
['what', 'is', 'your', 'favorite', 'color?']
>>> '-'.join(quest.split(' '))      #  合并元素
'what-is-your-favorite-color?'
>>> quest.find('or')        # 和quest.index(‘or’) 
16
>>> quest.find('sdfsdf')    # quest.index和find不同在于找不到报错
-1
 >>> '    what?   '.strip()         # 去掉两边空格包括空格，TAB和回车


字符串格式化输出
用format
print('Hello {}!'.format('world'))
print('I have {} apples.'.format(9))
print('I have {:.2f} apples.'.format(0.1234))
print('{} have {} apples.'.format('tom', 9))
print('{0} have {1} apples.'.format('tom', 9))
输出Hello world!
I have 9 apples.
I have 0.12 apples.
tom have 9 apples.
tom have 9 apples.


练习
1 取出url的域名
'https://www.zhihu.com/question/29998374'
url = 'https://www.zhihu.com/question/29998374'
url.split('/')[2]



2 计算banana中a的个数，不能用count


列表（list）
列表是一个有序的容器，可以通过下标或者切片操作来访问某一个或者某一块连续的元素。
列表是能保留任意数目的python对象的灵活的容器，可以
添加（append，extend，insert），
删除（remove，pop），
排序（sort）等各种灵活的操作

列表序列操作
>>> l = [‘e’, ‘b’, ‘c’, ‘d’]          # 创建列表   l = [] 空列表
>>> l[0] = ‘a’          # 赋值    l = [‘a', 'b', 'c', 'd']
>>> l[0]        # 'a'
>>> l[1:3]      # ['b', 'c']
>>> l[-1]       # 'd'
>>> l[-4]       # 'a‘
>>> l[-3:-1]        # ['b', 'c']
>>> l[2:]       # ['c', 'd']
>>> l[:3]       # ['a', 'b', 'c']
>>> 'e' in l        # False
if lst:                     # 判断列表不为空   if len(lst) ！= 0:不要这样写
    if lst == []   


列表方法
lst = [1, 2, 3, 4, 5]
添加元素
 lst.append(6)          # 在末尾添加单个元素
 lst.extend([7, 8, 9])  # 添加一个序列
 lst.insert(0, 0)       # 指定位置添加元素
 删除元素
 lst.pop()          # 删除并返回被删除的元素，默认最后一个
 lst.pop(4)     # 删除指定位置的元素
 lst.remove(4)      # 删除指定元素
 找出特定元素下标
 lst.index()                        # list没有find方法
思考：append，extend一个字符串有什么不同

列表方法
排序
 lst.sort()         
 lst.sort(reverse=True) # 倒序排序
 lst.sort()   和  sorted(lst) 区别?
 前者在原来的列表上操作，无返回值，后者返回一个新的列表

 翻转
 lst.reverse()      # [1,3,2,4]  ----> [4,2,3,1]
 lst.reverse()   和 reversed()区别？

循环技巧
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for n in sorted(basket):
     print(n)
for n in reversed(basket):
    print(n)
for i, v in enumerate(basket):
   print(i, v)

练习
1 去掉names中元素两边的空格并生成一个新的列表
names = ['   Tom', '   Jack   ', 'Mary', 'Jerry     ']
striped_names = []
for name in names:
    striped_names.append(name.strip())
print(striped_names)
2 得到一个元素不重复的列表
   lst = [1,3,5,4,2,3,4,5,6,4,3]
lst2 = []
for n in lst:
    if n not in lst2:
        lst2.append(n)
3
1. lst = [ [ ] ] * 3
2. lst  # output?
3. lst[0].append(10)
4. lst  # output?
5. lst[1].append(20)
6. lst  # output?
7. lst.append(30)
8. lst  # output?
第2，4，6，8行的输出是什么？解释你的答案.




元组（tuple）
元组和列表非常类似，可以用下标和切片获取元素
定义一个元组 t = (1, 2, 3)， 定义单元素元组?
t = (1,)

元组是不可变类型，一旦创建，它自身的元素不可变，不能对元素赋值 
Python中3种不可变类型
数字，字符串，元组


关于元组的不可变是指元组所指向的元素不变，但那些所指向的元素不一定是不可变的
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])  # 改变的是列表

 列表元组可以通过list() , tuple()互转


zip(it0，it1….itN)
zip函数返回一个列表，他的第一个元素是it0，it1….itN这些可迭代对象的第一个元素组成的元组，第二个以此类推
zip([1,2,3], [‘a’,’b’,’c’])
指定值的排序，利用itemgetter
 from operator import itemgetter
 name_score = [('cat', 66), ('tom', 50), ('bob', 75), ('pig', 85)]
 sorted(name_score)
 sorted(name_score , key = itemgetter(0))
 sorted(name_score , key = itemgetter(1))


列表生成式（list comprehensions）
生成一个list，它的元素是[1, 2, 3, 4, 5]的平方
[n*n for n in range(1, 6)]
不用为了生成一个简单列表而写for循环，使代码更简洁
去掉names中元素两边的空格并生成一个新的list（用生成式写）
names = ['   Tom', '   Jack   ', 'Mary', 'Jerry     ']

生成一个列表，它的元素是奇数的平方
[n*n for n in range(1, 6) if n%2 == 1]

元素奇数的平方，偶数不变
[n*n if n%2 == 1 else n for n in range(1, 6)]

练习：有这样一个列表lst = ['HELLO', 123, 234, 'World', 'Python'] ，生成这样一个列表，把字符串都小写，其他不变
[n.lower()if isinstance(n, str)else n for n in lst  ]


