'''
from decision_tree_t2
mlp神经网络
'''
from itertools import product
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

'''
数值  武器类型    子弹  血量  身边队友  行为类别
0     手枪        少   少       没         逃跑
1     机枪        中   中       有         战斗
2                 多   多                  躲藏
'''

df = pd.read_csv(r'..\csv\fightrun2.csv')
df = df.ix[:,['子弹','武器','血量','身边队友','行为']] # 读取的列要么都是字符，要么都是数字

df = df.dropna()
# 用LabelEncoder转
classle = LabelEncoder()
df['武器'] = classle.fit_transform(df['武器'].values)
df['子弹'] = classle.fit_transform(df['子弹'].values)
df['血量'] = classle.fit_transform(df['血量'].values)
df['身边队友'] = classle.fit_transform(df['身边队友'].values)
df['行为'] = classle.fit_transform(df['行为'].values)

X = df[['武器','子弹','血量','身边队友']]
#print(x)
y = df['行为']#.astype(int)
#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)
model = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=1000)
m = model.fit(X_train, y_train)

# 预测
predicted = model.predict(X_test)  # 预测出的结果
expected = y_test  # 期望的结果
# 打印预测结果，
print(metrics.classification_report(expected, predicted))
cm = metrics.confusion_matrix(expected, predicted)
print(cm)


# 画混淆矩阵

plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
plt.imshow(cm, cmap = plt.cm.Blues)     # 画矩阵
half = cm.max() / 2
classes = ['狗','猫','兔子'] # 分类名
length = range(len(classes))  # 混淆矩阵的边长
plt.xticks(length, classes)
plt.yticks(length, classes)
plt.colorbar()
plt.ylabel('真值')
plt.xlabel('预测值')
# 每个块显示数字
for i, j in product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, cm[i, j],
             horizontalalignment="center",
             # 浅色背景深色字，深背景浅色字
             color="white" if cm[i, j] > half else "black") 
#sns.heatmap(cm, annot=True)
plt.show()