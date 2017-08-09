'''
猫狗兔子
ppt上示例
'''

from itertools import product
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

'''
是 1 
否 0
狗 1  猫 2  兔子 3
'''

df = pd.read_csv(r'..\csv\catdograbbit.csv')

# 特征处理 3选1
# 1 手动转
#df[df=='是'] = 1
#df[df=='否'] = 0
#df[df=='狗'] = 1
#df[df=='猫'] = 2
#df[df=='兔子'] = 3
#df = df.astype(np.int8)
## 选取训练集特征
#X = df[['喜欢吃萝卜','喜欢吃鱼','喜欢捉耗子','喜欢啃骨头','短尾巴','长耳朵']]
#y = df['分类']

# 2 用labelencoder 转
#classle = LabelEncoder()
#df['喜欢吃萝卜'] = classle.fit_transform(df['喜欢吃萝卜'].values)
#df['喜欢吃鱼'] = classle.fit_transform(df['喜欢吃鱼'].values)
#df['喜欢捉耗子'] = classle.fit_transform(df['喜欢捉耗子'].values)
#df['喜欢啃骨头'] = classle.fit_transform(df['喜欢啃骨头'].values)
#df['短尾巴'] = classle.fit_transform(df['短尾巴'].values)
#df['长耳朵'] = classle.fit_transform(df['长耳朵'].values)
##  选取训练集特征
#X = df[['喜欢吃萝卜','喜欢吃鱼','喜欢捉耗子','喜欢啃骨头','短尾巴','长耳朵']]
#y = classle.fit_transform(df['分类'].values)

# 3 用哑变量
#classle = LabelEncoder()
#X = pd.get_dummies(df.drop('分类', axis=1))
#y = classle.fit_transform(df['分类'].values)


# 特征转换，可以手动，可以用LabelEncoder，看情况使用
# 手动
df[df=='否'] = 0
df[df=='是'] = 1
# LabelEncoder
classle = LabelEncoder()
df['分类'] = classle.fit_transform(df['分类'])
#print(df.head())

X = df.drop('分类', axis=1)
y = df['分类']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3)

# 学习
model = GaussianNB()
model = MultinomialNB()
model.fit(X_train, y_train)

# 查看预测效果 -------------------start--------------------------------
print(model.score(X_test, y_test)) # 分数，就是report的f1-score

y_pred = model.predict(X_test)

report = metrics.classification_report(y_test, y_pred)
print(report)
# 混淆矩阵
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)


# 画混淆矩阵
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
plt.imshow(cm, cmap = plt.cm.Blues)     # 画矩阵
half = cm.max() / 2
#classes = ['狗','猫','兔子'] # 分类名
classes = classle.classes_
#print(classes)
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
#plt.show()
# 查看预测效果 ------------------end---------------------------------

# 预测一个值
n = model.predict([[0,0,0,1,1,1]])
print(classle.inverse_transform(n))
n = model.predict([[1,0,0,0,0,1]])
print(classle.inverse_transform(n))