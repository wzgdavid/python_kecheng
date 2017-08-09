'''
抓取51job上关键字是数据分析的职位，并简单作图分析
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def _salary(salary):
    '''薪资统一以月计算，取均值'''
    # 6-8千/月 2-6万/月  2.5-5万/月  0.8-1.5万/月   150元/天   20-30万/年  

    if salary is np.nan:# nan值不处理
        return
    elif salary.endswith('万/月'):
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
        rtn = float(salary) * 21.75

    return round(rtn)

def _exp(exp):
    if exp is np.nan:# nan值不处理
        return
    if exp == '无工作经验':
        rtn = 0
    elif exp.startswith('10年'):
        rtn = 10
    else:
        rtn = int(exp[:1])
    return rtn
#print(_exp('10年以上经验'))

def _area(area):
    if area is np.nan:# nan值不处理
        return
    elif '-' in area:
        rtn =  area.split('-')[0]
    else:
        rtn = area
    return rtn


sns.set_style("whitegrid")# darkgrid , whitegrid , dark , white ,和 ticks 
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
df =  pd.read_csv(r'data_51jobs.csv', encoding='gbk')
#df = df.dropna()
df['工作地点'] = df['工作地点'].apply(_area)
df['薪资'] = df['薪资'].apply(_salary)
df['经验'] = df['经验'].apply(_exp)

#df.to_csv('data_51jobs2.csv')

# 职位数量城市分布饼图， 以dropna前的数据画
#print(df['工作地点'].value_counts())
# 各地区数量饼图
def pie1():
    n = 8
    cnt = df['工作地点'].value_counts()
    cnt = cnt.drop('异地招聘')
    print(cnt)
    labels = list(cnt.index[:n]) + ['其他']
    sizes = list(cnt.values[:n]) + [cnt.values[n:].sum()]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal') # 轴相等，即圆形
    plt.title("不同地区职位比例")
    plt.show()
#pie1()

# 各经验数量饼图
def pie2():
    cnt = df['经验'].value_counts()[:5]
    print(cnt)
    labels = pd.Series(cnt.index).apply(lambda x: str(x)+'年以上')
    sizes = cnt.values
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal') # 轴相等，即圆形
    plt.title("不同经验要求职位比例")
    plt.show()
#pie2()


df = df.dropna()
#print(df.head(20))
#print(df.shape[0])
print(df.describe())




# 全国月薪柱状分布图
# 以城市分
#df = df[df['工作地点'] ==  '深圳']
#plt.title('数据分析职位月薪(深圳)')
#bins=range(0,40000,5000) # 范围0到200，每个柱的宽度20
## hist画柱状图
#plt.hist(df["薪资"],bins,color='#3333ee',width=4000) 
#plt.xlabel('月薪')
#plt.ylabel('计数')
#plt.text(1, 10000,'sdfsdf')
#plt.plot()
## 平均值
#plt.axvline(df['薪资'].mean(),linestyle='dashed',color='red')
#plt.show()


# 主要城市盒形图
#main_cities = df['工作地点'].value_counts()[:10]
#main_cities = main_cities.drop('异地招聘')
#dfbox = df[df['工作地点'].isin(main_cities.index)]
##print(dfbox.head())
#plt.title('主要城市盒形图')
#sns.boxplot(x="工作地点", y = '薪资', data = dfbox)
#plt.ylim(0,40000)
#plt.show()



# 经验月薪盒形图
#plt.title('经验薪资盒形图')
#sns.boxplot(x="经验", y = '薪资', data = df)
#plt.ylim(0,50000)
##plt.text('sfsf')
#plt.show()


# 学历月薪盒形图
plt.title('学历月薪盒形图')
sns.boxplot(x="学历", y = '薪资', data = df)
plt.ylim(0,50000)
#plt.text('sfsf')
plt.show()
#print(df.describe())
