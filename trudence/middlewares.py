# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
from selenium import webdriver
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CustomProxyMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "proxyspider":
            proxy = random.choice(spider.proxy_pool)
            request.meta['proxy'] = "http://" + str(proxy)
            print("New proxy  for ", request.url, proxy)


class SeleniumMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        self.driver = open_driver(random.choice(spider.proxy_pool))
        self.driver.get(request.url)

        body = to_bytes(self.driver.page_source)  # body must be of type bytes
        response = HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
        self.driver.close()
        return response

    def spider_opened(self, spider):
        pass

    def spider_closed(self, spider):
        pass


def open_driver(proxy):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    return webdriver.Chrome(chrome_options=chrome_options)
