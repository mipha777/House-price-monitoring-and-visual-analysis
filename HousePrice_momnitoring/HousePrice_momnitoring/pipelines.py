# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import time
import datetime
import pymysql
from itemadapter import ItemAdapter
from .settings import mubiaochengshi,mubiaoshenghui


class HousepriceMomnitoringPipeline:

    def __init__(self):
        self.size = 100
        self.lastTime = time.time()
        # self.container = []
        self.house = []

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='shaozi777',
            db='houseprice',
            charset='utf8',
            autocommit=False, #关闭自动提交
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute("SET SESSION innodb_lock_wait_timeout = 30")

    def process_item(self, item, spider):

        item["crawl_time"] = datetime.datetime.now()
        item['province'] = mubiaoshenghui
        self.house.append((
            item['house_id'],
            item['platform_id'],
            item['province'],
            item['city'],
            item['district'],
            item['price'],
            item['unit_price'],
            item['area'],
            item['layout'],
            item['floor'],
            item['orientation'],
            item['year_built'],
            item['community'],
            item['title'],
            item['url'],
            item['crawl_time'],
        ))

        # 条件1：达到批量大小  条件2：每30秒强制提交一次
        if len(self.house) >= self.size or time.time() - self.lastTime > 30:
            self.insterINTO(spider)
        return item
        # 'https://lishui.anjuke.com/sale/?from=HomePage_TopBar'

    def insterINTO(self,spider):
        sqlconect = '''
                    INSERT IGNORE INTO ershoufang(houseID, platformID, province, city, district, price, unit_price, area, 
                                           house_type, floor, orientation, year_built, community, title, source_url,crawl_time) 
                    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    '''
        try:
            self.cursor.executemany(sqlconect, self.house)
            self.conn.commit()
            self.house.clear()
            self.last_commit_time = time.time()  # 更新提交时间
        except Exception as e:
            self.conn.rollback()
            spider.logger.error(f"批量插入失败:{e}")


    def close_spider(self, spider):
        if self.house:
            self.insterINTO(spider)
        self.cursor.close()
        self.conn.close()


