#from sklearn.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
#import sklearn.linear_model
#print(dir(sklearn.linear_model))
height = 171,175,159,155,152,158,154,164,168,166,159,164
weight = 60,64,41,47,35,44,41,57,57,49,47,46


#plt.show()
dct = {
    'height':height,
    'weight':weight
}
df=pd.DataFrame(dct)
#print(df)
#print(df.height.corr(df.weight))

X_train = df.height.values.reshape(-1, 1)
#print(X_train)
#print(X_train.shape)
y_train = df.weight
# 构建模型
#model = LinearRegression()
#model.fit(X_train, y_train) #训练模型
joblib.dump(model, 'lm.pkl') # 保存训练完的模型
#print(model.predict(180))
m = joblib.load('lm.pkl')    # 加载保存的模型
print(m.predict(189))
#a, b = model.intercept_, model.coef_
#print(a,b)
#plt.scatter(height, weight, color='blue')
##plt.plot(X_train, model.predict(X_train), color='red')
#plt.plot(df.height, b*df.height + a, color='red')
#plt.show()