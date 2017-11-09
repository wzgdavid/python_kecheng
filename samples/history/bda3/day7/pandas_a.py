# pandas 主要有三种类型 
# 对应于numpy 一维     二维       三维
#            Series   DataFrame   Panel
#     Pan   Da   S

import numpy as np
import pandas as pd
scores = [89,34,12,67,78]
english_scores = [89,56,12,98,12]
arr = np.array(scores)
s = pd.Series([1, 2, 3, 3]) # 构建一个series
#print(s.index)
#print(s, type(s))
# 给定一个索引
s = pd.Series(scores, index=list('abedc'))
#print(s, s['b'], s[1])
## values属性返回ndarray
#print(s.values, type(s.values))
#print(s.shape)
#for name in s.index:
#    print(name)
s2 = pd.Series(english_scores, index=s.index)
print(s2)
print(s2['a':'d'])  # 用标签 都包含
print(s2[0:4])  # 4不包含
#s2 = pd.Series(english_scores,index=[1,2,3,4,5])
#print(s2)
#print(s2[0:4])
#print(s2.mean())
#print(s2[ [0,1,3] ]) # 
#print(s2[ ['a','e','c','d','a'] ]) # 选择多个

#s2['b':'c'] = 99
#print(s2)

bc = s2['b': 'c'].copy() # 
#print(bc)
#s2[:] = 0
#print(bc)
print(s2.unique()) # 返回的数组

print(s2 >= 60)
print(s2[s2>=60]) # 布尔索引
s60 = s2[s2>=60]
#print(s60[0:99]) # 
#np.sqrt(s60)
print('c' in s60)

scores_dict = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
scores = pd.Series(scores_dict)

#if n in scores: # 判断的是series的索引
#for n in scores: # 迭代的是series的值
#
# 把series（索引没有重复）、转成字典
new_scores = {}
for name in scores.index: # 
    new_scores[name] = scores[name]
print(new_scores)
# 生成式
new_scores2 = {name:scores[name] for name in scores.index}
print(new_scores2)
new_scores3 = dict(zip(scores.index, scores.values))
print(new_scores3)

print('------------------------------------')
print(scores)

scores.index = list('abcd')
print(scores)
print(scores.value_counts())

scores_dict = {'cat': None, 'tom': 666, 'pig': 555, 'moon': 555}
s = pd.Series(scores_dict)
print(s)
print(s.isnull())
print('-----------')
print(s.notnull())
print('-----------')
print(np.isnan(s))