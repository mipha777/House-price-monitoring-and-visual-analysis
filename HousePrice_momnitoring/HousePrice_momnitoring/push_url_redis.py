# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/11 22:46
@Desc     : 
"""
import json
import time
# from scrapy_redis.connection import to_bytes
import redis
from settings import mubiaochengshi, mubiaoshenghui
import requests
from lxml import etree

r = redis.Redis(
    host="159.75.144.33",
    port=6379,
    password="shaozi777",
    decode_responses=False
)
page = 10  # 页数 后期挪到setting


class url_to_redis:
    def __init__(self):
        self.r = r
        self.page = page
        self.mubiaoshenghui = mubiaoshenghui
        self.mubiaochengshi = mubiaochengshi

    def redis_anjuke(self):
        with open('./tools/city_info_anjuk.json', 'r', encoding='utf-8') as f:
            jsonanjuke = json.loads(f.read())
            city_anjuke = jsonanjuke[mubiaoshenghui]

        citys_anjuke = []
        if mubiaochengshi == 0:
            for city_name, city_code in city_anjuke.items():
                citys_anjuke.append(city_code)
        else:
            citys_anjuke.append(city_anjuke.get(mubiaochengshi))
        print(citys_anjuke)
        # city = 'hz' # 城市缩写 后期从json获取
        for city in citys_anjuke:
            url_anjuke = city + 'sale/?from=HomePage_TopBar'
            r.rpush("anjuke:start_urls", url_anjuke)
        print("anjukede爬取url已推送到Redis")

    def redis_lj(self):
        with open('./tools/city_info_lianjia.json', 'r', encoding='utf-8') as f:
            jsonLJ = json.loads(f.read())
            city_lj = jsonLJ[mubiaoshenghui]
        citys_lj = []
        if mubiaochengshi == 0:
            for name, code in city_lj.items():
                citys_lj.append(code)
        else:
            citys_lj.append(city_lj.get(mubiaochengshi))
        print(citys_lj)

        for city in citys_lj:
            url_lianjia = city + 'ershoufang/pg1/'
            r.rpush("lianjia:start_urls", url_lianjia)
        print('链家已推送redis')

    def redis_ftx(self):
        with open('./tools/city_info_ftx.json', 'r', encoding='utf-8') as f:
            jsonftx = json.loads(f.read())
            city_ftx = jsonftx[mubiaoshenghui]
        citys_ftx = []
        if mubiaochengshi == 0:
            for name, code in city_ftx.items():
                citys_ftx.append(code)
        else:
            citys_ftx.append(city_ftx.get(mubiaochengshi))
        print(citys_ftx)
        for city in citys_ftx:
            url_ftx = f"{city}/house/h316-i3/"
            r.rpush("ftx:start_urls", url_ftx)

        print('ftx已推送redis')


if __name__ == '__main__':
    piovt = url_to_redis()
    piovt.redis_anjuke()
    piovt.redis_ftx()
    piovt.redis_lj()
