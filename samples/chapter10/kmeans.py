#使用K-Means算法聚类消费行为特征数据
#ppt上示例
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #画3D图
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
sns.set_style("whitegrid")


df = pd.read_csv(r'..\csv\consumption_data.csv')
df = df.ix[:,['R','F','M']]


# 观察数据，看是否有异常值
# 可以画箱型图，直观
#sns.boxplot(data=df.R)
#plt.ylim(0,df.R.max()) 
#plt.ylim(0,130) 
#sns.boxplot(data=df.F)
#plt.ylim(0,df.F.max())
#sns.boxplot(data=df.M)
#plt.ylim(0,df.M.max())
#plt.ylim(0, 20000)
#plt.show()

# 去掉夸张离群点
df = df[(df.R<80) | (df.F<50) | (df.M<8400)]
# 数据规范化  选一种
# 1  零-均值规范化，均值为0，标准差为1
df2 = (df - df.mean())/df.std() # df2为规范化的数据集
# 2  最小-最大规范化， 范围限定在0到1之间
#df2 = (df - df.min())/(df.max() - df.min())

#分为n_clusters类，聚类最大循环次数500
model = KMeans(n_clusters = 5, max_iter = 500)
model.fit(df2) #开始聚类学习

#print(model.labels_)
#print(model.cluster_centers_)
#统计各个类别的数目
r1 = pd.Series(model.labels_).value_counts()
#找出聚类中心
r2 = pd.DataFrame(model.cluster_centers_)
#横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r2, r1], axis = 1) 
#重命名表头
r.columns = list(df2.columns) + ['类别数目'] 
print(r)


## 3D散点图
##model.fit_predict(df2) # == model.fit(df2).predict(df2)
#y_pred = model.predict(df2) # 因为这个model已经fit过，只要predict
#sd = plt.figure().add_subplot(111, projection = '3d')  
#sd.set_xlabel('R')  
#sd.set_ylabel('F')  
#sd.set_zlabel('M') 
#sd.scatter(df.R, df.F, df.M, c=y_pred)
#plt.show() 



# 带图例的3D散点图
y_pred = model.predict(df2) # 因为这个model已经fit过，只要predict
sd = plt.figure().add_subplot(111, projection = '3d')  
sd.set_xlabel('R')  
sd.set_ylabel('F')  
sd.set_zlabel('M')  
# 分组构建不同类型的集合
type0 = ([], [], []) # 一系列(x, y, z)坐标这里为R, F, M
type1 = ([], [], [])
type2 = ([], [], [])
type3 = ([], [], [])
type4 = ([], [], [])
types = tuple(set(y_pred))
length = len(y_pred)
for i in range(length):
    if y_pred[i] == types[0]:
        type0[0].append(df.R[i])
        type0[1].append(df.F[i])
        type0[2].append(df.M[i])
    elif y_pred[i] == types[1]:
        type1[0].append(df.R[i])
        type1[1].append(df.F[i])
        type1[2].append(df.M[i])
    elif y_pred[i] == types[2]:
        type2[0].append(df.R[i])
        type2[1].append(df.F[i])
        type2[2].append(df.M[i])
    elif y_pred[i] == types[3]:
        type3[0].append(df.R[i])
        type3[1].append(df.F[i])
        type3[2].append(df.M[i])
    elif y_pred[i] == types[4]:
        type4[0].append(df.R[i])
        type4[1].append(df.F[i])
        type4[2].append(df.M[i]) 

t0 = sd.scatter(type0[0], type0[1],type0[2], marker='x', color='b')
t1 = sd.scatter(type1[0], type1[1],type1[2], marker='x', color='c')
t2 = sd.scatter(type2[0], type2[1],type2[2], marker='o', color='r')
t3 = sd.scatter(type3[0], type3[1],type3[2], marker='o', color='y')
t4 = sd.scatter(type4[0], type4[1],type4[2], marker='o', color='g')
plt.legend((t0, t1, t2, t3, t4),
           ('type0', 'type1', 'type2', 'type3', 'type4'),
           scatterpoints=1,
           loc=2,   # 显示位置
           ncol=2,  # 几列
           fontsize=8)
plt.show()