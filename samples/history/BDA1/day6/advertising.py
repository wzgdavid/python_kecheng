import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
df = pd.read_csv(r'E:\python_files\csv\Advertising.csv')
#print(df.head())
# 选择特征
X = df[['TV','Radio','Newspaper']]
y = df['Sales']

# 交叉验证  train_size默认0.75
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)
model = LinearRegression()
model.fit(X_train, y_train)

#a, b = model.intercept_, model.coef_
#print(a, b)

y_pred = model.predict(X_test)
#print(y_pred)
#print(y_test)
#y_pred = pd.Series(y_pred)
#print(y_test.corr(y_pred))
dct = {'y_test': y_test,
'y_pred': y_pred}
df = pd.DataFrame(dct)
#print(df.y_test.corr(df.y_pred))

#sns.violinplot(data=df)
#plt.show()