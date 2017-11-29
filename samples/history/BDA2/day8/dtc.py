import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
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

#model = GaussianNB()
#model = DecisionTreeClassifier()
#model = RandomForestClassifier()
#help(KNeighborsClassifier)
#model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train, y_train)



y_pred = model.predict(X_test)
#print(pred1)
print(le.classes_)

# 看预测效果
cm = metrics.confusion_matrix(y_test, y_pred) # 混淆矩阵
#print(cm)
report = metrics.classification_report(y_test, y_pred)
#print(report)

score = model.score(X_test, y_test)
print(score)



# 画混淆矩阵
#cm = np.random.randint(9, size=(4,4))
plt.rcParams['font.sans-serif'] = ['SimHei']
le.classes_
plt.imshow(cm, cmap=plt.cm.Greens) # 画矩阵
plt.xticks([0,1,2], le.classes_) # 第一个参数是下标，
plt.yticks([0,1,2], le.classes_)
plt.colorbar() # 用颜色表示数值大小
half = cm.max()/2
# 给数字上色，深底浅色字，反之亦然
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(i,j,cm[j,i],
            color='white' if cm[j,i]>half else 'black',
            size=16
            )
#plt.show()

    
