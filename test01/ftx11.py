# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/16 04:14
@Desc     : 
"""

import requests

cookies = {
    'global_cookie': 'lzdfh7k99xr3qy8jtvtqade8l30me7fx2op',
    'city.sig': 'OGYSb1kOr8YVFH0wBEXukpoi1DeOqwvdseB7aTrJ-zE',
    'resourceDetail': '1',
    'city': 'hz',
    '__utma': '147393320.961549608.1754936566.1755205538.1755264052.10',
    '__utmc': '147393320',
    '__utmz': '147393320.1755264052.10.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'csrfToken': 'JheGbTh3cCiRILvvpOQGKEQs',
    'g_sourcepage': 'esf_fy%5Elb_pc',
    'unique_cookie': 'U_fbu1x78zklwuytffn19151ktk3qmecuw8c9*3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://hz.esf.fang.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'global_cookie=lzdfh7k99xr3qy8jtvtqade8l30me7fx2op; city.sig=OGYSb1kOr8YVFH0wBEXukpoi1DeOqwvdseB7aTrJ-zE; resourceDetail=1; city=hz; __utma=147393320.961549608.1754936566.1755205538.1755264052.10; __utmc=147393320; __utmz=147393320.1755264052.10.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); csrfToken=JheGbTh3cCiRILvvpOQGKEQs; g_sourcepage=esf_fy%5Elb_pc; unique_cookie=U_fbu1x78zklwuytffn19151ktk3qmecuw8c9*3',
}

response = requests.get('https://hz.esf.fang.com/newsecond/esfcities.aspx', cookies=cookies, headers=headers)
from lxml import etree
import json

res = etree.HTML(response.text)
all = res.xpath('//*[@id="c02"]/ul/li')
i = 1
dict1 = {}
for each in all:

    if i == 1:
        names = each.xpath('./a')
        for a in names:
            dict2 = {}
            i +=1

            sheng = a.xpath('./text()')[0]
            shi = a.xpath('./text()')[0]
            link =  a.xpath('./@href')[0]
            dict2[shi] = link
            dict1[sheng] = dict2
    else:
        sheng = each.xpath('./strong/text()')[0]
        a = each.xpath('./a')
        dict2 = {}
        for city in a:
            shi = city.xpath('./text()')[0]
            link = 'https:' + city.xpath('./@href')[0]
            dict2[shi] = link
        dict1[sheng] = dict2

with open('../HousePrice_momnitoring/HousePrice_momnitoring/tools/city_info_ftx.json', 'w', encoding='utf-8') as f:
    json.dump(dict1, f, ensure_ascii=False,indent=4)