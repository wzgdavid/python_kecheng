'''
用chapter8中51jobs2.py抓取的csv数据，通过经验，学历，地点预测职位工资
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #画3D图
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def _salary(salary):
    '''薪资统一以月计算，取均值'''
    # 6-8千/月 2-6万/月  2.5-5万/月  0.8-1.5万/月   150元/天   20-30万/年   
    if salary.endswith('万/月'):
        salary = salary.replace('万/月', '')
        s = salary.split('-')
        rtn = (float(s[0]) + float(s[1]))*10000 / 2
    elif salary.endswith('千/月'):
        salary = salary.replace('千/月', '')
        s = salary.split('-')
        rtn = (float(s[0]) + float(s[1]))*1000 / 2
    elif salary.endswith('万/年'):
        salary = salary.replace('万/年', '')
        s = salary.split('-')
        rtn = (float(s[0]) + float(s[1]))*10000 / 2 / 12
    elif salary.endswith('元/天'):
        salary = salary.replace('元/天', '')
        rtn = float(salary) * 22.75
    #print(rtn)
    return rtn

def _exp(exp):
    if exp == '无工作经验':
        rtn = 0
    else:
        rtn = int(exp[:1])
    return rtn
#print(_exp('无工作经验'))

def _area(area):
    if '-' in area:
        rtn =  area.split('-')[0]
    else:
        rtn = area
    return rtn
#print(_area('杭州'))

df = pd.read_csv(r'..\csv\51jobs.csv', encoding='gbk')
df = df.dropna()
df = df[['工作地点','经验','学历','薪资']]

df['薪资'] = df['薪资'].map(_salary) # series用map dataframe用applymap
le = LabelEncoder()
df['学历'] = le.fit_transform(df['学历'].values)
#print(dir(le))
#print(le.inverse_transform(0))
#print(le.classes_) # encoder之后的值是这个classes_的index
df['经验'] = df['经验'].map(_exp)
df['工作地点'] = df['工作地点'].map(_area)
area_list = df['工作地点'].unique()
#print(area_list)

# 工作地点用哑变量
area = pd.get_dummies(df['工作地点'])
df = pd.concat([area, df], axis=1).drop('工作地点', axis=1)

#print(df)


X = df.drop('薪资', axis=1)
y = df['薪资']


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3)
#print(X_test)
model = LinearRegression()
model.fit(X_train, y_train)

a, b = model.intercept_, model.coef_
#print(a)
#print(b)
#y=2.668+0.0464*TV+0.192*Radio-0.00349*Newspaper

# 预测
y_pred = model.predict(X_test) 
## 打印特征与结果
#for i, y in enumerate(y_pred):
#    xi = X_test.iloc[i]
#    print(xi[xi>0], y)

xueli = list(le.classes_).index('本科')
#print(xueli)

# 自己构建一个函数，来预测具体给定的值
def predict_salary(area, xueli, exp):
    xueli = list(le.classes_).index('本科')
    x = X_test.iloc[0].copy() # 随便取一行，构建一个特征的结构
    x[:] = 0
    x['学历'] = xueli
    x['经验'] = exp
    x[area] = 1
    #print(x)
    x = x.values.reshape(1, -1)
    #print(x)
    pred = model.predict(x) 
    print(pred)
    

predict_salary('北京', '大专', 4)
predict_salary('北京', '本科', 3)
predict_salary('上海', '本科', 2)