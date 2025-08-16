# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/13 12:59
@Desc     : 
"""
import json
import requests
from lxml import etree

import requests

cookies = {
    'lianjia_uuid': 'ba2b9b5e-6fcd-4b23-880d-c22bfb4f23f5',
    '_ga': 'GA1.2.1371856236.1754841900',
    '_gid': 'GA1.2.1651726810.1754841900',
    'crosSdkDT2019DeviceId': '-e2glo7--i8b8r9-zknq4jw9q56cpbf-p48qwmhqh',
    'lfrc_': '8c92c41a-aed8-4fe7-84de-7fde8834c691',
    '_ga_KJTRWRHDL1': 'GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0',
    '_ga_QJN1VP0CMS': 'GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0',
    'ftkrc_': '7b4da81a-e66f-4732-9862-ae7ec223fda1',
    'Hm_lvt_46bf127ac9b856df503ec2dbf942b67e': '1754935812,1754998837,1755060312,1755179440',
    'HMACCOUNT': '6A026BE687B0DE8F',
    '_jzqc': '1',
    '_jzqckmp': '1',
    'login_ucid': '2000000498012233',
    'lianjia_token': '2.001049ed51446390f401e4c460f3d53828',
    'lianjia_token_secure': '2.001049ed51446390f401e4c460f3d53828',
    'security_ticket': 'I9/xDvF5edYX1XTRglwz1pAB7w2k0tEfeprzDDCZW5HUdee3JvJKpBeneeJM8jZ/8lsFzI09ke8NWaXQNYYKlZDcnY/6UZKJzKQdnWq+dtSWdHXk6t9owtQl2qMj4Sa9JYhrm+N8DhL/boquhGFNvKYdlmv/e1hyQuVBFAQdGzg=',
    '_qzjc': '1',
    'select_city': '330100',
    '_ga_1W6P4PWXJV': 'GS2.2.s1755198250$o8$g1$t1755198277$j33$l0$h0',
    '_ga_W9S66SNGYB': 'GS2.2.s1755198250$o8$g1$t1755198277$j33$l0$h0',
    'lianjia_ssid': '828ace19-3c37-4ac9-b2af-206258411bd2',
    'Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e': '1755204156',
    '_jzqa': '1.961501559170015000.1754841894.1755198215.1755204156.17',
    '_jzqx': '1.1754841894.1755204156.14.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22%24device_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D',
    '_qzja': '1.1868638741.1754841897525.1755198236384.1755204157846.1755198236384.1755204157846.0.0.0.6.6',
    '_qzjto': '2.2.0',
    '_jzqb': '1.2.10.1755204156.1',
    '_qzjb': '1.1755204157846.1.0.0.0',
    'srcid': 'eyJ0Ijoie1wiZGF0YVwiOlwiYjBmYTFkNjkxMzQ1YTFjODg2OWM4MDcyNTJhOTRlNWUyMGM2YzVkN2Y5M2MyMzAxYjQyNjE5MzRlMGU1NDg1NjIyZGU1NWNmZGFiYTQwZGU4YTFmYjA5Mjk4OTJjNjA0YWU4MDcyNDQ4ZWQ4YmY5OWE5ZDYwN2UzYmQyYjQ0ZjEzY2JkY2Q1N2U0Y2JlZDdlYzhkNWNlYTEwYjU3Mzk0ODQ4YzE1ODA3OTBjYzc0YWJlY2YxZDM5OTY5NGJiZTAxZjA2ODM0NzY1ZTM0Zjg3OGQ1YzFiYjNlMDNjZDE3YmFkNTQxM2Y0NTc1YjE2OTZlNDJiMzkxMThkZTFkZjI0NFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyZTYyY2U0YVwifSIsInIiOiJodHRwczovL3d3dy5saWFuamlhLmNvbS9jaXR5LyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9',
    '_ga_WLZSQZX7DE': 'GS2.2.s1755204160$o4$g0$t1755204160$j60$l0$h0',
    '_ga_TJZVFLS7KV': 'GS2.2.s1755204160$o4$g0$t1755204160$j60$l0$h0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://hz.lianjia.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'lianjia_uuid=ba2b9b5e-6fcd-4b23-880d-c22bfb4f23f5; _ga=GA1.2.1371856236.1754841900; _gid=GA1.2.1651726810.1754841900; crosSdkDT2019DeviceId=-e2glo7--i8b8r9-zknq4jw9q56cpbf-p48qwmhqh; lfrc_=8c92c41a-aed8-4fe7-84de-7fde8834c691; _ga_KJTRWRHDL1=GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0; _ga_QJN1VP0CMS=GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0; ftkrc_=7b4da81a-e66f-4732-9862-ae7ec223fda1; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1754935812,1754998837,1755060312,1755179440; HMACCOUNT=6A026BE687B0DE8F; _jzqc=1; _jzqckmp=1; login_ucid=2000000498012233; lianjia_token=2.001049ed51446390f401e4c460f3d53828; lianjia_token_secure=2.001049ed51446390f401e4c460f3d53828; security_ticket=I9/xDvF5edYX1XTRglwz1pAB7w2k0tEfeprzDDCZW5HUdee3JvJKpBeneeJM8jZ/8lsFzI09ke8NWaXQNYYKlZDcnY/6UZKJzKQdnWq+dtSWdHXk6t9owtQl2qMj4Sa9JYhrm+N8DhL/boquhGFNvKYdlmv/e1hyQuVBFAQdGzg=; _qzjc=1; select_city=330100; _ga_1W6P4PWXJV=GS2.2.s1755198250$o8$g1$t1755198277$j33$l0$h0; _ga_W9S66SNGYB=GS2.2.s1755198250$o8$g1$t1755198277$j33$l0$h0; lianjia_ssid=828ace19-3c37-4ac9-b2af-206258411bd2; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1755204156; _jzqa=1.961501559170015000.1754841894.1755198215.1755204156.17; _jzqx=1.1754841894.1755204156.14.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22%24device_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _qzja=1.1868638741.1754841897525.1755198236384.1755204157846.1755198236384.1755204157846.0.0.0.6.6; _qzjto=2.2.0; _jzqb=1.2.10.1755204156.1; _qzjb=1.1755204157846.1.0.0.0; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYjBmYTFkNjkxMzQ1YTFjODg2OWM4MDcyNTJhOTRlNWUyMGM2YzVkN2Y5M2MyMzAxYjQyNjE5MzRlMGU1NDg1NjIyZGU1NWNmZGFiYTQwZGU4YTFmYjA5Mjk4OTJjNjA0YWU4MDcyNDQ4ZWQ4YmY5OWE5ZDYwN2UzYmQyYjQ0ZjEzY2JkY2Q1N2U0Y2JlZDdlYzhkNWNlYTEwYjU3Mzk0ODQ4YzE1ODA3OTBjYzc0YWJlY2YxZDM5OTY5NGJiZTAxZjA2ODM0NzY1ZTM0Zjg3OGQ1YzFiYjNlMDNjZDE3YmFkNTQxM2Y0NTc1YjE2OTZlNDJiMzkxMThkZTFkZjI0NFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyZTYyY2U0YVwifSIsInIiOiJodHRwczovL3d3dy5saWFuamlhLmNvbS9jaXR5LyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _ga_WLZSQZX7DE=GS2.2.s1755204160$o4$g0$t1755204160$j60$l0$h0; _ga_TJZVFLS7KV=GS2.2.s1755204160$o4$g0$t1755204160$j60$l0$h0',
}

response = requests.get('https://www.lianjia.com/city/', cookies=cookies, headers=headers)
res = etree.HTML(response.text)

all_city = res.xpath('.//div[@class="city_province"]')
all_city_info = {}
for city in all_city:
    shenghui = city.xpath('.//div[@class="city_list_tit c_b"]/text()')[0]
    citys_name = city.xpath('.//a/text()')
    citys_url = city.xpath('.//a/@href')
    a = {}
    for i in range(len(citys_name)):
        city_name = citys_name[i]
        city_url = citys_url[i]
        a[city_name] = city_url
    all_city_info[shenghui] = a
import json
with open('city_info_lianjia.json', 'w', encoding='utf-8') as f:
    json.dump(all_city_info, f, ensure_ascii=False)
    f.close()