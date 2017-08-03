'''

'''

from itertools import product
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier  
'''
是 1 
否 0
狗 1  猫 2  兔子 3
'''

#names = ['luobo','yu','haozi','gutou','dwb','ced','fenlei']
## 读取csv时自定义列名
#df = pd.read_csv('D:\csv\catdograbbit.csv', names = names)
df = pd.read_csv(r'..\csv\catdograbbit.csv')

# 用labelencoder 转
classle = LabelEncoder()
df['喜欢吃萝卜'] = classle.fit_transform(df['喜欢吃萝卜'].values)
df['喜欢吃鱼'] = classle.fit_transform(df['喜欢吃鱼'].values)
df['喜欢捉耗子'] = classle.fit_transform(df['喜欢捉耗子'].values)
df['喜欢啃骨头'] = classle.fit_transform(df['喜欢啃骨头'].values)
df['短尾巴'] = classle.fit_transform(df['短尾巴'].values)
df['长耳朵'] = classle.fit_transform(df['长耳朵'].values)
# 选取训练集特征
X = df[['喜欢吃萝卜','喜欢吃鱼','喜欢捉耗子','喜欢啃骨头','短尾巴','长耳朵']]
y = classle.fit_transform(df['分类'].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)

model1 = GaussianNB()
model2 = MultinomialNB()
model3 = KNeighborsClassifier()
model4 = DecisionTreeClassifier()
model5 = LogisticRegression()
models = [model1,model2,model3,model4,model5]
labels = ['GaussianNB','MultinomialNB','KNeighborsClassifier','DecisionTreeClassifier','LogisticRegression']
eclf = VotingClassifier(estimators=list(zip(labels, models))) 

models.append(eclf)
labels.append('VotingClassifier')

for model, label in list(zip(models, labels)):  
    
    scores = cross_val_score(model, X_train, y_train)  
    #print(scores)
    print("Accuracy: {0:.2f} (+/- {1:.2f}) -{2}".format(scores.mean(), scores.std(), label))



'''
-----------------------------------------------------------------------------------------------------
'''
