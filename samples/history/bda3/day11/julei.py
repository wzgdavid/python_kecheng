import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
sand = plt.figure().add_subplot(111, projection='3d')

df = pd.read_csv(r'E:\python_files\csv\consumption_data.csv')

df = df.ix[:,['R','F','M']]

#plt.scatter(df.R, df.M) # f<40  r<100 m < 25000
#plt.show()

#sns.boxplot(y=df.M)
#plt.show()
# 过滤掉异常值
df = df[(df.F<40) & (df.R<44) & (df.M<2500)]
# 数据规范化
ss = StandardScaler()
#ss = MinMaxScaler()
scaled = ss.fit_transform(df)  # X
#print(scaled)

model = KMeans(n_clusters=5)
# n_clusters    model.inertia_ 
# 3             1449
# 5             929
# 7             697
# 9             598
# 11            520

#x = range(3,40)
#inertias = []
## 肘方法  估计聚类分多少类
#for n in range(3,40):
#    inertia = KMeans(n_clusters=n).fit(scaled).inertia_
#    inertias.append(inertia)
#plt.plot(x, inertias)
#plt.show()

model.fit(scaled)

print(model.inertia_)
#print(model.labels_) # 聚类之后的标签
#df['分类'] = model.labels_
#df.to_csv('temp.csv')


# 聚类  每个类别的中心点
center = model.cluster_centers_
print( ss.inverse_transform(center) ) # fit_transform
# c 以哪个特征区分颜色
#sand.scatter(df.R, df.F, df.M, c=model.labels_)
#sand.set_xlabel('R')
#sand.set_ylabel('F')
#sand.set_zlabel('M')
#plt.show()
#        R               F               M         类别数量
#[[   21.41935484     4.57526882   502.80021505]     123
# [   10.76595745    20.22340426  1131.65930851]    12
# [    9.19125683     6.53005464  1589.2704918 ]    345
# [   25.375         11.55113636  1389.58761364]    34 
# [    7.2797619      4.77380952   467.28970238]]   34
#
# 生成一个csv   有 RFM三列  还有 每个类别的数量

# 计算每个标签的数量
label_cnt = pd.Series(model.labels_).value_counts()
df_centers = pd.DataFrame(ss.inverse_transform(center))
print(label_cnt)
print(df_centers)

#df_label_cnt = df_centers.add(label_cnt, axis=1)
# series和df的拼接
df_cnt = pd.concat([df_centers, label_cnt], axis=1)
df_cnt.columns = list(df.columns) + ['类别数量']
print(df_cnt)