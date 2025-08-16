# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/16 05:14
@Desc     : 
"""
import os
import json

# 获取当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 拼接 city_back_ftx.json 的绝对路径
ftx_path = os.path.join(base_dir, 'city_back_ftx.json')
ajk_path = os.path.join(base_dir, 'city_back_ajk.json')
lj_path = os.path.join(base_dir, 'city_back_lianjia.json')

def back_your_name(link,parmas):
    if parmas == 'lianjia':
        with open(lj_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        for k,v in json_data.items():
            if link in k:
                return v

    elif parmas == 'ftx':
        with open(ftx_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        for k,v in json_data.items():
            if link in k:
                return v

    elif parmas == 'anjuke':
        with open(ajk_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        for k,v in json_data.items():
            if link in k:
                return v

if __name__ == '__main__':
    a = back_your_name('hangzhou.anjuke.com','anjuke')
    print(a)
