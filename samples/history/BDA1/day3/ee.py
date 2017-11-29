from copy import copy, deepcopy

lst = [1,2,[3,4]]

lst2 = copy(lst)
#print(lst2)
lst2[2].append(3)

#print(lst)
#print(lst2)

lst = [1,2,[3,4]]

lst2 = deepcopy(lst)
#print(lst2)
lst2[2].append(3)

a = '你好'

autf8 = a.encode('utf-8')
agbk = a.encode('gbk')
print(autf8)
print(agbk)

a1 = autf8.decode('utf-8')
a2 = agbk.decode('utf-8')
print(a1)