'''
手动转换数据
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import uniform as sp_rand
'''
数值  武器类型    子弹  血量  身边是否有队友  行为类别
0     手枪        少   少       没              逃跑 
1     机枪        多   多       有             战斗
'''

#names = ['zidan','wuqi','xueliang','do_what','duiyou']

#df = pd.read_csv('fightrun.csv',encoding='utf-8',names=names) # 指定列名
df = pd.read_csv('fightrun.csv')
df = df.ix[:,['子弹','武器','血量','身边队友','行为']]
#print(df)
df[df=='手枪'] = 0
df[df=='少'] = 0
df[df=='没'] = 0
df[df=='逃跑'] = 0
df[df!=0] = 1
# 此时df中数据类型是object，要转换一下astype(int)
df = df.astype(int)
print(df)
model = DTC()

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
#             precision    recall  f1-score   support
#
#          0       0.73      0.89      0.80         9
#          1       0.95      0.87      0.91        23
#
#avg / total       0.89      0.88      0.88        32
# 以上为metrics.classification_report的返回结果，
#[[ 8  1]   
# [ 3 20]]
# 上面两行metrics.confusion_matrix的结果
# 其中precision = 8 / (8 + 3)
# recall = 8 / (8 + 1)
# f1-score = 2 * (precision * recall) / (precision + recall)
# support是权重
# avg / total 是加权均值 比如recall = (0.89*9+0.87*23)/(9+23)



