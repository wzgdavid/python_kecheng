'''可作为回家作业
探索数据，观察幸存者和哪个因素关系大点
'''
'''
字段含义
survived => 是否获救 0 = No, 1 = Yes
pclass => 乘客等级(1/2/3等舱位)
bame => 乘客姓名
sex => 性别
age => 年龄
sibSp => 堂兄弟/妹个数
parch => 父母与小孩个数
ticket => 船票信息
fare => 票价
cabin => 客舱
embarked => 登船港口  C = Cherbourg, Q = Queenstown, S = Southampton
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set_style("darkgrid")# darkgrid , whitegrid , dark , white ,和 ticks 

plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文

df =  pd.read_csv(r'..\csv\titanic.csv')

# 获救情况
#df.survived.value_counts().plot(kind='bar') # 1 用plt画
#sns.countplot(data=df, x='survived')       # 2 用seaborn
#plt.show()
#画饼图
#survived = df.survived[df.survived==1].count()
#not_survived = df.survived[df.survived==0].count()                                       
#print(survived,not_survived)
#plt.pie([survived, not_survived],
#        labels=['Survived','Not Survived'],
#        autopct='%1.0f%%')
#plt.show()

# 男女人数
#sns.countplot(data=df, x='survived')
#plt.show()

# 乘客等级
#sns.countplot(data=df, x='pclass')
#plt.show()

# 登船港口人数
#sns.countplot(data=df, x='embarked')
#plt.show()

# 年龄分布
#df.age.plot(kind='kde')
#df.age[df.pclass==1].plot(kind='kde')
#df.age[df.pclass==2].plot(kind='kde')
#df.age[df.pclass==3].plot(kind='kde')
#plt.legend(['所有', 'pclass 1','pclass 2','pclass 3'])
#plt.show()

# 男女分别获救情况  和前面一样，只是在筛选后的df上操作
#male = df[df.sex=='male']
#plt.subplot(121)
#sns.countplot(data=male, x='survived')  
#plt.title('male')
#female = df[df.sex=='female']
#plt.subplot(122)
#sns.countplot(data=female, x='survived') 
#plt.title('female')
#plt.show()