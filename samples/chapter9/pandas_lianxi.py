import numpy as np
import pandas as pd
'''
1, 有两门课的成绩，打印出两门课都及格的学生名字
'''
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}
df = pd.DataFrame([math,english], index=['math', 'english'])
df= df.T
#print(df)
# way 1
df = df[df>=60].dropna()
print(df.index)


# way 2
df = df[(df.math>=60)&(df.english>=60)]

print(df.index)

'''
2, 以总分由高到低打印出学生名字，缺考为零分
'''
df = pd.DataFrame([math,english], index=['math', 'english'])
df= df.T
df = df.fillna(0)
df['total'] = df['math'] + df['english']
df = df.sort_values(by='total', ascending=False)
[print(n) for n in df.index]

# 课堂边做
# https://github.com/guipsamora/pandas_exercises/blob/master/01_Getting_%26_Knowing_Your_Data/Occupation/Exercise_with_Solution.ipynb
# 
#users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')
#users.to_csv('users.csv')
# 这些练习用user.csv做
users = pd.read_csv('users.csv')
# 1 得到，前20条记录
users.head(20)
# 2 这个数据集一共有几条数据
users.shape[0]
# 3 一共有几个列
