'''
抓取51job上关键字是数据分析的职位，并简单作图分析
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def _salary(salary):
    '''薪资统一以月计算，取均值'''
    # 8K-12K
    salary = salary.replace('K', '')
    print(salary)
    s = salary.split('-')
    salary = (int(s[0]) + int(s[1]))/2*1000
    return round(salary)
#print(_salary('7K-12K'))


def _exp(exp):
    if exp is np.nan:# nan值不处理
        return
    if exp == '应届生' or exp == '经验不限':
        rtn = 0
    elif exp == '1年以内':
        rtn = 0.5
    else:
        rtn = int(exp[:1])
    return rtn
#print(_exp('3-5年'))



sns.set_style("whitegrid")# darkgrid , whitegrid , dark , white ,和 ticks 
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
df =  pd.read_csv(r'boss.csv', encoding='gbk')


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
df = df[df['工作地点'] ==  '北京']
plt.title('数据分析职位月薪(北京)')
bins=range(0,40000,5000) # 范围0到200，每个柱的宽度20
# hist画柱状图
plt.hist(df["薪资"],bins,color='#3333ee',width=4000) 
plt.xlabel('月薪')
plt.ylabel('计数')
plt.plot()
# 平均值
plt.axvline(df['薪资'].mean(),linestyle='dashed',color='red')
plt.show()


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
#plt.show()
#print(df.describe())
