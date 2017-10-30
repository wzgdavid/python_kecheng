#from sklearn.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv(r'E:\python_files\csv\51jobs.csv', encoding='gbk')
df = df.dropna()

print(df['学历'].head(9))

# 用哑变量构建学习集特征
X = pd.get_dummies(df['学历'])
print(X.head(19))
#print(X.head())
#y = le.fit_transform(df['分类'].values)

