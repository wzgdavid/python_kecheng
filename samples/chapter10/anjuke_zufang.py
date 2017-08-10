'''
根据chapter8 anjuke_zufang.py 抓取的数据
房源推荐系统，
根据用户浏览的房源，推荐相似区域，租金，房型等的房源  (基于内容的推荐)

一个函数接收用户经常访问的房源
def accept()
另一个函数推荐和前面一个函数接收的房源 类似的房源
def recommend()

初步设想思路是
1 先用聚类分好类，产生data
2 然后用knn（K最近邻）算法，去学习上述分好类的data，产生一个model
3 再用上面的model去预测我accept进来的房源，
  如果accept了几条房源的话，看属于哪个类别的房源最多
4 recommend函数就推荐那个最多类别的房源，推5条左右

简单起见，这里只考虑，租金，装修，面积，租赁方式
'''
import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import LabelEncoder, StandardScaler
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
sns.set_style("whitegrid")

df = pd.read_csv(r'..\csv\anjuke.csv', encoding='gbk')
#print(df)
print(df.columns)
X = df.loc[:, ['租金', '租赁方式', '装修', '面积', '年代']]
# 特征整理
def get_mianji(mianji):
    return mianji.replace('平米', '')
def get_niandai(niandai):
    if niandai == "暂无":
        rtn = None
    else:
        rtn = niandai.replace('年', '')
    return rtn
# 装修用手工整理，安装装修的简单到豪华排序，LabelEncoder的顺序不一定，所以不用
zx = X['装修'].copy()
zx[zx=='毛坯'] = 1
zx[zx=='简单装修'] = 2
zx[zx=='中等装修'] = 3
zx[zx=='精装修'] = 4
zx[zx=='豪华装修'] = 5
X['装修'] = zx
X['面积'] = X['面积'].apply(get_mianji)
X['年代'] = X['年代'].apply(get_niandai)
X['租赁方式'] = LabelEncoder().fit_transform(X['租赁方式'].values)
X = X.dropna()
print(X.head(20))
ss = StandardScaler()
X2 = ss.fit_transform(X)
kmeans = KMeans(n_clusters=10, max_iter=100)
kmeans.fit(X2)

#统计各个类别的数目
r1 = pd.Series(kmeans.labels_).value_counts()
# 找出聚类中心
#r2 = pd.DataFrame(kmeans.cluster_centers_)
# 聚类中心真实值
r2 = pd.DataFrame(ss.inverse_transform(kmeans.cluster_centers_))
#横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r2, r1], axis = 1) 
#重命名表头
r.columns = list(X.columns) + ['类别数目']
print(r)


y = kmeans.predict(X2)
