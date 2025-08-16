import requests
import json
from lxml import etree
url= 'https://hangzhou.anjuke.com/sale/?from=HomePage_TopBar'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

}
import re
response = requests.get(url, headers=headers)
if '没有找到相关房源' not in response.text:
    resp = etree.HTML(response.text)
    next_page_list = resp.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[4]/div/a[2]/@href')
    next_page = next_page_list[0] if next_page_list else None
    houses_info = resp.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]')
    print(len(houses_info))
    print('nihaonihao')
    # 去除广告
    for house_info in houses_info:
        guangao = house_info.xpath('.//div[@class="property-content-title-othertag"]//img')
        if guangao:
            print('aizhuguangg')
            pass
        else:
            house_id_str = house_info.xpath('./a/@data-lego')[0]  # 这是字符串
            data = json.loads(house_id_str)  # 转成字典
            house_id = data.get("entity_id", "")
            # 平台id
            platform_id = '58tongcheng'
            # 标题，比如“朝南两居室，近地铁”
            title = house_info.xpath('.//div[@class="property-content-title"]/h3/@title')[0].strip()
            # 价格
            price = float(house_info.xpath('.//p[@class="property-price-total"]/span/text()')[0])
            # 均价
            price_str = house_info.xpath('.//p[@class="property-price-average"]/text()')[0]

            if price_str:
                price_str = price_str.strip()  # 去掉空格、换行
                match = re.search(r'(\d+(\.\d+)?)', price_str)
                if match:
                    unit_price = float(match.group(1))

            # 面积，平方米
            area = house_info.xpath('.//div[@class="property-content-info"]/p[2]/text()')[0].strip()
            # 户型，比如“2室1厅1卫”
            layout = house_info.xpath('string(.//div[@class="property-content-info"]/p[1])').strip().replace(' ',
                                                                                                             '')
            # 房屋朝向，比如“南 北”
            orientation = house_info.xpath('.//div[@class="property-content-info"]/p[3]/text()')[0].strip()
            # 楼层，比如“中层(共6层)”
            floor = house_info.xpath('.//div[@class="property-content-info"]/p[4]/text()')[0].strip()
            # 建筑年代
            year_built_text = house_info.xpath('.//div[@class="property-content-info"]/p[5]/text()')[0].strip()
            match = re.search(r'\d{4}', year_built_text)
            year_built = int(match.group()) if match else None
            # 小区名称
            community = house_info.xpath(
                './/div[@class="property-content-info property-content-info-comm"]/p[@class="property-content-info-comm-name"]/text()')[
                0].strip()
            # 区域，比如“朝阳区”
            district = house_info.xpath(
                './/div[@class="property-content-info property-content-info-comm"]/p[2]/span[1]/text()')[0].strip()
            # 地址详情
            # address = house_info.xpath('.//div[@class="property-content-info property-content-info-comm"]/p[2]/span[3]/text()')[0]
            # 房源链接
            url = house_info.xpath('./a/@href')[0]
            print(house_id,platform_id,title,price,area,layout,orientation,floor,year_built,community,district,url,unit_price)
            break