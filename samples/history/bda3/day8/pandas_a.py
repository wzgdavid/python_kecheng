import numpy as np
import pandas as pd

np.random.seed(5)
df = pd.DataFrame( np.random.randint(1,10,size=(10, 4)) )
df.columns = list('ABCD')
#df.index = list('')
#df = pd.read_csv(r'D:\download\tai.csv')
#print(df.head())
#df = df.set_index(df.name)
#print(df.head())
print(df)
#print( df.iloc[2:5, 1:] )
#print( df.iloc[ [3, 6], [1, 2]] )
#print( df.ix[df.A>5, ['C', 'D']] )  #
print('-------df2----------')
df2 = df[df.A > 5]
print(df2)
print(df2.ix[4])  # 选标签
print(df2.iloc[4])  # 默认index
print(df.A.value_counts())

print('---------==================')
print(df.sum())  # arr.sum() 默认求所有元素
                 # 但 dataframe默认求0轴

#df.ix['sum'] = df.sum()  # 添加一行

#df.sum(axis=1)
#df['sum'] = df.sum(axis=1) # 添加一列
print(df)
#df[[a,b,c,d,e,f,g,e,d,s,a,s]] # 
#df.drop([w,y], axis=1) # 

#df.ix[1,1] = np.nan
print(df)
#print(df.sum(axis=1, skipna=False))
#print(df.idxmax())  # 最大值的下标
#print(df.sort_values(by='A'))
#print(df.A.quantile(0.2))
#print(df.cumsum(1))
#df['A2'] = df.A.rolling(3).sum()
#print(df)

#print(df.A.corr(df.A))
#print(df.A.corr(df.C))


#s = pd.Series([1,2,3,4,3,2,5,6,7])
#t = pd.Series([2,4,3,4,3,2,5,6,7])
#q = pd.Series([1,4,5,8,5,1,2,3,4])
#print(s.corr(s*2))
df['A2'] = df.A.shift(-1) # 正数向下，反之亦然
print(df)