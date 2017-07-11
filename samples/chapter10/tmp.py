'''
手动转换数据
3种结果行为，战斗，逃跑，躲藏， 
有空值
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import tree
from sklearn.externals.six import StringIO
import os
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from scipy.stats import uniform as sp_rand
'''
数值  武器类型    子弹  血量  身边队友  行为类别
0     手枪        少   少       没         逃跑
1     机枪        中   中       有         战斗
2                 多   多                  躲藏
'''

df = pd.read_csv('fightrun3.csv')
df = df.ix[:,['子弹','武器','血量','身边队友','行为']] 
#df[df=='少'] = 0
#df[df=='手枪'] = 0
#df[df=='逃跑'] = 0
df = df.dropna()
sq = df['武器'].copy()
sq[sq=='手枪'] = 0
sq[sq=='机枪'] = 1
df['武器'] = sq
print(df)

#df[(df=='手枪')|(df=='少')|(df=='没')|(df=='逃跑')] = 0
#df[(df=='机枪')|(df=='中')|(df=='有')|(df=='战斗')] = 1
#df[(df=='多')|(df=='躲藏')] = 2
#df = df.astype(int)

