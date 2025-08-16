import scrapy
import re
import json
from bs4 import BeautifulSoup
from scrapy_redis.spiders import RedisSpider
from ..items import HousepriceMomnitoringItem
from ..tools.back_city_name import back_your_name

class FangtianxiaSpider(RedisSpider):
    name = "fangtianxia"
    redis_key = "ftx:start_urls"
    custom_settings = {
        "DOWNLOAD_DELAY": 3,  # 0.1秒间隔
        "CONCURRENT_REQUESTS": 2,  # 高并发
    }
    def parse(self, response):
        print('fangtainxia')
        main_url = response.url.split('/')[2]
        soup = BeautifulSoup(response.text, "lxml")

        city_name = back_your_name(main_url,'ftx')
        next_url = None
        link_tag = soup.select_one('div.page_box p.last a')
        if link_tag and 'href' in link_tag.attrs:
            next_page = link_tag['href']
            next_url = 'https://' + main_url + next_page
        # 找到所有房源信息容器
        all_info = soup.select('div.shop_list.shop_list_4 dl')

        for info in all_info:
            try:
                # 房源ID（假设在 data-bg 属性里）
                house_id = json.loads(info.get("data-bg", ""))
                house_id = house_id['houseid']
                # 平台id
                platform_id = "fangtianxia"
                # 标题
                title_tag = info.select_one('h4 span.tit_shop')
                title = title_tag.get_text(strip=True).replace(' ', '') if title_tag else ""
                # 价格
                price_tag = info.select_one('dd.price_right span:nth-of-type(1)')
                price = float(price_tag.get_text(strip=True).replace('万', '')) if price_tag else ""
                # 均价
                price_average_tag = info.select_one('dd.price_right span:nth-of-type(2)')
                unit_price = float(
                    price_average_tag.get_text(strip=True).replace('元/㎡', '')) if price_average_tag else ""
                # 面积
                p_tag = info.select_one('p.tel_shop')
                if p_tag:
                    # 去掉所有 <i> 标签
                    for i_tag in p_tag.select('i'):
                        i_tag.decompose()
                    p_texts = [t.strip() for t in p_tag.stripped_strings if t.strip()]
                    layout = p_texts[0]  # 户型
                    area = float(p_texts[1].replace('㎡', ''))  # 面积
                    floor = p_texts[2]  # 楼层
                    orientation = p_texts[4]  # 朝向
                    year_built_text = p_texts[5]  # 建造年份
                    match = re.search(r'\d{4}', year_built_text)
                    year_built = int(match.group()) if match else None
                else:
                    layout = area = floor = orientation = year_built = ""

                # 小区名称
                community_tag = info.select_one('p.add_shop a')
                community = community_tag.get_text(strip=True) if community_tag else ""

                # 区域
                district_tag = info.select_one('p.add_shop span')
                district = district_tag.get_text(strip=True) if district_tag else ""

                # 链接
                url_tag = info.select_one('h4 a')
                house_url = "https://" + main_url + url_tag["href"] if url_tag else ""
            except:
                continue


            yield HousepriceMomnitoringItem(
                house_id=house_id,
                platform_id=platform_id,
                city = city_name,
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
                url=house_url
            )

        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)
