import requests
import re


cookies = {
    'SECKEY_ABVK': 'RUvjd1PNzcqi/7fxJvDrGueP3pxLn1fKer5hPs6j/oM%3D',
    'BMAP_SECKEY': 'lQWfRlPYVPmM_oMROwyu165yuZOFyOZVYxnafu3DMOmwgxFjswQCxwyMKLZKsYAG8W0ZKEa2zuj7TpaSYfnbt-5uarI7SYhdS5fbZHJcYZCuxfTb7NXHCJ9Ha8dmdqfH18uEkd0P8Z1_AOENH4ce5sMQ4fIkQh283mLwUMNhBpYlk_pk_IVfxuupFJ0_BySk',
    'lianjia_uuid': 'ba2b9b5e-6fcd-4b23-880d-c22bfb4f23f5',
    '_ga': 'GA1.2.1371856236.1754841900',
    '_gid': 'GA1.2.1651726810.1754841900',
    'crosSdkDT2019DeviceId': '-e2glo7--i8b8r9-zknq4jw9q56cpbf-p48qwmhqh',
    'lfrc_': '8c92c41a-aed8-4fe7-84de-7fde8834c691',
    '_ga_KJTRWRHDL1': 'GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0',
    '_ga_QJN1VP0CMS': 'GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0',
    'login_ucid': '2000000498012233',
    'lianjia_token': '2.0013c929ef47e3544a026400def59495cf',
    'lianjia_token_secure': '2.0013c929ef47e3544a026400def59495cf',
    'security_ticket': 'fGHFpd00+CIxA2jHjSFQ+i+xRZDOgdtvGsoSlAqTucB98stFajLu6AFkvo70SmRTOpQQEPOVU26q5QY3fTtaG8fQV9J4yqT17VGgQ+9GF4JgN0ZZqS+Tw2/WhK25ndAV0yzkr1CUN8osf1OjXTP3jvwRPnj0Jw0KUN3kCTP9/3s=',
    'ftkrc_': '7b4da81a-e66f-4732-9862-ae7ec223fda1',
    'Hm_lvt_46bf127ac9b856df503ec2dbf942b67e': '1754841894,1754935812,1754998837,1755060312',
    'HMACCOUNT': '6A026BE687B0DE8F',
    '_jzqc': '1',
    '_jzqckmp': '1',
    '_ga_TJZVFLS7KV': 'GS2.2.s1755061101$o2$g0$t1755061101$j60$l0$h0',
    '_ga_WLZSQZX7DE': 'GS2.2.s1755061102$o2$g0$t1755061102$j60$l0$h0',
    'lianjia_ssid': '69333572-347e-23ab-b061-fd4522359d62',
    '_jzqa': '1.961501559170015000.1754841894.1755060312.1755085563.12',
    '_jzqx': '1.1754841894.1755085563.10.jzqsr=google%2Ecom|jzqct=/.jzqsr=xc%2Elianjia%2Ecom|jzqct=/ershoufang/pg2/',
    'select_city': '330100',
    '_qzjc': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22%24device_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e': '1755087765',
    '_qzja': '1.312485962.1754935841096.1755008975625.1755086037990.1755087669666.1755087764779.0.0.0.57.5',
    '_qzjb': '1.1755086037990.7.0.0.0',
    '_qzjto': '7.1.0',
    '_jzqb': '1.9.10.1755085563.1',
    'srcid': 'eyJ0Ijoie1wiZGF0YVwiOlwiNTc1YzVmZTY3ZjE5NGQ5MjE3MTRlMDc4MDgwOGVkODA1YjI0MTI1MGE5Y2EzMWY0YzVjYzdjMGZmNDMxNDljMzQzNThmMGE2Y2JiZGQ5ODE5ZTAwZGI4NjZmNTRhYTc0OTkzMzUyMTg4OTUyY2UzZmFlYmZlY2M1Yzg5ZmU4MDJhYTE1ZmZhYjhjMGRiNTJkNzhhYjIwYTkyNGZiZDUyMTg4MTk5NWMyYjQ0MmNhYzRhMjRjNmRmNTBiNjAzODAwOGU1MGVlMjg0MjQ1ZGViYjRmMDBhYzgwZWI4YmM5NGEyOTVkOGE0M2U1Zjg0ZWYxYWM1YTU4ZTRlMDc0MDUxZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJiMzg0YjI4NlwifSIsInIiOiJodHRwczovL2h6LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcWlhb3NpLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9',
    '_gat': '1',
    '_gat_past': '1',
    '_gat_global': '1',
    '_gat_new_global': '1',
    '_gat_dianpu_agent': '1',
    '_ga_1W6P4PWXJV': 'GS2.2.s1755086051$o5$g1$t1755087776$j60$l0$h0',
    '_ga_W9S66SNGYB': 'GS2.2.s1755086051$o5$g1$t1755087776$j60$l0$h0',
}

