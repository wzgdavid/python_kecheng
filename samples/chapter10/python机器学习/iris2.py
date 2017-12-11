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
#print(y_pred) 
#print(y_test.values) # 真实值

# 分类效果  混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(cm)
# 直接看混淆矩阵还是不太好区分分类效果好坏
# 用分类报告，直接显示一些分数
report = classification_report(y_test, y_pred)
print(report)

'''
                  混淆矩阵      0   1  2
                          0  [[20  0  0]
                          1   [ 0 10  5]
                          2   [ 0  2 23]]
          根据混淆矩阵得到的分类报告
             precision    recall  f1-score   support

          0       1.00      1.00      1.00        20
          1       0.83      0.67      0.74        15
          2       0.82      0.92      0.87        25
       
avg / total       0.88      0.88      0.88        60    加权平均，权重是support
                                     总分
                                     
        precision 预测出正确的占所有预测成这一类的比例    0.83 =  10 / (10 + 2)
        recall    预测出正确的占所有真实的这一类的比例    0.67 =  10 / (10 + 5) 
                   20       12.45  20.5
        0.88 =  (1*20 + 0.83*15+0.82*25)/ 60 

''' 