#a = [1, 2, 3]
#b = a
#a += [1,1,1]
#print(b)
#
#a = [1, 2, 3]
#b = a
#c = a + [1,1,1]
#print(b)

#a[1]
#a[i] # i = np.array([1,2,3])
import numpy as np
a = np.arange(1, 13)

a > 5  # 数组，元素是布尔值
print(a>2)
print(a[(a>2)  & (a<7)]) # 与 & 或 |

b = np.arange(1, 13).reshape(4,3)
print(b[b>5])  # 在b数组中选出大于5的元素
               # 和b的形状无关
print((b>5).sum()) # 几个元素大于5