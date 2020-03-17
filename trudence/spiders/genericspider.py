# -*- coding: utf-8 -*-
import urllib

import scrapy
from scrapy import Request
from scrapy.exceptions import CloseSpider

from trudence.tools.spider_monitor import SpiderMonitor
from trudence.items import TrudenceItem
from trudence.settings import MAIN_SHEET, FILE_NAME, CREDENTIALS, CONF_SHEET, API_KEY, PROJECT_ID
from trudence.tools.google_sheet_handler import GoogleSheetHandler


class GenericSpider(scrapy.Spider):
    name = 'genericspider'
    headers = {
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    # custom_settings = {
    #     "HTTPCACHE_ENABLED": "True"
    # }
    ignore_words = ["mailto", ".pdf", ".xlsx", ".csv", 'tel:', '.jpg', '.png', '.mp4', "ogg", 'mp3', '.psd', '.avi']
    force_stop = False
    run_next_enabled = True

    def __init__(self, is_master=True, lower_bound=0, **kwargs):
        super().__init__(**kwargs)
        self.gs_handler = GoogleSheetHandler(CREDENTIALS, FILE_NAME, MAIN_SHEET, CONF_SHEET)
        lower_bound = int(lower_bound)
        self.lower_bound = lower_bound
        # Keywords + weights
        self.keywords, self.weights = self.gs_handler.get_keywords()
        self.gs_handler.get_totals()
        # Batches sizes
        self.batches_size = self.gs_handler.get_batches_sizes()

        # Domains to consider
        self.all_domains = self.gs_handler.get_domain()
        upper_bound = int(lower_bound) + self.batches_size[self.name]
        self.domains = self.get_spider_domains()[lower_bound:upper_bound]

        self.logger.info(f"Spider bounds : {lower_bound, upper_bound}")
        self.logger.info(f"Spider domains : {self.domains}")
        self.is_master = is_master

        # Spider monitor to interact with other jobs in ScrapingHub
        self.spider_monitor = SpiderMonitor(self.batches_size, API_KEY, PROJECT_ID)

        # Prevent spider of running by error
        if self.name == "genericspider" and is_master == True and self.spider_monitor.jobs_summary() >= 2:
            raise CloseSpider(reason="Previous crawling is not done yet")

        # Run next batch if needed
        if upper_bound < len(self.all_domains) and self.run_next_enabled:
            self.spider_monitor.run_next_batch(self.name, upper_bound)

    def start_requests(self):
        for url in self.domains:
            yield Request(url, self.parse_main_page, headers=self.headers, meta={"domain": url})

    def parse_main_page(self, response):
        meta = {"domain": response.meta['domain']}
        for url in set(response.css("a::attr(href)").getall()):
            if self.check_if_ignore(url):
                continue
            parsed_uri = urllib.parse.urlparse(response.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            if 'http' in url and domain not in url:
                continue
            yield response.follow(url, self.extract_content, meta=meta)
        yield from self.extract_content(response)

    def extract_content(self, response):
        item = TrudenceItem()
        try:
            item["content"] = " ".join([i.strip() for i in
                                        response.xpath("//*[not(self::script) and not(self::style)]/text()").getall() if
                                        i.strip() != ""])
            item["url"] = response.url
            item["domain"] = response.meta["domain"]
            yield item
        except Exception as e:
            # Exception may happen when following a link .pdf or @email ...
            print(e)

    def check_if_ignore(self, url):
        for i in self.ignore_words:
            if i in url:
                return True
        return False

    def close(spider, reason):
        # Start the master spider of proxy spiders
        spider.spider_monitor.run_next_batch("proxyspider", 0, is_master=True, lower_bound=spider.lower_bound)

    def get_spider_domains(self):
        return self.all_domains
