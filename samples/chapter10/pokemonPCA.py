import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt

df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')
# Renaming one column for clarity
#columns = df.columns.tolist()
#columns[0] = 'id'
#df.columns = columns

# 考虑这六个特征
cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

#print(df.head())


#scaler = StandardScaler().fit(df[cols])
df_scaled = StandardScaler().fit_transform(df[cols])

pca = PCA(n_components=0.8)  # n_components 可认为是压缩比例
pca.fit(df_scaled)
pcscores = pd.DataFrame(pca.transform(df_scaled))
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