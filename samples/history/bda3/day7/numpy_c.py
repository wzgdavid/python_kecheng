import numpy as np

#np.random.seed(89)
scores = np.random.randint(40,99, size=(10, 3))
print(scores)
#1 求每个人的平均分和总分
mean = scores.mean(axis=1)
print( mean )
print(np.round(mean, 2))
score = scores[:,0]
print(score)              
print( np.where(score>=60, 'A', 'C') )
print( np.where(score>=60, score, 'C') )
print( np.where(score>=60, score, np.nan) )
# np.where(条件, 为真时的值，假时的值)

jige = np.where(score>=80, 'A', 'B')
bujige = np.where(score>=50, 'C', 'D')
print( np.where(score>=60, jige, bujige) )
print('-----------集合--------------')
a = np.array( [1, 2, 3, 4] )
b = np.array( [5, 2, 3, 6, 3] )
print( np.intersect1d(a, b) )
print( np.union1d(a, b) )
print( np.in1d(a, b) )
print( np.in1d(b, a) )
print('-----------集合--------------')
# 不管是几维，都当成一维处理
a2 = np.array([[1,2],[3,4]])
b2 = np.array([[1,2],[5,4],[6,7]])
print( np.intersect1d(a2, b2) )
print( np.union1d(a2, b2) )
print( np.in1d(a2, b2) )

import matplotlib.pyplot as plt
a = np.array([1,2,3,4,3,4,5])
#plt.plot(a) #  画图
#plt.ylim(-5,5)
#plt.show()  #  显示图形

a = np.random.randint(0, 2, size=(1000, 500))
b = np.where(a==0, -1, a)
b = b.cumsum()
plt.plot(b)
print(b)
#plt.show()
#[
#[ 1  2  1  2  3  2  3  2  1  2 ...],
#[ 1  2  1  2  3  2  3  2  1  2 ...],
#[ 1  2  1  2  3  2  3  2  1  2 ...],
#...
#..
#...]

print('-------------骰子概率--------------')
total = 9999
np.random.seed(6)
a = np.random.randint(1, 7, size=(2, total))
print(a)
duizi = (a[0] == a[1]).sum()
print(duizi/total, 1/6,'一对的概率')
dui6 = ( (a[0] == a[1]) & (a[0] == 6) ).sum()# 出现几次对6
print(dui6/total,1/36,'一对6的概率')
gt10 = ( (a[0] + a[1])>10 ).sum()
print(gt10/total,3/36,'大于10的概率')

ndarray
#np.matrix
#
1X2 + 2X1 = 4
1X4 + 2X2 = 8