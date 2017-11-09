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
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
df = pd.read_csv(r'E:\python_files\csv\catdograbbit.csv')

#df[df=='是'] =1
#print(df.head())

# 用LabelEncoder把特征转换成数字
le = LabelEncoder()
df['喜欢吃萝卜'] = le.fit_transform(df['喜欢吃萝卜'].values)
#print(le.inverse_transform(0), le.inverse_transform(1))
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

#print(df.head())
#颜色        红色    绿色    蓝色
#红色  0      1        0       0
#绿色  1       0        1       0
#蓝色  2       0       0       0   1
#print(df.head())
#
# 用哑变量构建学习集特征
#X = pd.get_dummies(df.drop('分类', axis=1))
#print(X.columns)
#le = LabelEncoder()
#y = le.fit_transform(df['分类'].values)
#print(dir(le))

#X = df.drop('分类', axis=1)
#y = df['分类']

# 交叉验证
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)
model = DTC()
#model = GaussianNB()
model.fit(X_train, y_train)

predicted = model.predict(X_test)
expected = y_test
report = metrics.classification_report(predicted, expected)
print(report)
print(model.score(X_test, y_test))


#one_feature = X.iloc[0]
#one_feature[:] = 0
#print(one_feature)

#n = model.predict(one_feature)
#le.inverse_transform(n)
#n = model.predict([
#    [1,1,0,0,1,1],
#    [0,1,0,0,0,0],
#    [1,1,1,0,1,1],
#    [1,0,0,0,0,0],
#    [1,1,1,0,1,0],
#    [0,1,0,0,1,1],
#    ])
#print(n)
#for i in range(len(n)):
#
#    print(le.inverse_transform(n[i]))
#cm = metrics.confusion_matrix(predicted, expected)
#print(0,le.inverse_transform(0))
#print(1,le.inverse_transform(1))
#print(2,le.inverse_transform(2))
#print(cm)
#report = metrics.classification_report(predicted, expected)
#print(report)

#data = np.random.randint(9,size=(4,4))
#plt.imshow(data, cmap=plt.cm.Greens)
#plt.show()

#plt.imshow(cm, cmap=plt.cm.Greens)
#
#classes = ['兔子', '狗', '猫']
#plt.xticks(range(3), classes)
#plt.yticks(range(3), classes)
#plt.colorbar()
#shape0 = range(cm.shape[0])
#shape1 = range(cm.shape[1])
##
#half = cm.max()/2
## 迭代矩阵，给每个块填上数字
#for i, j in product(shape0,shape1):
#    #print(cm[i,j])
#    color = 'white' if cm[i,j]> half else 'black' 
#    plt.text(j,i,cm[i,j],
#        #horizontalalignment='center',
#        color = color
#        )
  
#plt.show()