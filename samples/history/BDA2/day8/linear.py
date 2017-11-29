import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib


height = (171,175,159,155,152,158,154,164,168,166,159,164)
weight = (57,64,41,38,35,44,41,51,57,49,47,46)

# 构建一个DataFrame
dct = {'height':height,
        'weight':weight}
df = pd.DataFrame(dct)
# 特征
X = df['height'].values.reshape(-1, 1)
y = df['weight']
#print(X)
model = LinearRegression()
model.fit(X, y)
# 保存训练完的模型
#joblib.dump(model, 'lr.pkl')
# 预测
#print(model.predict(172))
# predict的参数是一个二维的结构（DataFrame，二维的数组，二维结构的列表）
# 加载持久化的模型
#model = joblib.load('lr.pkl')
pred2 = model.predict([[172],[179]])
pred3 = model.predict(X)
#print(pred3)

#a, b = model.intercept_, model.coef_
#print(a,b)
# 画散点图和拟合后的直线
plt.scatter(height, weight)
plt.plot(height, pred3, color='R')
#plt.plot(height, b*df.height+a, color='R')
plt.show()


