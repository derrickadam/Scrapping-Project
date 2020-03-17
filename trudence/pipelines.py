# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re


class TrudencePipeline(object):
    counts = {}
    done = 0

    def process_item(self, item, spider):
        domain = item["domain"]
        if domain not in self.counts:
            self.counts[domain] = {i: 0 for i in spider.keywords}
            self.counts[domain]["sub_domains"] = 0
        content = item["content"].lower()
        for i in spider.keywords:
            if len(i.split()) == 1:
                self.counts[domain][i] += content.split().count(i)
            else:
                self.counts[domain][i] += content.count(i)
        self.counts[domain]["sub_domains"] += 1
        return item

    def close_spider(self, spider):
        if self.done == 1:
            return
        self.done = 1
        spider.gs_handler.upload_results(spider, self.counts)
