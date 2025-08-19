# Scrapy settings for HousePrice_momnitoring project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "HousePrice_momnitoring"

SPIDER_MODULES = ["HousePrice_momnitoring.spiders"]
NEWSPIDER_MODULE = "HousePrice_momnitoring.spiders"

ADDONS = {}

first_to_all = True # 第一次爬取全部 改为flase即为日常更新



# 启用 scrapy-redis 去重和调度器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

mubiaoshenghui = '浙江' #
# mubiaochengshi = '杭州' # 如果要爬取整个省会下的所有 就注销这里/
mubiaochengshi = 0 # 如果要爬取整个省会下的所有 就打开这里


# TargetContent = '二手房' # 租房  二手房   暂时未写代码


#代理api
API_URL = 'https://dps.kdlapi.com/api/getdps/?secret_id=okchdbkacxuxeml03p3z&signature=tla8yi7jqamjge4cxobfgrvlul930qa5&num=5&format=json&sep=1&dedup=1'

# Redis连接配置
REDIS_HOST = "159.75.144.33"
REDIS_PORT = 6379
REDIS_PARAMS = {
    "password": "shaozi777",
    "decode_responses": False
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT ="Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"

REDIS_REQUEST_SERIALIZER = "scrapy_redis.pipelines.JSONRequestSerializer"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'DEBUG'

# Concurrency and throttling settings
CONCURRENT_REQUESTS = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 2




# settings.py
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = False  # 不保留队列
SCHEDULER_IDLE_BEFORE_CLOSE = 100  # 队列空闲 10 秒后关闭爬虫



# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "HousePrice_momnitoring.middlewares.HousepriceMomnitoringSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "HousePrice_momnitoring.middlewares.HousepriceMomnitoringDownloaderMiddleware": 543,
   "HousePrice_momnitoring.middlewares.MyHeadersMiddleware": 350,
   "HousePrice_momnitoring.middlewares.MyProxyMiddleware": 310,
   "HousePrice_momnitoring.middlewares.MyDeal302Middleware": 300,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "HousePrice_momnitoring.pipelines.HousepriceMomnitoringPipeline": 300,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

CONNECTION_LIST = [
    "keep-alive",
    "close",
    "Keep-Alive",
    "Upgrade",
    "keep-alive, Upgrade"
]
REFERER_LIST_lj = [
    # 链家站内
    "https://lianjia.com/",
    "https://lianjia.com/ershoufang/",
    "https://sh.lianjia.com/xiaoqu/",
    "https://bj.lianjia.com/chengjiao/",

    # 搜索引擎来源
    "https://www.baidu.com/",
    "https://m.baidu.com/",
    "https://www.google.com/",
    "https://cn.bing.com/",

    # 少量社交媒体流量
    "https://weibo.com/",
]
REFERER_LIST_anjuke = [
    # 安居客站内
    "https://anjuke.com/",
    "https://www.anjuke.com/sale/",
    "https://bj.anjuke.com/sale/",
    "https://sh.anjuke.com/sale/",
    "https://gz.anjuke.com/sale/",

    # 搜索引擎来源
    "https://www.baidu.com/",
    "https://m.baidu.com/",
    "https://www.google.com/",
    "https://cn.bing.com/",

    # 社交媒体来源
    "https://weibo.com/",
    "https://www.zhihu.com/",
    "https://www.douban.com/"
]

REFERER_LIST_fangtianxia = [
    # 房天下站内
    "https://fang.com/",
    "https://esf.fang.com/",
    "https://bj.esf.fang.com/",
    "https://sh.esf.fang.com/",
    "https://hz.esf.fang.com/",

    # 搜索引擎来源
    "https://www.baidu.com/",
    "https://m.baidu.com/",
    "https://www.google.com/",
    "https://cn.bing.com/",

    # 社交媒体来源
    "https://weibo.com/",
    "https://www.zhihu.com/",
    "https://www.douban.com/"
]

ACCEPT_LANGUAGE_LIST = [
    "zh-CN,zh;q=0.9",
    "zh-CN,zh;q=0.8,en;q=0.7",
    "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "en-US,en;q=0.9,zh-CN;q=0.8",
    "zh-CN;q=0.9,en;q=0.6,ja;q=0.4",
    "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
    "zh;q=0.9,en;q=0.8",
    "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "zh-CN,zh;q=0.7,en;q=0.6,fr;q=0.5",
    "zh-CN;q=0.9,en;q=0.8,ko;q=0.6",
    "zh-CN,zh;q=0.9,en;q=0.7,ru;q=0.5"
]

USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/125.0.2535.51 Chrome/125.0.6422.112 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.82 Safari/537.36",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6432.15 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6432.2 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.70 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6483.22 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6483.12 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6432.23 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6483.32 Safari/537.36",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/127.0.2595.45 Chrome/127.0.6483.35 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.90 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6483.48 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.130 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6500.18 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.112 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.7 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6500.40 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6500.28 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.8 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6500.66 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6483.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/128.0.2656.70 Chrome/128.0.6500.70 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.8.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6510.15 Safari/537.36"
    ]