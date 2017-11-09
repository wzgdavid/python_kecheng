import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.linear_model import LinearRegression


def get_area(area):
    '''取得工作地点中的城市   如：北京-海淀区 -----》北京'''
    if '-' in area:
        rtn =  area.split('-')[0]
    else:
        rtn =  area
    return rtn

def get_exp(exp):
    '''2年经验  3-4年经验 10年以上经验  无工作经验 '''
    if exp=='无工作经验':
        rtn = 0
    elif exp=='10年以上经验':
        rtn = 10
    #elif '-' in exp:
    #    rtn = exp[:1]
    else:
        rtn = exp[:1]
    return rtn
#print(get_exp('无工作经验'))

def get_salary(salary):
    '''15-20万/年 1.3-1.8万/月 3-4.5千/月 220元/天'''
    if salary.endswith('万/年'):
        salary = salary.replace('万/年', '')
        nums = salary.split('-')
        rtn = (float(nums[0]) + float(nums[1]))/2/12*10000
    elif salary.endswith('万/月'):
        salary = salary.replace('万/月', '')
        nums = salary.split('-')
        rtn = (float(nums[0]) + float(nums[1]))/2*10000
    elif salary.endswith('千/月'):
        salary = salary.replace('千/月', '')
        nums = salary.split('-')
        rtn = (float(nums[0]) + float(nums[1]))/2*1000
    elif salary.endswith('元/天'):
        salary = salary.replace('元/天', '')
        rtn = float(salary) * 21.75
    return rtn
#print(get_salary('220元/天'))

df = pd.read_csv(r'E:\python_files\csv\51jobs.csv', encoding='gbk')
df = df.dropna()
#print(df.head())
df = df[['工作地点', '经验', '学历', '薪资']]

#  特征处理
df['工作地点'] = df['工作地点'].map(get_area)
df['经验'] = df['经验'].apply(get_exp)
df['薪资'] = df['薪资'].apply(get_salary)
le_area = LabelEncoder()
#le_xueli = LabelEncoder()
df['工作地点'] = le_area.fit_transform(df['工作地点'])
#df['学历'] = le_xueli.fit_transform(df['学历'])
xueli = df['学历'].copy()
lst = ['中专', '高中', '大专','本科','硕士']
xueli[xueli=='中专']=0
xueli[xueli=='高中']=1
xueli[xueli=='大专']=2
xueli[xueli=='本科']=3
xueli[xueli=='硕士']=4
df['学历'] = xueli
X = df[['工作地点', '经验', '学历']]
y = df['薪资']

#print(df.head())

#print(df.head())
model = LinearRegression()
model.fit(X, y)

#print(model.predict([[6,5,2]]))

def predict_salary(area, xueli, exp):
    #print(le_area.inverse_transform(0))
    areaidx = list(le_area.classes_).index(area)
    #print(areaidx)
    #xueliidx = list(le_xueli.classes_).index(xueli)
    xueliidx = list(lst).index(xueli)
    pred = model.predict([[areaidx, xueliidx, exp]])
    print(pred)

#predict_salary('上海', '高中', 1)
predict_salary('上海', '大专', 1)
#predict_salary('北京', '本科', 1)
predict_salary('上海', '本科', 1)
predict_salary('上海', '硕士', 1)
predict_salary('北京', '大专', 1)
#predict_salary('北京', '本科', 1)
predict_salary('北京', '本科', 1)
predict_salary('北京', '硕士', 1)
#predict_salary('上海', '本科', 1)
#
#
if __name__ == '__main__':
    pass
    #area = _get_area('北京-海淀区')
    #print(area)