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

df = df[(df.R<130) | (df.M<25000) | (df.F<40)]
#plt.scatter(df.F, df.M)

# 数据规范化
#ss = StandardScaler()
#df2 = ss.fit_transform(df)

ss = MinMaxScaler()
scaled_df = ss.fit_transform(df)
df2 = pd.DataFrame(ss.fit_transform(df), columns=list('RFM'))


model = DBSCAN(eps=0.05, min_samples=10)
model.fit(scaled_df)

# 3D散点图
#model.fit_predict(df2) # == model.fit(df2).predict(df2)
#y_pred = model.predict(df) # 因为这个model已经fit过，只要predict
sd = plt.figure().add_subplot(111, projection = '3d')
sd.set_xlabel('R')  
sd.set_ylabel('F')  
sd.set_zlabel('M') 
sd.scatter(df2.R, df2.F, df2.M, c=model.labels_)
plt.show()