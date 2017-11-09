import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from logic import _load_pkl, _save_pkl, column_names


def train():
    area = ['浦东新区', '闵行区', '松江区', 
    '徐汇区', '普陀区', '长宁区', 
    '青浦区', '静安区', '上海周边', 
    '杨浦区', '虹口区', '宝山区', 
    '嘉定区', '黄浦区', '奉贤区', 
    '崇明区', '金山区']
    # 查询网址http://www.gpsspg.com/maps.htm  百度地图gps
    gps = (
        (31.2274065041,121.5505840120), (31.1189141643,121.3886803785), (31.0383289332,121.2330541677),
        (31.1946458680,121.4433055580), (31.2553119532,121.4035442489), (31.2265243725,121.4304185175),
        (31.1555447438,121.1308224101), (31.2296614952,121.4624372609), (31.2363429624,121.4803295328),
        (31.2656839054,121.5326577316), (31.2703244262,121.5118910226), (31.4109435502,121.4959742660),
        (31.3805628349,121.2727914784), (31.2374294453,121.4912966392), (30.9239497878,121.4806129429),
        (31.6288408354,121.4038337007), (30.7479665497,121.3489176446)
    )
    
    area_gps = dict(zip(area, gps))
    #print(area_gps)
    
    df = pd.read_csv(r'E:\python_files\csv\anjuke.csv', encoding='gbk')
    
    # 聚类处理的特征
    columns = ['区域1', '租金', '面积']
    X = df.ix[:,columns] # X = df[columns]
    X['区域1'] = X['区域1'].apply(lambda area:area_gps[area])
    X['area_x'] = X['区域1'].apply(lambda gps:gps[0])
    X['area_y'] = X['区域1'].apply(lambda gps:gps[1])
    X = X.drop('区域1', axis=1)
    #X['面积'] = X['面积'].apply(lambda mianji:mianji.replace('平米',''))
    X['面积'] = X['面积'].apply(lambda mianji:mianji[:-2]).astype(int)
    def foo():
        '''用来观测离群值'''
        plt.scatter(X['面积'], X['租金'])
        plt.show()
    #foo()
    def bar(): # 租金上限 16000  222
        sns.boxplot(data=X,y='面积')
        plt.show()
    #bar()
    # X_filtered去除离群值之后的样本
    X_filtered = X[(X['面积']<=222) & (X['租金']<=16000)]
    # df_filtered的index和X_filtered的index一样，
    df_filtered = df[df.index.isin(X_filtered.index)]
    #print(X.shape, X_filtered.shape)
    #print(X.columns)
    X_scaled = StandardScaler().fit_transform(X_filtered)
    #X_scaled = MinMaxScaler().fit_transform(X_filtered)
    #print(X_scaled)
    
    # 聚类 学习
    model = KMeans(n_clusters=20)
    model.fit(X_scaled)
    
    y_pred = model.fit_predict(X_scaled)
    y_data = pd.DataFrame(y_pred, columns=['分类'], index=df_filtered.index)
    
    #print(model.labels_, model.labels_.shape)
    # model.labels_转成DataFrame，之后才可用concat
    labels = pd.DataFrame(model.labels_, columns=['分类'], index=df_filtered.index)
    #print(y_pred == model.labels_)
    #print(labels)
    # 聚类之后打上标签的数据集
    data_recommend = pd.concat([df_filtered, labels], axis=1)
    #data_recommend = pd.concat([df_filtered, y_data], axis=1)
    #print(data_recommend.shape)
    return data_recommend, model.labels_

# 假数据， 假设是点击过的数据的index（index看做主键）
#history_viewed = 3,4,5,6,15,19,22,38,40


def _random_choice(lst, n=5):
    '''从一个列表中随机不重复的选n个元素'''
    if len(lst) < n:
        return lst
    choosed_list = []
    for i in range(n):
        choosed = random.choice(lst) # 从原来的列表中随机选取一个元素
        choosed_list.append(choosed)
        lst.remove(choosed)    # 移除原来列表中已被选取的元素
    return choosed_list
    #print(lst, choosed)

def recommend():
    # 用另一个数组的元素作为下标去取model.labels_的元素，返回值还是数组
    data_recommend, labels = train()

    history_viewed = _load_pkl('history_click.pickle')
    viewed_types = labels[np.array(history_viewed)]
    #print(viewed_types)
    value_counts = pd.Series(viewed_types).value_counts() #
    #print(value_counts)
    most_view = value_counts.index[0] # 浏览最多的类别
    print(most_view, '--------most view-----------')
    sametype = data_recommend[data_recommend['分类']==most_view]
    #print(sametype.head())
     
    choosed_index = _random_choice(list(sametype.index))
    #print(choosed_index)
    #print(data_recommend.ix[choosed_index,:])
    rows = []
    for idx in choosed_index:
        dct = dict(zip(column_names, [idx]+list(data_recommend.ix[idx])))
        #print(dct)
        rows.append(dct)
    print(rows)
    return rows
    #return data_recommend.ix[choosed_index,:]


if __name__ == '__main__':
    #lst = [1,2,3,4,5,6,7,8,9,0,11,22,33]
    #print(lst, _random_choice(lst))
    recommend()
    pass
    