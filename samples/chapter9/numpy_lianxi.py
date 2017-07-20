'''
创建一个由1到9组成的每个数字随机出现一次的3X3的二维数组

'''
import numpy as np
arr = np.arange(1,10)
np.random.shuffle(arr)
arr = arr.reshape(3,3)
#print(arr)


a = np.random.randint(9, size=(9,3))
#有这样一个9X3的二维数组，统计一行中3个值都大于3的行的个数

row = (a>3).sum(1)
print((row==3).sum())
