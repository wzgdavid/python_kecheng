import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

# 看一下不同分类的散点图
# 分别选出各分类的数据
seto = df[df.Species=='Iris-setosa']
vers = df[df.Species=='Iris-versicolor']
virg = df[df.Species=='Iris-virginica']
#SepalLengthCm   SepalWidthCm
plt.scatter(seto.SepalLengthCm, seto.SepalWidthCm, label='Iris-setosa',s=10)
plt.scatter(vers.SepalLengthCm, vers.SepalWidthCm, label='Iris-versicolor',s=10)
plt.scatter(virg.SepalLengthCm, virg.SepalWidthCm, label='Iris-virginica',s=10)
plt.legend()
plt.title('Sepal Length & Width')
plt.xlabel('length');plt.ylabel('width')
#plt.savefig('sepal.png')
plt.clf() # clear 画布
#PetalLengthCm  PetalWidthCm
#plt.scatter(seto.PetalLengthCm, seto.PetalWidthCm, label='Iris-setosa',s=10)
#plt.scatter(vers.PetalLengthCm, vers.PetalWidthCm, label='Iris-versicolor',s=10)
#plt.scatter(virg.PetalLengthCm, virg.PetalWidthCm, label='Iris-virginica',s=10)
#plt.legend()
#plt.xlabel('length');plt.ylabel('width')
#plt.title('Petal Length & Width')
#plt.savefig('petal.png')



#sand = plt.figure().add_subplot(111, projection='3d')
#sand.scatter(seto.SepalLengthCm, seto.SepalWidthCm, seto.PetalLengthCm, label='Iris-setosa',s=10)
#sand.scatter(vers.SepalLengthCm, vers.SepalWidthCm, vers.PetalLengthCm, label='Iris-versicolor',s=10)
#sand.scatter(virg.SepalLengthCm, virg.SepalWidthCm, virg.PetalLengthCm, label='Iris-virginica',s=10)
#sand.legend()
#sand.set_xlabel('SepalLength');
#sand.set_ylabel('SepalWidth')
#sand.set_zlabel('SepalWidth')
#plt.show()






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


# 二。学习
clf = DecisionTreeClassifier() # 用决策树分类器学习
#clf = GaussianNB()   # 朴素贝叶斯 
clf.fit(X_train, y_train)
# 预测一个分类
n = clf.predict([ [4.4, 8.5,1.8,2.3] ])
print(le.inverse_transform(n))
#print(le.classes_)
# 三。看分类结果好坏
y_pred = clf.predict(X_test)

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(le.classes_)
print(cm)
##print(help(classification_report))
print(classification_report(y_test, y_pred))
print(clf.score(X_test, y_test))

plt.imshow(cm, cmap=plt.cm.Blues)
plt.xticks(range(3),le.classes_)
plt.yticks(range(3),le.classes_)
half = cm.max()/2
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i,j],
            color='white' if cm[i,j] > half else 'black',
            size=20,
            horizontalalignment='center',
            )
#plt.show()
