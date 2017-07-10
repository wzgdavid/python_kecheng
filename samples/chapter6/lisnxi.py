def extendList(val, lst=[]):
    print(id(lst))
    lst.append(val)
    return lst

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')



#写一个函数，输入身高（米）体重（千克），
#根据BMI公式（体重(千克)除以身高的平方）
#返回结果
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
