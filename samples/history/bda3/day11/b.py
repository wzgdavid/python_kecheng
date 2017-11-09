import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# classify  Classifier 分类器 简称clf
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,\
                            confusion_matrix


# 数读取据
df = pd.read_csv(r'E:\python_files\csv\Iris.csv')
# 一。获得学习集
X = df.drop(['Id','Species'], axis=1)
y = df.Species
# 交叉验证
(X_train, X_test, y_train, 
y_test) = train_test_split(X,y,train_size=0.8,test_size=0.2)


clf1 = DecisionTreeClassifier()
clf2 = GaussianNB()
clf3 = KNeighborsClassifier()
clf4 = LogisticRegression()
clf5 = SVC()

clf1.fit(X_train, y_train)
clf2.fit(X_train, y_train)
clf3.fit(X_train, y_train)
clf4.fit(X_train, y_train)
clf5.fit(X_train, y_train)

print(clf1.score(X_train, y_train))
print(clf2.score(X_train, y_train))
print(clf3.score(X_train, y_train))
print(clf4.score(X_train, y_train))
print(clf5.score(X_train, y_train))