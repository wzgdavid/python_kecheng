import pymysql
import pandas as pd
import numpy as np
import chardet

# 这个csv中有两行的名字是特殊编码，手动改一下
df =  pd.read_csv(r'E:\python_files\csv\Pokemon.csv')

# 打开数据库连接
db = pymysql.connect("localhost","root","111111","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
length = df.shape[0]

def insert_onebyone():
    for idx in range(length):
        print(idx)
        row = df.ix[idx].copy()
        #print(row['Type 2'])
        if row['Type 2'] is np.nan:
            #print('---------nan--------')
            row['Type 2'] = 'null'
        row = tuple(row)
        #print(row)
        sql = "insert into pokemon values {}".format(str(row))
        #print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            db.rollback()
    # 关闭数据库连接
    db.close()

def insert_all():
    rows = []
    for idx in range(5,11):

        row = df.ix[idx].copy()
        if row['Type 2'] is np.nan:
            row['Type 2'] = 'null'
        rows.append( str(tuple(row)) )
    rows = ','.join(rows)
    sql = "insert into pokemon values {}".format(rows)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    insert_onebyone()
    #insert_all()