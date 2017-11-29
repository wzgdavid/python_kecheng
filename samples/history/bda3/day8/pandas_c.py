import numpy as np
import pandas as pd

users = pd.read_csv(r'E:\python_files\csv\users.csv')

m = users.groupby(['gender', 'occupation'])['age'].mean()
#print(m)
#print(m.index) # 复合索引

# 以条件分组
m = users.groupby([users.age>50, users['occupation']=='doctor'] )['age'].mean()
#print(m)


# dataframe 拼接
np.random.seed(5)
df1 = pd.DataFrame( np.random.randint(1,10,size=(4, 4)) )
df1.columns = list('ABCD')

df2 = pd.DataFrame( np.random.randint(1,10,size=(4, 4)) )
df2.columns = list('ABCD')

print(df1)
print(df2)
# 上下拼接
#df = pd.concat([df1, df2], axis=0)
##df = df.reset_index().drop('index',axis=1)
#df = df.set_index(pd.Series(list('abcdefg')))
#
#print(df)

print('-----------------------')
# 左右
df = pd.concat([df1, df2], axis=1)
#print(df)


df.columns = df.columns.str.lower()
df.index = list('abcd')
df.index = df.index.str.upper()
#print(df)