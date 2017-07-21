
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #画3D图
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
sns.set_style("whitegrid")


df = pd.read_csv(r'D:\python_kecheng\samples\csv\Pokemon.csv')
df = df.set_index('Name').drop(['#'],axis=1)
df2 = df[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']]
#print(df)

# 观察数据，看是否有异常值
# 可以画箱型图，直观
sns.boxplot(data=df.HP)
plt.ylim(0,df.HP.max()) 
#plt.ylim(0,130) 
#sns.boxplot(data=df.F)
#plt.ylim(0,df.F.max())
#sns.boxplot(data=df.M)
#plt.ylim(0,df.M.max())
#plt.ylim(0, 20000)
#plt.show()



#分为n_clusters类，聚类最大循环次数500
model = KMeans(n_clusters=4, max_iter = 500).fit(df2)


#print(model.labels_)
#print(model.cluster_centers_)
#统计各个类别的数目
r1 = pd.Series(model.labels_).value_counts()
#找出聚类中心
r2 = pd.DataFrame(model.cluster_centers_)
#横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r2, r1], axis = 1) 
#重命名表头
r.columns = list(df2.columns) + ['类别数目'] 
print(r)


## 3D散点图
##model.fit_predict(df2) # == model.fit(df2).predict(df2)
#y_pred = model.predict(df2) # 因为这个model已经fit过，只要predict
#sd = plt.figure().add_subplot(111, projection = '3d')  
#sd.set_xlabel('R')  
#sd.set_ylabel('F')  
#sd.set_zlabel('M') 
#sd.scatter(df.R, df.F, df.M, c=y_pred)
#plt.show() 
#pikachu = df.ix['Pikachu'].values[3:9].reshape(1, -1)
#print(pikachu)
#print(model.predict(pikachu))

def predict_one(name):
    pokemon = df.ix[name].values[3:9].reshape(1, -1)
    print(pokemon)
    print(model.predict(pokemon))
predict_one('Pikachu')
predict_one('Wartortle')