'''
针对零基础的同学，应该再简单点，先让他们有编程的感觉
这里的零基础是指总来没接触过任何编程
'''
# 计算这个列表里有几个1
lst = [1,1,2,2,1,1,2,3,4,2,1]
cnt = 0
for n in lst:
    if n == 1:
        cnt += 1
print(cnt)



#输入的字典 = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
#颠倒字典中的键和值 {'sdf':'1ff3'}
#写一个函数返回{123: 'cat', 666: 'tom', 555: ['pig', 'moon']}
#写一个函数，接收一个字典，返回一个键值颠倒字典，
#如果值不重复的话，直接键值颠倒
#如果值重复的话，把原来字典的键放在列表里
#做一下异常处理，检查这个参数是不是一个字典
#然后检查key是不是字符串，value是不是数字
#一个不符合就整个不处理

# 简化版本，不用做异常处理 (其实还是不适合初学者)
def reverse_keyvalue(dct):
    # 检查完毕
    dict_return = {}
    for key, value in dct.items():
        if value not in dict_return:
            dict_return[value] = key
        else:
            dict_return[value] = [dict_return[value]]
            dict_return[value].append(key)
    print(dict_return)
    return dict_return
dct = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
reverse_keyvalue(dct)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# pandas 作业
# 用anjuke.csv

plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
df =  pd.read_csv(r'E:\python_files\csv\anjuke.csv', encoding='gbk')

# 1 生成新的一列面积，值只包含数字
def get_area(area):
    return area.replace('平米', '')
df['面积(平米)'] = df['面积'].apply(get_area).astype(int)

# 2 筛选出浦东新区，精装修，朝南，面积在30到50平米的房源,月租在4000元以内

pudong = (df['区域1'] == '浦东新区')
jingzhuangxiu = (df['装修'] == '精装修')
chaoxiang = (df['朝向'] == '南')
gt30lt50 = ( (df['面积(平米)'] > 30) & (df['面积(平米)'] < 50) )
lt4000 = ( df['租金'] < 4000 )
a = df[pudong & jingzhuangxiu & chaoxiang & gt30lt50 & lt4000]
#print(a)

# 每个区的平均单价  （租金/面积）
df['租金单价'] = df['租金'] / df['面积(平米)']

#print(df['租金单价'])
#zjdj = df.groupby('区域1')['租金单价'].mean()
#zjdj = zjdj.sort_values()
##zjdj.plot(type='bar')
#sns.barplot(x=zjdj.index, y=zjdj.values,hue=zjdj.index)
#plt.title('各区租金单价')
#plt.show()

zjdj = df.groupby(['区域1', df['朝向']=='南' ])['租金单价'].mean()
print(zjdj)

#zjdj.plot(type='bar')

#sns.barplot(
#    x=zjdj.index, 
#    y=zjdj.values,
#    hue=zjdj.index.labels[1]
#)
#plt.xlabel(rotation=90,s=20)
#plt.title('各区租金单价')
#plt.show()
#print(zjdj.index.labels[1])
#print(zjdj['崇明区'][False]) # 复合索引 选一个值