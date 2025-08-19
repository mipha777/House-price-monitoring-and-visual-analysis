# import scrapy
# import re
# import json
# from lxml import etree
# from ..items import HousepriceMomnitoringItem
# from scrapy_redis.spiders import RedisSpider



'''

58已经转移为安居客
58已经转移为安居客
58已经转移为安居客

'''















# class A58priceSpider(RedisSpider):
#     name = "a58Price"
#     # allowed_domains = ["58.com"]
#     # Redis 队列键名
#     redis_key = "house58:start_urls"
#     custom_settings = {# 58速度
#         "DOWNLOAD_DELAY": 1,  # 0.1秒间隔
#         "CONCURRENT_REQUESTS": 1,  # 并发
#     }


#     def parse(self, response):

#         resp = etree.HTML(response.text)
#         houses_info = resp.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]')
#         print(f'已经获取数据{len(houses_info)}')
#         # 去除广告
#         for house_info in houses_info:
#             guangao = house_info.xpath('.//div[@class="property-content-title-othertag"]//img')
#             if guangao:
#                 pass
#             else:
#                 house_id_str = house_info.xpath('./a/@data-lego')[0]  # 这是字符串
#                 data = json.loads(house_id_str)  # 转成字典
#                 house_id = data.get("entity_id", "")
#                 # 平台id
#                 platform_id = '58tongcheng'
#                 # 标题，比如“朝南两居室，近地铁”
#                 title = house_info.xpath('.//div[@class="property-content-title"]/h3/@title')[0].strip()
#                 # 价格
#                 price = house_info.xpath('string(.//p[@class="property-price-total"])').strip()
#                 # 均价
#                 unit_price = house_info.xpath('string(.//p[@class="property-price-average"])').strip()
#                 # 面积，平方米
#                 area = house_info.xpath('.//div[@class="property-content-info"]/p[2]/text()')[0].strip()
#                 # 户型，比如“2室1厅1卫”
#                 layout = house_info.xpath('string(.//div[@class="property-content-info"]/p[1])').strip().replace(' ', '')
#                 # 房屋朝向，比如“南 北”
#                 orientation = house_info.xpath('.//div[@class="property-content-info"]/p[3]/text()')[0].strip()
#                 # 楼层，比如“中层(共6层)”
#                 floor = house_info.xpath('.//div[@class="property-content-info"]/p[4]/text()')[0].strip()
#                 # 建筑年代
#                 year_built_text = house_info.xpath('.//div[@class="property-content-info"]/p[5]/text()')[0].strip()
#                 match = re.search(r'\d{4}', year_built_text)
#                 year_built = int(match.group()) if match else None
#                 # 小区名称
#                 community = house_info.xpath('.//div[@class="property-content-info property-content-info-comm"]/p[@class="property-content-info-comm-name"]/text()')[0].strip()
#                 # 区域，比如“朝阳区”
#                 district = house_info.xpath('.//div[@class="property-content-info property-content-info-comm"]/p[2]/span[1]/text()')[0].strip()
#                 # 地址详情
#                 # address = house_info.xpath('.//div[@class="property-content-info property-content-info-comm"]/p[2]/span[3]/text()')[0]
#                 # 房源链接
#                 url = house_info.xpath('./a/@href')[0]
#                 # 送走
#                 yield HousepriceMomnitoringItem(
#                     house_id=house_id,
#                     platform_id=platform_id,

#                     district=district,
#                     price=price,
#                     unit_price=unit_price,
#                     area=area,
#                     layout=layout,
#                     floor=floor,
#                     orientation=orientation,
#                     year_built=year_built,
#                     community=community,
#                     title=title,
#                     url=url
#                 )

