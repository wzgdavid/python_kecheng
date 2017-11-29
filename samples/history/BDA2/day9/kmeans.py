import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from mpl_toolkits.mplot3d import Axes3D #画3D图
from sklearn.cluster import KMeans, DBSCAN

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv(r'E:\python_files\csv\consumption_data.csv')
df = df.drop('Id', axis=1)
#plt.scatter(df.F, df.M)
#sns.boxplot(data=df,y=df.M)
# R < 130   M < 25000  F < 40
#plt.show()

df = df[(df.R<130) | (df.M<25000) | (df.F<40)]
#plt.scatter(df.F, df.M)

# 数据规范化
#ss = StandardScaler()
#df2 = ss.fit_transform(df)

ss = MinMaxScaler()
scaled_df = ss.fit_transform(df)
df2 = pd.DataFrame(ss.fit_transform(df), columns=list('RFM'))

# 3D散点图
#model.fit_predict(df2) # == model.fit(df2).predict(df2)
#y_pred = model.predict(df) # 因为这个model已经fit过，只要predict
#sd = plt.figure().add_subplot(111, projection = '3d')
#sd.set_xlabel('R')  
#sd.set_ylabel('F')  
#sd.set_zlabel('M') 
#sd.scatter(df2.R, df2.F, df2.M)
#plt.show()

model = KMeans(n_clusters=8)
model.fit(scaled_df)
#print(model.cluster_centers_) # 聚类中心
#print(model.labels_)

print(model.inertia_)


# 肘方法
ine = [[],[]] # 画图用的坐标点
for n in range(2, 31):
    inertia = KMeans(n_clusters=n).fit(scaled_df).inertia_
    ine[0].append(n)
    ine[1].append(inertia)
# 肘方法
plt.plot(ine[0], ine[1])
plt.show()

# 找出聚类中心，做成一个dataframe，
r1 = pd.Series(model.labels_).value_counts()
#print(r1)
r2 = pd.DataFrame(model.cluster_centers_, columns=list('RFM'))
#print(r2)
r = pd.concat([r2, r1], axis=1)
r.columns = list(r2.columns)+['类别数量']
#print(r)
#y_pred = model.predict(scaled_df)
#print(scaled_df.shape, y_pred.shape)
#print(model.predict([[0.1, 0.1,0.1]]))


# 3D散点图
#model.fit_predict(df2) # == model.fit(df2).predict(df2)
#y_pred = model.predict(df) # 因为这个model已经fit过，只要predict
sd = plt.figure().add_subplot(111, projection = '3d')
sd.set_xlabel('R')  
sd.set_ylabel('F')  
sd.set_zlabel('M') 
sd.scatter(df.R, df.F, df.M, c=model.labels_)
#plt.show()