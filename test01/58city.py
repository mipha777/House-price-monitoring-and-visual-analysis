import requests

cookies = {
    'aQQ_ajkguid': 'ACFE80A0-3725-427E-B94B-C33DE0F1D6A6',
    'sessid': '0D57068C-005C-4345-BFD1-9D47EC8BAF62',
    'ajk-appVersion': '',
    'ctid': '245',
    'fzq_h': 'bf53c1f868eec615be3f395d63969793_1755206400906_d2c85fbf08274631961d370ee8ef558e_2027637618',
    'fzq_js_anjuke_ershoufang_pc': '35b39918d9625819e8c36a345a1453f6_1755206402098_25',
    'id58': 'CroOomieUwKOpb9KCHUNAg==',
    'twe': '2',
    'ctid': '245',
    'xxzlclientid': '08e095e4-970e-4f97-bb92-1755206402971',
    'xxzlxxid': 'pfmx9ZrFiaOcd9D4/r8ETBeJoOPObf462Hh5NOGCDanNVMCfhc2JKIfYq6JiMvBsdnUb',
    'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjF8MTc1NTIwNjUyOTQ4MDcwMzc2NnxNZ0NOemxGd3JDdWorcUJnbUYxc0p1WWh3b0Q3REQva1BuK2ZLZDMwRkFvPXxiYzFkODk2MGU0ZGU5OWFiMzVjNjc0OTQwNjliZGY4ZF8xNzU1MjA2NTI4NjM1X2JhMmI2OTNlZDQ1MjRmYmY5MzRiMzBmZTk0N2I4MzY0XzIwMjc2Mzc2MTh8NTU5NzJhYTk4MDlkNzRjZmI1ZGM3NDFiODhiYmYxNzhfMTc1NTIwNjUyODk4MF8yNTk=',
    'obtain_by': '2',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'priority': 'u=0, i',
    'referer': 'https://www.anjuke.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
    # 'cookie': 'aQQ_ajkguid=ACFE80A0-3725-427E-B94B-C33DE0F1D6A6; sessid=0D57068C-005C-4345-BFD1-9D47EC8BAF62; ajk-appVersion=; ctid=245; fzq_h=bf53c1f868eec615be3f395d63969793_1755206400906_d2c85fbf08274631961d370ee8ef558e_2027637618; fzq_js_anjuke_ershoufang_pc=35b39918d9625819e8c36a345a1453f6_1755206402098_25; id58=CroOomieUwKOpb9KCHUNAg==; twe=2; ctid=245; xxzlclientid=08e095e4-970e-4f97-bb92-1755206402971; xxzlxxid=pfmx9ZrFiaOcd9D4/r8ETBeJoOPObf462Hh5NOGCDanNVMCfhc2JKIfYq6JiMvBsdnUb; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTc1NTIwNjUyOTQ4MDcwMzc2NnxNZ0NOemxGd3JDdWorcUJnbUYxc0p1WWh3b0Q3REQva1BuK2ZLZDMwRkFvPXxiYzFkODk2MGU0ZGU5OWFiMzVjNjc0OTQwNjliZGY4ZF8xNzU1MjA2NTI4NjM1X2JhMmI2OTNlZDQ1MjRmYmY5MzRiMzBmZTk0N2I4MzY0XzIwMjc2Mzc2MTh8NTU5NzJhYTk4MDlkNzRjZmI1ZGM3NDFiODhiYmYxNzhfMTc1NTIwNjUyODk4MF8yNTk=; obtain_by=2',
}

response = requests.get('https://anjuke.com/sale/lang/', cookies=cookies, headers=headers)

from lxml import etree

res = etree.HTML(response.text)

next_page_list = res.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[4]/div/a[1000]/@href')
# 如果列表有内容就取第一个，没有就给 None
next_page = next_page_list[0] if next_page_list else None

print(next_page)
