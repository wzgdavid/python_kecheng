import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# classify  Classifier 分类器 简称clf
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,\
                            confusion_matrix


# 数读取据
df = pd.read_csv(r'E:\python_files\csv\Iris.csv')
#print(df.head())  
#Id  SepalLengthCm  SepalWidthCm  
#PetalLengthCm  PetalWidthCm      Species
# 零。数据简单变换
le = LabelEncoder()
df.Species = le.fit_transform(df.Species.values)
#print(df.head())

# 一。获得学习集
X = df.drop(['Id','Species'], axis=1)
y = df.Species
# 交叉验证
(X_train, X_test, y_train, 
y_test) = train_test_split(X,y,train_size=0.6,test_size=0.4)

# 二。学习
clf = DecisionTreeClassifier() # 用决策树分类器学习
#clf = GaussianNB()   # 朴素贝叶斯 
clf.fit(X_train, y_train)
# 预测一个分类
n = clf.predict([ [4.4, 8.5,1.8,2.3] ])
print(le.inverse_transform(n))
print(le.classes_)
# 三。看分类结果好坏
y_pred = clf.predict(X_test)

#print(help(classification_report))
print(classification_report(y_test, y_pred))
# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(cm)


# classes ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
# 画鸢尾花散点图
seto = df[df.Species == 0]
vers = df[df.Species == 1]
virg = df[df.Species == 2]
plt.scatter(seto.SepalLengthCm, seto.SepalWidthCm, label='Iris-setosa', s=10)
plt.scatter(vers.SepalLengthCm, vers.SepalWidthCm, label='Iris-versicolor', s=10)
plt.scatter(virg.SepalLengthCm, virg.SepalWidthCm, label='Iris-virginica', s=10)
plt.legend()
plt.savefig('sepal.png')

plt.clf() # clear the current figure
# 不clf的画，下面savefig把前面的scatter的内容都save了
plt.scatter(seto.PetalLengthCm, seto.PetalWidthCm, label='Iris-setosa', s=10)
plt.scatter(vers.PetalLengthCm, vers.PetalWidthCm, label='Iris-versicolor', s=10)
plt.scatter(virg.PetalLengthCm, virg.PetalWidthCm, label='Iris-virginica', s=10)
plt.legend()
plt.savefig('petal.png')











