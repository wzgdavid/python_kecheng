import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# 原始数据
height = (171,175,159,155,152,158,154,164,168,166,159,164)
weight = (57,64,41,38,35,44,41,51,57,49,47,46)
# 构建一个字典
dct = {'height': height,
       'weight': weight}
# 构建一个dataframe
df = pd.DataFrame(dct)
x_train = df.height.values.reshape(-1, 1)
y_train = df.weight

model = LinearRegression()
model.fit(x_train, y_train)
print(model.predict(170))

# 画图
plt.plot(x_train, model.predict(x_train), color='r')
plt.scatter(height, weight, color='b')
plt.xlabel('height')
plt.ylabel('weight')
plt.show()
