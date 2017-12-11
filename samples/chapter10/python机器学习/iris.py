import numpy as np
import pandas as pd

# 朴素贝叶斯分类    
from sklearn.naive_bayes import GaussianNB
# 决策树
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'E:\python_files\csv\Iris.csv')


# 得到分类标签， 方式一 手动处理
def species_labels(species):
    if species == 'Iris-setosa':
       rtn = 0
    elif species == 'Iris-versicolor':
       rtn = 1
    elif species == 'Iris-virginica':
       rtn = 2
    return rtn
#print( species_labels('Iris-versicolor') )
#df['labels'] = df['Species'].apply(species_labels)
#print(df.head())
#print(df['labels'].values)

#分类没有大小之分，方式二，用LabelEncoder
le = LabelEncoder()
df['labels'] = le.fit_transform(df.Species)
print(df.head())




# 训练集
X_train = df[ ['SepalLengthCm',  
               'SepalWidthCm',   
               'PetalLengthCm',  
               'PetalWidthCm'
            ] ]
y_train = df['labels']


clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)


#print( clf.predict([[4.2,   3,   2,   1]]) )

one_pred = clf.predict([[4.2,   3,   2,   1]])
#print(le.classes_)
#inverse_tranform 返回真实分类标签
one_pred = le.inverse_transform(one_pred)
print(one_pred)

y_pred = clf.predict(X_train)
print(y_pred)