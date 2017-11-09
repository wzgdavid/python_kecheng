import numpy as np
import pandas as pd

users = pd.read_csv(r'E:\python_files\csv\users.csv')
u20 = users.head(20)
#print(u20)
# 几条数据
users.shape[0] 
# 几个字段  fields
users.shape[1] 
# 机器学习中称为 特征 features
users.columns 
users.index

# 5
users.occupation
# 6 有多少不同职位
# unique()方法返回array
print(users.occupation.unique().size)

# 7 最多的职位
a = users.occupation.value_counts()
print(a)
# 8 所有人的平均年龄
users.age.mean()
# 9 所有男性的平均年龄
mage = users.age[users.gender=='M'].mean()
mage = users[users.gender=='M'].age.mean()
print(round(mage, 1))


# 练习2
# 都及格的学生
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}
df = pd.DataFrame([math, english], index=['math', 'english'])
df = df.T
print(df)

dfjige = df[ (df.math>=60) & (df.english>=60) ]
print(dfjige.index)

# 总分从高到低打出学生名字
df = df.fillna(0) # 缺考作为0分
df['total'] = df.math+df.english
print(df)
df = df.sort_values(by='total', ascending=False)
print(df.index)