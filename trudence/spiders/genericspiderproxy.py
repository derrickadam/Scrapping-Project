import json
import urllib
from random import random

import requests
from scrapy import Request
from scrapy.http import TextResponse

from trudence.spiders.genericspider import GenericSpider


class GenericSpiderProxy(GenericSpider):
    name = "genericspiderproxy"
    custom_settings = {
        # "LOG_LEVEL": "ERROR"
    }

    def start_requests(self):
        self.proxy_pool = get_proxies()
        self.get_google_sheet_data()
        self.domains_blocked = self.domains_to_retry()
        for url in self.domains_blocked:
            yield Request(url, self.parse_main_page, headers=self.headers, meta={"domain": url})

    def domains_to_retry(self):
        totals = self.wks.col_values(4)[1:]
        res = []
        for total, domain in zip(totals, self.domains):
            if total == '0':
                res.append(domain)
                print(domain,total)
        return res


def get_proxies():
    r = requests.get("https://github.com/fate0/proxylist/blob/master/proxy.list")
    response = TextResponse(r.url, body=r.text, encoding='utf-8')
    res = []
    for i in response.css("td::text").getall():
        ii = json.loads(i)
        country = ii["country"] or ""
        if country == "US" and ii["response_time"] < 5:
            res.append(f"{ii['host']}:{ii['port']}")
    return res
