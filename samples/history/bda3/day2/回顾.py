1）python中3种不可变类型
    数值 int float 
    字符串 str
    元组 tuple
2）容器
    列表 和 元组 （后面学字典，rangeobject）
3）可迭代对象（可以用for遍历）
    字符串，列表，元组，字典，集合
    怎么判断对象是可迭代的
    from collections import Iterable
    isinstance(a, Iterable)
    >>> isinstance([1,2], Iterable)
    True
    >>> isinstance('aaaa', Iterable)
    True
    >>> isinstance(range(8), Iterable)
    True
4）语句结构
    if condition:
        block1
    elif condition2:
        block2  # 见到：就是一个新的语句块
    else:
        block3
    
    while condition:
        block
    
    while 4: # 默认会对非布尔值做布尔测试 bool(4)
        block
    
    for element in iterable_object:
        block

5）已接触的内建函数 id    type   help  isinstance
   isinstance(a, b)  # 可以判断父类
   type(a)==b
   sorted   reversed   enumerate   range  zip
6）序列
   字符串  列表  元组
   seq[0]     seq[start:end:step]  start应该小于end
   seq*n  [[],[],[]]
   element in seq   'a' in 'abc'
   
   序列的拼接    
        通用   seq+seq  同类型
        列表   lst.extend(iterable)
        列表的方法  append, pop, remove, sort, clear
        字符串  join.(iterable)

        >>> [1,2].extend([1])
        >>> [1,2]+[1]
        [1, 2, 1]
7） 列表生成式 
    需要赋值时，就是for的简便写法
    [我需要的值 for循环 条件判断(可选)] 
    [n*n for n in range(8)]
    [条件表达式 for循环 条件判断(可选)]