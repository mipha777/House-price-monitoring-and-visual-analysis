# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# from requests_toolbelt import user_agent
import time

from scrapy import signals
import random
import base64
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .proxy_Pool import ProxyPool
from scrapy.utils.project import get_project_settings
import threading
from .playwright_human import anjuke_302_verification

class HousepriceMomnitoringSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    async def process_start(self, start):
        # Called with an async iterator over the spider start() method or the
        # maching method of an earlier spider middleware.
        async for item_or_request in start:
            yield item_or_request

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class HousepriceMomnitoringDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # print(request.text)
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

class MyHeadersMiddleware:
    def __init__(self):
        settings = get_project_settings()
        self.user_agents = settings.get('USER_AGENTS')
        # self.Referer_lj = settings.get("REFERER_LIST_lj")
        # self.Referer_ajk = settings.get('REFERER_LIST_ajk')
        # self.Referer_ftx = settings.get('REFERER_LIST_ftx')
        self.accept = settings.get('ACCEPT_LANGUAGE_LIST')
        self.CONNECTION = settings.get('CONNECTION_LIST')

    def process_request(self,request,spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)
        # if spider.name == 'lianjiaPrice':
        #     print('正在为链家设置不同的请求头参数')
        #     request.headers['Referer'] = random.choice(self.Referer_lj)
        #     request.headers['accept-language'] = random.choice(self.accept)
        #     request.headers['Connection'] = random.choice(self.CONNECTION)
        # elif spider.name == 'anjuke':
        #     print('anjuke请求头设置')
        #     request.headers['Referer'] = random.choice(self.Referer_ajk)
        #     request.headers['accept-language'] = random.choice(self.accept)
        #     request.headers['Connection'] = random.choice(self.CONNECTION)
        # elif spider.name == 'fangtianxia':
        #     print('fangtianxia请求头设置中')
        #     request.headers['Referer'] = random.choice(self.Referer_ftx)
        #     request.headers['accept-language'] = random.choice(self.accept)
        #     request.headers['Connection'] = random.choice(self.CONNECTION)


# zidingyi代理中间件 使用代理 清除被封的代理

from scrapy.http import HtmlResponse
from twisted.internet.threads import deferToThread
from twisted.internet import reactor, defer
from twisted.internet.task import deferLater


class MyDeal302Middleware:
    def process_response(self, request, response, spider):
        if response.status == 302:
            spider.logger.info(f"302 验证页面：{response.url}")

            if spider.name == 'anjuke':  # a安居客的请求验证频繁
                # 在单独线程里执行 Playwright
                def run_playwright():
                    return anjuke_302_verification(
                        url=response.url,
                        proxy=request.meta.get('proxy'),
                        debug=True
                    )

                d = deferToThread(run_playwright)

                def _create_response(result):
                    if not result:
                        spider.logger.warning("Playwright没有返回内容，使用原始response")

                        return response

                    return HtmlResponse(
                        url=response.url,
                        body=result.encode('utf-8'),
                        encoding='utf-8',
                        request=request
                    )

                d.addCallback(_create_response)
                return d
            else:
                spider.crawler.engine.pause()
                deferLater(reactor, 30, spider.crawler.engine.unpause)
        return response




class MyProxyMiddleware:
    def __init__(self):
        settings = get_project_settings()
        api_url = settings.get('API_URL')
        if not api_url:
            raise ValueError("请确认settings.py中已配置 API_URL")
        self.Proxy_tool = ProxyPool(api_url)
        self.proxies = []
        self.lock = threading.RLock()
        self.min_size = 3
        self._init_proxies()
        self.fail_counts = {}  # 改为 {proxy: {domain: count}}

    def _init_proxies(self):
        self.proxies = self.Proxy_tool.fetch_proxies()

    def _ensure_proxies(self):
        with self.lock:
            if len(self.proxies) < self.min_size:
                print('代理不足 正在补充')
                new_proxies = self.Proxy_tool.fetch_proxies()
                for p in new_proxies:
                    if p not in self.proxies:
                        self.proxies.append(p)

    def get_random_proxy(self):
        with self.lock:
            self._ensure_proxies()
            if not self.proxies:
                return None
            return random.choice(self.proxies)

    def _get_domain(self, url):
        from urllib.parse import urlparse
        return urlparse(url).netloc

    def process_request(self, request, spider):
        proxy = self.get_random_proxy()
        if proxy:
            request.meta['proxy'] = proxy
            request.meta['original_url'] = request.url
            request.meta['dont_redirect'] = True
            print(f'使用的代理: {proxy}')
        else:
            spider.logger.warning("代理全部被封禁，无法补充")

    async def process_response(self, request, response, spider):
        proxy = request.meta.get('proxy')
        domain = self._get_domain(request.url)

        # 初始化计数器结构
        if proxy not in self.fail_counts:
            self.fail_counts[proxy] = {}
        if domain not in self.fail_counts[proxy]:
            self.fail_counts[proxy][domain] = 0

        if response.status in [403, 429, 500, 502, 503, 504, 404, 302]:

            print(f'代理 {proxy} 在 {domain} 遇到问题，状态码: {response.status}')
            self.fail_counts[proxy][domain] += 1

            if self.fail_counts[proxy][domain] >= 3:
                self.remove_proxy(proxy)
                spider.logger.warning(f"删除封禁代理: {proxy} 在 {domain}")
                self.fail_counts.pop(proxy, None)  # 完全删除，避免内存泄漏

            # 重新请求原 URL
            new_request = request.replace(
                url=request.meta.get('original_url', request.url),
                dont_filter=True,
                meta={**request.meta, 'dont_redirect': True}
            )
            return new_request
        else:
            # 成功请求，重置该代理在该域名的计数
            self.fail_counts[proxy].pop(domain, None)
            return response

    def remove_proxy(self, proxy):
        with self.lock:
            if proxy in self.proxies:
                self.proxies.remove(proxy)

    def process_exception(self, request, exception, spider):
        proxy = request.meta.get('proxy')
        if proxy in self.proxies:
            self.remove_proxy(proxy)
            spider.logger.warning(f"请求异常，删除代理: {proxy}")
        new_request = request.copy()
        new_request.dont_filter = True
        new_request.meta['dont_redirect'] = True
        return new_request

class MyLikePeople():
    def process_request(self, request, spider):
        standstill = random.uniform(1, 5)
        time.sleep(standstill) # su随机停顿
