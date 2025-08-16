# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/16 04:05
@Desc     : 
"""
import json
def lj():
    with open('city_info_lianjia.json','r',encoding='utf-8') as f:
        data = json.load(f)

    dict_lj = {}
    for p,city in data.items():
        for c,code in city.items():
            dict_lj[code] = c

    with open('city_back_lianjia.json', 'w',encoding='utf-8') as f:
        json.dump(dict_lj, f,ensure_ascii=False,indent=2)

def ftx():
    with open('city_info_ftx.json','r',encoding='utf-8') as f:
        data = json.load(f)
    dict_ftx = {}
    for p,city in data.items():
        for c,code in city.items():
            dict_ftx[code] = c

    with open('city_back_ftx.json', 'w',encoding='utf-8') as f:
        json.dump(dict_ftx,f,ensure_ascii=False,indent=2)

def ajk():
    with open('city_info_anjuk.json','r',encoding='utf-8') as f:
        data = json.load(f)

    dict_ajk = {}
    for p,city in data.items():
        for c,code in city.items():
            dict_ajk[code] = c

    with open('city_back_ajk.json', 'w',encoding='utf-8') as f:
        json.dump(dict_ajk,f,ensure_ascii=False,indent=2)





if __name__ == '__main__':
    ftx()