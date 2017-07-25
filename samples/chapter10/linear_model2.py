'''
多元线性回归
参考http://blog.csdn.net/lulei1217/article/details/49386295
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns

# Advertising.csv来自http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv
# "","TV","Radio","Newspaper","Sales"
df = pd.read_csv(r'..\csv\Advertising.csv')
#print(df)
#
#print(df.Sales.corr(df.TV))
#print(df.Sales.corr(df.Radio))
#print(df.Sales.corr(df.Newspaper))

# 选择特征库 
X = df[['TV', 'Radio', 'Newspaper']]
#print(x)
# 生成训练集和测试集
y = df['Sales'] 
# 交叉验证，用一部分数据来训练，另一部分来验证，这两部分数据不能重复
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)
#print(X_train.shape)  
#print(y_train.shape) 
#print(X_test.shape) 
#print(y_test.shape)

model = LinearRegression()
model.fit(X_train, y_train)

a, b = model.intercept_, model.coef_
#print(a)
#print(b)
#y=2.668+0.0464*TV+0.192*Radio-0.00349*Newspaper

# 预测
predicted = model.predict(X_test)
#print(predicted)

#print(metrics.accuracy_score(y_test, predicted))
# 以上报错 continuous is not supported
dct = {
    'y_test':y_test,
    'y_pred': predicted
}
df = pd.DataFrame(dct)
print(df.y_test.corr(df.y_pred))
print(df.describe())

sns.violinplot(data = df)
plt.ylim(0,35)
plt.ylabel('sales')
plt.show()