import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
from mpl_toolkits.mplot3d import Axes3D #画3D图

# 读入源数据
df = pd.read_csv(r'E:\python_files\csv\Advertising.csv')
# 选取特征
X_list = ['TV', 'Radio', 'Newspaper'] # 特征的列名
X = df[X_list]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

pred1 = model.predict([[111,100,100]])
pred2 = model.predict(X)
#print(pred2)

a, b = model.intercept_, model.coef_
print(a)
print(b)

sd = plt.figure().add_subplot(111, projection = '3d')
sd.plot(df.TV, df.Radio, pred2, color='R')
#plt.show()

dct = {'y': y, 'pred2':pred2}
df2 = pd.DataFrame(dct)

print(df2.y.corr(df2.pred2))