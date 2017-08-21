
import pickle
import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from random import choice

column_names = ('idx', 'title', 'rent', 'roomtype', 'rentway', 'deco', 'area1', 'area2', 'mianji',
        'face', 'type_', 'comm_name', 'address', 'build_year', 'rj_rate', 'green_rate', 'link')


def _save_pickle(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def _load_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def get_page(n):
    '''n代表第几页，一页20条记录'''
    
    df = pd.read_csv(r'D:\Users\Administrator\Desktop\flaskminisite\data\anjuke.csv', encoding='gbk')
    #['标题', '租金', '房型', '租赁方式', '装修', '区域1', '区域2', '面积', '朝向', '住宅类型', '小区名',
    #   '地址', '年代', '容积率', '绿化率', '链接']
    page_rows = 50  # 一页50条记录
    start = (n-1)*page_rows 
    end = start+page_rows-1
    df['地址'] = df['地址'].apply(str.strip)


    rows = []
    for n in range(start, end+1):
        row = dict(zip(column_names, [n]+list(df.ix[n]))) # 用df中的索引来表示这条数据的主键

        rows.append(row)
    #print(rows)
    return rows

def record_clicked(idx):
    '''记录点击过的房源index,记录最近30条'''
    #data = []
    #with open('click_history.pickle', 'wb') as f:
    #    pickle.dump(data, f)
    max_ = 30
    #with open('click_history.pickle', 'rb') as f:
    #    data = pickle.load(f)
    data = _load_pickle('click_history.pickle')
    if len(data) > max_:
        data.pop()
        data.insert(0, idx)
    else:
        data.insert(0, idx)
    print(data)
    #with open('click_history.pickle', 'wb') as f:
    #    pickle.dump(data, f)
    _save_pickle('click_history.pickle', data)

def train_model():
    '''
    训练模型，然后返回一个分好类的dataframe，推荐的时候从这个dataframe中选择浏览类型最多的记录
    '''
    area = ['浦东新区', '闵行区', '松江区', 
    '徐汇区', '普陀区', '长宁区', 
    '青浦区', '静安区', '上海周边', 
    '杨浦区', '虹口区', '宝山区', 
    '嘉定区', '黄浦区', '奉贤区', 
    '崇明区', '金山区']
    gps = (
        (31.2274065041,121.5505840120), (31.1189141643,121.3886803785), (31.0383289332,121.2330541677),
        (31.1946458680,121.4433055580), (31.2553119532,121.4035442489), (31.2265243725,121.4304185175),
        (31.1555447438,121.1308224101), (31.2296614952,121.4624372609), (31.2363429624,121.4803295328),
        (31.2656839054,121.5326577316), (31.2703244262,121.5118910226), (31.4109435502,121.4959742660),
        (31.3805628349,121.2727914784), (31.2374294453,121.4912966392), (30.9239497878,121.4806129429),
        (31.6288408354,121.4038337007), (30.7479665497,121.3489176446)
    )
    area_gps = dict(zip(area, gps))

    df = pd.read_csv(r'D:\Users\Administrator\Desktop\flaskminisite\data\anjuke.csv', encoding='gbk')
    X = df.loc[:, ['租金', '装修', '面积', '区域1']]
    # 特征整理
    def get_mianji(mianji):
        return mianji.replace('平米', '')
    def get_area_gps(area):
        return area_gps[area]
    
    # 装修用手工整理，安装装修的简单到豪华排序，LabelEncoder的顺序不一定，所以不用
    zx = X['装修'].copy()
    zx[zx=='毛坯'] = 1
    zx[zx=='简单装修'] = 2
    zx[zx=='中等装修'] = 3
    zx[zx=='精装修'] = 4
    zx[zx=='豪华装修'] = 5
    X['装修'] = zx
    X['面积'] = X['面积'].apply(get_mianji)
    # 处理区域坐标
    X['区域1'] = X['区域1'].apply(get_area_gps)
    X['area_x'] = X['区域1'].apply(lambda x:x[0])
    X['area_y'] = X['区域1'].apply(lambda x:x[1])
    X = X.drop('区域1', axis=1)
    X = X.astype(float)
    
    X_filtered = X[(X['面积']<300) | (X['租金']<20000)]
    df_filtered = df[df.index.isin(X_filtered.index)]
    
    ss = StandardScaler()
    X2 = ss.fit_transform(X_filtered)
    model = KMeans(n_clusters=15, n_init=50)
    #model = DBSCAN(eps = 0.1, min_samples=10)
    
    y_pred = model.fit_predict(X2)
    #print(y_pred)
    y_data = pd.DataFrame(y_pred, columns=['分类'], index=df_filtered.index)
    #with open('y_pred.pickle', 'wb') as f:
    #    pickle.dump(y_pred, f)
    _save_pickle('y_pred.pickle', y_pred)
    # 推荐用
    data_recommend = pd.concat([df_filtered, y_data], axis=1)
    # 保存
    #with open('data_recommend.pickle', 'wb') as f:
    #    pickle.dump(data_recommend, f)
    _save_pickle('data_recommend.pickle', data_recommend)



def _random_choice(lst, n):
    '''从列表lst中随机选择n个不重复的元素'''
    if n > len(lst):
        return lst
    choiced_elements = []
    lst = lst.copy()
    while n > 0:
        element = choice(lst)
        choiced_elements.append(element)
        lst.remove(element) # 避免重复选择
        n -= 1
    return choiced_elements


def recommend():
    '''
    根据用户最近的浏览记录，推荐浏览类型最多的房源
    '''
    #train_model()
    #with open('y_pred.pickle', 'rb') as f:
    #    y_pred = pickle.load(f)
    y_pred = _load_pickle('y_pred.pickle')
    #print(y_pred)
    #with open('click_history.pickle', 'rb') as f:
    #    viewed_index = pickle.load(f)
    viewed_index = _load_pickle('click_history.pickle')
    viewed_types = y_pred[np.array(viewed_index)]
    value_counts = pd.Series(viewed_types).value_counts()
    most_view = value_counts.index[0] # 推荐最多浏览的类型
    #print(most_view)
    #with open('data_recommend.pickle', 'rb') as f:
    #    data_recommend = pickle.load(f)
    data_recommend = _load_pickle('data_recommend.pickle')
    recommended = data_recommend[data_recommend['分类'] == most_view]
    #idx = np.array([1,2,3,4,5])
    n = 5

    # 随机选这一类别的n跳记录
    choiced_idx = _random_choice(list(recommended.index), n)
    #print(choiced_idx)
    
    recommended = recommended.ix[choiced_idx, :]
    print('-----------------------------推荐的----------------------------------------------')
    print(recommended)
    #return recommended
    rows = []
    for n in choiced_idx:
        row = dict(zip(column_names, [n]+list(recommended.ix[n]))) # 用df中的索引来表示这条数据的主键

        rows.append(row)
    #print(rows)
    return rows

if __name__ == '__main__':
    #rows = get_page(2)
    #print(rows)
    #train_model()
    #record_clicked(98)
    recommend()