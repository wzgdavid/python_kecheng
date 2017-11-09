import numpy as np
from copy import deepcopy
np.random.seed(13)
arr = np.random.randint(1, 10, size=(4,3) )
print(arr) # 
#print(arr[0]) # 
#print(arr[2][0])

print(arr[1:3]) # 切片

arr1d = np.arange(10)
print(arr1d)
# s = arr1d[1:4]# [1,2,3] # s还是指向arr1d
#s = deepcopy(arr1d[1:4]) 
s = arr1d[1:4].copy()   # 
print(s, 's')
arr1d[1:8] = 99
print(arr1d)
print(s, 's')

np.random.seed(13)
a = np.arange(1,10).reshape(3,3)
print(a)
print(a[:2])
print(a[2, 0]) # a[1][1]
a[:2, 1:] = 0
print(a)



a = np.arange(1, 13) **2
print(a,'-----a')

i = np.array([5,4,2,5])
print(a[i], '-----a[i]')

j = np.array([[2,3], [1,4],[5,6]])
print(a[j], '-----a[j]') # 返回的shape和j（下标）的shape相同

a = a.reshape(4, 3)
print(a, '----------reshaped a')
i = [[1,2],[1,2]]  
j = [[2,2],[2,0]]
#print(a[i, j], '=-=======a[i, j]')
print(a[i, :], '=-=======a[i, 2]')

print('--------------------------------------')
a = np.arange(1, 10).reshape(3,3)
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.max(axis=1))
print(a.argmax(axis=1))


scores = np.array([
   [67, 34, 90],
   [87, 54, 98],
   [89, 56, 78],
   [98, 54, 56]]
    )
print(scores)
print(scores.mean(axis=1))
print(scores.mean(axis=0))
print(scores.max(axis=0))

a = np.array([56,38,67])
b = np.array([78,49,98])
print(a + b)
print(b > a)
print(np.all(b > a))