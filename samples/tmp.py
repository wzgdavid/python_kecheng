class Base():
    x = 'base'

class A(Base):
    pass

class B(Base):
    x = 'b'

#print(A.x)
print(B.x)

class C(A, B):
    pass

print(C.x)


数据处理
    空数据 dropna fillna 
    属性转成数字
        手动转
        labelencoder
            from sklearn.preprocessing import LabelEncoder
            df['column'] = LabelEncoder.fit_transform(df.column)
        哑变量 
            pd.get_dummies  返回的df 和原df concat
    筛选一下，去掉异常值
    数据规范化
        from sklearn.preprocessing import MinMaxScaler, StandardScaler
        df2 = StandardScaler().fit_transform(df)
选择学习集
    X 特征  y 标签
    交叉验证
        from model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X,y)
选择模型
    from sklearn.naive_bayes import GaussianNB
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.linear_model import LinearRegression, LogisticRegression
    model=SomeModel()
    学习 model.fit(X_train, y_train)
验证结果
    y_pred = model.predict(X_test)
    混淆矩阵, 分类报告
        from sklearn.metrics import confusion_matrix, classification_report
        confusion_matrix(y_test, y_pred)
        classification_report(y_test, y_pred)
    混淆矩阵可视化
    代价函数
        cost = ((y_test - y_pred)**2).sum()
        比较几个方法的cost，cost越小分类效果越好