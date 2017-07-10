'''
格式
pagen  title
content
'''


page 5  numpy
Numpy提供了真正的数组功能
Numpy核心模块是用c语言编写，速度快
Numpy对数组进行快速运算的标准数学函数（无需编写循环）
很多扩展库也依赖numpy库，比如scipy，pandas
numpy安装
linux直接安装，windows下先安装wheel，然后去
http://www.lfd.uci.edu/~gohlke/pythonlibs/
下载对应版本的numpy的whl文件，然后本地安装whl

page6  创建numpy数组（ndarray）
import numpy as np  # 导入numpy包，惯例写法
np.array([2,3,4])   # 传入一个列表创建
np.array([2,3,4], dtype=np.float32)  # 指定类型创建
np.array([(1.5,2,3), (4,5,6)])  # 二维数组
np.arange(6)    # 0 到 5 的值
np.arange( 10, 30, 5 )  # 产生[10, 30)的值，步长5
np.zeros((3,4))     # 二维数组，元素值都是0
np.ones((2,3,4))    # 三维数组，值都是1
np.empty( (2,3) )   # 没初始化的值，值随机


page7  ndarray属性
ndarray.ndim  # 维度
ndarray.shape # 形状
ndarray.size   # 元素数量
ndarray.dtype   # ndarray中元素的数据类型



page8 Numpy基础操作
索引和切片
a = np.arange(10)
a[5]   # 索引
a[5:8]   #  切片
a[5:8] = 99  # 切片赋值，改变原对象
a_slice = a[5:8]
a_slice = 99 # 切片赋值，改变原对象
a_slice = a[5:8].copy()  # 不想改变原对象，用copy

page9 Numpy基础操作
二维数组索引和切片
a2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
a2d[2]
a2d[:2]
a2d[2,1]
a2d[:2, :1]    # 在两个维度上切片
a2d[1, :2]     # 一个维度索引，一个切片
a2d[:, :1]
a2d[:2, 1:] = 0  # 切片赋值

page10 Numpy基础操作
布尔型索引
array[布尔型数组]，如果索引中数组的元素不是布尔型，会转化成布尔型
a = np.arange(10)
a > 5
a[a>5]
a[a==5]
a[a!=5]
a[(a<9) & (a>3)]    # 与运算
a[(a==6) |( a==5)]   #  或


page11  numpy基础操作
算术运算
大小相同的数组之间的算术运算会应用到元素，这称作矢量化
a = np.array( [20,30,40,50] )
b = np.arange( 4 ) # array([0, 1, 2, 3])
c = a-b   # array([20, 29, 38, 47])
数组与标量的算术运算也是运算到各个元素
b**2 # array([0, 1, 4, 9])
比较运算，返回的元素是布尔值
a<35  # array([ True, True, False, False], dtype=bool)
增量运算，修改原对象，没有返回
a *= 3  # array([ 60,  90, 120, 150])


page12  Numpy基础操作
数组统计方法
a = np.array([2,3,4,9])
a.sum()    # 求和
a.max()  a.min()  # 最小值  最大值
a.argmax()  a.argmin()    # 最大最小值的索引 
a.mean()   # 算术平均
a.std()  a.var()  # 标准差， 方差
a.sumsum()   #  累计和
a.sumprod()   # 累计乘积

page13 Numpy基础操作
用于布尔型数组的方法
a = np.array( [40,50,20,30,40] )
(a<35).sum()   # 这边会将True转成1
a.all()     # 检测是否全是True
a.any()     # 检测是否存在True
排序
a.sort()    np.sort(a)  # 返回另一个数组
去重
np.unique(a)

page14 Numpy基础操作
Numpy的三元表达式numpy.where()
where(条件判断，为True的值，为False的值)
a = np.random.rand(10)
np.where(a>0.5, 1, 0)  # 赋值是一个常量
np.where(a>0.5, a, 0)  # 赋值是一个ndarray

page15 Numpy基础操作
随机数：numpy.random函数
rand      产生均匀分布的样本值，范围[0, 1) 
np.random.rand(3,2)， np.random.rand() 无参返回单个随机值
randn     产生正态分布（均值0，标准差1）的样本值，范围[0, 1)
randint   从给定的范围内随机选取整数
np.random.randint(3, size=10)
shuffle   随机打乱一个序列
arr = np.arange(10)
np.random.shuffle(arr)


page16 Numpy基础操作
示例: 随机漫步
一次性产生1000次“掷硬币”的结果，一面为1，一面为-1，计算累计和
draws = np.random.randint(0,2,1000)
steps = np.where(draws>0, 1, -1)
walk = steps.cumsum()


page17 Numpy基础操作
示例：骰子游戏
两个骰子一共可产生36种结果，用穷举法求得出某种结果的概率，
比如对6，比如大于10的概率
total_times = 9999
touzi = np.random.randint(1, 7, size=[2, 9999])
duizi_times = (touzi[0] == touzi[1]).sum()
dui6_times = ((touzi[0] == touzi[1])& (touzi[0]==6)).sum()
dayu10_times = (touzi[0]+touzi[1]>10).sum()
duizi_gailv = duizi_times / total_times
dui6_gailv = dui6_times / total_times
dayu10_gailv = dayu10_times / total_times