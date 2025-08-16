# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/16 07:15
@Desc     : 
"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from HousePrice_momnitoring.spiders.anjuke import AnjukeSpider
from HousePrice_momnitoring.spiders.lianjiaPrice import LianjiapriceSpider
from HousePrice_momnitoring.spiders.fangtianxia import FangtianxiaSpider
from HousePrice_momnitoring.push_url_redis import url_to_redis


# 主运行文件
def run():
    # 读取项目配置
    process = CrawlerProcess(get_project_settings())
    process.crawl(AnjukeSpider)
    process.crawl(LianjiapriceSpider)
    process.crawl(FangtianxiaSpider)
    # 启动
    process.start()


if __name__ == '__main__':

    run()
