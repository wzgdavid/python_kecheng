import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

au = pd.read_csv(r'D:\workspace\ana\data\au.csv')

def get_ma(df, n):
    column_name = 'ma' + str(n)
    df[column_name] = df.c.rolling(window=n).mean()
    return df
#au['ma20'] = au.c.rolling(window=20).mean()
#au['ma50'] = au.c.rolling(window=50).mean()


au = get_ma(au, 20)
au = get_ma(au, 50)
#au.to_csv('au_temp.csv')
#plt.plot(au.c, label='close')
#plt.plot(au.ma20, label='ma20')
#plt.plot(au.ma50, label='ma50')
#plt.legend()  # 图例
#plt.show()

# 散点图
plt.scatter(au.o, au.c, s=2)
plt.show()

