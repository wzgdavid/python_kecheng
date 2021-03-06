'''
手动转换数据
ppt上示例（移除）
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

'''
数值  武器类型    子弹  血量  身边是否有队友  行为类别
0     手枪        少   少       没              逃跑 
1     机枪        多   多       有             战斗
'''

#names = ['zidan','wuqi','xueliang','do_what','duiyou']

#df = pd.read_csv('fightrun.csv',encoding='utf-8',names=names) # 指定列名
df = pd.read_csv(r'..\csv\fightrun.csv')

#df = df.ix[1:,['武器','子弹','血量','身边队友','行为']]
df.columns = ['#', 'zidan', 'wuqi', 'hp', 'duiyou', 'do']
df = df.drop('#', axis=1)

# 手动转
#df[(df=='手枪')|(df=='少')|(df=='没')|(df=='逃跑')] = 0
#df[(df=='机枪')|(df=='中')|(df=='有')|(df=='战斗')] = 1
#df[(df=='多')|(df=='躲藏')] = 2
#df = df.astype(int)
# 用LabelEncoder转
classle = LabelEncoder()
df['zidan'] = classle.fit_transform(df['zidan'].values)
df['wuqi'] = classle.fit_transform(df['wuqi'].values)
df['hp'] = classle.fit_transform(df['hp'].values)
df['duiyou'] = classle.fit_transform(df['duiyou'].values)
df['do'] = classle.fit_transform(df['do'].values)

X = df[['zidan','wuqi','hp','duiyou']]
y = df['do']

#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, test_size=0.5)
model = DTC().fit(X_train, y_train)

# 预测
# 预测一组特征
y_pred = model.predict([(1,1,0,1)])
# 预测n组特征
y_pred = model.predict(X_test)  # 预测出的结果
# 预测结果，
print(metrics.classification_report(y_test, y_pred))
print(metrics.confusion_matrix(y_test, y_pred))

# 说明
#             precision    recall  f1-score   support
#
#          0       0.73      0.89      0.80         9
#          1       0.95      0.87      0.91        23
#
#avg / total       0.89      0.88      0.88        32
# 以上为metrics.classification_report的返回结果，
#[[ 8  1]   
# [ 3 20]]
# 上面两行metrics.confusion_matrix的结果
# 其中precision = 8 / (8 + 3)
# recall = 8 / (8 + 1)
# f1-score = 2 * (precision * recall) / (precision + recall)
# support是权重
# avg / total 是加权均值 比如recall = (0.89*9+0.87*23)/(9+23)





#probas_ = model.predict_proba(X_test)
#fpr, tpr, thresholds = metrics.roc_curve(y_test, probas_[:, 1], pos_label=1)
#
## 计算AUC值
#auc = metrics.auc(fpr, tpr, reorder=False)
#print('auc is ', auc)
#
## 作ROC曲线
#plt.plot(fpr, tpr, linewidth=2, label = 'ROC', color = 'green') #作出ROC曲线
#plt.xlabel('False Positive Rate') #坐标轴标签
#plt.ylabel('True Positive Rate') #坐标轴标签
#plt.ylim(0, 1.05) #边界范围
#plt.xlim(0, 1.05) #边界范围
#plt.show()