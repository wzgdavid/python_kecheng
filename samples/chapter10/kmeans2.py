#使用K-Means算法聚类消费行为特征数据
# 选两个特征， 以便画二维图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


df = pd.read_csv(r'D:\python_kecheng\samples\csv\consumption_data.csv')
df = df.ix[:,['F','M']]
# 去掉离散点
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

# 散点图
y_pred = model.fit_predict(df2)
#print(set(y_pred))
#plt.scatter(df.F, df.M)  # 未分类散点图
plt.scatter(df.F, df.M) # 分类
plt.xlabel('F')
plt.ylabel('M')
plt.show()