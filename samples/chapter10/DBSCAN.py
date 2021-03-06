#使用DBSCAN算法聚类消费行为特征数据

#
# 选两个特征， 以便画图
import matplotlib.pyplot as plt
import numpy as  np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN


df = pd.read_csv(r'..\csv\consumption_data.csv')
df = df.ix[:,['F','M']]

# 去掉夸张离群点
df = df[ (df.F<50) | (df.M<8400)]
# 数据规范化
df = (df - df.mean())/df.std()

# 参数eps：确定在同一聚类中两个点彼此之间的距离
#     min_samples: 每个分类最少点数
model = DBSCAN(eps = 0.1, min_samples=10)
model.fit(df) #开始聚类

#print(model.predict([[1, 2535]]))

# 散点图
y_pred = model.fit_predict(df)
#plt.scatter(df.F, df.M)  # 未分类散点图
plt.scatter(df.F, df.M, c=y_pred) # 分类
plt.show()