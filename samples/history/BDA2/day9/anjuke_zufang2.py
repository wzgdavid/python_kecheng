'''
根据chapter8 anjuke_zufang.py 抓取的数据
房源推荐系统，
根据用户浏览的房源，推荐相似区域，租金，房型等的房源  (基于内容的推荐)

一个函数接收用户经常访问的房源
def accept()
另一个函数推荐和前面一个函数接收的房源 类似的房源
def recommend()

1 先用聚类分好类，产生data
2 看历史最近浏览的房源的类别，看属于哪个类别的房源最多
3 recommend函数就推荐那个最多类别的房源，推5条左右

简单起见，这里只考虑，租金，装修，面积
'''

import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from random import choice

area = ['浦东新区', '闵行区', '松江区', 
'徐汇区', '普陀区', '长宁区', 
'青浦区', '静安区', '上海周边', 
'杨浦区', '虹口区', '宝山区', 
'嘉定区', '黄浦区', '奉贤区', 
'崇明区', '金山区']
# 查询网址http://www.gpsspg.com/maps.htm  百度地图gps
gps = (
    (31.2274065041,121.5505840120), (31.1189141643,121.3886803785), (31.0383289332,121.2330541677),
    (31.1946458680,121.4433055580), (31.2553119532,121.4035442489), (31.2265243725,121.4304185175),
    (31.1555447438,121.1308224101), (31.2296614952,121.4624372609), (31.2363429624,121.4803295328),
    (31.2656839054,121.5326577316), (31.2703244262,121.5118910226), (31.4109435502,121.4959742660),
    (31.3805628349,121.2727914784), (31.2374294453,121.4912966392), (30.9239497878,121.4806129429),
    (31.6288408354,121.4038337007), (30.7479665497,121.3489176446)
)
area_gps = dict(zip(area, gps))
print(area_gps)


df = pd.read_csv(r'..\csv\anjuke.csv', encoding='gbk')
#print(list(df['区域1'].unique()))
#print(df['区域1'].value_counts())
def history_viewed(viewed_index):
    '''根据输入的index选择几条数据，
       假装是某个用户最近的浏览历史记录最新的几条'''
    return df.ix[viewed_index, :]
#viewed_index = 3, 4, 5, 6, 22, 40, 43   # 四五十平米，租金2,3千
#viewed_index = 12, 18, 39, 46  # 中等装修
#viewed_index = 1, 8, 17, 20, 27, 30, 37  # 一百多平米
viewed_index = 0, 1, 6, 13, 15, 17,18,19  # 浦东新区
viewed = history_viewed(viewed_index)
#print('-----------------------------浏览过的----------------------------------------------')
#print(viewed)

#print(df.tail(10))
#print(df.columns)
#X = df.loc[:, ['租金', '租赁方式', '装修', '面积', '年代']]
X = df.loc[:, ['租金', '装修', '面积', '区域1']]
# 特征整理
def get_mianji(mianji):
    return mianji.replace('平米', '')
def get_area_gps(area):
    return area_gps[area]

# 装修用手工整理，安装装修的简单到豪华排序，LabelEncoder的顺序不一定，所以不用
zx = X['装修'].copy()
zx[zx=='毛坯'] = 1
zx[zx=='简单装修'] = 2
zx[zx=='中等装修'] = 3
zx[zx=='精装修'] = 4
zx[zx=='豪华装修'] = 5
X['装修'] = zx
X['面积'] = X['面积'].apply(get_mianji)
# 处理区域坐标
X['区域1'] = X['区域1'].apply(get_area_gps)
X['area_x'] = X['区域1'].apply(lambda x:x[0])
X['area_y'] = X['区域1'].apply(lambda x:x[1])
X = X.drop('区域1', axis=1)
print(X.head())
X = X.astype(float)

X_filtered = X[(X['面积']<300) | (X['租金']<20000)]
df_filtered = df[df.index.isin(X_filtered.index)]

#print(df_filtered.shape[0])
#print(X_filtered.shape[0])
ss = StandardScaler()
X2 = ss.fit_transform(X_filtered)
model = KMeans(n_clusters=15, n_init=50)
#model = DBSCAN(eps = 0.1, min_samples=10)
#model.fit(X2)
y_pred = model.fit_predict(X2)
y_data = pd.DataFrame(y_pred, columns=['分类'], index=df_filtered.index)
#print(y_data.index)
#print(y_data.shape[0])
# 推荐用
data_recommend = pd.concat([df_filtered, y_data], axis=1)
#print(data_recommend.shape[0])



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


def recommend():
    '''
    根据用户最近的浏览记录，推荐浏览类型最多的房源
    '''
    viewed_types = y_pred[np.array(viewed_index)]
    value_counts = pd.Series(viewed_types).value_counts()
    most_view = value_counts.index[0] # 推荐最多浏览的类型
    #print(most_view)
    recommended = data_recommend[data_recommend['分类'] == most_view]
    #idx = np.array([1,2,3,4,5])
    n = 5

    # 随机选这一类别的n跳记录
    choiced_idx = _random_choice(list(recommended.index), n)
    #print(choiced_idx)
    
    recommended = recommended.ix[choiced_idx, :]
    print('-----------------------------推荐的----------------------------------------------')
    print(recommended)
    return recommended

recommend()