import scrapy
import re
from ..items import HousepriceMomnitoringItem
from scrapy_redis.spiders import RedisSpider
from lxml import etree
from ..tools.back_city_name import back_your_name


class LianjiapriceSpider(RedisSpider):
    name = "lianjiaPrice"
    redis_key = "lianjia:start_urls"
    custom_settings = {
        "DOWNLOAD_DELAY": 3,  # 3秒间隔
        "CONCURRENT_REQUESTS": 2,  # 降低并发
    }


    def parse(self, response):
        print('lianjia')
        if '未找到符合' not in response.text:
            res = etree.HTML(response.text)
            main_url = response.url
            all_house_list = res.xpath('//ul[@class="sellListContent"]/li')
            base_url = '/'.join(main_url.split('/')[0:3])
            city_name = back_your_name(base_url,'lianjia')# 获取城市名字

            next_page_num = int(re.search(r'pg(\d+)', main_url).group(1)) + 1
            if next_page_num <= 6:
                next_url = base_url + '/ershoufang/pg' + str(next_page_num)+ '/'
                yield scrapy.Request(url=next_url, callback=self.parse)
            for house_list in all_house_list:
                yanzheng = house_list.xpath('./@data-lj_action_housedel_id')
                if not yanzheng:
                    continue
                house_id = house_list.xpath('./a[@class="noresultRecommend img LOGCLICKDATA"]/@data-housecode')[0]
                platform_id = 'lianjia'
                title = house_list.xpath('.//div[@class="title"]/a/text()')[0].strip().replace(' ', '')
                price = float(house_list.xpath('.//div[@class="totalPrice totalPrice2"]//text()')[1])
                unit_price = float(house_list.xpath('.//div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')[0].strip().replace('元/平', '').replace(',', ''))
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

                yield HousepriceMomnitoringItem(
                        house_id=house_id,
                        platform_id=platform_id,
                        city=city_name,
                        district=district,
                        price=price,
                        unit_price=unit_price,
                        area=area,
                        layout=layout,
                        floor=floor,
                        orientation=orientation,
                        year_built=year_built,
                        community=community,
                        title=title,
                        url=url
                )

