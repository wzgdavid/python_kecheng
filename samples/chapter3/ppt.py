if语句
if 之后的布尔表达式被称作条件（condition）。 如果它为真，则缩进的语句会被执行。 如果不是，则什么也不会发生
if 语句一个语句头跟着一个缩进的语句体
语句体中可出现的语句数目没有限制，但是至少得有一个，什么都不做可以用pass做占位符
判断变量a是否为0，None，空字符串，空列表，空字典，可直接写成 if a:
if x < y:
    print('x is less than y')
    print('helllllllllllllllllllo')

else
之前的if分支得不到执行，则会执行else语句块
if x < y:
    print('x is less than y')
    print(‘hello ’)
else:
    print('x is greater than y')

elif
 elif是else if的缩写
 elif可以写n个，python中没有switch语句
 if语句执行是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    pass

If嵌套
一个条件可以嵌到另一个里面。我们可以这样写前一节的例子：
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
练习
小明身高1.75，体重80.5kg。请根据BMI公式（体重(千克)除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18：过轻
18-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
打印结果：


条件表达式
b = 11
if b > 0:
    a =1
else:
    a = 2

简单的赋值可以写成一句
a = 1 if b > 0 else 2

while循环
只要条件满足，就不断循环，条件不满足时退出循环
比如我们要计算100以内所有数之和，可以用while循环实现
sum_ = 0
n = 99
while n > 0:
    sum_ += n
    n -= 1
print(sum_)


for循环
for x in iter 就是把iter中每个元素代入变量x，然后执行缩进块的语句
numbers = [2,3,4,5]
for n in numbers:
    print(n*n)

for中放入if执行不同操作
for n in numbers:
    if n%2 == 0:
        print(n)
range()迭代整数
for n in range(19):
    print(n)


多重循环
传统写法略
from itertools import product
for i,j,k in product(range(5), range(6),range(7)):
    print(i,j,k)

Continue语句
跳出当前单个循环，接着执行下一个循环，可以用在while和for中使用，
numbers = [2,3,4,5]
for n in numbers:
    if n%2 == 1:
        continue
    print(n)

break语句
break语句可以结束循环，跳出循环，可以用在while和for中使用
lst = ['tom', 'bob', 1, 2, 'mike', None]

for n in lst:
    if n == 'bob':
        print(n)
        break


练习1
请利用循环依次对列表中的每个名字打印出Hello, xxx!
lst = ['Bart', 123, None, 'Lisa', 'Adam']

练习2，统计出一段文本中的元音的个数!
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
print('number of {} is {}'.format('a', a_num))


练习3，打印出9 9乘法表
提示 print(a, end=‘’) 可以不用换行，默认end=‘\n’
 1*1=1  
 1*2=2   2*2=4  
 1*3=3   2*3=6   3*3=9  
 1*4=4   2*4=8   3*4=12  4*4=16 
 1*5=5   2*5=10  3*5=15  4*5=20  5*5=25 
 1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36 
 1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49 
 1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64 
 1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81
for i in range(1,10):  #循环9次，打印出9行
    for j in range(1,i+1):  
        s = '{}*{}={}'.format(j, i, i*j)
        print(s.center(8), end='')
    print('')



