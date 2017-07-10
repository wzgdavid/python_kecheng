'''
多元线性回归
参考http://blog.csdn.net/lulei1217/article/details/49386295
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Advertising.csv来自http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv
# "","TV","Radio","Newspaper","Sales"
df = pd.read_csv('Advertising.csv')
#print(df)
#
#print(df.Sales.corr(df.TV))
#print(df.Sales.corr(df.Radio))
#print(df.Sales.corr(df.Newspaper))

# 选择特征库 
x = df[['TV', 'Radio', 'Newspaper']]
#print(x)
# 生成训练集和测试集
y = df['Sales'] 
# 交叉验证，用一部分数据来训练，另一部分来验证，这两部分数据不能重复
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6, test_size=0.4)
#print(x_train.shape)  
#print(y_train.shape) 
#print(x_test.shape) 
#print(y_test.shape)

linreg = linear_model.LinearRegression()
linreg.fit(x_train, y_train)

a, b = linreg.intercept_, linreg.coef_
print(a)
print(b)
#y=2.668+0.0464*TV+0.192*Radio-0.00349*Newspaper

# 预测
y_predict = linreg.predict(x_test)
print(y_predict)

# 做曲线
##plt.figure()  
plt.plot(range(len(y_predict)),y_predict,'b',label="predict")
plt.plot(range(len(y_predict)),y_test,'r',label="test")
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()


#plt.scatter(x_test.Newspaper, y_test, color='blue')
#plt.show()