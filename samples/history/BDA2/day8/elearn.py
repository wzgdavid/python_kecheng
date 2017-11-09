import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier

#print(dir(nb))
# 读入源数据
#names = ['lb', 'yu', 'hz', 'gt', 'wb', 'ed','fl']  # 自定义列名  
#df = pd.read_csv(r'E:\python_files\csv\catdograbbit.csv', names=names)
df = pd.read_csv(r'E:\python_files\csv\catdograbbit.csv')

#喜欢吃萝卜   喜欢吃鱼    喜欢捉耗子   喜欢啃骨头   短尾巴 长耳朵 分类
le = LabelEncoder()

for column_name in df.columns:
    df[column_name] = le.fit_transform(df[column_name])


# 特征
X = df.drop('分类', axis=1)
y = df['分类']
#print(X.head())
#print(y.head())

# 交叉验证
# train_test_split返回4个值，第一个是特征的训练集，2是特征的测试值
# 3是结果集的训练集， 4 结果集的测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, test_size=0.4)

model1 = GaussianNB()
model2 = MultinomialNB()
model3 = DecisionTreeClassifier()
model4 = RandomForestClassifier()
model5 = KNeighborsClassifier(n_neighbors=7)
#model.fit(X_train, y_train)

models= [model1,model2,model3,model4,model5]
labels=['GaussianNB','MultinomialNB','DecisionTreeClassifier','RandomForestClassifier','KNeighborsClassifier']
estimators = list(zip(labels, models))
#print(estimators)
eclf = VotingClassifier(estimators=estimators)
eclf.fit(X_train, y_train)
#y_pred = eclf.predict(X_test,)

#print(eclf.score(X_test, y_test))

models.append(eclf)
labels.append('VotingClassifier')
for model, label in zip(models, labels):
    scores = cross_val_score(model, X_train, y_train)
    #print(scores)
    print(scores.mean(), scores.std(),label)


#predict('上海'，'本科'，1)

    
