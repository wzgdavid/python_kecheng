import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 线性回归
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import LabelEncoder

# 以身高预测体重
dct = {
    'height':(171,175,159,155,152,158,154,164,168,166,159,164,
                171,175,159,155,152,158,154,164,168,166,159,164),
    'gender':('女','女','女','女','女','女','女','女','女','女','女','女',
         '男','男','男','男','男','男','男','男','男','男','男','男',),
    'weight':(57,64,41,38,35,44,41,51,57,49,47,46,
           59,69,49,39,39,49,49,59,59,49,49,49)
}
df = pd.DataFrame(dct) # 构造一个df
# 训练集特征是一个二维结构，哪怕只有一个特征，如[[5],[7],……...]

le = LabelEncoder()
# 用labelEncoder把字符转成数字
df.gender = le.fit_transform(df.gender.values)
#df[df=='女']
print(le.classes_)
print(df.head())


X_train = df[['height', 'gender']]
y_train = df.weight
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict([[172,0],[172,1]])
print(y_pred)

