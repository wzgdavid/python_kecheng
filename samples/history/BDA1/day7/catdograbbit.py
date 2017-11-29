#from sklearn.
from itertools import product
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier



plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
df = pd.read_csv(r'E:\python_files\csv\catdograbbit.csv')

# 用LabelEncoder把特征转换成数字
le = LabelEncoder()
df['喜欢吃萝卜'] = le.fit_transform(df['喜欢吃萝卜'].values)
#print(le.inverse_transform(0), le.inverse_transform(1))
le = LabelEncoder()
df['喜欢吃鱼'] = le.fit_transform(df['喜欢吃鱼'].values)
#print(le.inverse_transform(0), le.inverse_transform(1))
df['喜欢捉耗子'] = le.fit_transform(df['喜欢捉耗子'].values)
#print(le.inverse_transform(0), le.inverse_transform(1))
df['喜欢啃骨头'] = le.fit_transform(df['喜欢啃骨头'].values)
#print(le.inverse_transform(0), le.inverse_transform(1))
df['短尾巴'] = le.fit_transform(df['短尾巴'].values)
#print(le.inverse_transform(0), le.inverse_transform(1))
df['长耳朵'] = le.fit_transform(df['长耳朵'].values)
#print(le.inverse_transform(0), le.inverse_transform(1))
df['分类'] = le.fit_transform(df['分类'].values)
X = df.drop('分类', axis=1)
#print(X.columns)
y = df['分类']


# 交叉验证
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)
#model = DTC()      猫
#model = GaussianNB()  猫
#model = KNeighborsClassifier() 兔子
#model = MLPClassifier()  猫
#model = SVC() gou
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
n = model.predict([[1,1,0,0,1,1]])
print(le.inverse_transform(n))

feature = ['否', '是','否', '是','否', '是']

def predict_class2(feature):
    f = []
    for i, n in enumerate(feature):
        if i in [1,2,3]:
            if n == '否':
                f.append(1)
            else:
                f.append(0)
        else:
            if n == '否':
                f.append(0)
            else:
                f.append(1)

    n = model.predict([f])
    print(le.inverse_transform(n))
predict_class2(feature)

#def predict_class(feature):
#    f = []
#    for n in feature:
#        if n == '否':
#            f.append(0)
#        else:
#            f.append(1)
#    n = model.predict([f])
#    print(le.inverse_transform(n))
#predict_class(feature)

#n = model.predict([
#    [1,1,0,0,1,1],
#    [0,1,0,0,0,0],
#    [1,1,1,0,1,1],
#    [1,0,0,0,0,0],
#    [1,1,1,0,1,0],
#    [0,1,0,0,1,1],
#    ])
#print(le.inverse_transform(n))
#for i in range(len(n)):
#
#    print(le.inverse_transform(n[i]))
