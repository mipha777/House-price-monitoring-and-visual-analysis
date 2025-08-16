# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/11 21:33
@Desc     : 
"""
import requests

cookies = {
    'f': 'n',
    'commontopbar_new_city_info': '79%7C%E6%9D%AD%E5%B7%9E%7Chz',
    'commontopbar_ipcity': 'zk%7C%E5%91%A8%E5%8F%A3%7C0',
    'f': 'n',
    'commontopbar_new_city_info': '79%7C%E6%9D%AD%E5%B7%9E%7Chz',
    'SECKEY_ABVK': 'RUvjd1PNzcqi/7fxJvDrGjtpclSqq2E1L8c0Oh3Nvb8%3D',
    'BMAP_SECKEY': 'V7-rjvnIpdbkKOFwLefYZRWHWP4b6J6OzoUOxMTPGw1jFi1BwrjwKaCWbKW-n2ZavCGWUVGsgQFzRCHNLfVE5KvhD-MKFeRbpfTPopYnP1vrcchhoA_-JPA-8ZezUTeYhi7SwP-0fABQTT9n0eH55SGpsr6Y8qwV0_3ZXpGpIwerFtwvEsgYaOCnpyuR3ms3Dj4RREAE3KjUfS7CDjZMYg',
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
    'fzq_h': '1544ee1a7d7bd94e20340fd107a5fd3a_1754842991933_209b5d008d8c4c8aa0df08c36b2d5ccc_2027637618',
    'xxzlclientid': '713f561e-4f97-4225-a5c9-1754842995080',
    'xxzlxxid': 'pfmxJRUGRg0YwaXIGF/6+W/EpZZSRL+EXdzPuobWbd74LXaGN92vmlWylhU7+73VJppQ',
    'wmda_report_times': '7',
    'city': 'zk',
    'wmda_visited_projects': '%3B2385390625025%3B8788302075828',
    'lp_lt_ut': '0b519fe5cb5b5b4e7c655f47bfd6acb8',
    'wmda_report_times': '2',
    'is_58_pc': '1',
    'new_uv': '6',
    'utm_source': '',
    'spm': '',
    '58_ctid': '18',
    'commontopbar_new_city_info': '17%7C%E5%A4%A9%E6%B4%A5%7Ctj',
    'new_session': '0',
    'ctid': '79',
    'init_refer': '',
    'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjB8MTc1NDkxODc4MDU5NDA0NDkxOXw4bnlrdk9qdFFtNysvU0dLdGEwU0VFUHpZbkNzbnFSbVVJclpCNEIwWDAwPXwzNTYxZTY0YjliYmEwNDVmMmZmZGNhNTA4ZjRmMjBjOF8xNzU0OTE4NzczNDQ3XzA5MGZjZDdmMDRkYzRlM2ViNmM2MTY5MDI3YTdmODc1XzIwMjc2Mzc2MTh8OWUxMDRiNzU2MmQwNTcwOTBkMjVlZjhlZjcwODczZWVfMTc1NDkxODc3ODc4N18yNTQ=',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://hz.58.com/ershoufang/p29/?PGTID=0d30000c-0004-f837-1ce3-b191a7d1cf9f&ClickID=1',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'f=n; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; commontopbar_ipcity=zk%7C%E5%91%A8%E5%8F%A3%7C0; f=n; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; SECKEY_ABVK=RUvjd1PNzcqi/7fxJvDrGjtpclSqq2E1L8c0Oh3Nvb8%3D; BMAP_SECKEY=V7-rjvnIpdbkKOFwLefYZRWHWP4b6J6OzoUOxMTPGw1jFi1BwrjwKaCWbKW-n2ZavCGWUVGsgQFzRCHNLfVE5KvhD-MKFeRbpfTPopYnP1vrcchhoA_-JPA-8ZezUTeYhi7SwP-0fABQTT9n0eH55SGpsr6Y8qwV0_3ZXpGpIwerFtwvEsgYaOCnpyuR3ms3Dj4RREAE3KjUfS7CDjZMYg; id58=ChBFJWiYxzaT0QfoWJ2HAg==; 58tj_uuid=4561f298-dde0-48bc-adb6-1cf60ca4c75f; als=0; 58home=zk; wmda_uuid=4a9ccc4b88a8f5c6c2c26d481e99c980; wmda_new_uuid=1; wmda_visited_projects=%3B2385390625025; aQQ_ajkguid=80198CD1-6FD9-49F4-AC1C-DCE686605CF4; sessid=53D32553-46EE-4ED7-BAE4-0D1FB60EC155; ajk-appVersion=; fzq_h=1544ee1a7d7bd94e20340fd107a5fd3a_1754842991933_209b5d008d8c4c8aa0df08c36b2d5ccc_2027637618; xxzlclientid=713f561e-4f97-4225-a5c9-1754842995080; xxzlxxid=pfmxJRUGRg0YwaXIGF/6+W/EpZZSRL+EXdzPuobWbd74LXaGN92vmlWylhU7+73VJppQ; wmda_report_times=7; city=zk; wmda_visited_projects=%3B2385390625025%3B8788302075828; lp_lt_ut=0b519fe5cb5b5b4e7c655f47bfd6acb8; wmda_report_times=2; is_58_pc=1; new_uv=6; utm_source=; spm=; 58_ctid=18; commontopbar_new_city_info=17%7C%E5%A4%A9%E6%B4%A5%7Ctj; new_session=0; ctid=79; init_refer=; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTc1NDkxODc4MDU5NDA0NDkxOXw4bnlrdk9qdFFtNysvU0dLdGEwU0VFUHpZbkNzbnFSbVVJclpCNEIwWDAwPXwzNTYxZTY0YjliYmEwNDVmMmZmZGNhNTA4ZjRmMjBjOF8xNzU0OTE4NzczNDQ3XzA5MGZjZDdmMDRkYzRlM2ViNmM2MTY5MDI3YTdmODc1XzIwMjc2Mzc2MTh8OWUxMDRiNzU2MmQwNTcwOTBkMjVlZjhlZjcwODczZWVfMTc1NDkxODc3ODc4N18yNTQ=',
}

params = {
    'PGTID': '0d30000c-0004-f837-1ce3-b191a7d1cf9f',
    'ClickID': '1',
}

response = requests.get('https://hz.58.com/ershoufang/p32/', params=params, cookies=cookies, headers=headers)
print()