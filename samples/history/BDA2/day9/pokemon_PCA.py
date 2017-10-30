import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 线性回归， 逻辑回归(分类器)
from sklearn.linear_model import LinearRegression, LogisticRegression
# 朴素贝叶斯
from sklearn.naive_bayes import GaussianNB, MultinomialNB
# 决策树
from sklearn.tree import DecisionTreeClassifier
# 随机森林
from sklearn.ensemble import RandomForestClassifier
# k最近邻
from sklearn.neighbors import KNeighborsClassifier
# 投票学习
from sklearn.ensemble import VotingClassifier
# 支持向量机
from sklearn.svm import SVC
# 聚类
from sklearn.cluster import KMeans, DBSCAN
# 交叉验证
from sklearn.model_selection import train_test_split
# 模型持久化
from sklearn.externals import joblib
# 数据预处理
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
# 分类报告       混淆矩阵
from sklearn.metrics import classification_report, confusion_matrix
# PCA降维
from sklearn.decomposition import PCA

df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')
cols = ['HP','Attack', 'Defense','Sp. Atk','Sp. Def','Speed']
df = df[cols]

#scaler = StandardScaler().fit(df[cols])
df_scaled = StandardScaler().fit_transform(df)

pca = PCA(n_components=5) # n_components 降维之后的维度
pca.fit(df_scaled)
#print(pca.transform(df_scaled))
pcscores = pd.DataFrame(pca.transform(df_scaled))
#                   [PC1, PC2, PC3, PC4]
pcscores.columns = ['PC'+str(i+1) for i in range(len(pcscores.columns))]
#print(pca.components_)
loadings = pd.DataFrame(pca.components_, columns=cols)
loadings.index = ['PC'+str(i+1) for i in range(len(pcscores.columns))]
#print(pd.DataFrame(df_scaled).head(), df_scaled.shape)
#print(pcscores.head(), pcscores.shape)
#print(loadings)

#由图可看出 
#高防低速度的宠物 PC2值更高.
#高 Sp. Defense低攻   PC3更高
#高HP 低攻防     PC4更高
ax = sns.heatmap(loadings.transpose(), center=0, linewidths=0.5, 
                 cmap="RdBu", vmin=-1, vmax=1, annot=True)
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=0)
ax.set_yticklabels(ax.yaxis.get_majorticklabels(), rotation=0)
plt.show()