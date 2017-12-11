import numpy as np
import pandas as pd
# 线性回归模型
from sklearn.linear_model import LinearRegression
# 凡是在windows下和路径有关的字符串，前面加个r
# 就不会转义
# 读取数据
df = pd.read_csv(r'E:\python_files\csv\Advertising.csv')
#print(df.head())

# 训练集 特征
X_train = df[ ['TV','Radio', 'Newspaper'] ]
#print(X_train.head())
## 训练集 标签
y_train = df['Sales']
#print(y_train)

# 学习
model = LinearRegression()
model.fit(X_train, y_train)
# predict的参数是特征，特征是二维结构
one_pred =  model.predict( [[100, 90, 40]] ) 
print(one_pred)

# 预测两个输入
two_pred =  model.predict( [
                              [100, 90, 40],
                              [230.1, 37.8, 69.2],
                         ] ) 
print(two_pred)

# 预测真实数据
y_pred = model.predict(X_train) # y的预测值
print(y_pred)
