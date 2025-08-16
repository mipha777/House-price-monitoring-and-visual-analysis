# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/11 03:59
@Desc     : 
"""
import requests

cookies = {
    'f': 'n',
    'commontopbar_ipcity': 'zk%7C%E5%91%A8%E5%8F%A3%7C0',
    'SECKEY_ABVK': 'RUvjd1PNzcqi/7fxJvDrGjRvb8siIcscUwHPbXuHVag%3D',
    'BMAP_SECKEY': 'V7-rjvnIpdbkKOFwLefYZekWMZasTdOBnzPY962ReX84Igi8GY4nBiQLcjZSOXUQSJaj5jnqSFdlXKBW9nBNJHdP1N0MkvfWH2MlS3SyVDKCQl6nrI4jbDMRGLRrGLhuXxIpkBVs-xjXWeHppEuC-SSpzPb2eFNNPqzPZ4qr2P6ljzyRv7Y6MPp_RuI_5jCeR2wgDTeL0Ii6tO20OwwHig',
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
    'is_58_pc': '1',
    'new_uv': '3',
    'utm_source': '',
    'spm': '',
    'new_session': '0',
    'wmda_report_times': '7',
    'city': 'zk',
    'init_refer': 'https%253A%252F%252Fwww.google.com%252F',
    '58_ctid': '79',
    'commontopbar_new_city_info': '18%7C%E6%9D%AD%E5%B7%9E%7Chz',
    'ved_loupans': '529016',
    'weapp_source': '',
    'wmda_session_id_8788302075828': '1754855685560-4eb3b2e4-c3bc-47c7-9550-c5529758e08d',
    'wmda_visited_projects': '%3B2385390625025%3B8788302075828',
    'qz_gdt': '',
    'lp_lt_ut': '8e761e56d3f34cff5246e1ba3b11ddf5',
    'wmda_report_times': '2',
    'ctid': '79',
    'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjB8MTc1NDg1NTczMTA5MTE0NTIyOHxuRWxHb2ZnODM1bHBod3NtQ0J5c3NwOTFNNGJ0em55bFNvakpZejhDWUowPXw4YTc5ZjkzZTBmZGI1M2EzOWEwMmY0NWRjZjNiOTNlNl8xNzU0ODU1NzI4ODY1XzhiZjZjYjM2N2U1YTRjOTM5MzJjNWViNDMzNGU3NDA4XzIwMjc2Mzc2MTh8YzY5ZDdhZWQyYjgzODNmNWNmZTJlMjE3YTZiZGI4YWZfMTc1NDg1NTcyOTk0Nl8yNTY=',
}

headers = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',

    # 'referer': 'https://hz.58.com/ershoufang/?PGTID=0d000000-0000-0bde-3ff6-c584b37f9cb3&ClickID=1',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'f=n; commontopbar_ipcity=zk%7C%E5%91%A8%E5%8F%A3%7C0; SECKEY_ABVK=RUvjd1PNzcqi/7fxJvDrGjRvb8siIcscUwHPbXuHVag%3D; BMAP_SECKEY=V7-rjvnIpdbkKOFwLefYZekWMZasTdOBnzPY962ReX84Igi8GY4nBiQLcjZSOXUQSJaj5jnqSFdlXKBW9nBNJHdP1N0MkvfWH2MlS3SyVDKCQl6nrI4jbDMRGLRrGLhuXxIpkBVs-xjXWeHppEuC-SSpzPb2eFNNPqzPZ4qr2P6ljzyRv7Y6MPp_RuI_5jCeR2wgDTeL0Ii6tO20OwwHig; id58=ChBFJWiYxzaT0QfoWJ2HAg==; 58tj_uuid=4561f298-dde0-48bc-adb6-1cf60ca4c75f; als=0; 58home=zk; wmda_uuid=4a9ccc4b88a8f5c6c2c26d481e99c980; wmda_new_uuid=1; wmda_visited_projects=%3B2385390625025; aQQ_ajkguid=80198CD1-6FD9-49F4-AC1C-DCE686605CF4; sessid=53D32553-46EE-4ED7-BAE4-0D1FB60EC155; ajk-appVersion=; fzq_h=1544ee1a7d7bd94e20340fd107a5fd3a_1754842991933_209b5d008d8c4c8aa0df08c36b2d5ccc_2027637618; xxzlclientid=713f561e-4f97-4225-a5c9-1754842995080; xxzlxxid=pfmxJRUGRg0YwaXIGF/6+W/EpZZSRL+EXdzPuobWbd74LXaGN92vmlWylhU7+73VJppQ; is_58_pc=1; new_uv=3; utm_source=; spm=; new_session=0; wmda_report_times=7; city=zk; init_refer=https%253A%252F%252Fwww.google.com%252F; 58_ctid=79; commontopbar_new_city_info=18%7C%E6%9D%AD%E5%B7%9E%7Chz; ved_loupans=529016; weapp_source=; wmda_session_id_8788302075828=1754855685560-4eb3b2e4-c3bc-47c7-9550-c5529758e08d; wmda_visited_projects=%3B2385390625025%3B8788302075828; qz_gdt=; lp_lt_ut=8e761e56d3f34cff5246e1ba3b11ddf5; wmda_report_times=2; ctid=79; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTc1NDg1NTczMTA5MTE0NTIyOHxuRWxHb2ZnODM1bHBod3NtQ0J5c3NwOTFNNGJ0em55bFNvakpZejhDWUowPXw4YTc5ZjkzZTBmZGI1M2EzOWEwMmY0NWRjZjNiOTNlNl8xNzU0ODU1NzI4ODY1XzhiZjZjYjM2N2U1YTRjOTM5MzJjNWViNDMzNGU3NDA4XzIwMjc2Mzc2MTh8YzY5ZDdhZWQyYjgzODNmNWNmZTJlMjE3YTZiZGI4YWZfMTc1NDg1NTcyOTk0Nl8yNTY=',
}
import time

ts = int(time.time())
params = {

    'now_time': ts,

    # 'stats_key': '0ddd4f6b-d27c-4683-8d69-0ef575d084ab_1',

    # 'PGTID': '0d30000c-0004-f95c-9337-fbde1b3436b6',

}

response = requests.get('https://hz.58.com/ershoufang/3677314079432716x.shtml', params=params, headers=headers)
print(response.text)

