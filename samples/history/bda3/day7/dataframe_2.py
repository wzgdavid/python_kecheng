import numpy as np
import pandas as pd
#1,2,3,4,5,6,7,9,13,14,15,15,15,15,15
#分位数
#10% 20%
df = pd.DataFrame(
        np.random.randint(1,4,size=(10,4)),
        index=list('efhgabcdij'),
        columns=list('CDAB')
    )
#print(df.head(10))
#print(df.tail(4))
#print(df.describe())
#               A          B          C          D
#count  20.000000  20.000000  20.000000  20.000000
#mean    6.100000   5.150000   5.200000   4.950000
#std     2.863564   2.277464   2.546411   2.781045
#min     1.000000   2.000000   1.000000   1.000000
#25%     3.750000   3.000000   3.500000   2.750000#1/4位数
#50%     7.000000   5.000000   6.000000   5.000000# 中位数
#75%     9.000000   6.000000   7.000000   7.250000#3/4位数
#max     9.000000   9.000000   9.000000   9.000000#

#print(df)
#print(df.T)
#print(df.sort_index(axis=1)) # 对column排序
#print(df.sort_index())
#print(df.sort_values(by='A'))
#print(df.sort_values(by=['C','A'])) # 二次排序

# 读取csv文件
df = pd.read_csv(r'D:\download\tai.csv')
#print(df.head(10))
#print(df.sex.value_counts()) # 男女各有多少
male = df.sex.value_counts()['male']
#print(male)
#print(df.age.mean())
df = df.set_index(df.name) # 
#print(df.head())
#print(df.loc['Allison, Master. Hudson Trevor'])
#print(df.ix['Allison, Master. Hudson Trevor'])
#print(df.ix[0])
#print(df.loc['Allison, Master. Hudson Trevor'])
#print(df.iloc[0])
# loc + iloc    == ix
# 
#select name,age from
#print('-------------------')
allison = df.ix['Allison, Master. Hudson Trevor', ['age','sex']]
#print(allison)
allison = df.loc[['Allison, Master. Hudson Trevor',
                'Anderson, Mr. Harry'],
                 ['age','sex']]
allison = df.loc[['Allison, Master. Hudson Trevor',
                'Anderson, Mr. Harry'],
                 'age':'parch']
allison = df.loc['Allison, Master. Hudson Trevor':
                'Anderson, Mr. Harry',
                 'age':'parch']
allison = df.loc[
                'Anderson, Mr. Harry',
                 'age']
#print(allison)

allison = df.iloc[:7, 4:6]
#print(allison)
#print('-----------------------')
#print(df.shape[0]) # len(df.index) #
#print((df.age>50).sum())  # 布尔型索引
#print((df.survived==0).sum())
#print(df.survived.value_counts())

print(df[df.age>50])
#print(df[df>50])