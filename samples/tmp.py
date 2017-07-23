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

#names = ['luobo','yu','haozi','gutou','dwb','ced','fenlei']
## 读取csv时自定义列名
#df = pd.read_csv('D:\csv\catdograbbit.csv', names = names)
df = pd.read_csv(r'csv\catdograbbit.csv')

#x = pd.get_dummies(df.drop('分类', axis=1))
#classle = LabelEncoder()
#y = classle.fit_transform(df['分类'].values)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, test_size=0.3)

# 学习
#model = GaussianNB()
model = MultinomialNB()
model.fit(x_train, y_train)

# 预测结果
#print(model.predict([[0,0,0,0,0,1]]))  # 预测一个，传一组特征
predicted = model.predict(x_test)
expected = y_test
report = metrics.classification_report(predicted, expected)
print(report)

# 混淆矩阵
cm = metrics.confusion_matrix(predicted, expected)
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