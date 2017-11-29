import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 线性回归
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
# 以身高预测体重
dct = {
    'height':(171,175,159,155,152,158,154,164,168,166,159,164,
                171,175,159,155,152,158,154,164,168,166,159,164),
    'gender':(0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1),
    'weight':(57,64,41,38,35,44,41,51,57,49,47,46,
           59,69,49,39,39,49,49,59,59,49,49,49)
}
df = pd.DataFrame(dct) # 构造一个df
# 训练集特征是一个二维结构，哪怕只有一个特征，如[[5],[7],……...]
X_train = df.height.values.reshape(-1, 1) 
#print(X_train)
y_train = df.weight

#lr = LinearRegression()
#lr.fit(X_train, y_train)   # fit学习 
#joblib.dump(lr, 'lr.pkl')  # 保存在本地   数据持久化
lr = joblib.load('lr.pkl')  # 从硬盘上读取
# 预测
#print(lr.predict([[162]]))
#print(lr.predict([[162],[172],[135]]))
# ax + b = y
b = lr.intercept_ # b 
a = lr.coef_      # a       weight = 1.11height - 132
y_pred = lr.predict(X_train)
print(y_pred)
# 画拟合后的直线
#plt.plot(X_train, y_pred, color='r') # 
#plt.plot(X_train, a*X_train+b, color='r')
#plt.scatter(df.height, df.weight)
#plt.show()
 

'''
# 加一个特征， 性别
X_train = df[['height', 'gender']]
#print(X_train)
#
lr.fit(X_train, y_train)
y_pred = lr.predict([[172,0],[172,1]])
print(y_pred)

y_pred = lr.predict(X_train) 
# 预测的返回及结果是一个一维的ndarray
#print(np.round(y_pred,1))

# 验证结果
# (真实结果减去预测值) 平方
cost = ((y_train - y_pred)**2).sum()
#print(cost) # 
# 比如第二种方法的cost比较小 说明这第二种方法比较好，
# aX1 + bX2 + c = y  
# weight = 1,16*height + 4*gender - 133
a, b = lr.coef_
c = lr.intercept_
#print(a,b,c)
#print(a*172+b*0+c)

from mpl_toolkits.mplot3d import Axes3D
sand = plt.figure().add_subplot(111, projection='3d')
#sand.plot(df.height, df.gender, df.weight)
sand.plot(df.height, df.gender, y_pred)
sand.set_xlabel('height')
sand.set_ylabel('gender')
sand.set_zlabel('weight')
#plt.show()
'''