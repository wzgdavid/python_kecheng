'''
原文url
http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652565477&idx=1&sn=c61a8957fd08ad5a1e043c2bfdc45c5d&chksm=8464c7afb3134eb95d9de6bdb8aeaa20d17fe10bb10f70b27df8e229758f74a4d07165b54e45&mpshare=1&scene=23&srcid=0702A5ZduuSEm74R6gSRSu2Y#rd
原文是python2的，我这边python3，代码稍有改动
'''


'''现在，很多人想开发高效的算法以及参加机器学习的竞赛。所以他们过来问我：”该如何开始？”。一段时间以前，我在一个俄罗斯联邦政府的下属机构中领导了媒体和社交网络大数据分析工具的开发。我仍然有一些我团队使用过的文档，我乐意与你们分享。前提是读者已经有很好的数学和机器学习方面的知识（我的团队主要由MIPT（莫斯科物理与技术大学）和数据分析学院的毕业生构成）。

这篇文章是对数据科学的简介，这门学科最近太火了。机器学习的竞赛也越来越多（如，Kaggle, TudedIT），而且他们的资金通常很可观。

R和Python是提供给数据科学家的最常用的两种工具。每一个工具都有其优缺点，但Python最近在各个方面都有所胜出（仅为鄙人愚见，虽然我两者都用）。这一切的发生是因为Scikit-Learn库的腾空出世，它包含有完善的文档和丰富的机器学习算法。

请注意，我们将主要在这篇文章中探讨机器学习算法。通常用Pandas包去进行主数据分析会比较好，而且这很容易你自己完成。所以，让我们集中精力在实现上。为了确定性，我们假设有一个特征-对象矩阵作为输入，被存在一个*.csv文件中。

数据加载

首先，数据要被加载到内存中，才能对其操作。Scikit-Learn库在它的实现用使用了NumPy数组，所以我们将用NumPy来加载*.csv文件。让我们从UCI Machine Learning Repository下载其中一个数据集。
'''
import numpy as np
from urllib import request
from sklearn import preprocessing
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import uniform as sp_rand
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
def printbr(n):
    print('{}---------------------------------------------------------------------------------------'.format(n))
# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# download the file
raw_data = request.urlopen(url)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
# separate the data from the target attributes
X = dataset[:,0:7]
y = dataset[:,8]

'''数据标准化

我们都知道大多数的梯度方法（几乎所有的机器学习算法都基于此）对于数据的缩放很敏感。因此，在运行算法之前，我们应该进行标准化，或所谓的规格化。标准化包括替换所有特征的名义值，让它们每一个的值在0和1之间。而对于规格化，它包括数据的预处理，使得每个特征的值有0和1的离差。Scikit-Learn库已经为其提供了相应的函数。
'''

# normalize the data attributes
normalized_X = preprocessing.normalize(X)
# standardize the data attributes
standardized_X = preprocessing.scale(X)

'''特征的选取

毫无疑问，解决一个问题最重要的是是恰当选取特征、甚至创造特征的能力。这叫做特征选取和特征工程。虽然特征工程是一个相当有创造性的过程，有时候更多的是靠直觉和专业的知识，但对于特征的选取，已经有很多的算法可供直接使用。如树算法就可以计算特征的信息量。
'''
printbr(0)
model = ExtraTreesClassifier()
model.fit(X, y)
# display the relative importance of each attribute
print(model.feature_importances_)

#其他所有的方法都是基于对特征子集的高效搜索，从而找到最好的子集，意味着演化了的模型在这个子集上有最好的质量。递归特征消除算法（RFE）是这些搜索算法的其中之一，Scikit-Learn库同样也有提供。

model = LogisticRegression()
# create the RFE model and select 3 attributes
rfe = RFE(model, 3)
rfe = rfe.fit(X, y)
# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)

'''
算法的开发

正像我说的，Scikit-Learn库已经实现了所有基本机器学习的算法。让我来瞧一瞧它们中的一些。

逻辑回归

大多数情况下被用来解决分类问题（二元分类），但多类的分类（所谓的一对多方法）也适用。这个算法的优点是对于每一个输出的对象都有一个对应类别的概率。
'''
printbr(1)
model = LogisticRegression()
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(expected.shape, predicted.shape)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

printbr(2)
'''
朴素贝叶斯

它也是最有名的机器学习的算法之一，它的主要任务是恢复训练样本的数据分布密度。这个方法通常在多类的分类问题上表现的很好。
'''


model = GaussianNB()
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

printbr(3)
'''
k-最近邻

kNN（k-最近邻）方法通常用于一个更复杂分类算法的一部分。例如，我们可以用它的估计值做为一个对象的特征。有时候，一个简单的kNN算法在良好选择的特征上会有很出色的表现。当参数（主要是metrics）被设置得当，这个算法在回归问题中通常表现出最好的质量。
'''


# fit a k-nearest neighbor model to the data
model = KNeighborsClassifier()
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
#print(expected.ndim, expected.shape)
printbr(4)
'''
决策树

分类和回归树（CART）经常被用于这么一类问题，在这类问题中对象有可分类的特征且被用于回归和分类问题。决策树很适用于多类分类。
'''


# fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
printbr(5)
'''
支持向量机

SVM（支持向量机）是最流行的机器学习算法之一，它主要用于分类问题。同样也用于逻辑回归，SVM在一对多方法的帮助下可以实现多类分类。
'''


# fit a SVM model to the data
model = SVC()
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

'''
除了分类和回归问题，Scikit-Learn还有海量的更复杂的算法，包括了聚类， 以及建立混合算法的实现技术，如Bagging和Boosting。

如何优化算法的参数

在编写高效的算法的过程中最难的步骤之一就是正确参数的选择。一般来说如果有经验的话会容易些，但无论如何，我们都得寻找。幸运的是Scikit-Learn提供了很多函数来帮助解决这个问题。

作为一个例子，我们来看一下规则化参数的选择，在其中不少数值被相继搜索了：
'''
printbr(6)
# prepare a range of alpha values to test
alphas = np.array([1,0.1,0.01,0.001,0.0001,0])
# create and fit a ridge regression model, testing each alpha
model = Ridge()
grid = GridSearchCV(estimator=model, param_grid=dict(alpha=alphas))
grid.fit(X, y)
print(grid)
# summarize the results of the grid search
print(grid.best_score_)
print(grid.best_estimator_.alpha)

#有时候随机地从既定的范围内选取一个参数更为高效，估计在这个参数下算法的质量，然后选出最好的。

printbr(7)
# prepare a uniform distribution to sample for the alpha parameter
param_grid = {'alpha': sp_rand()}
# create and fit a ridge regression model, testing random alpha values
model = Ridge()
rsearch = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=100)
rsearch.fit(X, y)
print(rsearch)
# summarize the results of the random parameter search
print(rsearch.best_score_)
print(rsearch.best_estimator_.alpha)

#至此我们已经看了整个使用Scikit-Learn库的过程，除了将结果再输出到一个文件中。这个就作为你的一个练习吧，和R相比Python的一大优点就是它有很棒的文档说明。

#在下一篇文章中，我们将深入探讨其他问题。我们尤其是要触及一个很重要的东西——特征的建造。我真心地希望这份材料可以帮助新手数据科学家尽快开始解决实践中的机器学习问题。最后，我祝愿那些刚刚开始参加机器学习竞赛的朋友拥有耐心以及马到成功！