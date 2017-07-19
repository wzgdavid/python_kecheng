'''
猫狗兔子
'''

from itertools import product
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import train_test_split

'''
是 1 
否 0
狗 1  猫 2  兔子 3
'''

#names = ['luobo','yu','haozi','gutou','dwb','ced','fenlei']
## 读取csv时自定义列名
#df = pd.read_csv('D:\csv\catdograbbit.csv', names = names)
#df = df.ix[:,:] # 如果是自定义names的话，要从第二行开始选
df = pd.read_csv('D:\csv\catdograbbit.csv')
#df = df.ix[:,['喜欢吃萝卜','喜欢吃鱼','喜欢捉耗子','喜欢啃骨头','短尾巴','长耳朵','分类']]
df[df=='是'] = 1
df[df=='否'] = 0
df[df=='狗'] = 1
df[df=='猫'] = 2
df[df=='兔子'] = 3
df = df.astype(np.int8)

x = df[['喜欢吃萝卜','喜欢吃鱼','喜欢捉耗子','喜欢啃骨头','短尾巴','长耳朵']]
y = df['分类']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, test_size=0.3)

# 学习
model = GaussianNB()
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
plt.show()