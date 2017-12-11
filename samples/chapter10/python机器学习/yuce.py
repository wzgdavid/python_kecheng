import numpy as np
import pandas as pd
# 线性回归模型
from sklearn.linear_model import LinearRegression

# 生成训练集
# 学习训练集
# 预测
height = (171,175,159,155,152,158,154,164,168,166,159,164)
weight = (57, 64, 41, 38, 35,44,41,51,57,49,47,46) # 元组
df = pd.DataFrame()
df['height'] = height
df['weight'] = weight
#print(df)
# 训练集的特征是个二维的结构
# 标签是一维的
# X 代表特征
# y 代表标签
X_train = df['height'].values.reshape(-1,1)
y_train = df['weight']
model = LinearRegression() # 选一个模型
model.fit(X_train, y_train) # 学习
print(model.predict(170))# 预测
print(model.predict(X_train))