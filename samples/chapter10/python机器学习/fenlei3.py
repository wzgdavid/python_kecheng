import numpy as np
import pandas as pd

# 朴素贝叶斯分类    
from sklearn.naive_bayes import GaussianNB
# 决策树
from sklearn.tree import DecisionTreeClassifier

# 把这个预测问题，换成分类问题来做
# 把标签是连续值的问题，换成标签是离散值的问题
df = pd.read_csv(r'E:\python_files\csv\Advertising.csv')

# 注意大小
#很低 <5         1
#低   5  ~ 10    2
#中   10 ~ 15    3
#高   15 ~ 20    4
#非常高 >20      5


def sales_rank(sales):
    #print(type(sales))
    if sales < 5:
        rtn = 1  #'很低'
    elif sales <10:
        rtn = 2  #'低'
    elif sales <15:
        rtn = 3  #'中'
    elif sales <20:
        rtn = 4  #'高'
    else:
        rtn = 5  #'非常高'
    return rtn
#print(sales_rank(14)) # 测试一下


df['Salesrank'] = df.Sales.apply(sales_rank)
#print(df.head())


X_train = df[ ['TV', 'Radio', 'Newspaper'] ]
y_train = df['Salesrank']

# 选择分类模型
#clf = GaussianNB() # clf 表示一个分类器 classification的缩写
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

print(clf.predict([[100,90,40]]))

y_pred = clf.predict(X_train)
print(y_pred)