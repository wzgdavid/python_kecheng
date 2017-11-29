import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder

# 读取51job.csv
# 1 哪个城市平均月薪
# 2 上海各学历的平均月薪

# 0.01  0.014 *100  1  5.1
#names = ['job', 'link','company','place','salary','exp','xueli']
df = pd.read_csv(r'E:\python_files\csv\51jobs.csv',
            encoding='gbk',)



def get_place(jobplace):
    #if '-' in jobplace:
    #    return jobplace.split('-')[0]
    #else:
    #    return jobplace
    return jobplace.split('-')[0] if '-' in jobplace else jobplace

#print(get_place('上海浦东'))

def get_salary(salary):
    '''0.8-1.3万/月  6-8千/月  150元/天 20-30万/年'''
    #print(salary)
    salary=str(salary)
    if '万/月' in salary:
        #print(salary)
        #salary = salary[:-3].split('-')
        salary = salary.replace('万/月','').split('-')
        rtn = (float(salary[0]) + float(salary[1]))/2*10000
    elif '千/月' in salary:
        salary = salary[:-3].split('-')
        rtn = (float(salary[0]) + float(salary[1]))/2*1000
    elif '元/天' in salary:
        rtn = float(salary[:-3]) * 21.75
    elif '万/年' in salary:
        salary = salary[:-3].split('-')
        rtn = (float(salary[0]) + float(salary[1]))/2*10000/12
    else:
        rtn = None
    return rtn
#print(get_salary('20-30万/年'))


df= df.dropna()
df['地区'] = df['工作地点'].apply(get_place)
df['月薪'] = df['薪资'].apply(get_salary)
#df.to_csv('job.csv')
#print(df.head())
# df.groupby 返回一个groupby对象，这个对象当做dataframe
mean_salary = df.groupby(['地区','学历'])['月薪'].mean()
print(mean_salary)
#print(mean_salary.idxmax(), mean_salary.max())
#sorted_mean_salary = mean_salary.sort_values()
#print(sorted_mean_salary)
#

# 2 上海各学历的平均月薪
df_shanghai = df[df['地区'] == '上海']
mean_salary = df_shanghai.groupby('学历')['月薪'].mean()
print(mean_salary)


# 使用labelencoder
#le = LabelEncoder()
#df['学历'] = le.fit_transform(df['学历'].values)
#print(le.classes_)
#print(df['学历'])
#print(le.inverse_transform(7))

# 哑变量
# 把df['学历']用哑变量表示
xueli = pd.get_dummies(df['学历'])
# 拼接到原来的dataframe
df = pd.concat([df, xueli], axis=1)
df.to_csv('tmp.csv')
#print(xueli)
#X = 

def predict_salary(xueli, place, exp):
    

    return salary