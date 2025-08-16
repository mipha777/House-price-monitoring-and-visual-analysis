# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/13 14:30
@Desc     : 
"""

from playwright.sync_api import sync_playwright
import json
from lxml import etree



def get_city_list_ftx():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://esf.fang.com/newsecond/esfcities.aspx')
        # 等待页面完全渲染
        page.wait_for_load_state("networkidle")

        html = page.content()
        print(html)
        res = etree.HTML(html)
        all_city_info ={}
        all = res.xpath('.//div[@class="outCont"]//li')
        for city in all:

            shenghui = city.xpath('./strong/text()')[0]
            print(shenghui)
            citys_url = city.xpath('./a/@href')
            citys_name = city.xpath('./a/text()')
            print(citys_name)
            a = {}
            for i in range(len(citys_name)):

                name = citys_name[i]
                url = citys_url[i]
                a[name] = url
            print(a)
            all_city_info[shenghui] = a
    with open('city_info_ftx.json', 'w', encoding='utf-8') as f:
        json.dump(all_city_info, f, ensure_ascii=False)
        f.close()






if __name__ == '__main__':
    get_city_list_ftx()





