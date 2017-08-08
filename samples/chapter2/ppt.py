赋值语句
赋值语句（assignment statement）会新建变量，并为这个变量赋值。
在python中，一切都是对象。对象是通过引用传递的，在赋值时，不管这个对象是新建的还是已经存在的，都是将该对象的引用赋值给变量。
可用id()这个函数查看对象的唯一标识符，每个对象都有ID
name = ‘Tom’# 将一个字符串赋给一个叫message的新变量
n = 17                 # 将整型数17赋给n
name2 = ‘Tom’#  和name变量指向同一个对象

增量赋值
    n += 1
 多重赋值
    x = y = z = 1  # x,y,z指向同一个对象，即使是可变对象
 多元赋值
    x, y, z = 1, 2, ‘a’   # x=1, y=2, z=‘a’
    交换两个值  x, y = y, x


变量名
变量名可以任意长。它们可以包括字母和数字，但是不能以数字开头。 使用大写字母是合法的，但是根据惯例，变量名只使用小写字母。
下划线_可以出现在变量名中。 它经常用于有多个单词的变量名，例如my_name
不能以关键字做变量名
Python关键字 
 False      class      finally    is         return    None       continue   for        lambda     try     True       def        from       nonlocal   while      and        del        global     not        with      as         elif       if         or     yield       assert     else       import     pass       break      except     in         raise
不建议用内建函数名做变量名，比如id


整数
1， 0， 100，-888等等
浮点数
   1.23,  -3.14, 1.23e9，1.2e-5
字符串
字符串是以单引号'或双引号"括起来的任意文本，比如，’abc’, “xyz”,”I’m OK”
多行前后用三个引号， '''或"""括起来
字符串既包括带引号又包括双引号，用\转义， ‘He said:\“I\’m OK\”‘， 
 print('He said:\"I\'m OK\"')
 r’abc’    不转义


布尔值
True，False
空值
None，类似于C中的void，java中的null，一个函数没return会返回None
列表：list
是一种有序的集合 ，类似其他语言的数组， 
比如：[1,2,3,4,5,6]，['Tom', 'Bob', 1, 2, None, [3, 4]]
字典：dict
在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
比如  {'name':'Tom', 'score': 99}


类型转换
严格来讲没有类型转换，而是生成一个新的实例
int(), 转成整数型, int('123'), int(1.1), int('hello')
str()，字符串    str(1)   str([1,2,3])
float()，浮点数    float('1.23')
list(),     可迭代对象转成列表
bool()  布尔测试
类型判断， isinstance()函数


数学运算
  + - * /  %  //整除  **次方
逻辑运算
  and， 所有都为True，结果True
  or，只要其中有一个为True， 结果为True
  not，  非运算
  比较  >  <  >=  <=  !=  ==（值比较）  is（id比较）
  逻辑运算中，0,  0.0，空字符串，空列表，空字典,None,都为False，
  其他为True


a = 1
b = 1.0
a is b   # False
a == b   # True


