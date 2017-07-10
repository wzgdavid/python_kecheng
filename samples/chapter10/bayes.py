#多项式分布  
import numpy as np  
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.metrics import precision_recall_curve  
from sklearn.metrics import classification_report  

X = np.random.randint(5, size=(6, 9))  
y = np.array([1, 2, 3, 4, 5, 6])  
print(X)
p = np.random.randint(5, size=9).reshape(1, -1)
print(p)
clf = BernoulliNB().fit(X, y)
print(clf.predict(p))

#precision, recall, thresholds = precision_recall_curve(p, clf.predict(X))  
#answer = clf.predict_proba(X)[:,1]  
#report = answer > 0.5  
#print(classification_report(p, report, target_names = ['neg', 'pos']))  