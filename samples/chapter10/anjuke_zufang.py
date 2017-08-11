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
3 再用上面的model去预测历史浏览记录的房源，
  看属于哪个类别的房源最多
4 recommend函数就推荐那个最多类别的房源，推5条左右

简单起见，这里只考虑，租金，装修，面积
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from random import choice


df = pd.read_csv(r'..\csv\anjuke.csv', encoding='gbk')
#print(df.tail(10))
#print(df.columns)
#X = df.loc[:, ['租金', '租赁方式', '装修', '面积', '年代']]
X = df.loc[:, ['租金', '装修', '面积']]
# 特征整理
def get_mianji(mianji):
    return mianji.replace('平米', '')
#def get_niandai(niandai):
#    if niandai == "暂无":
#        rtn = 2000
#    else:
#        rtn = niandai.replace('年', '')
#    return int(rtn) - 1980

# 装修用手工整理，安装装修的简单到豪华排序，LabelEncoder的顺序不一定，所以不用
zx = X['装修'].copy()
zx[zx=='毛坯'] = 1
zx[zx=='简单装修'] = 2
zx[zx=='中等装修'] = 3
zx[zx=='精装修'] = 4
zx[zx=='豪华装修'] = 5
X['装修'] = zx
X['面积'] = X['面积'].apply(get_mianji)
#X['年代'] = X['年代'].apply(get_niandai)
#X['租赁方式'] = LabelEncoder().fit_transform(X['租赁方式'].values)
#X = X.dropna()
#print(X.head(50), X.shape)
ss = StandardScaler()
X2 = ss.fit_transform(X)
kmeans = KMeans(n_clusters=15, n_init=50)
kmeans.fit(X2)

#统计各个类别的数目
#r1 = pd.Series(kmeans.labels_).value_counts()
## 找出聚类中心
##r2 = pd.DataFrame(kmeans.cluster_centers_)
## 聚类中心真实值
#r2 = pd.DataFrame(ss.inverse_transform(kmeans.cluster_centers_))
##横向连接（0是纵向），得到聚类中心对应的类别下的数目
#r = pd.concat([r2, r1], axis = 1) 
##重命名表头
#r.columns = list(X.columns) + ['类别数目']
#print(r)


y = kmeans.predict(X2)
ydata = pd.DataFrame(y, columns=['分类'])
# knn学习用
data = pd.concat([X, ydata], axis=1)
# 推荐用
data_recommend = pd.concat([df, ydata], axis=1)

#print(data.head(30), data.shape[0])
X = data.drop('分类', axis=1)
y = data['分类']
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X, y)



def _random_choice(lst, n):
    '''从列表lst中随机选择n个不重复的元素'''
    if n > len(lst):
        return lst
    choiced_elements = []
    lst = lst.copy()
    while n > 0:
        element = choice(lst)
        choiced_elements.append(element)
        lst.remove(element) # 避免重复选择
        n -= 1
    return choiced_elements

#rc = _random_choice([1,2,3,4,5,6,7], 2)
#print(rc)


# 假装这是某个用户最近的浏览历史记录
viewed = [
    [9900,  1, 150],
    [9000,  4, 150],
    [9000,  4, 150],
    [9000,  3, 150],
    [9200,  4, 160],
    [9400,  4, 180],
    [9000,  4, 150],
    [9000,  4, 160],
    [92000, 4, 1120],
    [9000,  4, 190],
    [9500,  2, 127],
    ]

def history_view():
    
    # 从csv文件中随机选择20条，假装是某个用户最近的浏览历史记录
    choosed_idx = _random_choice(list(df.index), 20)
    choosed_rows = df.ix[choosed_idx,:]
    #print(choosed_rows)
    X = choosed_rows.loc[:, ['租金', '装修', '面积']]
    print('-----------------------------查看历史----------------------------------------------')
    print(X)
    zx = X['装修'].copy()
    zx[zx=='毛坯'] = 1
    zx[zx=='简单装修'] = 2
    zx[zx=='中等装修'] = 3
    zx[zx=='精装修'] = 4
    zx[zx=='豪华装修'] = 5
    X['装修'] = zx
    X['面积'] = X['面积'].apply(get_mianji)
    
    return X
#history_view()



def recommend(viewed):
    '''
    根据用户最近的浏览记录，推荐浏览类型最多的房源
    '''
    viewed_types = knn.predict(viewed)
    #print(viewed_types)
    value_counts = pd.Series(viewed_types).value_counts()
    #print(value_counts)
    most_view = value_counts.index[0] # 推荐最多浏览的类型
    #print(most_view)
    recommended = data_recommend[data_recommend['分类'] == most_view]
    #idx = np.array([1,2,3,4,5])
    n = 5
    #if recommended.shape[0]>n: # 在这一类别里随机选5条，否则就全部选出
    #    idx = list(recommended.index)
    #    choiced_idx = []
    #    while n > 0:
    #        a = choice(idx)
    #        choiced_idx.append(a)
    #        idx.remove(a) # 避免重复选择
    #        n -= 1
    ##choiced_idx = np.array(choiced_idx)
    choiced_idx = _random_choice(list(recommended.index), n)
    #print(choiced_idx)
    recommended = recommended.ix[choiced_idx, :]
    print('-----------------------------推荐的----------------------------------------------')
    print(recommended)
    return recommended


#recommend(viewed)
#recommend(history_view())