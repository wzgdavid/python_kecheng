#使用K-Means算法聚类消费行为特征数据
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #画3D图
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing

df = pd.read_csv(r'D:\python_kecheng\samples\csv\consumption_data.csv')
df = df.ix[:,['R','F','M']]
# 数据规范化  选一种
# 零-均值规范化，均值为0，标准差为1
df2 = (df - df.mean())/df.std()
# 最小-最大规范化， 范围限定在0到1之间
#df2 = (df - df.min())/(df.max() - df.min())

#分为n_clusters类，聚类最大循环次数500
model = KMeans(n_clusters = 5, max_iter = 500)
model.fit(df2) #开始聚类

print(model.predict([[0.1,10,0.1]]))
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

#print(model.predict([[34, 26, 6666]]))

# 3D散点图
#y_pred = model.fit_predict(df2) # == model.fit(df2).predict(df2)
y_pred = model.predict(df2)
sd = plt.figure().add_subplot(111, projection = '3d')  
sd.scatter(df.R, df.F, df.M, c=y_pred)
sd.set_xlabel('R')  
sd.set_ylabel('F')  
sd.set_zlabel('M') 
#sd.legend(loc=2) 
plt.show() 