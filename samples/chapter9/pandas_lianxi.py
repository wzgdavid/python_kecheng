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