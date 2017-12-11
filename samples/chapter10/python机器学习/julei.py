import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 数据规范化
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# 聚类算法
from sklearn.cluster import KMeans


df = pd.read_csv(r'E:\python_files\csv\consumption_data.csv')
print(df.head())

# 观察一下异常值
#sns.boxplot(y=df.M) # R < 44   F<33   M < 2960
#plt.show()

# 过滤掉异常值
df = df[(df.R<44)&(df.F<33)&(df.M<2960)]

# 数据规范化/标准化

ss = MinMaxScaler() #
df['R2'] = ss.fit_transform(df.R.values.reshape(-1,1))
df['F2'] = ss.fit_transform(df.F.values.reshape(-1,1))
df['M2'] = ss.fit_transform(df.M.values.reshape(-1,1))

#print(df.head())

X_train = df[ ['R2','F2','M2'] ]

model = KMeans(6)
model.fit(X_train)

#print(model.labels_)

# 聚类之后，每个数据的标签
df['labels'] = model.labels_
# 加上标签之后的数据，保存到csv文件中，方便查看
df = df.drop(['R2','F2','M2'], axis=1)
df.to_csv('temp.csv')

