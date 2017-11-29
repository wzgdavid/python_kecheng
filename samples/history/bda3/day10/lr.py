import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 线性回归
from sklearn.linear_model import LinearRegression
# 训练集和测试集分两部分
# 交叉验证
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'E:\python_files\csv\Advertising.csv')
# 训练集
X_train = df[['TV', 'Radio', 'Newspaper']]
y_train = df.Sales
# 学习
lr = LinearRegression()
lr.fit(X_train, y_train)

# a1 * TV + a2 * radio + a3 * Newspaper + b = y
a1, a2, a3 = lr.coef_ # coef_返回的是个一维ndarray
b = lr.intercept_
#print(a1, a2, a3)
#print(lr.predict([[12,3,4]]))
#print(12*a1+3*a2+4*a3+b)

# 检验结果
y_pred = lr.predict(X_train)
#预测值和真实值的相关系数
#ndarray没有corr方法 pd.Series有
corr = pd.Series(y_pred).corr(y_train) # y_pred预测值  y_train真实值
print(corr)

#X_train = df.iloc[:150][['TV', 'Radio', 'Newspaper']]
#y_train = df.iloc[:150]['Sales']
#
#X_test = df.iloc[150:][['TV', 'Radio', 'Newspaper']]
#y_test = df.iloc[150:]['Sales']
X = df[['TV', 'Radio', 'Newspaper']] # 特征
y = df.Sales  # 标签
# 交叉验证   过拟合overfit  欠拟合
(X_train, X_test, y_train, y_test) = train_test_split(X, y,train_size=0.6,test_size=0.4)
    # 随机取  默认75 训练 25测试
    # train_size,test_size和不能大于1
lr2 = LinearRegression()
lr2.fit(X_train, y_train)
print(lr2.coef_) # 0.04391002  0.19226497  0.01116475]

# 用test集验证结果
#y_pred = lr2.predict(X_test)
#cost = ((y_test.values - y_pred)**2).sum()
#print(cost) # 

print(lr2.predict([[22,10,4]]))