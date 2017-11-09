import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']


df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')
# 列名都改为小写
df.columns = df.columns.str.lower()

#print(df)
df = df.groupby('generation').hp.mean()
print(df)

#print(df.head(40))z
# legendary宠物的数量
#print(df[df.legendary==True].shape[0])
# 
#df = df.set_index(df.name) # set_index('name')
df = df.set_index(df.name)
df = df.drop('name', axis=1)
#print(df.head())
Pikachu = df.loc['Pikachu'] 
#print(Pikachu)

# 
type1 = df['type 1'].unique()
type2 = df['type 2'].dropna().unique()
# 用set
all_types = set(type1) | set(type2)
#print(all_types)

# 用numpy的集合逻辑
#np.union1d([type1, type2])
#print(np.union1d(type1, type2))

fire_dragon = df[ ((df['type 1']=='Fire') & (df['type 2']=='Dragon')) 
                 | ((df['type 2']=='Fire') & (df['type 1']=='Dragon')) 
]

#print(fire_dragon)

#print(df['hp'].idxmin(), df['hp'].min())

# 某类别中某属性最高的
type_fire = df[ (df['type 1']=='Fire') |  (df['type 2']=='Fire')]
#print(type_fire['attack'].idxmax())
#print(type_fire.sort_values(by='attack')[-3:]) # tail

# 某类型有多少种
type1 = df['type 1'].value_counts()
type2 = df['type 2'].value_counts()
types = type1 + type2
#print(types['Fire'])
#
#print('------------------------')
#strong = df.sort_values(by='total', ascending=False)
#strong = strong.drop_duplicates(subset=['type 1'], keep='first')
#print(strong.head(10))

# 画图
# plt.plot(
def hist():
    # 范围
    bins = range(0, 200, 20) # start end  width
    # 画柱状图
    plt.hist(df.attack, bins, width=16)
    plt.xlabel('攻击力')
    plt.ylabel('个数', rotation=0)
    # axvline 画垂直线  axhline 水平线
    #plt.axvline(40, color='red')
    plt.axvline(df.attack.mean(), color='red', linestyle='dashed')
    plt.show()

#hist()
#
#
#(1,1)  (1,2) (3,3)
# scatter(所有X的值，所有y的值)
#plt.scatter([1,1,3], [1,2,3])
#plt.xlim(0, 5) # 坐标轴的范围
#plt.ylim(0, 5)
#plt.show()
# 散点图
def scatter():
    fire = df[ df['type 1'] == 'Fire' ]
    water = df[ df['type 1'] == 'Water' ]
    grass = df[ df['type 1'] == 'Grass' ]
    plt.scatter(fire.hp, fire.speed, label='fire', color='r', marker='*')
    plt.scatter(water.hp, water.speed, label='water',color='#3344ff', s=10)
    #plt.scatter(grass.hp, grass.speed, label='grass',color='#669856', marker='+')
    plt.xlabel('hp')
    plt.ylabel('speed')
    plt.legend()
    plt.show()

#scatter()


def jointplot():
    fire = df[ df['type 1'] == 'Fire' ]
    water = df[ df['type 1'] == 'Water' ]
    sns.jointplot(x=fire.attack, y=fire.defense)
    sns.jointplot(x=water.attack, y=water.defense)
    plt.show()

#jointplot()

#sns.set_style('darkgrid') # white whitegrid dark darkgrid 
#print(df['type 1'].value_counts())
#sns.countplot(x=df['legendary']) # 计数图
#plt.show()

# 盒形图都是 真实值
def boxplot():
    df2 = df[['hp',  'attack',  'defense', 
        'sp. atk', 'sp. def', 'speed']]
    sns.boxplot(data=df2, whis=3)
    #print(s.hp.sort_values().values)
    plt.show()

#boxplot()
#sns.boxplot(df.hp)
#print(df.hp.sort_values().values)
#plt.show()

def boxplot2():
    sns.boxplot(x='generation', y='total', data=df)
    #print(s.hp.sort_values().values)
    plt.show()
#boxplot2()

def boxplot3():
    # 筛选一下数据，
    data = df[df.generation.isin([1,2])]
    data = data[data['type 1'].isin(['Fire', 'Water'])]
    #
    sns.violinplot(x='type 1', y='speed', 
        data=data, hue='generation', split=True)
    plt.show()
#boxplot3()

df = df.groupby(['generation', 'type 1']).count().reset_index()
df = df[['generation','type 1','total']]
df = df.pivot(
        index='generation', 
        columns='type 1',
        values='total'
    )
df = df[['Fire','Water','Dragon']]
#print(df)
#df.plot(marker='*')
#plt.show()

