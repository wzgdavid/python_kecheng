def extendList(val, lst=[]):
    print(id(lst))
    lst.append(val)
    return lst

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
print(list1,list2,list3)

#改动
def extendList2(val, lst=None):
    if not lst:
        lst = []
    lst.append(val)
    return lst
list1 = extendList2(10)
list2 = extendList2(123,[])
list3 = extendList2('a')
print(list1,list2,list3)


# 写一个计算次方的函数，默认值是计算平方
def power(n, cifang=2):
    if not isinstance(n, (int, float)):
        raise Exception('n need to be a number')
    if not isinstance(cifang, (int, float)):
        raise Exception('cifang need to be a number')
    return n**cifang

print(power(2,'3.4'))


#写一个函数，输入身高（米）体重（千克），
#根据BMI公式（体重(千克)除以身高的平方）
#返回结果
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
