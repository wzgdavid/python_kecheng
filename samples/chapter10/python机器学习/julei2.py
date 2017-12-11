import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 数据规范化
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# 聚类算法
from sklearn.cluster import KMeans

from sklearn.naive_bayes import GaussianNB


df = pd.read_csv(r'E:\python_files\csv\consumption_data.csv')
print(df.head())

# 观察一下异常值
#sns.boxplot(y=df.M) # R < 44   F<33   M < 2960
#plt.show()

# 过滤掉异常值
df = df[(df.R<44)&(df.F<33)&(df.M<2960)]

# 数据规范化/标准化

sr = MinMaxScaler() #
sf = MinMaxScaler()
sm = MinMaxScaler()
df['R2'] = sr.fit_transform(df.R.values.reshape(-1,1))
df['F2'] = sf.fit_transform(df.F.values.reshape(-1,1))
df['M2'] = sm.fit_transform(df.M.values.reshape(-1,1))

#print(df.head())
# 训练集只有特征
X_train = df[ ['R2','F2','M2'] ]

model = KMeans(10)
model.fit(X_train)

#print(model.labels_)
# centers聚类中心  比较好的代表这个类别的特征
print(model.cluster_centers_)
# 转成DataFrame
centers = pd.DataFrame(model.cluster_centers_, columns=list('RFM'))
print(centers)
centers['R_inversed'] = sr.inverse_transform(centers.R.values.reshape(-1,1))
centers['F_inversed'] = sf.inverse_transform(centers.F.values.reshape(-1,1))
centers['M_inversed'] = sm.inverse_transform(centers.M.values.reshape(-1,1))
print(centers)
# 聚类之后，每个数据的标签
df['labels'] = model.labels_

# 这里要预测一个值，编程分类问题
#print(df.head())
X = df[['R2', 'F2', 'M2']]
y = df['labels']

clf = GaussianNB()
clf.fit(X, y)

# 预测这个消费者的分类  4,  6  , 567
# 预测时也需要把这个数据的特征转换成规范化的形式

one_date = [[sr.transform(4)[0][0], 
            sf.transform(1)[0][0], 
            sm.transform(123)[0][0]]]
print(one_date)

print(clf.predict(one_date))


