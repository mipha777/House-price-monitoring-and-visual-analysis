# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/12 03:30
@Desc     : 
"""
import json

import requests
from lxml import etree


cookies = {
    'global_cookie': 'lzdfh7k99xr3qy8jtvtqade8l30me7fx2op',
    '__utmc': '147393320',
    '__utmz': '147393320.1754936566.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'g_sourcepage': 'esf_fy%5Elb_pc',
    '__utma': '147393320.961549608.1754936566.1754936566.1754940546.2',
    '__utmt_t0': '1',
    '__utmt_t1': '1',
    '__utmt_t2': '1',
    'csrfToken': '9v85ma_oOVWddp4Vzeapwg_o',
    'city': 'hz',
    'otherid': '6621c92def910a2e35c231a01346d843',
    'unique_cookie': 'U_lzdfh7k99xr3qy8jtvtqade8l30me7fx2op*12',
    '__utmb': '147393320.12.10.1754940546',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://hz.esf.fang.com/house/i3100/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'global_cookie=lzdfh7k99xr3qy8jtvtqade8l30me7fx2op; __utmc=147393320; __utmz=147393320.1754936566.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); g_sourcepage=esf_fy%5Elb_pc; __utma=147393320.961549608.1754936566.1754936566.1754940546.2; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; csrfToken=9v85ma_oOVWddp4Vzeapwg_o; city=hz; otherid=6621c92def910a2e35c231a01346d843; unique_cookie=U_lzdfh7k99xr3qy8jtvtqade8l30me7fx2op*12; __utmb=147393320.12.10.1754940546',
}
import re
from bs4 import BeautifulSoup
response = requests.get('https://hz.esf.fang.com/house/h316/',  headers=headers)

main_url = response.url.split('/')[-4]
soup = BeautifulSoup(response.text, "lxml")
next_url = None
link_tag = soup.select_one('div.page_box p.last a')
if link_tag and 'href' in link_tag.attrs:
    next_page = link_tag['href']
    next_url = 'https://' + main_url + next_page

print(next_url)

# 找到所有房源信息容器
all_info = soup.select('div.shop_list.shop_list_4 dl')

for info in all_info:
    try:
        # 房源ID（假设在 data-bg 属性里）
        house_id = json.loads(info.get("data-bg", ""))
        house_id = house_id['houseid']
        # 平台id
        platform_id = "fangtianxia"
        # 标题
        title_tag = info.select_one('h4 span.tit_shop')
        title = title_tag.get_text(strip=True).replace(' ', '') if title_tag else ""
        # 价格
        price_tag = info.select_one('dd.price_right span:nth-of-type(1)')
        price = float(price_tag.get_text(strip=True).replace('万','')) if price_tag else ""
        # 均价
        price_average_tag = info.select_one('dd.price_right span:nth-of-type(2)')
        unit_price = float(price_average_tag.get_text(strip=True).replace('元/㎡','')) if price_average_tag else ""
        # 面积
        p_tag = info.select_one('p.tel_shop')
        if p_tag:
            # 去掉所有 <i> 标签
            for i_tag in p_tag.select('i'):
                i_tag.decompose()
            p_texts = [t.strip() for t in p_tag.stripped_strings if t.strip()]
            layout = p_texts[0]  # 户型
            area = float(p_texts[1].replace('㎡',''))  # 面积
            floor = p_texts[2]  # 楼层
            orientation = p_texts[4]  # 朝向
            year_built_text = p_texts[5]  # 建造年份
            match = re.search(r'\d{4}', year_built_text)
            year_built = int(match.group()) if match else None
        else:
            layout = area = floor = orientation = year_built = ""

        # 小区名称
        community_tag = info.select_one('p.add_shop a')
        community = community_tag.get_text(strip=True) if community_tag else ""

        # 区域
        district_tag = info.select_one('p.add_shop span')
        district = district_tag.get_text(strip=True) if district_tag else ""

        # 地址详情（和区域一样的话需要二次处理）
        address = district

        # 链接
        url_tag = info.select_one('h4 a')
        house_url = "https://" + main_url + url_tag["href"] if url_tag else ""
    except:
        continue


    print({
        "house_id": house_id,
        "platform_id": platform_id,
        "title": title,
        "price": price,
        "price_average": unit_price,
        "area": area,
        "layout": layout,
        "floor": floor,
        "year_built": year_built,
        "community": community,
        "district": district,
        "address": address,
        "url": house_url,
        "orientation": orientation
    })
    break