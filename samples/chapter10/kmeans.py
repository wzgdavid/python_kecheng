#使用K-Means算法聚类消费行为特征数据

import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('consumption_data.csv')
#print(df.columns)
df = df.ix[:,['R','F','M']]

model = KMeans(n_clusters = 3, max_iter = 500) #分为n_clusters类，聚类最大循环次数500
model.fit(df) #开始聚类
#print(model.labels_)
#print(model.cluster_centers_)
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(df.columns) + [u'类别数目'] #重命名表头
print(r)

print(model.predict([[34, 26, 6666]]))

