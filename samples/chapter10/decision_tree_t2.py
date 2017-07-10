'''
手动转换数据
3种结果行为，战斗，逃跑，躲藏， 是不是作为作业
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import tree
from sklearn.externals.six import StringIO
import os

from sklearn import metrics
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import uniform as sp_rand
'''
数值  武器类型    子弹  血量  身边队友数量  行为类别
0     手枪        少   少       0              逃跑
1     机枪        中   中       1              战斗
2                 多   多       2或以上        躲藏
'''

df = pd.read_csv('fightrun2.csv')
df = df.ix[1:,['武器','子弹','血量','身边队友','行为']]
print(df)
df[df=='手枪'] = 0
df[df=='少'] = 0
df[df=='没'] = 0
df[df=='逃跑'] = 0
df[df!=0] = 1
df = df.astype(int)
#print(df)
model = DTC()
# 此时df中数据类型是object，要转换一下astype(int) 
x = df[['武器','子弹','血量','身边队友']]#.astype(int) 
#print(x)
y = df['行为']#.astype(int)
#print(y)
model.fit(x, y)

# 预测
# 预测一组特征
predicted = model.predict([(1,1,0,1)])
print(predicted)
# 预测n组特征
predicted = model.predict(x)  # 预测出的结果
expected = y  # 期望的结果
# 打印预测结果，
#print(expected.shape, predicted.shape) #出错时打印看看两者是否一致
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))




