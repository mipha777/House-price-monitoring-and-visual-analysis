# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/18 07:02
@Desc     : 
"""

import pymysql
import pandas as pd

from SQL_config import SQL_connect
from sqlalchemy import create_engine

def analysis():
    # 使用 SQLAlchemy engine 替代原来的 pymysql 连接
    user = SQL_connect['user']
    password = SQL_connect['password']
    host = SQL_connect['host']
    database = SQL_connect['database']
    port = SQL_connect.get('port', 3306)
    table = SQL_connect['table']


    # 创建 engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4")

    # 读取数据
    df = pd.read_sql('SELECT * FROM ershoufang_cleaned', engine)

    # 小区平均单价排序
    group_community = df.groupby('community')['unit_price'].mean().sort_values(ascending=False)
    print(group_community.head(10))

    # nnage哪个小区二手房最多 排名前十 #
    community_counts = df['community'].value_counts()
    print(community_counts.head(10))

    # 楼层平均价格
    floor_unit = df.groupby('floor')['unit_price'].mean().sort_values(ascending=False)
    print(floor_unit.head(10))

    # 不同区均价
    dis_unit = df.groupby('district')['unit_price'].mean().sort_values(ascending=False)
    print(dis_unit.head(50))

if __name__ == '__main__':
    analysis()