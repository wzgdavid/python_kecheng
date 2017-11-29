#numpy   处理矩阵
#pandas   基于numpy   数据处理  
#scikit-learn    python机器学习  （深度学习 tensorflow theano keras  ）
#matplotlib  seaborn 基于前者
#3   + 4   [1, 2, 3]  [1, 2, 3] 
#lst = [[1, 2, 3],  # 3X3
#       [3, 4, 5],
#       [4, 5, 6]]
#
#lst2 =[[1, 2],  # 3X2
#       [3, 4],
#       [4, 5]]
#
#lst + lst2 =[[2, 4, 6],  # 3X3
#             [3, 8, 10],
#             [8, 10, 12]]

import numpy as np
import random
# n dim
#00000000000000000000000000000001
#00000000000000000000000000000000000000000000000000000000001
arr1 = np.array([1., 2.2, 3.4], dtype=np.float16)
arr = np.array(
                [ [1, 2], 
                 [3, 4], 
                 [3, 4] ], dtype=np.float32
                 )

print(arr,  '维度：', arr.ndim)
print(arr1.shape)  # shape 返回的是元组
print(arr1.dtype)


#arr = np.array(range(1, 11))
arr = np.arange(1, 9) # 和range用法一样

print(arr, arr.shape)
arr2 = arr.reshape(2, -1)
print(arr2, arr2.shape)

arr = np.zeros((3, 4))
print(arr.size)

print('------------random-----------------')
arr = np.random.rand(2,3) # 参数表示维度
print(np.random.rand())
print(arr)

arr = np.random.randint( 1, 10, size=(6) )
print(arr)
np.random.seed(15)  # seed后面的代码产生伪随机数
arr = np.random.randint( 1, 10, size=(6) ) # 伪随机数
print(arr)

#np.random.shuffle(arr)
#print(arr)
# 5X3的二维数组，元素是1到9的随机整数
arr = np.random.randint( 1, 10, size=(5,3) )
print(arr)
np.random.seed() # 
np.random.shuffle(arr)
print(arr)
print('-----------------------------随机1到9')
np.random.seed(5)
arr = np.arange(1, 10) # 不会重复1到9
np.random.shuffle(arr)

print(arr)   # (9, )
arr2 = arr.reshape(3, -1)  #
#print(arr)
print(arr2)
