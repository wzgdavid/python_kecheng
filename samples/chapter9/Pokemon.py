import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")# darkgrid , whitegrid , dark , white ,和 ticks 

plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文


df =  pd.read_csv(r'..\csv\Pokemon.csv')
#df.head(n=10)

df.columns = df.columns.str.upper().str.replace('_', '') #change into upper case
#print(df.head())

df[df['LEGENDARY']==True]

df = df.set_index('NAME')
#### 清洗数据
# 通过查看数据，发现Mega前都是重复的文字
df[df.index.str.contains('Mega')]
# 去掉index中'Mega'前不需要的部分

df=df.drop(['#'],axis=1)

# 用类型1填充类型2
#df['TYPE 2'].fillna(df['TYPE 1'], inplace=True)

# 查看某个宠物的所有属性
Pikachu = df.loc['Pikachu']
#print(Pikachu)

# 筛选出既是火系，又是龙系的宠物
fire_dradon = df[((df['TYPE 1']=='Fire') & (df['TYPE 2']=='Dragon')) | ((df['TYPE 1']=='Dragon') & (df['TYPE 2']=='Fire'))]
#print(fire_dradon)

# 找出HP最高的宠物和它的HP量
maxhp = (df['HP'].argmax(), df['HP'].max())
#print(maxhp[0])

# 总属性值最高的3个
totalmax = df.sort_values('TOTAL',ascending=False).head(3)
#print(totalmax)

# 查看类型
types1 = df['TYPE 1'].unique()
types2 = df['TYPE 2'].unique()

# 火系中攻击力最高的宠物
typefire = df[(df['TYPE 1'] == 'Fire') | (df['TYPE 2'] == 'Fire')]
#print(typefire.ATTACK.idxmax())
# 火系中攻击力前三的宠物
#print(typefire.sort_values('ATTACK', ascending=False).head(3))




# 计算每个类型宠物的数量
type1 = df['TYPE 1'].value_counts()
type2 = df['TYPE 2'].value_counts()
#type1 = df.groupby(['TYPE 1']).size()
#type2 = df.groupby(['TYPE 2']).size()
typecount = (type1+type2).sort_values(ascending=False)
#print(typecount)

# 计算指定类型宠物的数量
bugsum = (df['TYPE 1']=='Bug').sum()
#print(bugsum)

# 每个类型中最强的
strong = df.sort_values(by='TOTAL', ascending=False)
strong = strong.drop_duplicates(subset=['TYPE 1'],keep='first')
#print(strong)

'''#########################################
#########################################
可视化
VISUALISATIONS
#########################################
#########################################
#########################################
'''#########################################

# 所有类型宠物的攻击力分布柱状图
def foo1(): # 写成函数加减注释容易
    bins=range(0,200,20) # 范围0到200，每个柱的宽度20
    # hist画柱状图
    plt.hist(df["ATTACK"],bins,color='#3333ee',width=16) 
    plt.xlabel('攻击力')
    plt.ylabel('计数')
    plt.plot()
    # 平均值
    plt.axvline(df['ATTACK'].mean(),linestyle='dashed',color='red')
    plt.show()
#foo1()

# 水系和火系攻击力防御力散点图分布
def scatter1():
    fire=df[(df['TYPE 1']=='Fire') | ((df['TYPE 2'])=="Fire")]
    water=df[(df['TYPE 1']=='Water') | ((df['TYPE 2'])=="Water")]
    plt.scatter(fire.ATTACK, fire.DEFENSE, color='R', label='Fire',marker="*",s=50)
    plt.scatter(water.ATTACK, water.DEFENSE, color='B', label="Water",s=25)
    plt.xlabel("攻击力")
    plt.ylabel("防御")
    plt.legend()
    plt.show()
#scatter1()


# 各系比例饼图
def pie1():
    labels = 'Water', 'Normal', 'Flying', 'Grass', 'Psychic', 'Bug', 'Ground', 'Fire', 'Poison', 'Rock', 'Fighting', 'Other' 
    sizes = [126, 102, 101, 95, 90, 72, 67, 64, 62, 58, 53, 324]
    # 突出显示
    explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
    plt.axis('equal') # 轴相等，即圆形
    plt.title("不同类型宠物比例")
    plt.show()
#pie1()


# 所有宠物各属性值箱型图分布
def boxplot1():
    df2=df.drop(['GENERATION','TOTAL','LEGENDARY'],axis=1)
    # 箱型图
    # whis参数指胡须的长度是盒子长度的几倍，
    # 超出这个值被认为是离群点（异常值）
    # #默认1.5
    sns.boxplot(data=df2, y='HP', x="TYPE 1")
    plt.ylim(0,300)  #change the scale of the plot
    plt.show()
#boxplot1()

# 宠物分类属性箱型图
def boxplot2(col, maxsize=200):
    plt.subplots(figsize = (15,5))
    plt.title('以TYPE 1分类{}'.format(col))
    sns.boxplot(x="TYPE 1", y =col, data = df)
    plt.ylim(0,maxsize)
    plt.show()
#boxplot2('ATTACK')

#提琴图，和盒形图作用类似，但不是显示真实值，显示的是概率分布
def violinplot1():
    plt.title('以TYPE 1分类ATTACK')
    sns.violinplot(x = "TYPE 1", y = "ATTACK",data = df)
    plt.ylim(0,200)
    plt.show()

#plt.title('Strongest Genaration')
##sns.violinplot(x = "GENERATION", y = "TOTAL",data = df)
#sns.violinplot(x = "LEGENDARY", y = "TOTAL",data = df)
#plt.show()


# 每个类型的类别散布图
def swarmplot1(col):
    plt.figure(figsize=(12,6))
    top_types=df['TYPE 1'].value_counts()[:10]
    # 取出数量最多的类型
    df1=df[df['TYPE 1'].isin(top_types.index)]
    # 每一点代表一个宠物
    sns.swarmplot(x='TYPE 1',y=col, data=df1, hue='GENERATION')
    # 均值画线
    plt.axhline(df1[col].mean(),color='red',linestyle='dashed')
    plt.show()
#swarmplot1('HP')

# 属性之间相关性
#sns.heatmap(df.corr(), annot=True)
#plt.show()
# 可见属性之间相关性并不强


# 各代各类型数量变化
def bar():
    a = df.groupby(['GENERATION','TYPE 1']).count().reset_index()
    a = a[['GENERATION','TYPE 1','TOTAL']]
    #print(a)
    a = a.pivot(index='GENERATION',columns='TYPE 1',values='TOTAL')
    #print(a)
    # 选出一部分画
    a = a[['Water','Fire','Grass','Dragon','Normal','Rock','Flying','Electric']]
    a.plot(marker='o')
    plt.show()
#bar()




sns.jointplot(x="HP", y="ATTACK", data=df)
plt.show()