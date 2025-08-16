import requests
import json
import time
from lxml import etree

url= 'https://hangzhou.anjuke.com/sale/p11/?from=HomePage_TopBar'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

}
import re
response = requests.get(url, headers=headers)
print('anjuke')
print(response.url)
# print(response.text)
# time.sleep(10)
main_url = response.url.split('/')[2]
# city_name = back_your_name(main_url,'anjuke')
resp = etree.HTML(response.text)
next_page_list = resp.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[4]/div/a[2]/@href')
print(next_page_list)
next_page = next_page_list[0] if next_page_list else None
if next_page: # 没有下一页 也就没有这一页 也就是房源空了
    houses_info = resp.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]')
    print(houses_info)
    # 去除广告
    for house_info in houses_info:
        guangao = house_info.xpath('.//div[@class="property-content-title-othertag"]//img')
        if guangao:
            print('daizhuguangg')
            pass
        else:
            print('开始解析')
            house_id_str = house_info.xpath('./a/@data-lego')[0]  # 这是字符串
            data = json.loads(house_id_str)  # 转成字典
            house_id = data.get("entity_id", "")
            # 平台id
            platform_id = 'anjuke'
            # 标题，比如“朝南两居室，近地铁”
            title = house_info.xpath('.//div[@class="property-content-title"]/h3/@title')[0].strip()
            price = float(house_info.xpath('.//p[@class="property-price-total"]/span/text()')[0])
            # 均价
            price_str = house_info.xpath('.//p[@class="property-price-average"]/text()')[0].strip()


            match = re.search(r'(\d+(\.\d+)?)', price_str)

            unit_price = float(match.group(1))
            # 面积，平方米
            area_str = house_info.xpath('.//div[@class="property-content-info"]/p[2]/text()')[0].strip()
            area = float(re.search(r'(\d+(\.\d+)?)', area_str).group(1))
            # 户型，比如“2室1厅1卫”
            layout = house_info.xpath('string(.//div[@class="property-content-info"]/p[1])').strip().replace(
                ' ',
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
                './/div[@class="property-content-info property-content-info-comm"]/p[2]/span[1]/text()')[
                0].strip()
            # 地址详情
            # address = house_info.xpath('.//div[@class="property-content-info property-content-info-comm"]/p[2]/span[3]/text()')[0]
            # 房源链接
            url = house_info.xpath('./a/@href')[0]
            print('送走')
            print(house_id, platform_id, title, price, area, layout, orientation, floor, year_built, community,
                          district, url)


else:
    print('<UNK>')