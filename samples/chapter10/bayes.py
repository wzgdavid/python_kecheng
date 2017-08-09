'''
from decision_tree_t2
'''
from itertools import product
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
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
df = df.ix[:,['子弹','武器','血量','身边队友','行为']] # 选取需要的列

df = df.dropna()

# 手动转
#df[(df=='手枪')|(df=='少')|(df=='没')|(df=='逃跑')] = 0
#df[(df=='机枪')|(df=='中')|(df=='有')|(df=='战斗')] = 1
#df[(df=='多')|(df=='躲藏')] = 2
#df = df.astype(int)
# 用LabelEncoder转
classle = LabelEncoder()
df['武器'] = classle.fit_transform(df['武器'].values)
df['子弹'] = classle.fit_transform(df['子弹'].values)
df['血量'] = classle.fit_transform(df['血量'].values)
df['身边队友'] = classle.fit_transform(df['身边队友'].values)
df['行为'] = classle.fit_transform(df['行为'].values)

X = df[['武器','子弹','血量','身边队友']]
y = df['行为']





#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)
model = GaussianNB()
m = model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)  # 预测出的结果
y_test = y_test  # 期望的结果
# 打印预测结果，
print(metrics.classification_report(y_test, y_pred))
# 混淆矩阵
cm = metrics.confusion_matrix(y_test, y_pred)
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
