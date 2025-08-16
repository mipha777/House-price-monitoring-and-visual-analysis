# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/11 21:28
@Desc     : 
"""
import requests
url= 'https://hz.58.com/ershoufang/p33/?PGTID=0d30000c-0004-f837-1ce3-b191a7d1cf9f&ClickID=1'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'referer':'https://hz.58.com/ershoufang/p20/?'
}
response = requests.get(url, headers=headers)
print(response.text)
print(len(response.text))