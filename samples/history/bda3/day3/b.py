# 集合
a = set() # 定义一个空集合
a = {1,2,3,3,3}  # 直接定义集合
lst = [1,4,2,3,2,2,3,3,2,2,1,23]
a = set(lst) # 用构造器定义
lst = list(a)
lst = list(set(lst)) # 
#print(lst)
#print(a, type(a))

#s = {id, id, type, help, str}
#print(s)

a.add(0) # 添加元素
a.update({2,3,4,5,6}) # 
a.remove(1)
#print(a)
 
#print(set('123456') >= set('12435'))
jiaoji = set('sheep') & set('shop') # 交集
print(jiaoji)
bingji = set('sheep') | set('shop')
print(bingji)
buji = set('sheep') - set('shop') # shep  shop  e
print(buji)

print('----------练习 -------------')
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}
math_jige = set() # 数学及格的同学
eng_jige = set()
# 分别找出数学及格和英语及格的名字
# 然后再用集合交集
for name, score in math.items(): 
    if score >= 60:
        math_jige.add(name)
for name, score in english.items():
    if score >= 60:
        eng_jige.add(name)
both = math_jige & eng_jige
print(both)

[n**2 for n in range(1, 11)] # 列表
{n**2 for n in range(1, 11)} # 集合
print({n:n**2 for n in range(1, 11)})  # 字典

print('----------练习 分数排序 -------------')
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
sorted_scores = sorted(math.values(), reverse=True)
#print(sorted_scores)
# 键值对颠倒
scores2 = {}
for name, score in math.items():
    scores2[score] = name

for score in sorted_scores:
    print(scores2[score])

from operator import itemgetter
#print(math.items())
sorted_items = sorted(math.items(), 
    key=itemgetter(1), reverse=True)

#for item in sorted_items: 
#    print(item[0])
for name, score in sorted_items: 
    print(name)
'''
4大容器
都是可迭代对象
可迭代对象不止这4中，比如zip 返回是 zip_object，range
怎么判断对象是可迭代对象
from collections import Iterable; 然后用instance
列表    可以排序
字典，集合   都是无序的
元组   不可变
列表和元组 是序列

列表生成式
字典，和元组  类似   
但 元组没有这种
[n**2 for n in range(1, 11)] # 列表
{n**2 for n in range(1, 11)} # 集合
{n:n**2 for n in range(1, 11)}  # 字典
(n**2 for n in range(1, 11)) # 生成器 generator
'''
