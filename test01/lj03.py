import requests


cookies = {
    'id58': 'ChBFJWiYxzaT0QfoWJ2HAg==',
    '58tj_uuid': '4561f298-dde0-48bc-adb6-1cf60ca4c75f',
    'als': '0',
    '58home': 'zk',
    'wmda_uuid': '4a9ccc4b88a8f5c6c2c26d481e99c980',
    'wmda_new_uuid': '1',
    'wmda_visited_projects': '%3B2385390625025',
    'aQQ_ajkguid': '80198CD1-6FD9-49F4-AC1C-DCE686605CF4',
    'sessid': '53D32553-46EE-4ED7-BAE4-0D1FB60EC155',
    'ajk-appVersion': '',
    'xxzlclientid': '713f561e-4f97-4225-a5c9-1754842995080',
    'xxzlxxid': 'pfmxJRUGRg0YwaXIGF/6+W/EpZZSRL+EXdzPuobWbd74LXaGN92vmlWylhU7+73VJppQ',
    'wmda_report_times': '7',
    'city': 'zk',
    'fzq_h': '81be3968f8a8dd1620ff2f83d43bfc5e_1754929456213_45ca2afd89354ab988ee6c3fd3e06985_2027637618',
    'ctid': '79',
    'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjB8MTc1NDk0NjE4MzY0MzExNjEzMnx2cGJxWDI5RUdoOVUweWwwTGFMZnVtUTlCWko3alo0Ujl1b1VwNkRKSm5vPXwwYWE3OWE2NGFhZDVhZGVlMjU1YjMzMmEwOTU2NTYwMF8xNzU0OTQ2MTgyNjIxX2ZkNjE3YmQ1Mjg5MjQ2MzlhOGY5ZTcwYTA5NTdlMDNhXzIwMjc2Mzc2MTh8MGQxN2EzN2UzODJjZTI5YjE3ODgzMjk0ZDRmYjU5NzdfMTc1NDk0NjE4MjkzMV8yNTQ=',
    'new_session': '1',
    'new_uv': '11',
    'utm_source': '',
    'spm': '',
    'init_refer': 'https%253A%252F%252Fwww.google.com%252F',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.58.com/ppkchuzu671/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'id58=ChBFJWiYxzaT0QfoWJ2HAg==; 58tj_uuid=4561f298-dde0-48bc-adb6-1cf60ca4c75f; als=0; 58home=zk; wmda_uuid=4a9ccc4b88a8f5c6c2c26d481e99c980; wmda_new_uuid=1; wmda_visited_projects=%3B2385390625025; aQQ_ajkguid=80198CD1-6FD9-49F4-AC1C-DCE686605CF4; sessid=53D32553-46EE-4ED7-BAE4-0D1FB60EC155; ajk-appVersion=; xxzlclientid=713f561e-4f97-4225-a5c9-1754842995080; xxzlxxid=pfmxJRUGRg0YwaXIGF/6+W/EpZZSRL+EXdzPuobWbd74LXaGN92vmlWylhU7+73VJppQ; wmda_report_times=7; city=zk; fzq_h=81be3968f8a8dd1620ff2f83d43bfc5e_1754929456213_45ca2afd89354ab988ee6c3fd3e06985_2027637618; ctid=79; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTc1NDk0NjE4MzY0MzExNjEzMnx2cGJxWDI5RUdoOVUweWwwTGFMZnVtUTlCWko3alo0Ujl1b1VwNkRKSm5vPXwwYWE3OWE2NGFhZDVhZGVlMjU1YjMzMmEwOTU2NTYwMF8xNzU0OTQ2MTgyNjIxX2ZkNjE3YmQ1Mjg5MjQ2MzlhOGY5ZTcwYTA5NTdlMDNhXzIwMjc2Mzc2MTh8MGQxN2EzN2UzODJjZTI5YjE3ODgzMjk0ZDRmYjU5NzdfMTc1NDk0NjE4MjkzMV8yNTQ=; new_session=1; new_uv=11; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.google.com%252F',
}

params = {
    'catepath': 'ershoufang',
    'catename': '58同城二手房出售',
    'fullpath': '12',
    'PGTID': '0d000008-0000-1023-ae48-94a4d4058c19',
    'ClickID': '1',
}

response = requests.get('https://www.58.com/changecity.html', params=params, cookies=cookies, headers=headers)
print(response.text)
import json
from lxml import etree

res = etree.HTML(response.text)

all_city = res.xpath('.//div[@class="content-letter"]/div[@class="content-province"]')
print(len(all_city))
all_city_info = {}
for i in all_city:
    shenghui = i.xpath('./div[@class="content-province-title"]/text()')[0]
    citys_name = i.xpath('.//a/text()')
    citys_url = i.xpath('.//a/@href')
    a = {}
    for j in range(len(citys_name)):
        city_name = citys_name[j]
        city_url = citys_url[j]
        a[city_name] = city_url
    all_city_info[shenghui] = a
with open('58city.json', 'w', encoding='utf-8') as f:
    json.dump(all_city_info, f, ensure_ascii=False)
    f.close()

