# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/18 08:01
@Desc     : 
"""

import os
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from SQL_config import SQL_connect

# 中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(BASE_DIR, "output", "figures")
REPORTS_DIR = os.path.join(BASE_DIR, "output", "reports")
os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def get_dataframe():
    #读取清洗后数据
    user = SQL_connect['user']
    password = SQL_connect['password']
    host = SQL_connect['host']
    database = SQL_connect['database']
    port = SQL_connect.get('port', 3306)
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4"
    )
    df = pd.read_sql("SELECT * FROM ershoufang_cleaned", engine)
    if df.empty:
        print("清洗表为空，无法绘图")
        return None
    return df


def plot_price_distribution(df):
    #总价分布直方图
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=50, color='skyblue')
    plt.title("二手房总价分布")
    plt.xlabel("总价(万)")
    plt.ylabel("数量")

    save_path = os.path.join(FIGURES_DIR, "price_distribution.png")
    plt.savefig(save_path)
    plt.close()
    print(f"图表已保存到 {save_path}")


def plot_unitprice_distribution(df):
    #单价分布直方图
    plt.figure(figsize=(10, 6))
    plt.hist(df['unit_price'], bins=50, color='lightgreen')
    plt.title("二手房单价分布")
    plt.xlabel("单价(元/㎡)")
    plt.ylabel("数量")

    save_path = os.path.join(FIGURES_DIR, "unitprice_distribution.png")
    plt.savefig(save_path)
    plt.close()
    print(f"图表已保存到 {save_path}")


def plot_top10_community(df):
    #小区均价 Top10条形图
    top10 = df.groupby('community')['price'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    top10.plot(kind='bar', color='orange')
    plt.title("小区均价 Top10")
    plt.ylabel("均价(万)")
    plt.xlabel("小区名")

    save_path = os.path.join(FIGURES_DIR, "top10_community.png")
    plt.savefig(save_path)
    plt.close()
    print(f"图表已保存到 {save_path}")


def plot_floor_box(df):
    #楼层价格箱型图
    plt.figure(figsize=(10, 6))
    df.boxplot(column='unit_price', by='floor', grid=False)
    plt.title("各楼层总价分布")
    plt.suptitle("")
    plt.xlabel("楼层")
    plt.ylabel("总价(万)")

    save_path = os.path.join(FIGURES_DIR, "floor_boxplot.png")
    plt.savefig(save_path)
    plt.close()
    print(f"图表已保存到 {save_path}")


def generate_all_figures():
    df = get_dataframe()
    if df is None:
        return
    plot_price_distribution(df)
    plot_unitprice_distribution(df)
    plot_top10_community(df)
    plot_floor_box(df)



if __name__ == '__main__':
    generate_all_figures()