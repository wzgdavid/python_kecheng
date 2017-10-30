import pandas as pd
import numpy as np
import pickle

column_names = ('idx', 'title', 'rent', 'roomtype', 'rentway', 'deco', 'area1', 'area2', 'mianji',
        'face', 'type_', 'comm_name', 'address', 'build_year', 'rj_rate', 'green_rate', 'link')

def read_data():
    return pd.read_csv(r'E:\python_files\csv\anjuke.csv', encoding='gbk')

#1 0 29
#2 30  59
#3 60  89
def get_page(n):
    '''一页30条记录'''
    start = (n-1)*30
    end = n*30-1
    df = read_data()

    rows = []
    for idx in range(start, end+1):
        dct = dict(zip(column_names, [idx]+list(df.ix[idx])))
        #print(dct)
        rows.append(dct)
    return rows
#print(df.head(5))

# 数据持久化
def _save_pkl(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

# 读取持久化的pickle对象
def _load_pkl(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def record_index(idx):
    '''记录点击过的房源的id, 记录20条'''
    # 
    #idx_list = []
    #_save_pkl('history_click.pickle', idx_list)
    idx_list = _load_pkl('history_click.pickle')
    if len(idx_list) >=10:
        idx_list.pop()
    idx_list.insert(0, idx)
    _save_pkl('history_click.pickle', idx_list)
    print(idx_list)

def look_record():
    print(_load_pkl('history_click.pickle'))

if __name__ == '__main__':
    #record_index(2)
    #get_page(1)
    look_record()
    pass