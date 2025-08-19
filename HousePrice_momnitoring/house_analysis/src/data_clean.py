# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/18 06:47
@Desc     : 
"""
import re
import pandas as pd
import pymysql
from SQL_config import SQL_connect
from sqlalchemy import create_engine


def clean_data():
    user = SQL_connect['user']
    password = SQL_connect['password']
    host = SQL_connect['host']
    port = SQL_connect.get('port', 3306)
    database = SQL_connect['database']
    table = SQL_connect['table']


    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4")

    # 1从数据库读取数据
    df = pd.read_sql(f"SELECT * FROM {table}", engine)

    # 数据清洗
    # 去重（面积、户型、价格、楼层、朝向）
    duplicate_cols = [col for col in ['area', 'house_type', 'unit_price', 'floor', 'orientation'] if col in df.columns]
    df = df.drop_duplicates(subset=duplicate_cols)
    # 缺失值处理
    required_cols = [col for col in ['community', 'unit_price', 'floor', 'district'] if col in df.columns]
    df = df.dropna(subset=required_cols)

    # 楼层规范化
    if 'floor' in df.columns:
        def parse_floor(f):
            if pd.isna(f):
                return None
            f = str(f).replace(' ', '')
            if '低层' in f or '底层' in f :
                return '低层'
            elif '中层' in f:
                return '中层'
            elif '高层' in f or '顶层' in f:
                return '高层'
            else:
                return '未知'

        df['floor'] = df['floor'].apply(parse_floor)
    #区域名进行规范
    df['district'] = df['district'].apply(lambda x: x.split('-')[0] if '-' in str(x) else x)

    #小区名
    df['community'] = df['community'].str.replace(r'\(.*?\)', '', regex=True).str.strip()





    df.to_sql('ershoufang_cleaned', engine, index=False, if_exists='replace')
    print(f"清洗完成，已保存到表：ershoufang_cleaned")
    # 爬取的时候已经进行了中要内容清洗

if __name__ == '__main__':
    clean_data()
