'''
手动转换数据
'''
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import tree
from sklearn.externals.six import StringIO
import os
import pydot
'''
数值  武器类型    子弹  血量  身边是否有队友  行为类别
0     手枪        少   少       没              逃跑 
1     机枪        多   多       有             战斗
'''

#names = ['zidan','wuqi','xueliang','do_what','duiyou']

#df = pd.read_csv('fightrun.csv',encoding='utf-8',names=names) # 指定列名
df = pd.read_csv('fightrun.csv')
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

predicted = model.predict(x)
#predicted = model.predict([1,1,0,1])
#predicted = model.predict([['手枪','多','少','有']])
print(predicted)
expected = y

print(expected.shape, predicted.shape)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))