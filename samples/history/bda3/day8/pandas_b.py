import numpy as np
import pandas as pd

np.random.seed(5)
df = pd.DataFrame( np.random.randint(1,10,size=(10, 4)) )
df.columns = list('ABCD')
#print(df.values.dtype)
df.iloc[[2,4,6], [1,3]] = np.nan
#print(df)
# 丢弃缺失值
#df = df.dropna(axis=1)
#print(df)

# 填充缺失值
#df = df.fillna(0)
# 针对不同的列填充缺失值
#df = df.fillna( {'B':111, 'D':999} )
# 填充平均值
dct = {'B':df.B.mean(), 'D':df.D.mean()}
df = df.fillna( dct )

# 保留小数
df.B = np.round(df.B, 1)
df.D = np.round(df.D, 1)
print(df)


print('------------------------------')
# 相同索引的项分别计算，没有对应的索引返回nan
s1 = pd.Series([1,2,3,4], index=list('ABCd'))
s2 = pd.Series([1,2,3,4,5,6], index=list('ccaadd'))
#print(s1 * s2)

# dataframe 和 series 相加
# +  都是按行计算
#print(df + df.ix[9]) # df.ix[9] index 是 ABCD
#print(df + s1)

df2 = pd.DataFrame( np.random.randint(1,10,size=(5, 3)) )
df2.columns = list('ABC')
df3 = df + df2
#print(df3)

#print( df.add(df2, fill_value=0) )

#print(df>4)
#print(df[df>4]) # 形状不变
#print(df[df.A>4])
#arr = df.values
#print(arr[arr>4]) #ndarry  返回一维数组
#     A    B    C    D
#0  NaN  7.0  7.0  NaN
#1  9.0  5.0  8.0  NaN
#2  NaN  NaN  NaN  NaN
#3  8.0  NaN  NaN  5.0
#4  7.0  NaN  NaN  NaN
#5  8.0  NaN  6.0  NaN
#6  NaN  NaN  5.0  NaN
#7  NaN  5.0  7.0  NaN
#8  NaN  NaN  NaN  6.0
#9  8.0  5.0  NaN  NaN
#[ 7.  7.  9.  5.  8.  8.  5.  7.  8.  6.  5.  5.  7.  6.  8.  5.]


#df.D = df.D +1
def add_one(x):
    return x+1
#df.D = df.D.apply(lambda x: x+1)
df.D = df.D.apply(add_one) # add_one 应用到df.D的每个元素上
df = df.applymap(add_one)  # add_one 应用到df的每个元素上
# 应用在df的行或者列上
#df['max-min'] = df.apply(lambda x:x.max()-x.min(), axis=1)
def max_min(x):
    return x.max() - x.min()
df['max-min'] = df.apply(max_min, axis=1)
print(df)

users = pd.read_csv(r'E:\python_files\csv\users.csv')
def age_range(age):
    if 0<age<=8:
        return '儿童'
    elif age<14:
        return '青少年'
    elif age<30:
        return '青年' 
    elif age<55:
        return '中年'   
    else:
        return '老年' 
def foo(occ):
    return occ[:3]
users['年龄段'] = users.age.apply(age_range) 
users['foo'] = users.occupation.apply(foo)



yidong = ('857', '940', '320', '435') #移动
liantong = ('152', '981', '913', '520') #联通
dianxin = ('100', '907', '303', '292') #电信
users['号码段'] = users.zip_code.apply(lambda x:x[:3])
def get_yunyingshang(x):
    if x in yidong:
        return '移动'
    elif x in liantong:
        return '联通'
    elif x in dianxin:
        return '电信'
    else:
        return '其他'

def get_运营商(x):
    dct = {yidong: '移动',
            liantong: '联通',
            dianxin:'电信'
           }
    for key in dct:
        if x in key:
            return dct[key]
    #return [dct[key] for key in dct if x in key][0]

users['运营商'] = users['号码段'].apply(get_运营商)
# 丢弃处理过程中的字段
users = users.drop(['foo', '号码段'], axis=1)
#users.to_csv('usersage.csv')
print(users['运营商'].value_counts())