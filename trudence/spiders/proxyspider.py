import json

import requests
from scrapy.http import TextResponse

from trudence.spiders.genericspider import GenericSpider


class ProxySpider(GenericSpider):
    name = "proxyspider"

    def __init__(self, is_master=True, lower_bound=0, **kwargs):
        super().__init__(is_master=True, lower_bound=0, **kwargs)
        self.proxy_pool = get_proxies()

    def get_spider_domains(self):
        totals = self.gs_handler.get_totals()
        res = []
        for total, domain in zip(totals, self.all_domains):
            if total == '0':
                res.append(domain)
        return res

    def close(spider, reason):
        pass


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
