# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/14 22:56
@Desc     : 
"""

import json
import random

import requests

#
class ProxyPool:
    def __init__(self, api_url):
        self.api_url = api_url
    def fetch_proxies(self):
        # 获取响应内容
        response = requests.get(self.api_url)
        print(response.text)
        if response.status_code == 200:
            proxys_list = []
            res = response.json()
            print('已经获取代理池{}'.format(res))
            for i in res['data']['proxy_list']:
                proxyMeta = f'https://{i}'
                proxys_list.append(proxyMeta)
            print('代理池已经更新')
            return proxys_list
        else:
            print("代理API请求失败", response.status_code)
            return []


if __name__ == '__main__': # 测试入口
    # 测试代理文件这里的返回值 以及代理能不能用
    p = ProxyPool(api_url='https://dps.kdlapi.com/api/getdps/?secret_id=okchdbkacxuxeml03p3z&signature=tla8yi7jqamjge4cxobfgrvlul930qa5&num=1&format=json&sep=1&dedup=1')  #自己的api提取连接
    list = p.fetch_proxies()
    print(list) # 以及网站的相应结构  不同的网站的代理 给ip的方式不一样
    # proxy = random.choice(list)
    # resp = requests.get( url='https://music.163.com/discover/toplist?id=3779629',proxies=proxy,timeout=10)
    # print(resp.text)