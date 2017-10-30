import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}

df = pd.DataFrame([math, english], index=['math', 'english'])

df = df.T
dfjige = df[(df.math>=60) & (df.english>=60)]
#print(dfjige.index) # 两个都及格的学生

df = df.fillna(0)
df['total'] = df.math + df.english # 新建一列总分
df = df.total.sort_values(ascending=False) # 以总分从高到低排序
print(df)
print(df.index)

#df = df.total.sort_values() # 以总分从高到低排序
#print(list(reversed(df.index)))

df2 = pd.DataFrame(np.random.randint(5, size=(5,4)), index=df.index)
print(df2)