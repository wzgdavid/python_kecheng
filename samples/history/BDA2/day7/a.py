import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D #画3D图
plt.rcParams['font.sans-serif'] = ['SimHei']
sns.set_style("darkgrid")# darkgrid , whitegrid , dark , white ,和 ticks 


df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')


df.columns = df.columns.str.lower() # 列名都转成小写
df = df.drop('#', axis=1)  # 去掉不需要的列
df = df.set_index('name')  # name属性作为index
#print(df.head(9))
#选出legendary的宠物
legendary = df[df.legendary==True]
#print(legendary)

# 选出某个宠物
Pikachu = df.loc['Pikachu']
#print(Pikachu)

# 查看所有类型
type1 = df['type 1'].unique()
#print(type1)
type2 = df['type 2'].unique()
#print(type2)
#type2 = df['type 2'].dropna()
#用set
alltype = set(type1) | set(type2) - set([np.nan])
print(len(alltype))

# 用numpy的集合操作
type1 = df['type 1'].unique()
type2 = df['type 2'].dropna() # union1d的时候需要非nan的值
type2 = type2.unique()
alltype = np.union1d(type1, type2)
print(len(alltype))

# 选出既是fire又是dragon的宠物
#fired = ((df['type 1']=='Fire') & (df['type 2']=='Dragon'))
#dfire = ((df['type 1']=='Dragon') & (df['type 2']=='Fire'))
#firedragon = df[fired | dfire]
#print(firedragon)


#typefd = ['Fire', 'Dragon']
##print(type(df))
#firedragon2 =  df[df['type 1'].isin(typefd) & df['type 2'].isin(typefd)]
#print(firedragon2)

# 找出HP最厚的宠物
#df.hp.max()
#print(df.sort_values(by='hp', ascending=False).ix[0])
#print(df[df.hp==df.hp.max()])
#print(df.ix[df.hp.idxmax()])

# 总属性值最高的3个
totalhigh = df.sort_values(by='total', ascending=False).head(3)
#print(totalhigh)

# type 1是Fire类型中攻击力最高的宠物
fire = df[(df['type 1']=='Fire') | (df['type 2']=='Fire')]
fire = fire.sort_values(by='attack', ascending=False)
#print(fire)
#print(fire.ix[fire.attack.idxmax()])

# 计算每个类型数量
type1 = df['type 1'].value_counts()
type2 = df['type 2'].value_counts()
typecnt = type1 + type2
#print(typecnt.sort_values())

#print(df.groupby(by='type 1').sum())

#print(typecnt['Fire'])

# 每个类型中total最高的

strong = df.sort_values(by='total', ascending=False)
#print(strong)
strong = strong.drop_duplicates(subset=['type 1'], keep='first')
#print(strong)

df['type'] = df['type 1']  # 新建一列，type，数据和type 1 一样
#print(df.columns)
need_drop = ['type 1', 'type 2']  # 把 type 1 和 type 2 drop掉
type1 = df.drop(need_drop, axis=1)
#print(type1.columns)
df['type'] = df['type 2']
type2 = df.drop(need_drop, axis=1)
#print(type2.columns)

#print(type1.shape)
#print(type2.shape)
# type1 type2 并成一个dataframe
concatlist = [type1, type2]
newdf = pd.concat(concatlist)
#print(newdf.shape)

strong = newdf.sort_values(by='total', ascending=False)
#print(strong)
strong = strong.drop_duplicates(subset=['type'], keep='first')
#print(strong.head())


#dragon = df[df['type 1']=='Dragon']
def draw_hist():
    #         第1， 2 个参数横坐标范围， 第三个参数每个柱子代表的范围
    bins = range(0, 90, 10)
    flying = df[df['type 1']=='Flying']
    #plt.hist(df.hp, bins, width=9, color='#3333ee')
    plt.hist(flying.defense, bins, width=9, color='#3333ee')
    #plt.plot()
    #plt.title('所有宠物攻击力分布')
    plt.xlabel('HP')
    plt.ylabel('计数', rotation=0)
    # axvline画垂直线， axhline水平线
    plt.axvline(df.hp.mean(), color='red', linestyle='dashed')
    #plt.savefig('temp.png')
    plt.show() # 显示图片
#draw_hist()

def draw_scatter():
    dragon = df[df['type 1']=='Dragon']
    bug = df[df['type 1']=='Bug']
    grass = df[df['type 1']=='Grass']
    plt.scatter(dragon.attack, dragon.defense, label='dragon', color='R')
    plt.scatter(bug.attack, bug.defense, label='bug', color='black')
    plt.scatter(grass.attack, grass.defense, label='grass', color='green')
    plt.xlabel('攻击力')
    plt.ylabel('防御力', rotation=0)
    plt.legend()
    plt.show()
#draw_scatter()


def draw_jointplot():
    data = df[df['type 1']=='Water']
    g = sns.jointplot(data=data, x='attack', y='defense')
    g.set_axis_labels('attack', 'defense')
    plt.show()
#draw_jointplot()

#sns.countplot(x='generation', data=df)
#plt.show()

def draw_pie():
    labels = 'Water', 'Normal', 'Flying', 'Grass', 'Psychic', 'Bug', 'Ground', 'Fire', 'Poison', 'Rock', 'Fighting', 'Other' 
    sizes = [126, 102, 101, 95, 90, 72, 67, 64, 62, 58, 53, 324]
    explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
#draw_pie()

#print(df.describe())

def draw_boxplot():
    needdrop = ['generation', 'total', 'legendary']
    df2 = df.drop(needdrop,axis=1)
    sns.boxplot(data=df, x='type 1', y='defense')
    plt.show()
#draw_boxplot()

def draw_violinplot():
    needdrop = ['generation', 'total', 'legendary']
    df2 = df.drop(needdrop,axis=1)
    sns.violinplot(data=df, x='type 1', y='defense')
    plt.show()
#draw_violinplot()

def draw_violinplot2():
    data = df[df['generation'].isin([1,2])]
    data = data[data['type 1'].isin(['Fire', 'Water', 'Grass', 'Dragon'])]
    sns.violinplot(x="type 1", y="total", hue="legendary", data=data, split=False)
    plt.show()
#draw_violinplot2()

def swarmplot():
    # 每个类型的类别散布图
    top_types=df['type 1'].value_counts()[:10]
    # 取出数量最多的类型
    df1=df[df['type 1'].isin(top_types.index)]
    # 每一点代表一个宠物
    sns.swarmplot(x='type 1',y= 'total', data=df1, hue='generation')
    # 均值线
    plt.axhline(df1['total'].mean(),color='red',linestyle='dashed')
    plt.show()
#swarmplot()


def draw_pivot():
    sortlist = ['generation', 'type 1']
    a = df.groupby(by=sortlist).count().reset_index()
    selected = ['generation', 'type 1', 'hp']
    a = a[selected]
    #print(a)
    a = a.pivot(index='generation', columns='type 1', values='hp')
    #print(a)
    a.plot(marker='+')
    plt.show()
#draw_pivot()

def draw_3dscatter():
    lst = ['Water', 'Fire']
    #c = [1,0,0,0,0,1,1,1,1,0,0,1,3,3,3,3,2,]
    #values = df['type 1'].values
    #values = np.where(values=='Water',2, 3)
    #print(type(values))
    fire = df[df['type 1'].isin(lst)]
    sd = plt.figure().add_subplot(111, projection = '3d')
    sd.set_xlabel('attack')  
    sd.set_ylabel('defense')  
    sd.set_zlabel('hp') 
    sd.scatter(fire.attack, fire.defense, fire.hp)
    plt.show() 
#draw_3dscatter()