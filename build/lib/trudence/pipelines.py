# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from itertools import groupby

import xlsxwriter
import datetime
from pytz import timezone


class TrudencePipeline(object):
    counts = {}

    def process_item(self, item, spider):
        domain = item["domain"]
        if domain not in self.counts:
            self.counts[domain] = {i: 0 for i in spider.keywords}
        content = item["content"].lower().split()

        for i in spider.keywords:
            self.counts[domain][i] += content.count(i)
        return item

    def close_spider(self, spider):
        last_keyword = xlsxwriter.utility.xl_col_to_name(len(spider.keywords) + 3)
        tz = timezone('EST')
        sheet_cells = spider.wks.range(f'B2:{last_keyword}{len(spider.domains) + 2}')
        for domain, (_, cell_list) in zip(spider.domains, groupby(sheet_cells, lambda x: x._row)):
            cell_list = [i for i in cell_list]
            now = datetime.datetime.now(tz)
            values = [self.counts.get(domain, {}).get(keyword, 0) for keyword in spider.keywords]
            values = [now.strftime("%Y-%m-%d %H:%M:%S"), int(sum(values))] + values
            for cell, value in zip(cell_list, values):
                cell.value = value
            print(domain, values)
        spider.wks.update_cells(sheet_cells)
