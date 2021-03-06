'''
一元线性回归
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib  # 模型持久化
from sklearn import metrics

height_weight = {
    'height': (171,175,159,155,152,158,154,164,168,166,159,164),
    'weight': (57,64,41,38,35,44,41,51,57,49,47,46)
}
#df = pd.DataFrame(fangjia)
df = pd.DataFrame(height_weight)
# 相关性高，用线性回归得出的结果才可靠
print(df.height.corr(df.weight))
# 训练集 特征
X_train = df.height.values.reshape(-1,1)
# 结果集
y_train = df.weight

# 学习训练集生成模型
model = LinearRegression()
model.fit(X_train, y_train)
# 训练完的模型持久化
#joblib.dump(model, 'lr.pkl')
# 读取持久化的模型
#model = joblib.load('lr.pkl')

# 预测
print(model.predict(170))

# 得到直线的斜率，截距
a, b = model.coef_, model.intercept_

# 画图
# 散点图
plt.scatter(df['height'], df['weight'], color='blue')
# 拟合的直线
plt.plot(X_train, model.predict(X_train), color='red', linewidth=3)
#plt.plot(df['height'], a*df['height']+b, color='red', linewidth=3)
plt.xlabel("height")
plt.ylabel('weight')
# 显示画图，保存画图
plt.savefig('lm.png')
plt.show()






