# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.driver.get(request.url)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body a::attr(href)"))
            )
        except:
            pass

        body = to_bytes(self.driver.page_source)  # body must be of type bytes
        response = HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
        for i in spider.bad_texts:
            if i in response.text or len(self.driver.page_source) < 10:
                spider.logger.warning(f"Wrong content for {request.url}")
                return None
        return response

    def spider_opened(self, spider):
        self.driver = open_driver()

    def spider_closed(self, spider):
        self.driver.close()


def open_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="//usr/local/bin/chromedriver")
    driver.set_page_load_timeout(5)
    return driver
