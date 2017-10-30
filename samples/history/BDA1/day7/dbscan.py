import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文

df = pd.read_csv('E:\python_files\csv\consumption_data.csv')
#print(df.head())
df = df.ix[:, ['R', 'F']]
#sns.boxplot(data=df,y='M')
#plt.ylim(0, 25000)
#plt.show()

df = df[(df.R < 130) & (df.F < 35)]
#df.ix[9999] = [45,23, 900]
#print(df.tail())
# 数据去除特征差异
df2 = StandardScaler().fit_transform(df)
#print(df2)

#model = KMeans(n_clusters=5, max_iter=50)
model = DBSCAN(eps=0.3)
y_pred = model.fit_predict(df2)

#print(model.labels_)
#r1 = pd.Series(model.labels_).value_counts()
##print(r1)
##print(model.cluster_centers_)
#r2 = pd.DataFrame(model.cluster_centers_)
#
#r = pd.concat([r1, r2], axis=1)
#r.columns = ['cnt', 'R', 'F', 'M']
#print(r)
#df2dataframe = pd.DataFrame(df2)
#print(df2dataframe.tail())
#p = model.predict([df2dataframe.ix[940]])
#print(p)
#p = model.predict([[45,23, 900]])
#print(p)

#y_pred = model.predict(df2)
#print(y_pred)

plt.scatter(df.R, df.F, c=y_pred)
#sd.set_xlabel('R')
#sd.set_ylabel('F')
#sd.set_zlabel('M')
plt.show()