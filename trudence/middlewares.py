# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random


class CustomProxyMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "genericspiderproxy":
            request.meta['proxy'] = "http://" + str(random.choice(spider.proxy_pool))
