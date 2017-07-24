'''
手动转换数据
3种结果行为，战斗，逃跑，躲藏， 
有空值
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

'''
数值  武器类型    子弹  血量  身边队友  行为类别
0     手枪        少   少       没         逃跑
1     机枪        中   中       有         战斗
2                 多   多                  躲藏
'''

df = pd.read_csv(r'..\csv\fightrun2.csv')
df = df.ix[1:,['子弹','武器','血量','身边队友','行为']] # 读取的列要么都是字符，要么都是数字

df = df.dropna()

# 用LabelEncoder转
classle = LabelEncoder()
df['武器'] = classle.fit_transform(df['武器'].values)
df['子弹'] = classle.fit_transform(df['子弹'].values)
df['血量'] = classle.fit_transform(df['血量'].values)
df['身边队友'] = classle.fit_transform(df['身边队友'].values)
df['行为'] = classle.fit_transform(df['行为'].values)


X = df[['武器','子弹','血量','身边队友']]
#print(X)
y = df['行为']#.astype(int)
#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)
model = DTC()
model.fit(X_train, y_train)

# 预测
predicted = model.predict(X_test)  # 预测出的结果
expected = y_test  # 期望的结果
# 打印预测结果，
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))




