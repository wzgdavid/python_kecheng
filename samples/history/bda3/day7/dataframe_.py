import numpy as np
import pandas as pd

df = pd.DataFrame(
        np.random.randint(1,10,size=(5,4)),
        index=list('abcde'),
        columns=list('ABCD')
    )
#print(df)
# 键作为 columns名
data = {'name':['tom', 'bob', 'dog'],
         'phone':np.array([123, 444, 789]),
         'age':18}
df = pd.DataFrame(data)
#print(df)
#print(df['name'], type(df.name))

# 用n个字典创建dataframe
#dict_a = {'name': 'tom',
#            'score': 99,
#            'age':99}
#dict_b = {'name1': 'ttt',
#            'score1': [999,88]}
#dict_c = {'name': 'jerry',
#            'score': 9}
#df = pd.DataFrame([dict_b,dict_c])
print(df)
#print('---------选一列df.name-------------')
#print(df.name) # df.name is a Series
#print('---------选一行df.ix[0]-------------')
#print(df.ix[0])
df['score'] = [99,88,77]
df['score2'] = df.score *10
print(df)
df = df.drop('score2', axis=1) # 丢弃一列 axis参数
#df = df.drop(['score2','score'], axis=1) # 丢弃n列 axis参数
#df.ix['4'] = [11,'cat',123]
print(df)
#print(df.ix[4])
#print(df.index)
print( df['name'] ) # 返回series
print( df[ ['name'] ], type(df[ ['name'] ]) ) # 返回dataframe
print( df[ ['name','score'] ] ) # 返回dataframe

