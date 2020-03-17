# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random


class CustomProxyMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "proxyspider":
            proxy = random.choice(spider.proxy_pool)
            request.meta['proxy'] = "http://" + str(proxy)
            print("New proxy  for ", request.url, proxy)
