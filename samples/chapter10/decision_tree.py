import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import tree
from sklearn.externals.six import StringIO
import os

'''
数值  武器类型    子弹  血量  身边是否有队友  行为类别
0     手枪        少   少       没              逃跑 
1     机枪        多   多       有             战斗
'''
wuqi =    [0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1]
zidan =   [0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0]
xueliang =[0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0]
duiyou  = [0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,1]
do_what = [0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,0]

data = {
    'wuqi':wuqi,
    'zidan':zidan,
    'xueliang':xueliang,
    'duiyou':duiyou,
    'do_what':do_what,
}

df = pd.DataFrame(data)
print(df)
dtc = DTC()
x = df[['wuqi','zidan','xueliang','duiyou']]
y = df['do_what']

dtc.fit(x, y)

r = dtc.predict([[1,0,0,1]])
print(r)

