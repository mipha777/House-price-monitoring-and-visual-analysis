# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousepriceMomnitoringItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 房源ID
    house_id = scrapy.Field()
    # 平台id
    platform_id = scrapy.Field()

    province = scrapy.Field() #省
    city = scrapy.Field() # 市
    # 区域，比如“朝阳区”
    district = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # danjia
    unit_price = scrapy.Field()
    # 面积，平方米
    area = scrapy.Field()
    # 户型，
    layout = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 房屋朝向，比如“南 北”
    orientation = scrapy.Field()
    # 建筑年代
    year_built = scrapy.Field()
    # 小区名称
    community = scrapy.Field()
    # 标题，比如“朝南两居室，近地铁”
    title = scrapy.Field()
    # 房源链接
    url = scrapy.Field()
    crawl_time = scrapy.Field()

    # 发布时间
    # publish_date = scrapy.Field()
