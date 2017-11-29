import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')
# 作为特征一些列
columns = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
df = df[columns]
df = StandardScaler().fit_transform(df)
model = KMeans(n_clusters=7, n_init=400)
model.fit(df)
#0.83840839  1.24438274  0.594985    1.58327971  0.93629583  1.13201572
print(model.predict([[60,10,90,50,98,77]]))
print(model.cluster_centers_) # 聚类的中心点


#ine = [[],[]] # 画图用的坐标点
#for n in range(50, 100):
#    inertia = KMeans(n_clusters=10, n_init=n).fit(df).inertia_
#    ine[0].append(n)
#    ine[1].append(inertia)
## 肘方法
#plt.plot(ine[0], ine[1])
#plt.show()