headers = {

    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",

    # 'Cookie': 'SECKEY_ABVK=RUvjd1PNzcqi/7fxJvDrGueP3pxLn1fKer5hPs6j/oM%3D; BMAP_SECKEY=lQWfRlPYVPmM_oMROwyu165yuZOFyOZVYxnafu3DMOmwgxFjswQCxwyMKLZKsYAG8W0ZKEa2zuj7TpaSYfnbt-5uarI7SYhdS5fbZHJcYZCuxfTb7NXHCJ9Ha8dmdqfH18uEkd0P8Z1_AOENH4ce5sMQ4fIkQh283mLwUMNhBpYlk_pk_IVfxuupFJ0_BySk; lianjia_uuid=ba2b9b5e-6fcd-4b23-880d-c22bfb4f23f5; _ga=GA1.2.1371856236.1754841900; _gid=GA1.2.1651726810.1754841900; crosSdkDT2019DeviceId=-e2glo7--i8b8r9-zknq4jw9q56cpbf-p48qwmhqh; lfrc_=8c92c41a-aed8-4fe7-84de-7fde8834c691; _ga_KJTRWRHDL1=GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0; _ga_QJN1VP0CMS=GS2.2.s1754852188$o4$g0$t1754852188$j60$l0$h0; login_ucid=2000000498012233; lianjia_token=2.0013c929ef47e3544a026400def59495cf; lianjia_token_secure=2.0013c929ef47e3544a026400def59495cf; security_ticket=fGHFpd00+CIxA2jHjSFQ+i+xRZDOgdtvGsoSlAqTucB98stFajLu6AFkvo70SmRTOpQQEPOVU26q5QY3fTtaG8fQV9J4yqT17VGgQ+9GF4JgN0ZZqS+Tw2/WhK25ndAV0yzkr1CUN8osf1OjXTP3jvwRPnj0Jw0KUN3kCTP9/3s=; ftkrc_=7b4da81a-e66f-4732-9862-ae7ec223fda1; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1754841894,1754935812,1754998837,1755060312; HMACCOUNT=6A026BE687B0DE8F; _jzqc=1; _jzqckmp=1; _ga_TJZVFLS7KV=GS2.2.s1755061101$o2$g0$t1755061101$j60$l0$h0; _ga_WLZSQZX7DE=GS2.2.s1755061102$o2$g0$t1755061102$j60$l0$h0; lianjia_ssid=69333572-347e-23ab-b061-fd4522359d62; _jzqa=1.961501559170015000.1754841894.1755060312.1755085563.12; _jzqx=1.1754841894.1755085563.10.jzqsr=google%2Ecom|jzqct=/.jzqsr=xc%2Elianjia%2Ecom|jzqct=/ershoufang/pg2/; select_city=330100; _qzjc=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22%24device_id%22%3A%2219894ba4dbb358-0c09f33809a3578-26011151-3049680-19894ba4dbc146a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1755087765; _qzja=1.312485962.1754935841096.1755008975625.1755086037990.1755087669666.1755087764779.0.0.0.57.5; _qzjb=1.1755086037990.7.0.0.0; _qzjto=7.1.0; _jzqb=1.9.10.1755085563.1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNTc1YzVmZTY3ZjE5NGQ5MjE3MTRlMDc4MDgwOGVkODA1YjI0MTI1MGE5Y2EzMWY0YzVjYzdjMGZmNDMxNDljMzQzNThmMGE2Y2JiZGQ5ODE5ZTAwZGI4NjZmNTRhYTc0OTkzMzUyMTg4OTUyY2UzZmFlYmZlY2M1Yzg5ZmU4MDJhYTE1ZmZhYjhjMGRiNTJkNzhhYjIwYTkyNGZiZDUyMTg4MTk5NWMyYjQ0MmNhYzRhMjRjNmRmNTBiNjAzODAwOGU1MGVlMjg0MjQ1ZGViYjRmMDBhYzgwZWI4YmM5NGEyOTVkOGE0M2U1Zjg0ZWYxYWM1YTU4ZTRlMDc0MDUxZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJiMzg0YjI4NlwifSIsInIiOiJodHRwczovL2h6LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcWlhb3NpLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_1W6P4PWXJV=GS2.2.s1755086051$o5$g1$t1755087776$j60$l0$h0; _ga_W9S66SNGYB=GS2.2.s1755086051$o5$g1$t1755087776$j60$l0$h0',
}

response = requests.get('https://hz.lianjia.com/ershoufang/pg1/', cookies=cookies, headers=headers)
# print(response.text)
from lxml import etree

if '未找到符合' not in response.text:

    res = etree.HTML(response.text)
    main_url = response.url
    all_house_list = res.xpath('//ul[@class="sellListContent"]/li')

    base_url = '/'.join(main_url.split('/')[0:3])
    print(base_url)
    next_page_num = int(re.search(r'pg(\d+)', main_url).group(1)) + 1
    next_url = base_url + '/ershoufang/pg' + str(next_page_num)+ '/'
    print(next_url)
    exit()
    for house_list in all_house_list:
        yanzheng = house_list.xpath('./@data-lj_action_housedel_id')
        if not yanzheng:
            continue
        house_id = house_list.xpath('./a[@class="noresultRecommend img LOGCLICKDATA"]/@data-housecode')[0]
        platform_id = 'lianjia'
        title = house_list.xpath('.//div[@class="title"]/a/text()')[0].strip().replace(' ', '')
        price = float(house_list.xpath('.//div[@class="totalPrice totalPrice2"]//text()')[1])

        unit_price = float(
            house_list.xpath('.//div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')[0].strip().replace(
                '元/平', '').replace(',', ''))
        text = house_list.xpath('.//div[@class="houseInfo"]/text()')[0]
        parts = [item.strip() for item in text.split("|")]
        area = float(parts[1].replace('平米', ''))
        layout = parts[0]
        orientation = parts[2]
        floor = parts[4]
        year_built = None
        community = house_list.xpath('.//div[@class="flood"]//a[1]/text()')[0].strip()
        district = house_list.xpath('.//div[@class="flood"]//a[2]/text()')[0].strip()

        url = house_list.xpath('./a[@class="noresultRecommend img LOGCLICKDATA"]/@href')[0]
        print(house_id, platform_id, title, price, unit_price, area, layout, orientation, floor, year_built, community,
              district,
              url, next_url)
