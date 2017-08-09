'''
用
chapter8中51jobs2.py
抓取的csv数据，通过经验，学历，地点预测职位工资
用LabelEncoder
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression


def get_salary(origin):
    '''# 0.5-1万/月 7-9千/月  20-30万/年  500元/天    
    统一以月薪计算，取平均
    '''
    if origin.endswith('万/月'):
        origin = origin.replace('万/月', '')
        splited = origin.split('-')
        #print(splited)
        rtn = (float(splited[0]) + float(splited[1] ))/2*10000
    elif origin.endswith('千/月'):
        origin = origin.replace('千/月', '')
        splited = origin.split('-')
        rtn = (float(splited[0] ) + float(splited[1] ))/2*1000
    elif origin.endswith('万/年'):
        origin = origin.replace('万/年', '')
        splited = origin.split('-')
        rtn = (float(splited[0] ) + float(splited[1] ))/12/2*10000
    elif origin.endswith('元/天'):
        #origin = origin.replace('元/天', '')
        #splited = origin.split('-')
        rtn = float(origin.replace('元/天', ''))*21.75
    return rtn

#print(get_salary('500元/天')) #8000

def get_area(origin):
    if '-' in origin:
        rtn = origin.split('-')[0]
    else:
        rtn = origin
    return rtn
#print(get_area('北京'))

def get_exp(origin):
    if origin == '无工作经验':
        rtn = 0
    else:
        rtn = int(origin[:1])
    return rtn
#print(get_exp('5-7年经验'))


df = pd.read_csv(r'E:\python_files\csv\51jobs.csv', encoding='gbk')
df = df.dropna()
df = df[['工作地点', '经验', '学历', '薪资']]
#print(df.head(10))
df['薪资'] = df['薪资'].apply(get_salary)
df['经验'] = df['经验'].apply(get_exp)
df['工作地点'] = df['工作地点'].apply(get_area)
#print(df.head(10))
print(df['工作地点'].value_counts())
le_area = LabelEncoder()
df['工作地点'] = le_area.fit_transform(df['工作地点'].values)

print(le_area.classes_)
print(le_area.inverse_transform(6))
le_xueli = LabelEncoder()
df['学历'] = le_xueli.fit_transform(df['学历'].values)
#print(df.head(10))

X = df[['工作地点', '经验', '学历']]
y = df['薪资']

model = LinearRegression()
model.fit(X, y)
#print(model.predict([[4, 3, 1]]))
#print(model.predict([[4, 3, 2]]))
#print(model.predict([[2, 3, 1]]))
#print(model.predict([[3, 3, 1]]))
#print(model.predict([[2, 2, 1]]))
#print(model.predict([[2, 3, 1]]))

#predict_salary('北京','大专',3)

def predict_salary(area, xueli, exp):
    # labelencoder后的数字就是这个类别在classes_中的下标
    area = list(le_area.classes_).index(area)
    xueli = list(le_xueli.classes_).index(xueli)
    n = model.predict([[area, xueli, exp]])
    print(n)

predict_salary('北京','大专',1)
predict_salary('北京','本科',1)
predict_salary('北京','硕士',1)

predict_salary('北京','大专',2)
predict_salary('北京','本科',2)
predict_salary('北京','硕士',2)


