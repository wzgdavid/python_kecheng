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

简单起见，这里只考虑，租金，装修，面积，房型，租赁方式
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
sns.set_style("whitegrid")

df = pd.read_csv(r'..\csv\anjuke.csv', encoding='gbk')
#print(df)
print(df.columns)
X = df.ix[:, ['租金', '房型', '租赁方式', '装修', '面积']]
# 特征整理
# 装修手工整理，安装装修的简单到豪华排序
#X[X=='毛坯'] = 1
#X[X=='简单装修'] = 2
#X[X=='中等装修'] = 3
#X[X=='精装修'] = 4
#X[X=='豪华装修'] = 5
print(X['装修'][X['装修']=='毛坯'])