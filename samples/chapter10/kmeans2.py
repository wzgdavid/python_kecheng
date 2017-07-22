#使用K-Means算法聚类消费行为特征数据
# 选两个特征， 以便画二维图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


df = pd.read_csv(r'..\csv\consumption_data.csv')
df = df.ix[:,['F','M']]
# 去掉离群点
df = df[(df.F<45) &(df.M<30000)]
# 数据标准化
df2 = (df - df.mean())/df.std()

#分为n_clusters类，聚类最大循环次数500
model = KMeans(n_clusters = 4, max_iter = 500)
model.fit(df2) #开始聚类
#print(model.labels_)
#print(model.cluster_centers_)
#统计各个类别的数目
r1 = pd.Series(model.labels_).value_counts() 
#找出聚类中心
r2 = pd.DataFrame(model.cluster_centers_) 
#横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r2, r1], axis = 1) 
#重命名表头
r.columns = list(df.columns) + ['类别数目'] 
print(r)

#print(model.predict([[1, 2535]]))


y_pred = model.fit_predict(df2)
# 散点图
plt.scatter(df.F, df.M, c=y_pred) # 分类
plt.xlabel('F')
plt.ylabel('M')
plt.show()


## 带图例的散点图
#type0 = ([], []) # 一系列(x, y)
#type1 = ([], [])
#type2 = ([], [])
#type3 = ([], [])
#types = tuple(set(y_pred))
#length = len(y_pred)
#for i in range(length):
#    if y_pred[i] == types[0]:
#        type0[0].append(df.F[i])
#        type0[1].append(df.M[i])
#    elif y_pred[i] == types[1]:
#        type1[0].append(df.F[i])
#        type1[1].append(df.M[i])
#    elif y_pred[i] == types[2]:
#        type2[0].append(df.F[i])
#        type2[1].append(df.M[i])
#    elif y_pred[i] == types[3]:
#        type3[0].append(df.F[i])
#        type3[1].append(df.M[i])
#
#t0 = plt.scatter(type0[0], type0[1], marker='x', color='b')
#t1 = plt.scatter(type1[0], type1[1], marker='x', color='c')
#t2 = plt.scatter(type2[0], type2[1], marker='o', color='r')
#t3 = plt.scatter(type3[0], type3[1], marker='o', color='y')
#plt.legend((t0, t1, t2, t3),
#           ('type0', 'type1', 'type2', 'type3'),
#           scatterpoints=1,
#           loc=2,   # 显示位置
#           ncol=2,  # 几列
#           fontsize=8)
#plt.show()