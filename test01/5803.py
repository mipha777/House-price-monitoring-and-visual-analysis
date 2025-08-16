# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/11 04:58
@Desc     : 
"""

import requests

url= 'https://hz.58.com/ershoufang/?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

}

response = requests.get(url, headers=headers)
print(response.text)