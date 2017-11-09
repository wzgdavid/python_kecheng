import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文



df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')
df.columns = df.columns.str.lower()
#print(df.head())
#print(df[df.legendary==True])
df = df.set_index(df.name)

#df = df.drop(['name','#'], axis=1)
df = df.drop(['#'], axis=1)
#print(df.head())
#print(df.loc['Pikachu'])
#type1 =v df['type 1'].unique()
#type2 = df['type 2'].unique()
#print(type1)
#print(type2)
fd1 = (df['type 1']=='Water') & (df['type 2']=='Dragon')
fd2 = (df['type 2']=='Water') & (df['type 1']=='Dragon')
fire_dragon = df[fd1 | fd2]
#print(fire_dragon)
#print(df.hp.max())
#print(df.hp.idxmax())

#print(df.head())
#total3 = df.total.sort_values(ascending=False).head(3)
#print(total3)
#fire1 = df[(df['type 1']=='Fire') | (df['type 2']=='Fire')].sort_values(by='attack', ascending=False).head(1)
#print(fire1)

#type1cnt = df['type 1'].value_counts()
#type2cnt = df['type 2'].value_counts()
#typecnt = type1cnt + type2cnt
#print(typecnt.sort_values())

#strong = df.sort_values(by='total', ascending=False)
#print(strong)
#strong = strong.drop_duplicates(subset=['type 1'], keep='first')
#print(strong)


#print(t1.head())
#df['type'] = df['type 1']
#t1 = df.drop(['type 2', 'type 1'], axis=1)
#df['type'] = df['type 2']
#t2 = df.drop(['type 2', 'type 1'], axis=1)
#print(df.shape[0])
#t2 = df.drop(['type 1'], axis=1)
#t3 = pd.concat([t1, t2])
#print(t3.head())
#print(t3.shape[0])
#strong = t3.sort_values(by='total', ascending=False)

#strong = strong.drop_duplicates(subset=['type'], keep='first')
#print(strong)

def hist1():
    bins = range(0,260,20)
    plt.hist(df['hp'], bins, rwidth=0.8)
    plt.xlabel('攻击力')
    plt.ylabel('个数')
    
    plt.axvline(df['hp'].mean(), linestyle='dotted', color='red')
    #plt.hist(df['attack'], bins)
    #plt.plot()
    #help(plt.hist)
    plt.show()
#hist1()

def scatter1():
    fire = df[(df['type 1']=='Fire') | (df['type 2']=='Fire')]
    flying = df[(df['type 1']=='Flying') | (df['type 2']=='Flying')]
    #plt.scatter([1,4,6],[3,5,3])
    #(1,3) (4, 5)  (6, 3)
    plt.scatter(fire.speed, fire.defense, color='R', label='Fire', marker='X')
    plt.scatter(flying.speed, flying.defense,color='B', label='Flying', marker='o')
    plt.axvline(flying.speed.mean(), linestyle='dotted', color='red')
    plt.axvline(fire.speed.mean(), linestyle='dotted', color='green')
    plt.xlabel('speed')
    plt.ylabel('防御')
    plt.savefig('fireflying.png')
    plt.legend()
    plt.show()
#scatter1()
#print(dir(plt))
#help(plt.axvline)

def pie1():
    label = 'water', 'normal','flying','grass','psychic','bug','ground','fire'
    size = 126,102,101,95,90,72,67,64
    explode = 0,0,0.1,0,0.2,0,0,0
    plt.pie(size, explode=explode,labels=label,autopct='%1.2f%%')
    plt.axis('equal')
    plt.show()
#pie1()
#0,1,2,3,4,5,6,7,8,9,10
#print(df.describe())
#df2 = df.drop(['generation', 'total', 'legendary'], axis=1)
#sns.boxplot(data=df2, whis=1.5)
#print(df2.describe())
#plt.show()

#sns.boxplot(x='type 1',y='total', data=df)
#plt.ylim(0,150)
#plt.show()

#top_types=df['type 1'].value_counts()[:5]
#print('Water' in top_types)
#df1 = df[df['type 1'].isin(top_types.index)]
#
#sns.swarmplot(x='type 1',y='total', data=df,hue='generation')
##plt.ylim(0,150)
#plt.show()


#df = pd.DataFrame(np.random.randint(3,size=(9,2)))
#df.plot()
#print(df)
#plt.show()

a = df.groupby(['generation', 'type 1']).count().reset_index()
#print(a.head())
#print(a.reset_index())
a = a[['generation', 'type 1', 'total']]
#print(a)
a = a.pivot(index='generation', columns='type 1', values='total')

print(a)
a.plot()
plt.show()