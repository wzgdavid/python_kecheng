import numpy as np
import pandas as pd

# 朴素贝叶斯分类    
from sklearn.naive_bayes import GaussianNB
# 决策树
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# 通常情况下，用一部分数据去训练，另一部分去测试
from sklearn.model_selection import train_test_split

# 混淆矩阵
from sklearn.metrics import confusion_matrix, classification_report


df = pd.read_csv(r'E:\python_files\csv\Iris.csv')
le = LabelEncoder()
df['labels'] = le.fit_transform(df.Species)

X = df[ ['SepalLengthCm',  
               'SepalWidthCm',   
               'PetalLengthCm',  
               'PetalWidthCm'
            ] ]
y = df['labels']

# 通常情况下，用一部分数据去训练，另一部分去测试
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                      train_size=0.6, # 默认0.75
                                      test_size=0.4)  # 默认0.25
                                  # train_size + test_size不能大于1

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test) # y_pred是对X_test部分数据的预测
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(report)

clf = GaussianNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test) # y_pred是对X_test部分数据的预测
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(report)




