'''
from decision_tree_t2
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
from itertools import product
'''
数值  武器类型    子弹  血量  身边队友  行为类别
0     手枪        少   少       没         逃跑
1     机枪        中   中       有         战斗
2                 多   多                  躲藏
'''

df = pd.read_csv(r'D:\python_kecheng\samples\csv\fightrun2.csv')
df = df.ix[:,['子弹','武器','血量','身边队友','行为']] # 选取需要的列

df = df.dropna()
#
df[(df=='手枪')|(df=='少')|(df=='没')|(df=='逃跑')] = 0
df[(df=='机枪')|(df=='中')|(df=='有')|(df=='战斗')] = 1
df[(df=='多')|(df=='躲藏')] = 2
# 单列处理数据变换
#sq = df['武器'].copy()
#sq[sq=='手枪'] = 0
#sq[sq=='机枪'] = 1
#df['武器'] = sq

df = df.astype(int)
#print(df)
x = df[['武器','子弹','血量','身边队友']]
#print(x)
y = df['行为']#.astype(int)
#print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6, test_size=0.4)
model = GaussianNB()
m = model.fit(x_train, y_train)

# 预测
predicted = model.predict(x_test)  # 预测出的结果
expected = y_test  # 期望的结果
# 打印预测结果，
print(metrics.classification_report(expected, predicted))
# 混淆矩阵
cm = metrics.confusion_matrix(expected, predicted)
## 矩阵标准化 值在0, 1 之间
#cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print(cm)


# 画混淆矩阵
classes = ['逃跑','战斗','躲藏'] # 分类名
length = range(len(classes))  # 混淆矩阵的边长
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
plt.imshow(cm, cmap = plt.cm.Blues)
thresh = cm.max() / 2.
for i, j in product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, cm[i, j],
             horizontalalignment="center",
             # 浅色背景深色字，深背景浅色字
             color="white" if cm[i, j] > thresh else "black") 
plt.xticks(length, classes)
plt.yticks(length, classes)
plt.colorbar()
plt.ylabel('真值')
plt.xlabel('预测值')
plt.show()
